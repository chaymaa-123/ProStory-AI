# Authentification et Flux d'Inscription Entreprise

Ce module gère l'authentification sécurisée via Supabase Auth et implémente une logique d'inscription intelligente pour les comptes de type **Entreprise**.

## 🚀 Flux d'Inscription "All-in-One"

Lorsqu'un utilisateur s'inscrit avec le rôle `entreprise`, le système effectue une création en cascade pour garantir l'intégrité des données.

### Étapes du processus :
1. **Frontend** : Le formulaire d'inscription collecte les infos de l'utilisateur + le nom de l'entreprise (`company_name`).
2. **Backend (FastAPI)** : La route `/auth/register` transmet ces données à Supabase Auth via les métadonnées (`options.data`).
3. **Base de Données (Trigger SQL)** : Un trigger `AFTER INSERT` sur `auth.users` intercepte la création et effectue automatiquement :
   - L'insertion dans `public.users` (Identité).
   - La recherche ou création de l'entreprise dans `public.companies` (Entité morale).
   - La création du profil dans `public.profiles` lié à la fois à l'utilisateur et à son entreprise.

## 🛠 Modèles de données
- **UserRegister** : Étendu pour inclure `company_name` optionnel.
- **Rôles supportés** : `user` (par défaut) et `entreprise`.

## 🛡 Sécurité
- Utilisation de **JWT** pour les sessions.
- Intercepteur Axios dans le frontend pour injecter le token et l'ID utilisateur (`x_user_id`) dans les headers.
