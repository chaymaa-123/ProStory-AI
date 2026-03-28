# prostory-ai

Bienvenue sur le dépôt du projet ! Ce document explique à l'équipe de développement comment configurer l'environnement de développement local après avoir récupéré le code.

## 📋 Prérequis

Avant de commencer, votre machine doit avoir ces outils d'installés :
- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/) (Version 18+ recommandée pour exécuter React)
- [Python](https://www.python.org/downloads/) (Version 3.10+ recommandée pour exécuter FastAPI)
- [PostgreSQL](https://www.postgresql.org/download/) en cours d'exécution localement (avec l'extension `pgvector` activée, ou via Docker)

---

## 🚀 Installation Étape par Étape

### 1. Cloner le dépôt

La toute première étape consiste à télécharger le code sur votre ordinateur :

```bash
git clone <URL_DU_DEPOT_GITHUB>
cd prostory-ai
```

### 2. Configuration du Backend (Python / FastAPI)

Le backend requiert un "environnement virtuel" pour que les paquets Python n'interfèrent pas avec le reste de votre ordinateur.

1. **Allez dans le dossier backend :**
   ```bash
   cd backend
   ```

2. **Créez l'environnement virtuel :**
   ```bash
   python -m venv venv
   ```

3. **Activez l'environnement virtuel :**
   - Sur **Windows** : `.\venv\Scripts\activate`
   - Sur **Mac/Linux** : `source venv/bin/activate`
   *(Vous saurez que ça a marché si vous voyez `(venv)` apparaître au début de votre ligne de commande)*

4. **Installez les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurez les variables secrètes :**
   - Prenez le fichier `.env.example` présent dans le dossier backend.
   - Copiez-le et renommez-le en **`.env`**
   - Ouvrez ce fichier `.env` et remplacez les valeurs de `DATABASE_URL` par vos propres identifiants de base de données locale.

6. **Préparez la base de données :**
   - Assurez-vous que PostgreSQL est allumé.
   - Lancez les migrations pour créer les tables automatiquement :
     ```bash
     alembic upgrade head
     ```

7. **Démarrez le serveur Backend :**
   ```bash
   uvicorn app.main:app --reload
   ```
   L'API est maintenant disponible sur : `http://localhost:8000`

---

### 3. Configuration du Frontend (React)

Les fichiers frontend utilisent le gestionnaire de paquets de Node.js (npm).

1. **Ouvrez un NOUVEAU terminal** (laissez le backend tourner dans le premier) et allez dans le frontend :
   ```bash
   cd frontend
   ```

2. **Installez les différents paquets (node_modules) :**
   ```bash
   npm install
   ```

3. **Démarrez le serveur Frontend :**
   ```bash
   npm run dev
   ```
   Le site web est maintenant disponible, généralement sur : `http://localhost:5173`

---

## 🛠 Guide de survie quotidien (Pour l'équipe)

Une fois cette installation initiale terminée, vous n'aurez plus besoin de tout refaire ! 

**À chaque fois que vous commencez à travailler, vous devez juste :**
1. Activer l'environnement Python (`.\venv\Scripts\activate`) et lancer `uvicorn`.
2. Lancer `npm run dev` dans le dossier frontend.

**Si votre code plante après avoir fait un `git pull` :**
- C'est probablement qu'un collègue a ajouté un paquet. Refaites un `npm install` (si c'est le front) ou un `pip install -r requirements.txt` (si c'est le back).
- Si c'est une erreur de base de données, un collègue a dû modifier les tables. Lancez `alembic upgrade head` dans le backend.
