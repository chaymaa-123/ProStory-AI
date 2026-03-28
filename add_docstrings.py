import os

base_path = r"C:\Users\hp\Desktop\prostory-ai"

comments_map = {
    # DATABASE & ENV
    r"backend\app\main.py": '"""\nFICHIER : main.py\nOBJECTIF : Point d\'entrée principal de l\'API FastAPI.\nCE QU\'IL FAUT FAIRE ICI :\n1. Importer et inclure (`app.include_router`) toutes les nouvelles routes (ex: utilisateurs, auth, admin).\n2. Configurer les middlewares CORS pour autoriser le frontend en production.\n3. Ajouter une gestion globale des exceptions si nécessaire.\n"""\n',
    
    r"backend\app\coeur\config.py": '"""\nFICHIER : config.py\nOBJECTIF : Gestion des variables d\'environnement.\nCE QU\'IL FAUT FAIRE ICI :\n1. Ajouter toute nouvelle clé secrète, URL externe ou paramètre de configuration (ex: API_KEY_OPENAI, URL_FRONTEND).\n2. Utiliser `pydantic-settings` si la validation des variables devient complexe.\n"""\n',
    
    r"backend\app\coeur\base_de_donnees.py": '"""\nFICHIER : base_de_donnees.py\nOBJECTIF : Configuration de la connexion PostgreSQL avec SQLAlchemy.\nCE QU\'IL FAUT FAIRE ICI :\n1. Ajuster les paramètres de pool de connexion si l\'application grossit.\n2. Ne pas toucher à `get_db()` sauf si vous implémentez un système asynchrone (asyncpg).\n"""\n',
    
    r"backend\app\coeur\securite.py": '"""\nFICHIER : securite.py\nOBJECTIF : Fonctions utilitaires pour le hachage des mots de passe et les tokens JWT.\nCE QU\'IL FAUT FAIRE ICI :\n1. Implémenter la fonction de décodage/validation du token.\n2. Créer une dépendance FastAPI `get_utilisateur_actuel` pour protéger les routes privées.\n"""\n',
    
    r"backend\app\modeles\utilisateur_modele.py": '"""\nFICHIER : utilisateur_modele.py\nOBJECTIF : Schéma de la table de base de données pour les Utilisateurs.\nCE QU\'IL FAUT FAIRE ICI :\n1. Ajouter les colonnes manquantes (ex: nom, prenom, bio, avatars).\n2. Créer la relation `experiences = relationship(...)` pour lier un utilisateur à ses posts.\n"""\n',
    
    r"backend\app\modeles\experience_modele.py": '"""\nFICHIER : experience_modele.py\nOBJECTIF : Schéma de la table de base de données pour les Expériences (Posts).\nCE QU\'IL FAUT FAIRE ICI :\n1. Décommenter et configurer la colonne `embedding` avec `pgvector`.\n2. Ajouter des champs supplémentaires (ex: domaine_activite, mots_cles, date_publication).\n"""\n',
    
    r"backend\app\schemas\experience_schema.py": '"""\nFICHIER : experience_schema.py\nOBJECTIF : Modèles Pydantic pour valider les données entrantes/sortantes des Expériences.\nCE QU\'IL FAUT FAIRE ICI :\n1. Ajouter des validateurs stricts (ex: longueur minimale du contenu).\n2. Créer `ExperienceUpdate` pour la modification des posts.\n"""\n',
    
    r"backend\app\schemas\auth_schema.py": '"""\nFICHIER : auth_schema.py\nOBJECTIF : Modèles Pydantic pour l\'authentification (Login, Inscription).\nCE QU\'IL FAUT FAIRE ICI :\n1. Ajouter le modèle `UtilisateurCreate` (email, mot de passe, confirmation).\n2. Ajouter le modèle `UtilisateurResponse` (sans le mot de passe hashé !).\n"""\n',
    
    r"backend\app\ia\embeddings.py": '"""\nFICHIER : embeddings.py\nOBJECTIF : Transformer le texte des expériences en vecteurs mathématiques (Embeddings).\nCE QU\'IL FAUT FAIRE ICI :\n1. Remplacer le mock `[0.0] * 384` par un vrai appel de modèle NLP.\n2. Soit utiliser `SentenceTransformer` (local, gratuit), soit l\'API OpenAI (si budget alloué).\n"""\n',
    
    r"backend\app\ia\filtrage_intelligent.py": '"""\nFICHIER : filtrage_intelligent.py\nOBJECTIF : Modération automatique du contenu (anti-spam, vulgarité).\nCE QU\'IL FAUT FAIRE ICI :\n1. Améliorer l\'algorithme : au lieu de mots interdits, utiliser un modèle NLP de classification ou une API spécialisée.\n2. Connecter cette logique à un système de signalement manuel pour les administrateurs.\n"""\n',
    
    r"backend\app\ia\scoring_qualite.py": '"""\nFICHIER : scoring_qualite.py\nOBJECTIF : Évaluer la qualité et la pertinence d\'une expérience partagée pour la mettre en avant.\nCE QU\'IL FAUT FAIRE ICI :\n1. Créer un vrai algorithme d\'évaluation (orthographe, structure, richesse du vocabulaire professionnel).\n2. Utiliser un LLM (ex: Mistral ou GPT) pour générer un score détaillé.\n"""\n',
    
    r"backend\app\repositories\repo_experience.py": '"""\nFICHIER : repo_experience.py\nOBJECTIF : Requêtes SQL SQLAlchemy liées aux expériences.\nCE QU\'IL FAUT FAIRE ICI :\n1. Ajouter une fonction `obtenir_toutes_experiences(db, limites, offset)`.\n2. Ajouter une fonction de recherche sémantique utilisant `pgvector` (ORDER BY embedding <-> vecteur_recherche).\n"""\n',
    
    r"backend\app\services\service_experience.py": '"""\nFICHIER : service_experience.py\nOBJECTIF : Logique métier (Business Logic) pour les expériences.\nCE QU\'IL FAUT FAIRE ICI :\n1. Avant de sauvegarder, appeler `generer_embedding` pour vectoriser le contenu.\n2. Gérer les erreurs proprement (ex: si l\'IA de filtrage échoue).\n"""\n',
    
    r"backend\app\routes\experiences_api.py": '"""\nFICHIER : experiences_api.py\nOBJECTIF : Contrôleurs / Points d\'accès (Endpoints) de l\'API pour les Expériences.\nCE QU\'IL FAUT FAIRE ICI :\n1. Ajouter l\'endpoint `GET /experiences` pour lister le fil d\'actualité.\n2. Utiliser `Depends(get_utilisateur_actuel)` pour sécuriser la création/modification d\'une expérience.\n"""\n',
    
    r"backend\app\routes\recommandations_api.py": '"""\nFICHIER : recommandations_api.py\nOBJECTIF : Endpoints pour le système de recommandation par IA.\nCE QU\'IL FAUT FAIRE ICI :\n1. Implémenter la logique pour trouver les posts les plus proches d\'un ID donné en utilisant pgvector.\n2. Relier cela à l\'historique de lecture d\'un utilisateur pour un feed 100% personnalisé.\n"""\n',

    # FRONTEND
    r"frontend\src\App.jsx": "/**\n * FICHIER : App.jsx\n * OBJECTIF : Composant racine et configuration du routeur (React Router).\n * CE QU'IL FAUT FAIRE ICI :\n * 1. Ajouter les nouvelles routes (ex: /profil, /parametres, /experience/:id).\n * 2. Implémenter des routes privées (PrivateRoute) pour bloquer l'accès aux utilisateurs non connectés.\n */\n",
    
    r"frontend\src\contextes\ContexteAuthentification.jsx": "/**\n * FICHIER : ContexteAuthentification.jsx\n * OBJECTIF : Gérer l'état global de l'utilisateur (connecté/non connecté).\n * CE QU'IL FAUT FAIRE ICI :\n * 1. Lors de l'initialisation, vérifier si un token existe dans localStorage.\n * 2. Créer une fonction pour appeler l'API `/auth/me` afin de récupérer les vraies infos du profil via le token.\n */\n",
    
    r"frontend\src\services_api\client_api.js": "/**\n * FICHIER : client_api.js\n * OBJECTIF : Configuration du client Axios pour communiquer avec le backend FastAPI.\n * CE QU'IL FAUT FAIRE ICI :\n * 1. Remplacer 'http://localhost:8000' par une variable d'environnement `import.meta.env.VITE_API_URL`.\n * 2. Gérer globalement les erreurs 401 (Expiration du token) pour déconnecter l'utilisateur automatiquement.\n */\n",
    
    r"frontend\src\composants\CarteExperience.jsx": "/**\n * FICHIER : CarteExperience.jsx\n * OBJECTIF : Composant visuel pour afficher un aperçu d'une expérience (Card).\n * CE QU'IL FAUT FAIRE ICI :\n * 1. Styliser la carte avec un design moderne (Tailwind ou CSS modules) et un effet de survol (hover).\n * 2. Ajouter les boutons d'interaction : Like (utile), Commenter, Partager.\n * 3. Formater la date de publication (ex: 'Il y a 2 jours').\n */\n",
    
    r"frontend\src\composants\BarreNavigation.jsx": "/**\n * FICHIER : BarreNavigation.jsx\n * OBJECTIF : Menu de navigation principal en haut de l'écran.\n * CE QU'IL FAUT FAIRE ICI :\n * 1. Rendre le design responsive (menu burger sur mobile).\n * 2. Afficher la photo de profil / le nom de l'utilisateur connecté dynamiquement.\n * 3. Mettre en évidence la page active.\n */\n",
    
    r"frontend\src\composants\ListeRecommandations.jsx": "/**\n * FICHIER : ListeRecommandations.jsx\n * OBJECTIF : Afficher la liste des expériences suggérées par l'IA en Sidebar ou en bas d'un post.\n * CE QU'IL FAUT FAIRE ICI :\n * 1. Appeler l'API `/recommandations/:id` dans un useEffect.\n * 2. Afficher une liste cliquable des résultats sous forme de mini-cartes.\n * 3. Gérer l'état de chargement (skeleton loader).\n */\n",
    
    r"frontend\src\pages\FilActualite.jsx": "/**\n * FICHIER : FilActualite.jsx\n * OBJECTIF : Page d'accueil contenant le feed d'expériences de la plateforme.\n * CE QU'IL FAUT FAIRE ICI :\n * 1. Appeler l'API `/experiences` pour récupérer les vraies données depuis PostgreSQL.\n * 2. Implémenter une pagination ou un scroll infini.\n * 3. Ajouter une barre de recherche textuelle combinée avec la recherche vectorielle de l'IA.\n */\n",
    
    r"frontend\src\pages\PublierExperience.jsx": "/**\n * FICHIER : PublierExperience.jsx\n * OBJECTIF : Formulaire permettant à un utilisateur de partager un retour d'expérience.\n * CE QU'IL FAUT FAIRE ICI :\n * 1. Remplacer le textarea basique par un éditeur de texte riche (ex: React Quill) pour formater (Gras, Listes).\n * 2. Gérer les états de chargement (désactiver le bouton pendant la requête, afficher un spinner).\n * 3. Ajouter des champs optionnels (Tags, Secteur d'activité, Anonymat).\n */\n",
    
    r"frontend\src\pages\ConnexionInscription.jsx": "/**\n * FICHIER : ConnexionInscription.jsx\n * OBJECTIF : Page pour la connexion et l'inscription (Authentification).\n * CE QU'IL FAUT FAIRE ICI :\n * 1. Relier le formulaire à l'API backend (`/auth/login`).\n * 2. Sauvegarder le vrai token reçu dans la fonction `login(token)` du contexte.\n * 3. Créer le formulaire de création de compte (Inscription) et gérer les validations de base (mots de passe identiques).\n */\n",
    
    r"frontend\src\pages\TableauBordAdmin.jsx": "/**\n * FICHIER : TableauBordAdmin.jsx\n * OBJECTIF : Interface permettant à l'équipe de modérer et valider les contenus.\n * CE QU'IL FAUT FAIRE ICI :\n * 1. Fetch les expériences ayant le statut 'EN_ATTENTE'.\n * 2. Créer les boutons d'action 'Approuver' ou 'Rejeter'.\n * 3. Afficher les statistiques de la plateforme (nombres d'utilisateurs, scores IA moyens).\n */\n"
}

for rel_path, docstring in comments_map.items():
    full_path = os.path.join(base_path, rel_path)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "FICHIER :" not in content:
            new_content = docstring + "\n" + content
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            # print(f"Commentaires ajoutes a {rel_path}")

print("Ajout de commentaires termine pour tous les fichiers cibles.")
