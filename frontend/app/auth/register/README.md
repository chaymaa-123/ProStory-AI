# Tâche : Page d'Inscription (Register)

C'est ici que commence l'aventure pour les nouveaux utilisateurs de ProStory-AI.

## 🚀 Fonctionnalités Détaillées

### 1. Sélecteur de Rôle Dynamique
- L'utilisateur peut choisir entre un profil **Utilisateur** ou **Entreprise** via un sélecteur visuel.
- L'interface s'adapte immédiatement (labels des champs, icônes) selon le choix effectué.

### 2. Validation des Données
- Vérification de la correspondance des mots de passe avant l'envoi au serveur.
- Gestion des erreurs d'inscription (ex: email déjà utilisé) avec affichage clair pour l'utilisateur.

### 3. Processus d'Auto-Login
- Pour améliorer l'expérience utilisateur (UX), le système connecte automatiquement l'utilisateur dès que le compte est créé avec succès.
- Redirection automatique vers le formulaire d'ADN professionnel (`/formulaire`) pour les nouveaux inscrits.

## 🛠 Détails Techniques

- **API** : Appelle l'endpoint Backend `POST /auth/register`.
- **Payload** : Envoie le nom, l'email, le mot de passe et le rôle (`user` ou `entreprise`).
- **Composants** : Utilisation intensive de Lucide-React (`Users`, `Building2`) pour une interface moderne.

## 📂 Fichiers
- `page.tsx` : Gestion du formulaire complexe et du choix de rôle.
