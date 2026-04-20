# Dockerfile pour ProStory-AI Backend avec Python 3.12
# Utilise Python 3.12 pour compatibilité complète avec transformers/keybert

FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de dépendances
COPY exigences.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r exigences.txt

# Copier le code de l'application
COPY . .

# Créer le répertoire pour les modèles IA (cache)
RUN mkdir -p /root/.cache/huggingface

# Exposer le port
EXPOSE 8000

# Commande pour lancer l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
