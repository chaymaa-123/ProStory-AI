# 📁 Structure Complète du Projet ProStory-AI

## 🎯 Vue d'ensemble
```
ProStory-AI/
├── 📁 backend/                    # API FastAPI + Supabase
├── 📁 frontend/                   # Application Next.js + React 19
├── 📁 base_de_donnees/            # Scripts et schémas DB
├── 📁 scripts/                    # Scripts d'automatisation
├── 📄 README.md                   # Documentation principale
├── 📄 docker-compose.yml          # Configuration PostgreSQL + pgvector
├── 📄 .gitignore                  # Fichiers ignorés par Git
└── 📄 LISEZMOI.md                 # Documentation française
```

---

## 🚀 Backend (FastAPI + Supabase)
```
backend/
├── 📁 app/
│   ├── 📄 main.py                 # Point d'entrée FastAPI
│   ├── 📄 database.py             # Configuration Supabase
│   ├── 📄 models.py               # Modèles Pydantic
│   ├── 📄 auth.py                 # Authentification JWT
│   ├── 📄 stories.py              # Gestion des histoires
│   ├── 📄 recommendations.py      # IA de recommandation
│   └── 📄 search.py               # Recherche sémantique
├── 📄 requirements.txt            # Dépendances Python
├── 📄 .env.example                # Variables d'environnement
└── 📄 exigences.txt               # Spécifications détaillées
```

---

## 🎨 Frontend (Next.js 16 + React 19 + TypeScript)
```
frontend/
├── 📁 app/                        # App Router Next.js 13+
│   ├── 📄 page.tsx                # Page d'accueil
│   ├── 📄 layout.tsx              # Layout principal
│   ├── 📄 globals.css             # Styles globaux
│   ├── 📁 auth/                   # Pages d'authentification
│   ├── 📁 feed/                   # Fil d'actualité
│   ├── 📁 dashboard/              # Tableau de bord
│   │   ├── 📄 page.tsx
│   │   ├── 📁 experiences/
│   │   ├── 📁 insights/
│   │   └── 📁 events/
│   └── 📁 events/                 # Gestion des événements
│       ├── 📄 page.tsx
│       ├── 📁 [id]/
│       └── 📁 create/
├── 📁 components/                 # Composants React
│   ├── 📁 ui/                     # Composants shadcn/ui
│   │   ├── 📄 button.tsx
│   │   ├── 📄 card.tsx
│   │   ├── 📄 dialog.tsx
│   │   ├── 📄 input.tsx
│   │   ├── 📄 tabs.tsx
│   │   └── 📄 ... (autres composants UI)
│   ├── 📄 Navigation.tsx          # Barre de navigation
│   ├── 📄 ExperienceCard.tsx      # Carte d'expérience
│   ├── 📄 EventCard.tsx           # Carte d'événement
│   ├── 📄 AIInsightCard.tsx       # Carte d'insight IA
│   ├── 📄 DashboardLayout.tsx     # Layout dashboard
│   ├── 📄 RichTextEditor.tsx      # Éditeur de texte
│   └── 📄 ... (autres composants)
├── 📁 lib/                        # Utilitaires et configuration
│   ├── 📄 supabase.ts             # Client Supabase
│   ├── 📄 api.ts                  # Client API Axios
│   └── 📄 utils.ts                # Fonctions utilitaires
├── 📁 hooks/                      # Hooks React personnalisés
│   ├── 📄 use-toast.ts
│   └── 📄 use-mobile.ts
├── 📁 public/                     # Fichiers statiques
│   ├── 🖼️ icon.svg
│   ├── 🖼️ placeholder-logo.png
│   └── 🖼️ ... (autres assets)
├── 📄 package.json                # Dépendances NPM
├── 📄 package-lock.json           # Lock des dépendances
├── 📄 tsconfig.json               # Configuration TypeScript
├── 📄 tailwind.config.js          # Configuration TailwindCSS
├── 📄 next.config.mjs             # Configuration Next.js
└── 📄 .gitignore                  # Fichiers ignorés
```

---

## 🗄️ Base de Données
```
base_de_donnees/
├── 📁 schemas/                    # Schémas de base de données
│   ├── 📄 users.sql               # Table utilisateurs
│   ├── 📄 stories.sql             # Table histoires
│   ├── 📄 likes.sql               # Table likes
│   ├── 📄 comments.sql            # Table commentaires
│   └── 📄 recommendations.sql     # Table recommandations IA
├── 📁 migrations/                 # Scripts de migration
└── 📄 seed_data.sql              # Données de test
```

---

## 🔧 Scripts d'Automatisation
```
scripts/
├── 📄 demarrer_local.bat          # Démarrage environnement local
├── 📄 installer_tout.bat          # Installation complète
└── 📄 setup_database.py          # Configuration base de données
```

---

## ⚙️ Fichiers de Configuration
```
ProStory-AI/
├── 📄 docker-compose.yml          # PostgreSQL + pgvector
├── 📄 .gitignore                  # Exclusions Git
├── 📄 README.md                   # Documentation technique
├── 📄 LISEZMOI.md                 # Documentation utilisateur
└── 📄 STRUCTURE_PROJET.md         # Ce fichier
```

---

## 🎯 Architecture Technique

### **Backend Stack**
- **FastAPI** : Framework API Python
- **Supabase** : Base de données PostgreSQL + Auth
- **OpenAI** : IA pour embeddings et recommandations
- **pgvector** : Recherche vectorielle sémantique
- **JWT** : Authentification sécurisée

### **Frontend Stack**
- **Next.js 16** : Framework React full-stack
- **React 19** : Dernière version de React
- **TypeScript** : Typage statique
- **TailwindCSS v4** : Framework CSS moderne
- **shadcn/ui** : Composants UI de qualité
- **Radix UI** : Composants accessibles

### **Base de Données**
- **PostgreSQL** : Base de données principale
- **pgvector** : Extensions pour recherche vectorielle
- **Supabase Auth** : Gestion des utilisateurs

---

## 🔄 Workflow de Développement

### **7 Features Principales**
1. **🔐 Authentification + Users** : Système d'inscription/connexion
2. **📝 Publication d'expérience** : Partage d'histoires professionnelles
3. **📖 Feed (affichage)** : Fil d'actualité des expériences
4. **💬 Interactions** : Likes et commentaires
5. **🤖 IA (cœur du projet)** : Recommandations intelligentes
6. **🔍 Recherche sémantique** : Recherche intelligente
7. **✨ Finition** : UI/UX et tests

---

## 📊 État Actuel du Projet

✅ **Configuration initiale** : Environnement prêt  
✅ **Backend** : API FastAPI + Supabase configuré  
✅ **Frontend** : Next.js + React 19 opérationnel  
✅ **Base de données** : PostgreSQL + pgvector prêt  
🔄 **Features** : Prêt pour développement par fonctionnalités  

---

*Document généré le 9 avril 2026*
