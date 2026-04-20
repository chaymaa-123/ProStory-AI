# 🤖 Module IA ProStory-AI

## 📋 Vue d'ensemble

Le module IA fournit des fonctionnalités d'analyse avancée pour les expériences professionnelles partagées sur ProStory-AI. Il combine plusieurs techniques d'IA pour générer des insights pertinents pour les entreprises.

## 🧠 Fonctionnalités

### 1. **Analyse de Sentiment** (`sentiment.py`)
- Utilise **Transformers** de Hugging Face
- Détection des sentiments : Positive, Negative, Neutral
- Score de confiance pour chaque analyse
- Support du batch processing

### 2. **Extraction de Mots-clés** (`keywords.py`)
- Basé sur **KeyBERT** pour l'extraction sémantique
- Support multilingue (configurable)
- Extraction avec scores de pertinence
- Optimisé pour la performance (limitation à 20-30 textes)

### 3. **Génération de Résumés** (`summary.py`)
- Crée des résumés intelligents des analyses
- Identification des tendances
- Génération de recommandations
- Calcul du niveau de confiance

### 4. **Pipeline Principal** (`pipeline.py`)
- Combine toutes les analyses
- Gestion des erreurs robuste
- Limitation pour la performance
- Logging détaillé

### 5. **API REST** (`analytics.py`)
- Endpoints FastAPI pour l'intégration
- Validation des entrées avec Pydantic
- Gestion des erreurs HTTP
- Documentation automatique

## 🚀 Installation

### Dépendances requises
```bash
pip install transformers torch keybert sentence-transformers numpy fastapi uvicorn
```

### Variables d'environnement
```env
# Configuration OpenAI (optionnel)
OPENAI_API_KEY=your-openai-key

# Configuration du serveur
DEBUG=True
HOST=0.0.0.0
PORT=8000
```

## 📡 Endpoints API

### `/api/ai/company/{company_id}/insights`
Analyse les insights pour une entreprise spécifique

**Paramètres :**
- `company_id` (path): ID de l'entreprise
- `max_experiences` (query): Max expériences à analyser (défaut: 30)
- `include_summary` (query): Inclure résumé (défaut: true)

**Réponse :**
```json
{
  "positive": 66.6,
  "negative": 33.3,
  "neutral": 0,
  "total": 3,
  "dominant_sentiment": "positive",
  "keywords": [["management", 2], ["team", 1]],
  "summary": "Cette période, l'entreprise est principalement perçue comme positive...",
  "confidence": "High (based on 120 experiences)",
  "trends": ["Forte perception positive"],
  "recommendations": ["Capitaliser sur les points forts"]
}
```

### `/api/ai/batch/analyze`
Analyse un lot d'expériences

**Body :**
```json
{
  "experiences": [
    {"content": "Great management..."},
    {"content": "Poor communication..."}
  ],
  "max_experiences": 30
}
```

### `/api/ai/test`
Test du pipeline IA avec données fictives

### `/api/ai/health`
Vérification de la santé du service

## 🏗️ Architecture

```
backend/app/ai/
├── __init__.py          # Configuration du module
├── sentiment.py         # Analyse de sentiment (Transformers)
├── keywords.py          # Extraction mots-clés (KeyBERT)
├── summary.py           # Génération de résumés
├── pipeline.py          # Pipeline principal (⭐ IMPORTANT)
├── analytics.py         # Endpoints FastAPI
└── README.md           # Documentation
```

## ⚡ Performance

### Optimisations implémentées
- **Limitation à 30 expériences max** par requête
- **Troncation des textes** à 512 caractères
- **Batch processing** pour les analyses multiples
- **Logging** pour le monitoring
- **Gestion d'erreurs** robuste

### Recommandations
- Utiliser le cache pour les requêtes répétitives
- Implémenter un système de file d'attente pour gros volumes
- Monitorer les temps de réponse

## 🧪 Tests

### Test du pipeline
```python
from app.ai.pipeline import test_pipeline

result = test_pipeline()
print(result)
```

### Test avec curl
```bash
# Test du pipeline
curl http://localhost:8000/api/ai/test

# Insights entreprise
curl http://localhost:8000/api/ai/company/123/insights

# Health check
curl http://localhost:8000/api/ai/health
```

## 🔧 Configuration

### Variables configurables
- `max_experiences`: Nombre max d'expériences (défaut: 30)
- `text_max_length`: Longueur max des textes (défaut: 512)
- `top_keywords`: Nombre de mots-clés (défaut: 5)
- `confidence_threshold`: Seuil de confiance (défaut: 0.7)

### Logging
Le module utilise le logging Python avec niveaux :
- `INFO`: Progression et résultats
- `WARNING`: Problèmes non critiques
- `ERROR`: Erreurs de traitement

## 🚨 Erreurs communes

### Problèmes de mémoire
- **Cause**: Trop d'expériences traitées simultanément
- **Solution**: Limiter `max_experiences` à 30

### Timeout des modèles
- **Cause**: Textes trop longs
- **Solution**: Tronquer les textes à 512 caractères

### Modèles non chargés
- **Cause**: Dépendances manquantes
- **Solution**: Installer toutes les dépendances requises

## 📈 Monitoring

### Métriques importantes
- Temps de réponse moyen
- Nombre d'expériences traitées
- Taux d'erreur
- Utilisation mémoire

### Logs à surveiller
- `Pipeline IA initialisé`
- `Analyse terminée : X expériences`
- `Erreur lors du traitement`

## 🔮 Évolutions futures

### Features prévues
- [ ] Cache Redis pour les résultats
- [ ] Analyse temporelle (évolution dans le temps)
- [ ] Détection de thèmes émergents
- [ ] Analyse comparative entre entreprises
- [ ] Export PDF des rapports

### Améliorations techniques
- [ ] Async processing avec Celery
- [ ] Modèles plus légers
- [ ] Analyse multilingue avancée
- [ ] Personnalisation par secteur

---

*Module IA ProStory-AI v1.0.0*
