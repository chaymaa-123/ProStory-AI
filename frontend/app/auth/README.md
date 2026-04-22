# Tâche : Authentification et Gestion des Sessions

Ce dossier est responsable de tout le cycle de vie de l'utilisateur sur ProStory-AI, de sa première inscription à sa déconnexion, en passant par la gestion des rôles.

## 🚀 Fonctionnalités implémentées

### 1. Inscription Multi-Rôles (`/auth/register`)
- **Deux types de comptes** : 
  - **Utilisateur (User)** : Pour ceux qui partagent leurs expériences.
  - **Entreprise (Company)** : Pour les structures qui souhaitent analyser leur image de marque.
- **Formulaire Dynamique** : Les étiquettes et placeholders s'adaptent selon le rôle choisi (ex: "Nom complet" devient "Nom de la structure").
- **Auto-Login** : Une fois inscrit, l'utilisateur est immédiatement connecté sans avoir à repasser par la page de login.

### 2. Connexion Sécurisée (`/auth/login`)
- Interface simplifiée pour l'authentification par email et mot de passe.
- Intégration directe avec **Supabase Auth**.

### 3. Gestion des Sessions (`authService.ts`)
- **Persistence** : Le jeton JWT et les données utilisateur sont stockés dans le `localStorage` pour éviter de se reconnecter à chaque rafraîchissement.
- **Protection des routes** : Logique de redirection selon l'état de connexion.

## 🛠 Détails Techniques

- **Côté Service** : Le fichier `services/authService.ts` centralise tous les appels vers le backend FastAPI. Il gère les erreurs et le stockage local de manière propre.
- **Synchronisation SQL** : Dans Supabase, un "Trigger" SQL est configuré pour que chaque nouvel utilisateur créé dans `auth.users` soit automatiquement ajouté à notre table `public.users` avec le rôle approprié.

## 📂 Fichiers clés
- `register/page.tsx` : Interface d'inscription avec sélecteur de rôle.
- `login/page.tsx` : Interface de connexion.
- `authService.ts` : Cœur de la logique client (Login/Logout/Register).
