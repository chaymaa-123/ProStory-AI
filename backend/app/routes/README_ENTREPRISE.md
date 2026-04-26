# API Entreprise & Insights

Ce module gère les données relatives aux entreprises et les agrégations d'insights IA.

## 📡 Routes API (`/api/company`)

- **`GET /search?q=...`** : Recherche en temps réel d'entreprises par nom. Utilisé pour l'autocomplétion dans les formulaires d'expériences et de profil.
- **`GET /{id}/insights`** : Compile les statistiques de toutes les expériences liées à une entreprise spécifique. Retourne le sentiment global et les mots-clés récurrents.

## 🔍 Composant `CompanySearch`
Un composant React réutilisable qui permet de :
1. Rechercher une entreprise existante.
2. Proposer d'utiliser un nom personnalisé si l'entreprise n'est pas trouvée (création automatique côté backend).

## 🗄️ Structure de données
Les entreprises sont liées aux expériences via la table `experience_company` pour permettre une relation many-to-many (une expérience peut techniquement concerner plusieurs entités, et une entreprise a plusieurs expériences).
