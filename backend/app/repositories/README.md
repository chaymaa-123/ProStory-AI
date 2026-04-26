# Couche Repository - ProStory-AI

Ce dossier contient la logique d'accès aux données (DAL) pour l'application. Chaque fichier correspond à un domaine métier et gère les interactions directes avec Supabase.

## 🗄️ Repositories disponibles

- **`repo_experience.py`** : Cœur de l'application. Gère la création, la lecture et la suppression des expériences.
- **`repo_event.py`** : Gestion du cycle de vie des événements.
- **`repo_insight.py`** : Stockage des analyses IA générées par le module de recommandation.

## 💡 Logique Spécifique : Gestion des Entreprises

Une attention particulière a été portée à la méthode `_get_or_create_company` dans `RepositoryExperience` pour éviter la prolifération de doublons (ex: "Capgemini" créé plusieurs fois).

### Fonctionnement :
1. **Validation UUID** : Si l'utilisateur sélectionne une entreprise existante dans la liste, nous utilisons directement son ID.
2. **Recherche Insensible à la Casse** : Si l'utilisateur saisit un nom manuellement, nous effectuons une recherche `ilike` après avoir nettoyé les espaces (`strip`).
3. **Sécurité Anti-concurrence** : En cas d'erreur lors d'une insertion (si une contrainte unique est présente), le système effectue une dernière recherche pour récupérer l'ID de l'entrée concurrente au lieu d'échouer.

## 🔗 Relations Complexes
Les expériences utilisent des tables de jointure pour maintenir une structure de base de données propre :
- `experience_tags` : Liaison N:N avec les tags.
- `experience_company` : Liaison avec les entreprises.
- `experience_event` : Liaison avec les événements.

Le repository se charge d'aplatir ces relations lors de la lecture (`_format_single_experience`) pour fournir un JSON simple au frontend.
