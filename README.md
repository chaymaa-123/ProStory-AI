# Connex

Plateforme sociale innovante dédiée au partage d'expériences professionnelles, enrichie par l'intelligence artificielle pour l'extraction d'insights stratégiques.

## 🎯 Vision du Projet

Connex transforme les récits professionnels bruts en données exploitables pour les utilisateurs et les entreprises. Notre mission est de créer un espace sécurisé où les expériences partagées deviennent une source d'informations stratégiques grâce à l'analyse par IA.

---

## 🛠 Stack Technique

### Frontend
- **Next.js 16** - Framework React moderne avec SSR
- **TailwindCSS** - Design system responsive
- **Radix UI** - Composants accessibles
- **Lucide React** - Icônes modernes
- **Recharts** - Visualisations de données

### Backend
- **FastAPI** - API REST performante avec documentation auto-générée
- **Python 3.10+** - Écosystème riche pour l'IA
- **JWT + Bcrypt** - Authentification sécurisée (utilisateurs + entreprises)
- **Pydantic** - Validation des données
- **Architecture microservices** : Séparation claire des responsabilités (User, Company, AI)

### Base de Données
- **Supabase (PostgreSQL)** - Base de données scalable
- **pgvector** - Stockage d'embeddings vectoriels

### Intelligence Artificielle
- **sentence-transformers** - Embeddings sémantiques
- **transformers (Hugging Face)** - Analyse de texte
- **KeyBERT** - Extraction de mots-clés
- **PyTorch** - Framework d'apprentissage profond
- **NumPy** - Calculs scientifiques

---

## � Démarrage Rapide

