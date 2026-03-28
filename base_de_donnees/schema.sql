/*
1. Objectif du fichier : Définir la structure des tables et activer l'extension pgvector.
2. Contenu prévu : Création des tables (utilisateurs, experiences, tags).
3. Responsable : Database / Data.
4. Interactions : Utilisé par PostgreSQL au démarrage ; contraint les Modèles du Backend.
5. Checklist de ce qu'on va coder dedans :
   - [ ] CREATE EXTENSION IF NOT EXISTS vector;
   - [ ] CREATE TABLE utilisateurs (rôle admin/user)
   - [ ] CREATE TABLE experiences (colonne vectorielle pour l'embedding)
*/

