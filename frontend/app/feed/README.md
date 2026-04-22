# Tâche : Flux d'Expériences (Feed)

Ce dossier gère le "Mur" principal de ProStory-AI, où les utilisateurs peuvent consulter, chercher et découvrir les expériences professionnelles partagées par la communauté.

## 🚀 Fonctionnalités implémentées

### 1. Affichage du Flux Dynamique
- **Cartes d'expérience (`ExperienceCard`)** : Affichage riche incluant le titre, un aperçu du texte, l'auteur, les tags associés et le sentiment détecté.
- **Indicateurs de sentiment** : Chaque carte affiche visuellement si l'expérience est positive, négative ou neutre (code couleur intuitif).

### 2. Recherche et Filtrage en Temps Réel
- **Barre de recherche intelligente** : Filtrage instantané basé sur le titre, le contenu ou les tags de l'expérience.
- **Optimisation** : Utilisation de `useMemo` pour assurer une fluidité maximale même avec un grand nombre d'expériences affichées.

### 3. Modal de Partage Rapide
- **`QuickExperienceModal`** : Permet à l'utilisateur de publier une nouvelle expérience directement depuis le flux, sans avoir à naviguer vers une autre page.

### 4. Layout Adaptatif (Responsive)
- **Barre latérale (Sidebar)** : Affichage de raccourcis et de catégories sur grand écran, masqué sur mobile pour gagner de l'espace.
- **En-tête collant (Sticky)** : Garde la barre de recherche à portée de main lors du défilement.

## 🛠 Détails Techniques

- **Composants atomiques** : Le flux repose sur une décomposition propre du code (`Sidebar`, `ExperienceCard`, `QuickExperienceModal`) pour une maintenance facilitée.
- **Données Mockées** : Actuellement configuré avec des données de test (`mockExperiences`) pour valider l'interface avant la synchronisation complète avec l'API de feed.

## 📂 Fichiers clés
- `page.tsx` : Contrôleur principal du flux d'actualité.
- `../../../components/ExperienceCard.tsx` : Composant visuel pour chaque histoire partagée.
- `../../../components/QuickExperienceModal.tsx` : Interface de création rapide.
