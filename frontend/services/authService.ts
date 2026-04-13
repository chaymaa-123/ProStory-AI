import api from '@/lib/api';

/**
 * Service authService
 * Centralise tous les appels API liés à la gestion des utilisateurs.
 */
export const authService = {
  
  /**
   * Inscription (Register)
   * Envoie les données (nom, email, password, role) au backend.
   */
  register: async (userData: any) => {
    try {
      // On utilise l'instance 'api' configurée dans lib/api.ts
      const response = await api.post('/auth/register', userData);
      return response.data;
    } catch (error: any) {
      // On extrait le message d'erreur précis envoyé par FastAPI (ex: "Email déjà utilisé")
      const errorMessage = error.response?.data?.detail || "Une erreur est survenue lors de l'inscription";
      throw new Error(errorMessage);
    }
  },

  /**
   * Connexion (Login)
   * Récupère le Token JWT et le stocke localement pour maintenir la session.
   */
  login: async (credentials: any) => {
    try {
      const response = await api.post('/auth/login', credentials);
      
      // Si la connexion réussit, on reçoit un access_token
      if (response.data.access_token) {
        // On enregistre le Token dans le localStorage du navigateur
        localStorage.setItem('token', response.data.access_token);
        
        // On enregistre aussi les infos de base (nom, rôle) pour l'affichage
        localStorage.setItem('user', JSON.stringify(response.data.user));
      }
      
      return response.data;
    } catch (error: any) {
      // Message d'erreur personnalisé pour le login
      const errorMessage = error.response?.data?.detail || "Identifiants incorrects";
      throw new Error(errorMessage);
    }
  },

//   /**
//    * Déconnexion (Logout)
//    * Nettoie les données de session et redirige.
//    */
//   logout: () => {
//     localStorage.removeItem('token');
//     localStorage.removeItem('user');
//     // On force le rafraîchissement vers la page de login
//     window.location.href = '/auth';
//   },

  /**
   * Récupérer l'utilisateur actuel
   * Utilitaire pour savoir qui est connecté.
   */
  getCurrentUser: () => {
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
  }
};