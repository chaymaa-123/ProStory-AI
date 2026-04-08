/**
 * FICHIER : client_api.js
 * OBJECTIF : Configuration du client Axios pour communiquer avec le backend FastAPI.
 * CE QU'IL FAUT FAIRE ICI :
 * 1. Remplacer 'http://localhost:8000' par une variable d'environnement `import.meta.env.VITE_API_URL`.
 * 2. Gérer globalement les erreurs 401 (Expiration du token) pour déconnecter l'utilisateur automatiquement.
 */

/*
1. Objectif : Centraliser les appels vers l'API FastAPI.
2. Contenu prévu : Instance Axios avec intercepteur de Token JWT.
3. Responsable : Frontend.
4. Interactions : Parle aux routes/ du Backend.
5. Checklist :
   - [ ] Configurer axios.create()
*/

// Configuration du client API