### Prérequis
- [Docker](https://www.docker.com/products/docker-desktop/) (Recommandé)
- [Node.js](https://nodejs.org/) (v18+)
- [Python](https://www.python.org/downloads/) (v3.10+)
- Compte [Supabase](https://supabase.com/)

### 1. Cloner le dépôt
```bash
git clone <URL_DU_DEPOT_GITHUB>
cd prostory-ai
```

### 2. Configuration Supabase
1. Créez un projet sur [supabase.com/dashboard](https://supabase.com/dashboard)
2. Activez l'extension `pgvector` dans Settings > Database > Extensions
3. Récupérez vos clés API dans Settings > API

### 3. Lancement avec Docker (Recommandé) 🐳
```bash
# Copier et configurer les variables d'environnement
cp .env.example .env
# Éditer .env avec vos clés Supabase

# Lancer l'application complète
docker-compose up -d
```

L'application sera disponible sur :
- Frontend : http://localhost:3001
- Backend API : http://localhost:8000
- Documentation API : http://localhost:8000/docs

### 4. Arrêter l'application
```bash
docker-compose down
```

---

## 📋 Fonctionnalités Principales

### 🔄 Pipeline IA Complet
- **Analyse de sentiment** : Évalue les émotions dans les récits
- **Extraction de mots-clés** : Identifie les thèmes principaux
- **Embeddings sémantiques** : Recherche intelligente par similarité
- **Dashboard analytique** : Insights pour les entreprises

### 👥 Fonctionnalités Sociales
- **Authentification sécurisée** : JWT + Bcrypt
- **Fil d'actualité** : Consultation des expériences communautaires
- **Interactions** : Likes, commentaires, sauvegardes
- **Recherche avancée** : Filtrage par secteur et mots-clés

### 🏢 Plateforme Entreprise (B2B)
Connex offre une solution complète pour les entreprises souhaitant analyser leur marque employeur et les retours d'expérience :

- **Dashboard Analytics** : Interface dédiée avec visualisations en temps réel
- **Insights Stratégiques** : Analyse des tendances et émotions des employés
- **Perception Employeur** : Score de sentiment global et évolution temporelle
- **Benchmarking Sectoriel** : Comparaison avec les entreprises du même secteur
- **Alertes et Notifications** : Suivi des mentions et nouvelles expériences
- **Exports de Données** : Rapports personnalisables (PDF, Excel, CSV)
- **Gestion de Profil Entreprise** : Informations publiques et branding
- **Événements Corporatifs** : Publication d'événements et actualités

---

## � Architecture du Projet

```
ProStory-AI/
├── backend/                 # FastAPI
│   ├── app/
│   │   ├── ai/               # Modules IA (sentiment, keywords, analytics)
│   │   ├── coeur/            # Configuration Supabase & sécurité
│   │   ├── repositories/     # Accès aux données
│   │   ├── routes/           # Endpoints API
│   │   ├── services/         # Logique métier
│   │   └── schemas/          # Validation Pydantic
│   ├── seed_poc_data.py      # Données de démonstration
│   └── requirements.txt
├── frontend/                  # Next.js 16
│   ├── app/                  # Pages et layouts
│   ├── components/           # Composants UI
│   ├── lib/                 # Utilitaires et client API
│   └── package.json
├── docker-compose.yml         # Orchestration complète
├── rapport.md               # Rapport de projet détaillé
└── README.md
```

---

## 🔧 Développement Local

### Backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
```

---

## 📊 API Endpoints

### Authentification
- `POST /api/auth/login` - Connexion utilisateur
- `POST /api/auth/register` - Inscription

### Expériences
- `GET /experiences` - Lister les expériences
- `POST /experiences` - Créer une expérience
- `GET /experiences/{id}` - Détails d'une expérience
- `POST /experiences/{id}/like` - Liker une expérience
- `POST /experiences/{id}/comment` - Commenter une expérience

### Entreprise (B2B)
- `GET /api/company/profile/{id}` - Profil entreprise
- `POST /api/company/profile` - Créer/modifier profil
- `GET /api/company/events/{id}` - Événements entreprise
- `POST /api/company/events` - Créer événement
- `GET /api/company/analytics/{id}` - Dashboard analytics

### Analyse IA
- `POST /ai/analyze` - Analyser un texte
- `GET /ai/company-insights/{company_id}` - Insights entreprise
- `GET /ai/sentiment-trends/{company_id}` - Tendances sentiment
- `GET /ai/keywords-analysis/{company_id}` - Analyse mots-clés

### Documentation complète : http://localhost:8000/docs

---

## 🎯 Méthodologie de Développement

Nous adoptons une approche **Feature-Based Workflow** :

1. **Authentification** : Système de connexion sécurisé
2. **Publication** : Création et partage d'expériences
3. **Feed** : Affichage dynamique du contenu
4. **Interactions** : Likes, commentaires, favoris
5. **Pipeline IA** : Analyse sémantique et extraction d'insights
6. **Dashboard** : Interface analytique pour entreprises
7. **Finition** : Tests, sécurité, optimisation

---

## 🤝 Contribuer

1. Forker le projet
2. Créer une branche : `git checkout -b feature/nom-de-la-feature`
3. Commiter les changements : `git commit -m 'Ajout de la feature X'`
4. Pousser : `git push origin feature/nom-de-la-feature`
5. Ouvrir une Pull Request

---

## 📝 License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour détails.

---

## 🔗 Liens Utiles

- **Documentation API** : http://localhost:8000/docs
- **Dashboard Supabase** : https://supabase.com/dashboard
- **Rapport de projet** : [rapport.md](./rapport.md)
- **Issues** : [GitHub Issues](https://github.com/chaymaa-123/ProStory-AI/issues)

---

## 📈 Roadmap

### Version 1.0 (Actuelle)
- ✅ Authentification sécurisée
- ✅ Pipeline IA complet
- ✅ Dashboard entreprise
- ✅ Fil d'actualité

### Version 2.0 (En cours)
- 🔄 Agent conversationnel IA
- 🔄 Système de certification
- 🔄 Analyse prédictive
- 🔄 Gamification

### Version 3.0 (Futur)
- 📋 Blockchain pour vérification
- 📋 Dashboard analytique avancé
- 📋 Expansion B2B

---

**Connex - Transformons les expériences en insights stratégiques** 🚀
