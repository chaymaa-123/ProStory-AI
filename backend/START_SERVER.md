# 🚀 Lancement du Backend ProStory-AI

## 1️⃣ Prérequis
- Python 3.8+ installé
- Git installé

## 2️⃣ Configuration de l'environnement

```bash
# Naviguer dans le dossier backend
cd backend

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel (Windows)
venv\Scripts\activate

# Activer l'environnement virtuel (Linux/Mac)
source venv/bin/activate

# Installer les dépendances
pip install -r exigences.txt

# Configurer les variables d'environnement
copy .env.example .env
# Éditez .env avec vos clés Supabase/OpenAI
```

## 3️⃣ Démarrage du serveur

### Développement (avec rechargement automatique)
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 4️⃣ Vérification

Le backend sera accessible à :
- **API** : http://localhost:8000
- **Documentation** : http://localhost:8000/docs
- **Alternative docs** : http://localhost:8000/redoc

## 5️⃣ Configuration requise dans .env

```env
# Supabase (obligatoire)
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-anon-key-here
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key-here

# OpenAI (optionnel, pour embeddings avancés)
OPENAI_API_KEY=your-openai-api-key-here

# JWT (obligatoire)
JWT_SECRET=your-jwt-secret-here

# Serveur
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

## 🔧 Problèmes courants

### Erreur : ModuleNotFoundError
```bash
# Réactiver l'environnement virtuel
venv\Scripts\activate
```

### Erreur : Port déjà utilisé
```bash
# Utiliser un autre port
uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

### Erreur : Clés Supabase invalides
- Vérifiez vos clés dans le dashboard Supabase
- Assurez-vous d'utiliser la bonne URL de projet

---

*Serveur prêt à recevoir les requêtes du frontend !*
