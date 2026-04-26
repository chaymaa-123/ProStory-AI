# Repository Experience (Backend)

Ce repository gère la logique métier complexe liée aux expériences professionnelles et à leurs relations.

## Fonctionnalités Clés

### 1. Mécanisme "Get or Create" pour les Entreprises
Lors de la création d'une expérience, si un nom d'entreprise est fourni à la place d'un UUID :
- Le repository cherche si une entreprise avec ce nom existe (insensible à la casse).
- Si elle existe, il utilise son ID.
- Sinon, il crée une nouvelle entrée dans la table `companies`.

### 2. Gestion des Tables de Jointure
Conformément au schéma de base de données, les relations sont gérées via des tables pivots :
- `experience_company` : Lie une expérience à une entreprise.
- `experience_event` : Lie une expérience à un événement.
- `experience_tags` : Lie une expérience à des tags.

### 3. Formatage Automatique (Flattening)
La méthode `_format_single_experience` transforme les résultats imbriqués de Supabase en un objet JSON simple et plat, facilitant la consommation par le frontend.

## Méthodes Principales
- `creer_experience` : Gère l'insertion atomique et les liaisons.
- `obtenir_par_id` : Récupère l'expérience avec ses tags et son entreprise associée.
- `mettre_a_jour` : Gère le nettoyage et la ré-insertion des liaisons (tags/entreprise).
- `supprimer` : Assure le nettoyage manuel des tables de jointure.
