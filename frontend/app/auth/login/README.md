# Tâche : Page de Connexion (Login)

Ce dossier gère l'accès des utilisateurs existants à la plateforme ProStory-AI.

## 🚀 Fonctionnalités Détaillées

### 1. Interface de Saisie (UI)
- **Champs sécurisés** : Utilisation de composants `Input` personnalisés avec des icônes `Mail` et `Lock` pour une meilleure ergonomie.
- **Validation en temps réel** : Les champs sont marqués comme `required` pour empêcher l'envoi de formulaires vides.
- **Feedback visuel** : Un indicateur de chargement (`Loader`) s'affiche sur le bouton pendant la vérification des identifiants pour éviter les doubles clics.

### 2. Logique de Redirection Intelligente
Après une connexion réussie, le système redirige l'utilisateur selon son rôle :
- ✨ **Entreprise** : Redirection vers `/dashboard`.
- 👥 **Utilisateur Standard** : Redirection vers `/feed`.

### 3. Gestion des Erreurs
- Capture des erreurs renvoyées par l'API FastAPI (ex: "Identifiants incorrects").
- Affichage dynamique des messages d'erreur dans une bannière rouge animée en haut du formulaire.

## 🛠 Détails Techniques

- **Service** : Utilise la méthode `authService.login()` qui effectue un `POST` vers `/auth/login`.
- **Session** : En cas de succès, le `access_token` et l'objet `user` sont stockés dans le stockage local du navigateur.

## 📂 Fichiers
- `page.tsx` : Contient la structure React et la gestion d'état de la page.
