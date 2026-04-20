# ProStory-AI

Plateforme de partage d'expériences professionnelles avec IA de recommandation.

## 🎯 Méthodologie de Travail : Feature-Based Workflow

Nous travaillons par fonctionnalités complètes pour une progression rapide et cohérente :

### 🧩 Découpage du Projet en Features

**🔹 Feature 1 : Authentification + Users**
- DB : table users (Supabase Auth)
- Backend : endpoints login/register
- Front : pages login/register
- 🎯 Objectif : système fonctionnel de base

**🔹 Feature 2 : Publication d'expérience**
- DB : table stories
- Backend : POST /stories
- Front : formulaire de publication
- 🎯 Objectif : pouvoir poster

**🔹 Feature 3 : Feed (affichage)**
- Backend : GET /stories
- Front : affichage liste des posts
- 🎯 Objectif : voir les posts

**🔹 Feature 4 : Interaction (likes/commentaires)**
- DB : tables likes, comments
- Backend : endpoints correspondants
- Front : boutons + affichage
- 🎯 Objectif : interactions sociales

**🔹 Feature 5 : IA (cœur du projet)**
- Embeddings avec OpenAI/SentenceTransformers
- Stockage pgvector dans Supabase
- Calcul de similarité
- 🎯 Objectif : recommandations intelligentes

**🔹 Feature 6 : Recherche sémantique**
- Backend : endpoint search
- Front : input recherche
- 🎯 Objectif : recherche intelligente

**🔹 Feature 7 : Finition**
- UI amélioration, sécurité, tests
- 🎯 Objectif : production ready

---

## 🛠 Stack Technique

- **Frontend** : React + TailwindCSS
- **Backend** : FastAPI (Python)
- **Database** : Supabase (PostgreSQL + pgvector)
- **IA** : OpenAI Embeddings / SentenceTransformers
- **Auth** : Supabase Auth

---

## 📋 Prérequis

Avant de commencer, votre machine doit avoir :
- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/) (Version 18+ recommandée)
- [Python](https://www.python.org/downloads/) (Version 3.10+ recommandée)
- [Docker](https://www.docker.com/products/docker-desktop/) (Optionnel - pour développement local avec PostgreSQL)
- Compte [Supabase](https://supabase.com/) (gratuit)

---

## 🚀 Installation Étape par Étape

### 1. Cloner le dépôt

```bash
git clone <URL_DU_DEPOT_GITHUB>
cd prostory-ai
```

### 2. Option A : Docker (Développement Local) 🐳

**Pour utiliser PostgreSQL + pgvector localement avec Docker :**

1. **Lancez Docker Compose** :
   ```bash
   docker-compose up -d
   ```
   Cela démarre PostgreSQL avec pgvector sur `localhost:5432`

2. **Vérifiez que tout fonctionne** :
   ```bash
   docker-compose ps
   ```

3. **Arrêtez les conteneurs** (quand vous avez fini) :
   ```bash
   docker-compose down
   ```

### 2. Option B : Supabase (Cloud) ☁️

1. **Créez un projet Supabase** : [supabase.com/dashboard](https://supabase.com/dashboard)
2. **Activez pgvector** dans votre projet Supabase :
   - Allez dans Settings > Database > Extensions
   - Cherchez "vector" et activez `pgvector`
3. **Récupérez vos clés** :
   - Project URL (Settings > API)
   - anon key et service_role key

### 4. Configuration du Backend (Python / FastAPI)

1. **Allez dans le dossier backend** :
   ```bash
   cd backend
   ```

2. **Créez l'environnement virtuel** :
   ```bash
   python -m venv venv
   ```

3. **Activez l'environnement virtuel** :
   - Sur **Windows** : `.\venv\Scripts\activate`
   - Sur **Mac/Linux** : `source venv/bin/activate`

4. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurez les variables d'environnement** :
   - Copiez `.env.example` vers `.env`
   - Remplissez vos clés Supabase (ou utilisez `localhost:5432` si vous utilisez Docker)

6. **Démarrez le serveur Backend** :
   ```bash
   uvicorn app.main:app --reload
   ```
   L'API est disponible sur : `http://localhost:8000`

---

### 5. Configuration du Frontend (React)

1. **Ouvrez un NOUVEAU terminal** et allez dans le frontend :
   ```bash
   cd frontend
   ```

2. **Installez les dépendances** :
   ```bash
   npm install
   ```

3. **Configurez Supabase dans le frontend** :
   - Créez `.env.local` avec vos clés Supabase
   - Le template est déjà configuré

4. **Démarrez le serveur Frontend** :
   ```bash
   npm run dev
   ```
   Le site est disponible sur : `http://localhost:5173`

---

## 🛠 Guide de Survie Quotidien

**Pour commencer à travailler chaque jour :**
1. **Si vous utilisez Docker** : `docker-compose up -d` (une seule fois)
2. Activer l'environnement Python et lancer `uvicorn`
3. Lancer `npm run dev` dans le frontend

**Si ça plante après un `git pull` :**
- Refaites `npm install` ou `pip install -r requirements.txt`
- Vérifiez les variables d'environnement
- Redémarrez Docker : `docker-compose down && docker-compose up -d`

**Workflow par feature :**
1. Créez une branche : `git checkout -b feature/nom-de-la-feature`
2. Travaillez DB + Backend + Front
3. Testez la feature complète
4. Mergez et passez à la suivante

---

## 📁 Structure du Projet

```
ProStory-AI/
├── backend/                 # FastAPI
│   ├── app/
│   │   ├── coeur/          # Configuration Supabase
│   │   ├── ia/             # Logique IA (embeddings, similarité)
│   │   ├── modeles/        # Modèles de données
│   │   ├── routes/         # Endpoints API
│   │   ├── services/       # Logique métier
│   │   └── schemas/        # Schémas Pydantic
│   └── requirements.txt
├── frontend/               # React
│   ├── src/
│   │   ├── components/     # Composants réutilisables
│   │   ├── pages/          # Pages principales
│   │   ├── services/       # Appels API
│   │   └── utils/          # Utilitaires
│   └── package.json
├── docker-compose.yml      # Configuration Docker (PostgreSQL + pgvector)
└── README.md
```

Chaque feature ajoute des fichiers dans les dossiers correspondants en suivant cette structure.
