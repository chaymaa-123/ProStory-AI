# Tâche : Gestion du Profil Utilisateur (Dashboard)

Ce dossier gère l'identité numérique de l'utilisateur sur la plateforme. Il s'agit d'un tableau de bord interactif affichant son "ADN professionnel" et permettant des modifications en temps réel.

## 🚀 Fonctionnalités implémentées

### 1. Hub d'Identité "Premium"
- **Affichage dynamique** : Présentation du nom, poste actuel, entreprise, ville et années d'expérience avec des effets visuels de haut niveau (glassmorphisme, ombres portées).
- **Compteur de vues** : Suivi du nombre de fois où le profil a été consulté (donnée synchronisée avec Supabase).
- **Badges de statut** : Indicateurs visuels pour le statut "Vérifié" ou "En recherche active".

### 2. Édition "In-Place" (Mode Édition)
- **Bascule de mode** : Passage fluide entre le mode "Lecture" et "Édition" sans changer de page.
- **Modification de la Bio** : Zone de texte riche pour permettre à l'utilisateur de raconter son parcours.
- **Gestion des Tags Dynamiques** : Interface permettant d'ajouter ou de supprimer des compétences, des préférences de travail ("Adore") et des points de douleur ("Évite").

### 3. Liens Sociaux et Réseaux
- Intégration de liens cliquables vers LinkedIn, GitHub et les sites web personnels avec des icônes Lucide.

## 🛠 Détails Techniques

- **Synchronisation Supabase** : Les données sont récupérées via l'endpoint `/auth/profile/{user_id}` et mises à jour via `PUT /auth/profile/update/{id}`.
- **Gestion d'état** : Utilisation intensive de `useState` et `useEffect` pour gérer les données temporaires lors de l'édition avant la sauvegarde finale.
- **Sécurité** : Chaque requête est authentifiée par un jeton Bearer (JWT) stocké localement.

## 📂 Fichiers clés
- `page.tsx` : Le composant principal gérant à la fois l'affichage et le formulaire d'édition du profil.
