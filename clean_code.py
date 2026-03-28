import os

base_path = r"C:\Users\hp\Desktop\prostory-ai"

files_code = {
# DATABASE
r"base_de_donnees\schema.sql": """-- Fichier pour définir la structure (tables) de la base de données
""",
r"base_de_donnees\donnees_test.sql": """-- Fichier pour les requêtes d'insertion de données de test
""",

# BACKEND ENV
r"backend\environnement.env": """DATABASE_URL=
JWT_SECRET_KEY=
ALGORITHM=
""",
r"backend\exigences.txt": """fastapi
uvicorn
sqlalchemy
psycopg2-binary
pgvector
sentence-transformers
python-dotenv
pydantic
""",

# BACKEND APP
r"backend\app\main.py": """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
""",
r"backend\app\coeur\config.py": """from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()
""",
r"backend\app\coeur\base_de_donnees.py": """from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Mettre en place SQLAlchemy ici

Base = declarative_base()
""",
r"backend\app\coeur\securite.py": """# Logique d'authentification et de hash de mot de passe
""",
r"backend\app\modeles\utilisateur_modele.py": """from ..coeur.base_de_donnees import Base

# Définir le modèle SQLAlchemy Utilisateur
""",
r"backend\app\modeles\experience_modele.py": """from ..coeur.base_de_donnees import Base

# Définir le modèle SQLAlchemy Experience
""",
r"backend\app\schemas\experience_schema.py": """from pydantic import BaseModel

# Définir les schémas Pydantic pour Experience
""",
r"backend\app\schemas\auth_schema.py": """from pydantic import BaseModel

# Définir les schémas Pydantic pour l'Authentification
""",
r"backend\app\ia\embeddings.py": """# Mettre la logique de sentence-transformers ici
""",
r"backend\app\ia\filtrage_intelligent.py": """# Mettre la logique de filtrage ici
""",
r"backend\app\ia\scoring_qualite.py": """# Mettre la logique de scoring ici
""",
r"backend\app\repositories\repo_experience.py": """from sqlalchemy.orm import Session

# Requêtes CRUD liées aux expériences
""",
r"backend\app\services\service_experience.py": """# Logique métier liée aux expériences
""",
r"backend\app\routes\experiences_api.py": """from fastapi import APIRouter

router = APIRouter()

# Routes pour /experiences
""",
r"backend\app\routes\recommandations_api.py": """from fastapi import APIRouter

router = APIRouter()

# Routes pour /recommandations
""",
r"backend\app\routes\administration_api.py": """from fastapi import APIRouter

router = APIRouter()

# Routes pour /admin
""",

# FRONTEND
r"frontend\package.json": """{
  "name": "frontend",
  "version": "1.0.0",
  "dependencies": {}
}
""",
r"frontend\src\App.jsx": """import React from 'react';

export default function App() {
  return (
    <div>
      <h1>App</h1>
    </div>
  );
}
""",
r"frontend\src\contextes\ContexteAuthentification.jsx": """import { createContext } from 'react';

export const AuthContext = createContext(null);
""",
r"frontend\src\services_api\client_api.js": """// Fichier pour configurer axios ou fetch
""",
r"frontend\src\composants\CarteExperience.jsx": """import React from 'react';

export default function CarteExperience() {
  return (
    <div>
      CarteExperience
    </div>
  );
}
""",
r"frontend\src\composants\BarreNavigation.jsx": """import React from 'react';

export default function BarreNavigation() {
  return (
    <nav>
      BarreNavigation
    </nav>
  );
}
""",
r"frontend\src\composants\ListeRecommandations.jsx": """import React from 'react';

export default function ListeRecommandations() {
  return (
    <div>
      ListeRecommandations
    </div>
  );
}
""",
r"frontend\src\pages\FilActualite.jsx": """import React from 'react';

export default function FilActualite() {
  return (
    <div>
      FilActualite
    </div>
  );
}
""",
r"frontend\src\pages\PublierExperience.jsx": """import React from 'react';

export default function PublierExperience() {
  return (
    <div>
      PublierExperience
    </div>
  );
}
""",
r"frontend\src\pages\ConnexionInscription.jsx": """import React from 'react';

export default function ConnexionInscription() {
  return (
    <div>
      ConnexionInscription
    </div>
  );
}
""",
r"frontend\src\pages\TableauBordAdmin.jsx": """import React from 'react';

export default function TableauBordAdmin() {
  return (
    <div>
      TableauBordAdmin
    </div>
  );
}
""",

# SCRIPTS & DOCKER
r"scripts\installer_tout.sh": """#!/bin/bash
# Script bash pour installer le projet
""",
r"scripts\demarrer_local.sh": """#!/bin/bash
# Script bash pour démarrer le projet en local
""",
r"docker-compose.yml": """version: '3.8'
services:
  # Ajouter les services ici
"""
}

