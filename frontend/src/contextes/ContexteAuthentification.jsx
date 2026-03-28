/**
 * FICHIER : ContexteAuthentification.jsx
 * OBJECTIF : Gérer l'état global de l'utilisateur (connecté/non connecté).
 * CE QU'IL FAUT FAIRE ICI :
 * 1. Lors de l'initialisation, vérifier si un token existe dans localStorage.
 * 2. Créer une fonction pour appeler l'API `/auth/me` afin de récupérer les vraies infos du profil via le token.
 */

/*
1. Objectif : Garder la trace de l'utilisateur connecté partout.
2. Contenu prévu : Hook global useAuth() stockant le Token.
3. Responsable : Frontend.
4. Interactions : Protège les pages du front.
5. Checklist :
   - [ ] Créer état user et fonctions login/logout
*/

import { createContext } from 'react';

export const AuthContext = createContext(null);
