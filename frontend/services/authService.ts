import api from '@/lib/api';

/**
 * Service authService : Centralise la logique d'authentification.
 * Gère les jetons (tokens) et les données utilisateur en local.
 */
export const authService = {
  
  /**
   * INCRIPTION : Envoie les données et stocke la session si succès (auto-login).
   */
  register: async (userData: any) => {
    try {
      const response = await api.post('/auth/register', userData);
      
      // Si le backend renvoie un token, on connecte l'utilisateur immédiatement
      if (response.data.access_token) {
        authService.setSession(response.data.access_token, response.data.user);
      }
      
      return response.data;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || "Erreur lors de l'inscription");
    }
  },

  /**
   * CONNEXION : Valide les identifiants et stocke la session.
   */
  login: async (credentials: any) => {
    try {
      const response = await api.post('/auth/login', credentials);
      
      if (response.data.access_token) {
        authService.setSession(response.data.access_token, response.data.user);
      }
      
      return response.data;
    } catch (error: any) {
      throw new Error(error.response?.data?.detail || "Identifiants incorrects");
    }
  },

  /**
   * UTILITAIRE : Enregistre le token et l'utilisateur dans le stockage local.
   */
  setSession: (token: string, user: any) => {
    localStorage.setItem('token', token);
    localStorage.setItem('user', JSON.stringify(user));
  },

  /**
   * RÉCUPÉRATION : Retourne l'utilisateur actuellement stocké.
   */
  getCurrentUser: () => {
    if (typeof window === 'undefined') return null;
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
  },

  /**
   * DÉCONNEXION : Nettoie tout et redirige.
   */
  logout: () => {
    localStorage.clear();
    window.location.href = '/auth/login';
  }
};