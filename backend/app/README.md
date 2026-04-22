# Architecture du Backend (FastAPI)

Ce dossier constitue le "moteur" de ProStory-AI. Il expose une API REST performante permettant au frontend de communiquer avec la base de données Supabase et d'exécuter des analyses IA.

## 🚀 Architecture Globale

### 1. Point d'Entrée (`main.py`)
- **FastAPI** : Framework principal pour sa rapidité et sa gestion native de l'asynchrone.
- **Middleware CORS** : Configuré pour autoriser exclusivement le frontend (`localhost:3000`) à interagir avec l'API.
- **Routage** : Centralisation des routes d'authentification, d'expériences et d'analyse IA.

### 2. Cœur de l'Authentification (`auth.py`)
- **Migration vers Supabase Auth** : Abandon de la gestion manuelle des mots de passe pour utiliser le système sécurisé de Supabase.
- **Triggers SQL** : Utilisation de déclencheurs côté base de données pour synchroniser instantanément les nouveaux comptes `auth.users` avec notre table `public.users`.
- **Génération de Tokens** : Création de Jetons JWT (JSON Web Tokens) pour sécuriser les sessions et les échanges.

### 3. Module d'IA (`ai/`)
C'est ici que réside la valeur ajoutée du projet.
- **Analyse de Sentiment** : Utilisation de modèles Transformers (Hugging Face) pour classer le contenu des expériences (POSITIF / NÉGATIF / NEUTRE).
- **Extraction de Mots-clés** : Utilisation de KeyBERT pour isoler les thèmes principaux d'un témoignage.
- **Optimisation (Lazy Loading)** : Pour éviter que le serveur ne fige au démarrage pendant le téléchargement des modèles (plusieurs centaines de Mo), nous avons mis en place un chargement "paresseux" (à la demande).

## 🛠 Détails Techniques & Sécurité

- **Supabase Client** : Initialisé dans `coeur/base_de_donnees.py`, il permet des opérations CRUD (Create, Read, Update, Delete) ultra-rapides sur PostgreSQL.
- **Validation Pydantic** : Chaque donnée entrante est strictement validée par des schémas (dossier `schemas/`) pour garantir l'intégrité de la base de données.
- **Logging** : Système de logs standardisé pour faciliter le débogage en cas d'erreur IA ou DB.

## 📂 Fichiers clés
- `main.py` : Entrée de l'application et configuration du serveur.
- `auth.py` : Logique de connexion et d'inscription.
- `ai/` : Dossier contenant les pipelines d'Intelligence Artificielle.
- `services/` : Contient la logique métier (calculs, transformations de données).
- `repositories/` : Gère les accès directs aux tables Supabase.
```
