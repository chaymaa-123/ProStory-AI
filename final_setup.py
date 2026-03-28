import os

base_path = r"C:\Users\hp\Desktop\Projet_Pfa"

# Mapping: { Path: (Detailed Comment, Default Skeleton) }
files_data = {
# DATABASE
r"base_de_donnees\schema.sql": (
"""/*
1. Objectif du fichier : Définir la structure des tables et activer l'extension pgvector.
2. Contenu prévu : Création des tables (utilisateurs, experiences, tags).
3. Responsable : Database / Data.
4. Interactions : Utilisé par PostgreSQL au démarrage ; contraint les Modèles du Backend.
5. Checklist de ce qu'on va coder dedans :
   - [ ] CREATE EXTENSION IF NOT EXISTS vector;
   - [ ] CREATE TABLE utilisateurs (rôle admin/user)
   - [ ] CREATE TABLE experiences (colonne vectorielle pour l'embedding)
*/""", ""),

r"base_de_donnees\donnees_test.sql": (
"""/*
1. Objectif du fichier : Insérer des données fictives pour faciliter le développement.
2. Contenu prévu : Requêtes INSERT utiles pour test.
3. Responsable : Database.
4. Interactions : Exécuté après schema.sql.
5. Checklist de ce qu'on va coder dedans :
   - [ ] Insérer un compte Admin par défaut
   - [ ] Insérer des expériences factices
*/""", ""),

# BACKEND ENV
r"backend\environnement.env": (
"""# 1. Objectif : Stocker les secrets et configurations locales.
# 2. Contenu prévu : Variables (URL DB, clés secrètes JWT).
# 3. Responsable : Backend.
# 4. Interactions : Lu par config.py.
# 5. Checklist :
#    - [ ] Déclarer DATABASE_URL
#    - [ ] Déclarer JWT_SECRET_KEY""", 
"""DATABASE_URL=
JWT_SECRET_KEY=
ALGORITHM=HS256
"""),

r"backend\exigences.txt": (
"""# 1. Objectif : Lister les bibliothèques Python nécessaires.
# 2. Contenu prévu : Liste des paquets pour pip.
# 3. Responsable : Backend / IA.
# 4. Interactions : Utilisé par pip install.
# 5. Checklist :
#    - [ ] Ajouter fastapi, uvicorn, sqlalchemy, pgvector
#    - [ ] Ajouter sentence-transformers""", 
"""fastapi
uvicorn
sqlalchemy
psycopg2-binary
pgvector
sentence-transformers
python-jose
passlib
python-dotenv
pydantic
"""),

# BACKEND APP
r"backend\app\main.py": (
'''"""
1. Objectif : Point d'entrée principal de l'API FastAPI.
2. Contenu prévu : Initialisation de l'application, configuration CORS, inclusion des routeurs.
3. Responsable : Backend.
4. Interactions : Inclut tout le dossier routes/. Connecté au Frontend.
5. Checklist :
   - [ ] Instancier FastAPI
   - [ ] Configurer les middlewares CORS pour React
   - [ ] app.include_router(...) pour l'auth, les expériences, l'admin
"""''', 
"""from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\ndef read_root():\n    return {'message': 'Hello World'}\n"""),

r"backend\app\coeur\config.py": (
'''"""
1. Objectif : Charger et valider les variables d'environnement.
2. Contenu prévu : Classe Pydantic Settings.
3. Responsable : Backend.
4. Interactions : Lu par base_de_donnees.py et securite.py.
5. Checklist :
   - [ ] Importer .env et exposer un objet settings
"""''',
"""from pydantic_settings import BaseSettings\n\nclass Settings(BaseSettings):\n    database_url: str = ''\n    \n    class Config:\n        env_file = '.env'\n\nsettings = Settings()\n"""),

r"backend\app\coeur\base_de_donnees.py": (
'''"""
1. Objectif : Gérer la connexion à PostgreSQL.
2. Contenu prévu : Création de l'engine SQLAlchemy et du model de session.
3. Responsable : Backend / Database.
4. Interactions : Fournit la DB aux repositories.
5. Checklist :
   - [ ] Créer l'engine et la fonction get_db()
"""''',
"""from sqlalchemy import create_engine\nfrom sqlalchemy.orm import declarative_base\nfrom sqlalchemy.orm import sessionmaker\n\n# Configuration de la base de donnees ici\n\nBase = declarative_base()\n"""),

r"backend\app\coeur\securite.py": (
'''"""
1. Objectif : Gérer les mots de passe et les tokens.
2. Contenu prévu : Fonctions de hachage (bcrypt) et génération JWT.
3. Responsable : Backend.
4. Interactions : Utilisé par service_auth.py et les routes.
5. Checklist :
   - [ ] Coder create_access_token() et verify_password()
"""''',
"""# Logique d'authentification et de hash de mot de passe\n"""),

r"backend\app\modeles\utilisateur_modele.py": (
'''"""
1. Objectif : Mapping objet-relationnel (ORM) de la table utilisateur.
2. Contenu prévu : Classe Utilisateur avec colonnes SQLAlchemy.
3. Responsable : Backend.
4. Interactions : Lu par les repositories.
5. Checklist :
   - [ ] Définir email, mot_de_passe_hash, role
"""''',
"""from sqlalchemy import Column, Integer\nfrom ..coeur.base_de_donnees import Base\n\n# class Utilisateur(Base):\n#     __tablename__ = 'utilisateurs'\n#     id = Column(Integer, primary_key=True, index=True)\n"""),

r"backend\app\modeles\experience_modele.py": (
'''"""
1. Objectif : Mapping ORM de la table expérience.
2. Contenu prévu : Titre, contenu, score_ia, statut_validation, embedding.
3. Responsable : Backend / IA.
4. Interactions : Relation avec Utilisateur et Tags.
5. Checklist :
   - [ ] Définir la colonne embedding = Column(Vector(384))
"""''',
"""from sqlalchemy import Column, Integer\nfrom ..coeur.base_de_donnees import Base\n\n# class Experience(Base):\n#     __tablename__ = 'experiences'\n#     id = Column(Integer, primary_key=True, index=True)\n"""),

r"backend\app\schemas\experience_schema.py": (
'''"""
1. Objectif : Valider les données entrantes/sortantes des requêtes HTTP.
2. Contenu prévu : Classes Pydantic (ExperienceCreate, ExperienceResponse).
3. Responsable : Backend.
4. Interactions : Utilisé par les routes.
5. Checklist :
   - [ ] Créer ExperienceCreate (titre, texte, tags)
"""''',
"""from pydantic import BaseModel\n\n# class ExperienceBase(BaseModel):\n#     pass\n"""),

r"backend\app\schemas\auth_schema.py": (
'''"""
1. Objectif : Valider le login/mot de passe.
2. Contenu prévu : Classes Pydantic pour l'authentification.
3. Responsable : Backend.
4. Interactions : Utilisé par les routes d'authentification.
5. Checklist :
   - [ ] Créer TokenResponse et UserLogin
"""''',
"""from pydantic import BaseModel\n\n# class UserLogin(BaseModel):\n#     pass\n"""),

r"backend\app\ia\embeddings.py": (
'''"""
1. Objectif : Transformer le texte en vecteur pour les recommandations.
2. Contenu prévu : Modèle Sentence-Transformers local.
3. Responsable : IA.
4. Interactions : Appelé quand on crée une expérience.
5. Checklist :
   - [ ] Coder generer_embedding(texte: str) -> list[float]
"""''',
"""# Logique d'embeddings avec sentence-transformers\n"""),

r"backend\app\ia\filtrage_intelligent.py": (
'''"""
1. Objectif : Détecter et bloquer le contenu inapproprié.
2. Contenu prévu : Algorithme de détection de mots ou zero-shot.
3. Responsable : IA.
4. Interactions : Appelé avant d'enregistrer une expérience.
5. Checklist :
   - [ ] Coder est_contenu_approprie(texte) -> bool
"""''',
"""# Logique de filtrage\n"""),

r"backend\app\ia\scoring_qualite.py": (
'''"""
1. Objectif : Noter l'expérience postée.
2. Contenu prévu : Logique basé sur longueur, structure.
3. Responsable : IA.
4. Interactions : Affecte un score à l'expérience.
5. Checklist :
   - [ ] Coder calculer_score(texte) -> int
"""''',
"""# Logique de scoring de l'experience\n"""),

r"backend\app\repositories\repo_experience.py": (
'''"""
1. Objectif : Isoler les requêtes SQL/SQLAlchemy.
2. Contenu prévu : Fonctions CRUD (Créer, trouver par similarité d'embedding).
3. Responsable : Backend / Database.
4. Interactions : Interroge les modèles, appelé par les services.
5. Checklist :
   - [ ] Coder trouver_experiences_similaires(db, vecteur)
"""''',
"""from sqlalchemy.orm import Session\n\n# Fonctions de requetes DB pour Experience\n"""),

r"backend\app\services\service_experience.py": (
'''"""
1. Objectif : Orchestrer IA, Database et Règles Métier.
2. Contenu prévu : Workflow de publication (Filtrer -> Score -> Embedding -> DB).
3. Responsable : Backend.
4. Interactions : Appelle ia/, repositories/, appelé par routes/.
5. Checklist :
   - [ ] Coder publier_nouvelle_experience()
"""''',
"""# Fonctions de logique metier\n"""),

r"backend\app\routes\experiences_api.py": (
'''"""
1. Objectif : Exposer les URLs pour gérer le fil d'actualité et la création.
2. Contenu prévu : GET /experiences, POST /experiences.
3. Responsable : Backend.
4. Interactions : Appelle services/, consommé par le Frontend.
5. Checklist :
   - [ ] Créer route protégée pour créer un post
"""''',
"""from fastapi import APIRouter\n\nrouter = APIRouter()\n"""),

r"backend\app\routes\recommandations_api.py": (
'''"""
1. Objectif : Exposer l'URL pour suggérer du contenu similaire.
2. Contenu prévu : GET /experiences/{id}/similaires.
3. Responsable : Backend.
4. Interactions : Consommé par le composant React de recommandation.
5. Checklist :
   - [ ] Créer la route calculant la distance vectorielle
"""''',
"""from fastapi import APIRouter\n\nrouter = APIRouter()\n"""),

r"backend\app\routes\administration_api.py": (
'''"""
1. Objectif : Outils pour les modérateurs.
2. Contenu prévu : Routes pour supprimer/valider les posts suspendus.
3. Responsable : Backend.
4. Interactions : Vérifie le rôle ADMIN du token.
5. Checklist :
   - [ ] Créer DELETE /admin/experience/{id}
"""''',
"""from fastapi import APIRouter\n\nrouter = APIRouter()\n"""),

# FRONTEND
r"frontend\package.json": (
"""/*
1. Objectif : Lister les dépendances React.
2. Contenu prévu : React, React-Router, Axios.
3. Responsable : Frontend.
4. Interactions : Node.js, npm.
5. Checklist :
   - [ ] Ajouter axios, react-router-dom
*/""",
"""{\n  "name": "frontend",\n  "version": "1.0.0",\n  "dependencies": {}\n}\n"""),

r"frontend\src\App.jsx": (
"""/*
1. Objectif : Cœur de l'application React.
2. Contenu prévu : Configuration du Router.
3. Responsable : Frontend.
4. Interactions : Affiche les pages/.
5. Checklist :
   - [ ] Définir les <Route>
*/""",
"""import React from 'react';\n\nexport default function App() {\n  return (\n    <div>\n      <h1>App</h1>\n    </div>\n  );\n}\n"""),

r"frontend\src\contextes\ContexteAuthentification.jsx": (
"""/*
1. Objectif : Garder la trace de l'utilisateur connecté partout.
2. Contenu prévu : Hook global useAuth() stockant le Token.
3. Responsable : Frontend.
4. Interactions : Protège les pages du front.
5. Checklist :
   - [ ] Créer état user et fonctions login/logout
*/""",
"""import { createContext } from 'react';\n\nexport const AuthContext = createContext(null);\n"""),

r"frontend\src\services_api\client_api.js": (
"""/*
1. Objectif : Centraliser les appels vers l'API FastAPI.
2. Contenu prévu : Instance Axios avec intercepteur de Token JWT.
3. Responsable : Frontend.
4. Interactions : Parle aux routes/ du Backend.
5. Checklist :
   - [ ] Configurer axios.create()
*/""",
"""// Configuration du client API\n"""),

r"frontend\src\composants\CarteExperience.jsx": (
"""/*
1. Objectif : Afficher visuellement un post d'expérience.
2. Contenu prévu : UI avec titre, auteur, score IA, badges.
3. Responsable : Frontend.
4. Interactions : Utilisé par le fil d'actualité.
5. Checklist :
   - [ ] Créer la card React
*/""",
"""import React from 'react';\n\nexport default function CarteExperience() {\n  return (\n    <div>\n      CarteExperience\n    </div>\n  );\n}\n"""),

r"frontend\src\composants\BarreNavigation.jsx": (
"""/*
1. Objectif : Le menu principal en haut de page.
2. Contenu prévu : Liens vers sections.
3. Responsable : Frontend.
4. Interactions : Présent dans App.jsx.
5. Checklist :
   - [ ] Gérer l'affichage conditionnel (connecté/admin)
*/""",
"""import React from 'react';\n\nexport default function BarreNavigation() {\n  return (\n    <nav>\n      BarreNavigation\n    </nav>\n  );\n}\n"""),

r"frontend\src\composants\ListeRecommandations.jsx": (
"""/*
1. Objectif : Afficher l'IA visuellement (Expériences similaires).
2. Contenu prévu : Appelle l'API de reco et affiche des cartes.
3. Responsable : Frontend.
4. Interactions : Apparaît sous le détail d'une expérience.
5. Checklist :
   - [ ] useEffect pour fetch les recommandations
*/""",
"""import React from 'react';\n\nexport default function ListeRecommandations() {\n  return (\n    <div>\n      ListeRecommandations\n    </div>\n  );\n}\n"""),

r"frontend\src\pages\FilActualite.jsx": (
"""/*
1. Objectif : Page d'accueil listant toutes les expériences.
2. Contenu prévu : Menu latéral de filtres et liste.
3. Responsable : Frontend.
4. Interactions : Appelle client_api.js.
5. Checklist :
   - [ ] Gérer les variables d'état pour les filtres
*/""",
"""import React from 'react';\n\nexport default function FilActualite() {\n  return (\n    <div>\n      FilActualite\n    </div>\n  );\n}\n"""),

r"frontend\src\pages\PublierExperience.jsx": (
"""/*
1. Objectif : Page avec le formulaire de création.
2. Contenu prévu : Inputs et soumission.
3. Responsable : Frontend.
4. Interactions : POST l'expérience.
5. Checklist :
   - [ ] Gérer le formulaire et bloquer si filtrage échoue
*/""",
"""import React from 'react';\n\nexport default function PublierExperience() {\n  return (\n    <div>\n      PublierExperience\n    </div>\n  );\n}\n"""),

r"frontend\src\pages\ConnexionInscription.jsx": (
"""/*
1. Objectif : Formulaire sécurisé d'authentification.
2. Contenu prévu : Inputs email, mot de passe.
3. Responsable : Frontend.
4. Interactions : Met à jour AuthContext.
5. Checklist :
   - [ ] Fetch le token et stocker localement
*/""",
"""import React from 'react';\n\nexport default function ConnexionInscription() {\n  return (\n    <div>\n      ConnexionInscription\n    </div>\n  );\n}\n"""),

r"frontend\src\pages\TableauBordAdmin.jsx": (
"""/*
1. Objectif : Back-office pour la modération.
2. Contenu prévu : Tableau de gestion.
3. Responsable : Frontend.
4. Interactions : Appelle routes admin.
5. Checklist :
   - [ ] Vérifier rôle administrateur avant affichage
*/""",
"""import React from 'react';\n\nexport default function TableauBordAdmin() {\n  return (\n    <div>\n      TableauBordAdmin\n    </div>\n  );\n}\n"""),

# SCRIPTS & DOCKER
r"scripts\installer_tout.sh": (
"""# 1. Objectif : Accélérer le setup d'un nouveau développeur.
# 2. Contenu prévu : Commandes pip et npm.
# 3. Responsable : Architecte.
# 4. Interactions : Backend, Frontend.
# 5. Checklist :
#    - [ ] Scripter l'install""", 
"#!/bin/bash\n"),

r"scripts\demarrer_local.sh": (
"""# 1. Objectif : Lancer le projet complet.
# 2. Contenu prévu : docker-compose, npm run dev, uvicorn.
# 3. Responsable : Architecte.
# 4. Interactions : Global.
# 5. Checklist :
#    - [ ] Lancer les processus en parallèle""", 
"#!/bin/bash\n"),

r"docker-compose.yml": (
"""# 1. Objectif : Conteneuriser la base de données.
# 2. Contenu prévu : base postgres avec pgvector.
# 3. Responsable : Database.
# 4. Interactions : DB locale.
# 5. Checklist :
#    - [ ] Déclarer l'image et le volume""", 
"version: '3.8'\nservices:\n  # config...\n")
}

for rel_path, (comment, code) in files_data.items():
    full_path = os.path.join(base_path, rel_path)
    content = comment + "\n\n" + code
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Merge Comments + Empty Skeleton Reussi !")