# The goal is to KEEP the original comment block (my French comments ending with */ or """) 
comments = {
    r"base_de_donnees\schema.sql": "/*\n1. Objectif : Définir la structure des tables et activer l'extension IA.\n*/",
    r"base_de_donnees\donnees_test.sql": "/*\n1. Objectif : Insérer des données fictives.\n*/",
    r"backend\environnement.env": "# 1. Objectif : Stocker les secrets et config.",
    r"backend\exigences.txt": "# 1. Objectif : Dépendances Python.",
    
    r"backend\app\main.py": '"""\n1. Objectif : Point d\'entrée principale, monter les routeurs.\n"""',
    r"backend\app\coeur\config.py": '"""\n1. Objectif : Charger variables environement.\n"""',
    r"backend\app\coeur\base_de_donnees.py": '"""\n1. Objectif : Connection Database SQLAlchemy\n"""',
    r"backend\app\coeur\securite.py": '"""\n1. Objectif : JWT et Hashing\n"""',
    r"backend\app\modeles\utilisateur_modele.py": '"""\n1. Objectif : Modèle ORM User\n"""',
    r"backend\app\modeles\experience_modele.py": '"""\n1. Objectif : Modèle ORM Experience\n"""',
    r"backend\app\schemas\experience_schema.py": '"""\n1. Objectif : Pydantic schemas (Data Validation)\n"""',
    r"backend\app\schemas\auth_schema.py": '"""\n1. Objectif : Pydantic Auth\n"""',
    r"backend\app\ia\embeddings.py": '"""\n1. Objectif : Génération vectorielle IA\n"""',
    r"backend\app\ia\filtrage_intelligent.py": '"""\n1. Objectif : Anti-spam/Insultes\n"""',
    r"backend\app\ia\scoring_qualite.py": '"""\n1. Objectif : Score texte \n"""',
    r"backend\app\repositories\repo_experience.py": '"""\n1. Objectif : Data Access Layer CRUD\n"""',
    r"backend\app\services\service_experience.py": '"""\n1. Objectif : Business Logic\n"""',
    r"backend\app\routes\experiences_api.py": '"""\n1. Objectif : API router pour les posts\n"""',
    r"backend\app\routes\recommandations_api.py": '"""\n1. Objectif : API router embeddings\n"""',
    r"backend\app\routes\administration_api.py": '"""\n1. Objectif : API router admin\n"""',

    r"frontend\package.json": "// 1. Objectif : Dépendances NPM.",
    r"frontend\src\App.jsx": "// 1. Objectif : React App Root Router.",
    r"frontend\src\contextes\ContexteAuthentification.jsx": "// 1. Objectif : React Context API.",
    r"frontend\src\services_api\client_api.js": "// 1. Objectif : Main Axios caller.",
    r"frontend\src\composants\CarteExperience.jsx": "// 1. Objectif : UI Card Component.",
    r"frontend\src\composants\BarreNavigation.jsx": "// 1. Objectif : Top Navbar UI.",
    r"frontend\src\composants\ListeRecommandations.jsx": "// 1. Objectif : Display Recommendations.",
    r"frontend\src\pages\FilActualite.jsx": "// 1. Objectif : Home Feed.",
    r"frontend\src\pages\PublierExperience.jsx": "// 1. Objectif : Create Post Page.",
    r"frontend\src\pages\ConnexionInscription.jsx": "// 1. Objectif : Auth Pages.",
    r"frontend\src\pages\TableauBordAdmin.jsx": "// 1. Objectif : Dashboard Admin.",
    
    r"scripts\installer_tout.sh": "# 1. Objectif : Run NPM et PIP install.",
    r"scripts\demarrer_local.sh": "# 1. Objectif : Bash dev local.",
    r"docker-compose.yml": "# 1. Objectif : Compose file postgres."
}

for rel_path, code in files_code.items():
    full_path = os.path.join(base_path, rel_path)
    content = comments.get(rel_path, "") + "\n\n" + code
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Réinitialisation vierge réussie !")
