import os

base_path = r"C:\Users\hp\Desktop\prostory-ai"

files_code = {
# DATABASE
r"base_de_donnees\schema.sql": """-- Extension pour les embeddings
CREATE EXTENSION IF NOT EXISTS vector;

-- Table Utilisateurs
CREATE TABLE IF NOT EXISTS utilisateurs (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    mot_de_passe_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'USER'
);

-- Table Experiences
CREATE TABLE IF NOT EXISTS experiences (
    id SERIAL PRIMARY KEY,
    titre VARCHAR(255) NOT NULL,
    contenu TEXT NOT NULL,
    score_ia INTEGER DEFAULT 0,
    statut_validation VARCHAR(50) DEFAULT 'EN_ATTENTE',
    auteur_id INTEGER REFERENCES utilisateurs(id),
    embedding vector(384)
);
""",

r"base_de_donnees\donnees_test.sql": """-- Admin par défaut (mdp à hacher dans l'application)
INSERT INTO utilisateurs (email, mot_de_passe_hash, role) 
VALUES ('admin@platform.com', 'hash_ici', 'ADMIN') ON CONFLICT DO NOTHING;
""",

# BACKEND ENV
r"backend\environnement.env": """DATABASE_URL=postgresql://user:password@localhost:5432/nom_base
JWT_SECRET_KEY=votre_cle_secrete_tres_longue
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
""",

r"backend\exigences.txt": """fastapi==0.109.2
uvicorn==0.27.1
sqlalchemy==2.0.25
psycopg2-binary==2.9.9
pgvector==0.2.4
sentence-transformers==2.3.1
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-dotenv==1.0.1
pydantic==2.6.1
""",

# BACKEND APP
r"backend\app\main.py": """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from .routes import experiences_api, authentification_api

app = FastAPI(title="Plateforme Experiences API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes
# app.include_router(authentification_api.router)
# app.include_router(experiences_api.router)

@app.get("/")
def defaut():
    return {"message": "API Fonctionnelle"}
""",

r"backend\app\coeur\config.py": """import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/nom_base")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")

settings = Settings()
""",

r"backend\app\coeur\base_de_donnees.py": """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
""",

r"backend\app\coeur\securite.py": """from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verifier_mot_de_passe(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hacher_mot_de_passe(password):
    return pwd_context.hash(password)

def creer_token_acces(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
""",

r"backend\app\modeles\utilisateur_modele.py": """from sqlalchemy import Column, Integer, String
from ..coeur.base_de_donnees import Base

class Utilisateur(Base):
    __tablename__ = "utilisateurs"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    mot_de_passe_hash = Column(String)
    role = Column(String, default="USER")
""",

r"backend\app\modeles\experience_modele.py": """from sqlalchemy import Column, Integer, String, Text, ForeignKey
# from pgvector.sqlalchemy import Vector
from ..coeur.base_de_donnees import Base

class Experience(Base):
    __tablename__ = "experiences"
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True)
    contenu = Column(Text)
    score_ia = Column(Integer, default=0)
    statut_validation = Column(String, default="EN_ATTENTE")
    auteur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    # embedding = Column(Vector(384)) # Décommenter quand pgvector est completement installe
""",

r"backend\app\schemas\experience_schema.py": """from pydantic import BaseModel

class ExperienceBase(BaseModel):
    titre: str
    contenu: str

class ExperienceCreate(ExperienceBase):
    pass

class ExperienceResponse(ExperienceBase):
    id: int
    score_ia: int
    statut_validation: str

    class Config:
        from_attributes = True
""",

r"backend\app\schemas\auth_schema.py": """from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    mot_de_passe: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
""",

r"backend\app\ia\embeddings.py": """# from sentence_transformers import SentenceTransformer
# model = SentenceTransformer('all-MiniLM-L6-v2')

def generer_embedding(texte: str) -> list[float]:
    # TODO: Remplacer par model.encode(texte).tolist()
    return [0.0] * 384
""",

r"backend\app\ia\filtrage_intelligent.py": """MOTS_INTERDITS = ["insulte1", "insulte2", "spam"]

def est_contenu_approprie(texte: str) -> bool:
    texte_min = texte.lower()
    for mot in MOTS_INTERDITS:
        if mot in texte_min:
            return False
    return True
""",

r"backend\app\ia\scoring_qualite.py": """def calculer_score(texte: str) -> int:
    mots = len(texte.split())
    if mots > 100:
        return 9
    elif mots > 50:
        return 7
    return 5
""",

r"backend\app\repositories\repo_experience.py": """from sqlalchemy.orm import Session
from ..modeles.experience_modele import Experience
from ..schemas.experience_schema import ExperienceCreate

def creer_experience(db: Session, exp: ExperienceCreate, auteur_id: int, score: int):
    db_exp = Experience(
        titre=exp.titre,
        contenu=exp.contenu,
        auteur_id=auteur_id,
        score_ia=score
    )
    db.add(db_exp)
    db.commit()
    db.refresh(db_exp)
    return db_exp
""",

r"backend\app\services\service_experience.py": """from sqlalchemy.orm import Session
from ..schemas.experience_schema import ExperienceCreate
from ..repositories import repo_experience
from ..ia.filtrage_intelligent import est_contenu_approprie
from ..ia.scoring_qualite import calculer_score

def publier_nouvelle_experience(db: Session, exp: ExperienceCreate, auteur_id: int):
    if not est_contenu_approprie(exp.contenu):
        raise ValueError("Contenu inapproprié détecté.")
    score = calculer_score(exp.contenu)
    return repo_experience.creer_experience(db, exp, auteur_id, score)
""",

r"backend\app\routes\experiences_api.py": """from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..coeur.base_de_donnees import get_db
from ..schemas.experience_schema import ExperienceCreate, ExperienceResponse
from ..services.service_experience import publier_nouvelle_experience

router = APIRouter(prefix="/experiences", tags=["Experiences"])

@router.post("/", response_model=ExperienceResponse)
def creer_experience(exp: ExperienceCreate, db: Session = Depends(get_db)):
    try:
        # TODO: dynamiser l'ID auteur via le token JWT
        return publier_nouvelle_experience(db, exp, auteur_id=1)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
""",

r"backend\app\routes\recommandations_api.py": """from fastapi import APIRouter

router = APIRouter(prefix="/recommandations", tags=["Recommandations"])

@router.get("/{experience_id}")
def obtenir_similaires(experience_id: int):
    # TODO: Logique de pgvector (cosine distance)
    return {"message": "Liste des expériences similaires en cours de dev"}
""",


# FRONTEND
r"frontend\package.json": """{
  "name": "plateforme-experiences",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "axios": "^1.6.7",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.22.0"
  }
}
""",

r"frontend\src\App.jsx": """import { BrowserRouter, Routes, Route } from 'react-router-dom';
import BarreNavigation from './composants/BarreNavigation';
import FilActualite from './pages/FilActualite';
import PublierExperience from './pages/PublierExperience';
import ConnexionInscription from './pages/ConnexionInscription';
import TableauBordAdmin from './pages/TableauBordAdmin';
import { AuthProvider } from './contextes/ContexteAuthentification';

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <BarreNavigation />
        <main style={{ padding: '20px' }}>
          <Routes>
            <Route path="/" element={<FilActualite />} />
            <Route path="/publier" element={<PublierExperience />} />
            <Route path="/login" element={<ConnexionInscription />} />
            <Route path="/admin" element={<TableauBordAdmin />} />
          </Routes>
        </main>
      </BrowserRouter>
    </AuthProvider>
  );
}
""",

r"frontend\src\contextes\ContexteAuthentification.jsx": """import { createContext, useState, useContext } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null); // null si non connecté

  const login = (token) => setUser({ token, role: 'USER' });
  const logout = () => setUser(null);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
""",

r"frontend\src\services_api\client_api.js": """import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
});

// Ajout du token automatiquement à chaque requête
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
""",

r"frontend\src\composants\CarteExperience.jsx": """export default function CarteExperience({ exp }) {
  return (
    <div style={{ border: '1px solid #ccc', padding: '15px', marginBottom: '15px', borderRadius: '8px' }}>
      <h3>{exp.titre}</h3>
      <p>{exp.contenu}</p>
      <small>Score IA : {exp.score_ia}/10 | Statut : {exp.statut_validation}</small>
    </div>
  );
}
""",

r"frontend\src\composants\BarreNavigation.jsx": """import { Link } from 'react-router-dom';
import { useAuth } from '../contextes/ContexteAuthentification';

export default function BarreNavigation() {
  const { user, logout } = useAuth();

  return (
    <nav style={{ background: '#333', padding: '15px', color: 'white', display: 'flex', gap: '15px' }}>
      <Link to="/" style={{ color: 'white', textDecoration: 'none' }}>Accueil</Link>
      <Link to="/publier" style={{ color: 'white', textDecoration: 'none' }}>Publier</Link>
      <Link to="/admin" style={{ color: 'white', textDecoration: 'none' }}>Admin</Link>
      
      <div style={{ marginLeft: 'auto' }}>
        {user ? (
          <button onClick={logout}>Déconnexion</button>
        ) : (
          <Link to="/login" style={{ color: 'white', textDecoration: 'none' }}>Connexion</Link>
        )}
      </div>
    </nav>
  );
}
""",

r"frontend\src\composants\ListeRecommandations.jsx": """export default function ListeRecommandations() {
  return (
    <div style={{ marginTop: '20px', padding: '10px', background: '#f5f5f5' }}>
      <h4>Recommandations similaires (IA)</h4>
      <p>Bientôt disponible...</p>
    </div>
  );
}
""",

r"frontend\src\pages\FilActualite.jsx": """import { useState, useEffect } from 'react';
import api from '../services_api/client_api';
import CarteExperience from '../composants/CarteExperience';

export default function FilActualite() {
  const [experiences, setExperiences] = useState([
    { id: 1, titre: "Dev React à Paris", contenu: "Super expérience dans une startup...", score_ia: 8, statut_validation: "PUBLIE" },
    { id: 2, titre: "Data Engineer (Télétravail)", contenu: "J'ai mis en place un pipeline de données complet avec Airflow.", score_ia: 9, statut_validation: "PUBLIE" }
  ]);

  useEffect(() => {
    // api.get('/experiences').then(res => setExperiences(res.data));
  }, []);

  return (
    <div>
      <h2>Fil d'Actualité</h2>
      {experiences.map(exp => (
        <CarteExperience key={exp.id} exp={exp} />
      ))}
    </div>
  );
}
""",

r"frontend\src\pages\PublierExperience.jsx": """import { useState } from 'react';
import api from '../services_api/client_api';

export default function PublierExperience() {
  const [titre, setTitre] = useState('');
  const [contenu, setContenu] = useState('');

  const submit = async (e) => {
    e.preventDefault();
    try {
      // await api.post('/experiences', { titre, contenu });
      alert('Publié avec succès !');
      setTitre(''); setContenu('');
    } catch (err) {
      alert('Erreur: ' + (err.response?.data?.detail || err.message));
    }
  };

  return (
    <div>
      <h2>Partager une Expérience</h2>
      <form onSubmit={submit} style={{ display: 'flex', flexDirection: 'column', gap: '10px', maxWidth: '400px' }}>
        <input placeholder="Titre" value={titre} onChange={(e) => setTitre(e.target.value)} required />
        <textarea placeholder="Votre expérience détaillée..." rows={5} value={contenu} onChange={(e) => setContenu(e.target.value)} required />
        <button type="submit">Soumettre</button>
      </form>
    </div>
  );
}
""",

r"frontend\src\pages\ConnexionInscription.jsx": """import { useState } from 'react';
import { useAuth } from '../contextes/ContexteAuthentification';

export default function ConnexionInscription() {
  const { login } = useAuth();
  const [email, setEmail] = useState('');
  const [mdp, setMdp] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();
    // Normalement api.post('/auth/login')
    login("fake-jwt-token-123");
    alert("Connecté !");
  };

  return (
    <div>
      <h2>Connexion</h2>
      <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '10px', maxWidth: '300px' }}>
        <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
        <input type="password" placeholder="Mot de passe" value={mdp} onChange={e => setMdp(e.target.value)} />
        <button type="submit">Se connecter</button>
      </form>
    </div>
  );
}
""",

r"frontend\src\pages\TableauBordAdmin.jsx": """export default function TableauBordAdmin() {
  return (
    <div>
      <h2>Tableau de Bord Administrateur</h2>
      <p>Espace de modération des contenus signalés.</p>
    </div>
  );
}
""",

r"scripts\installer_tout.sh": """#!/bin/bash
echo "Installation des dépendances Backend..."
# cd backend && pip install -r exigences.txt

echo "Installation des dépendances Frontend..."
# cd frontend && npm install
""",

r"scripts\demarrer_local.sh": """#!/bin/bash
echo "Lancement Base de données (Docker)..."
# docker-compose up -d

echo "Lancement Backend API..."
# cd backend && uvicorn app.main:app --reload &

echo "Lancement Frontend..."
# cd frontend && npm run dev &
""",

r"docker-compose.yml": """version: '3.8'
services:
  db:
    image: pgvector/pgvector:pg16
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: nom_base
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
"""
}

for rel_path, code in files_code.items():
    full_path = os.path.join(base_path, rel_path)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            old_content = f.read()
        
        # Avoid duplicate code appending
        if "from fastapi import" in old_content or "import React" in old_content or "export default" in old_content:
            continue
            
        new_content = old_content.strip() + "\n\n" + code
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    else:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(code)

print("Le plein de code a ete injecte dans toutes les pages !")
