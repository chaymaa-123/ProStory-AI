# Tâche : Formulaire ADN (Onboarding)

Ce dossier contient l'expérience d'onboarding "Premium" de ProStory-AI. C'est ici que l'utilisateur définit son profil professionnel détaillé après son inscription.

## 🚀 Fonctionnalités implémentées

### 1. Tunnel d'Onboarding en 3 Étapes
- **Étape 1 : Identité** : Informations de base (Prénom, Nom, Âge, Ville).
- **Étape 2 : Vie Professionnelle** : Poste actuel, domaine d'activité, entreprise/école, et compétences techniques (Hard Skills).
- **Étape 3 : ADN de Travail** : Biographie professionnelle, préférences environnementales ("Ce que tu adores") et irritants ("Ce que tu évites").

### 2. Système de "Tag Clouds" Interactif
- **Suggestions intelligentes** : Une liste de compétences et de préférences courantes est proposée pour faciliter la saisie.
- **Ajout personnalisé** : L'utilisateur peut ajouter ses propres tags s'ils ne sont pas dans les suggestions.
- **Micro-interactions** : Suppression facile des tags via une petite croix sur chaque badge.

### 3. Logique de Sauvegarde et Nettoyage
- **Formatage des données** : Le formulaire nettoie automatiquement les entrées (ex: transforme les chaînes vides en `null`) pour garantir la compatibilité avec la base de données PostgreSQL.
- **Persistance** : Envoi des données via une requête `PUT` authentifiée vers le backend.
- **Finalisation** : Une fois terminé, le statut `is_onboarding_complete` est mis à jour localement pour rediriger l'utilisateur vers le flux (`/feed`).

## 🛠 Détails Techniques

- **Design Premium** : Utilisation d'un dégradé radial sombre et d'effets de flou (backdrop-blur) pour une esthétique moderne et luxueuse.
- **Système de Progression** : Barre de progression dynamique calculée en temps réel selon l'étape actuelle.
- **Icônes Sémantiques** : Utilisation de la bibliothèque Lucide pour illustrer chaque champ du formulaire.

## 📂 Fichiers clés
- `page.tsx` : Le composant monolithique gérant la logique des étapes et la soumission finale.
