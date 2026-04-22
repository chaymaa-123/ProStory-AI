# Tâche : Gestion des Événements Professionnels

Ce dossier permet aux utilisateurs de découvrir et de participer à des rassemblements, conférences et ateliers du secteur technologique.

## 🚀 Fonctionnalités implémentées

### 1. Grille de découverte d'événements
- **Affichage structuré** : Les événements (Conférences, Workshops, Webinars, Meetups) sont présentés sous forme de cartes descriptives.
- **Détails riches** : Chaque événement affiche le titre, la date, l'heure, le lieu et une brève description.

### 2. Filtrage par Catégorie
- **Boutons de filtre rapides** : Permet de n'afficher que les événements d'un certain type (ex: uniquement les workshops).
- **Recherche par mot-clé** : Recherche textuelle dans les titres et descriptions.

### 3. Création d'Événements
- Accès direct via un bouton "Créer un événement" pour permettre aux utilisateurs d'organiser leurs propres rencontres.

## 🛠 Maintenance et Correctifs récents (Avril 2026)

- **Correction des Dépendances (Build)** : Nous avons résolu des erreurs critiques "Module not found" en installant manuellement les primitives Radix UI nécessaires aux composants Shadcn (`@radix-ui/react-navigation-menu`, etc.).
- **Mise à jour des Métadonnées (Next.js 15+)** : Migration de la configuration `viewport` vers le standard d'export séparé pour éliminer les avertissements lors de la compilation.

## 📂 Fichiers clés
- `page.tsx` : Page principale de listing des événements.
