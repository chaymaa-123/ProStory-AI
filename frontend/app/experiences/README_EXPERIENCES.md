# Module Expériences (UI & Logique)

Ce module permet aux utilisateurs de partager leurs expériences professionnelles et aux entreprises de recueillir des feedbacks.

## 🎨 Interface Utilisateur (UX)

L'interface a été simplifiée pour offrir une expérience focalisée sur le contenu :
- **Centrage** : Toutes les pages (`Mes Expériences`, `Détails`, `Création`, `Édition`) sont centrées sur l'écran (`max-w-4xl mx-auto`).
- **Layout épuré** : Le `DashboardLayout` a été retiré de ces pages pour supprimer la barre latérale et maximiser l'espace de lecture.
- **Navigation** : Intégration du composant `Navigation` standard pour une navigation fluide.

## ⚙️ Logique Backend & Repository

### Repository (`repo_experience.py`)
- **Liaisons complexes** : Gère les relations via des tables de jonction (`experience_company`, `experience_event`, `experience_tags`).
- **Update Robuste** : La méthode `mettre_a_jour` synchronise automatiquement les tables de liaison si l'entreprise ou l'événement est modifié.
- **Formatage** : Une méthode interne `_format_single_experience` aplatit les réponses complexes de Supabase pour le frontend.

### Intégrations
- **Entreprise** : Utilise le composant `CompanySearch` pour lier une expérience à une entreprise existante ou en créer une "fictive" à la volée.
- **Insights IA** : Chaque expérience génère automatiquement des insights (sentiment, mots-clés) via le module IA lors de sa création.
