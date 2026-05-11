# 📊 Trame de Présentation : Plateforme CONNEX (IA & Expériences)

Ce document contient le plan détaillé des 13 diapositives pour votre soutenance.

---

## 🏗️ Slide 1 : Titre & Introduction
- **Visuel :** Logo Connex au centre (`logo.png`)
- **Titre :** **Connex** : Plateforme Intelligente de Partage d'Expériences Professionnelles
- **Sous-titre :** Projet d'Architecture de Données & Intelligence Artificielle - EMSI
- **Présentateurs :**
    - Chaymaa Amdaai
    - Riyadh
    - Mehdi
- **Date :** Mai 2026

---

## 📑 Slide 2 : Sommaire (Agenda)
1.  Contexte et Problématique
2.  La Solution Connex
3.  Objectifs du Projet
4.  Architecture Globale du Système
5.  Stack Technique (Front, Back, Cloud)
6.  Gestion des Données & Supabase
7.  IA : Analyse de Sentiment (BERT)
8.  Extraction de Thèmes & Keywords
9.  Recherche Sémantique (Vector Search)
10. Fonctionnalités Entreprises & Dashboard
11. Ingestion de Données POC (Seeding)
12. Monitoring & Déploiement Docker
13. Conclusion & Perspectives

---

## 🔍 Slide 3 : Contexte et Problématique
- **Le constat :** Difficulté pour les talents de trouver des retours d'expérience authentiques et non censurés.
- **La problématique :** Comment transformer des milliers de témoignages textuels en données exploitables pour les entreprises ?
- **Le besoin :** Une plateforme capable d'analyser le langage naturel pour détecter le ressenti (sentiment) et les sujets critiques.

---

## 💡 Slide 4 : La Solution Connex
- **Concept :** Un réseau social professionnel intelligent où chaque expérience est analysée par une IA.
- **Valeur ajoutée :**
    - **Utilisateurs :** Découvrir des entreprises via des insights objectifs.
    - **Entreprises :** Comprendre la perception de leur marque et agir via des événements ciblés.

---

## 🎯 Slide 5 : Objectifs du Projet
- **Technique :** Architecture découplée FastAPI / Next.js.
- **Analytique :** Automatiser le traitement de texte (NLP) pour générer des scores de perception.
- **UX/UI :** Interface premium et dynamique (Design moderne).
- **Performance :** Recherche vectorielle pour une pertinence accrue.

---

## ⚙️ Slide 6 : Architecture Globale
- **Frontend :** Next.js (App Router) – Interface réactive.
- **Backend :** FastAPI (Python) – Moteur de calcul et API.
- **Database :** Supabase (PostgreSQL) – Stockage relationnel et vectoriel.
- **Pipeline IA :** Traitement asynchrone (Sentiment + Keywords).

---

## 🛠️ Slide 7 : Stack Technique
- **Frontend :** React, TailwindCSS, Shadcn UI.
- **Backend :** Python, FastAPI, Pydantic.
- **IA :** HuggingFace Transformers, KeyBERT, Sentence-Transformers.
- **DevOps :** Docker, Docker-Compose, Supabase Cloud.

---

## 🤖 Slide 8 : Intelligence Artificielle - Sentiment Analysis
- **Modèle :** `nlptown/bert-base-multilingual-uncased-sentiment`.
- **Analyse :** Classification automatique des textes en **Positif**, **Neutre** ou **Négatif**.
- **Objectif :** Alimenter le score de satisfaction global des entreprises.

---

## 🏷️ Slide 9 : Extraction de Mots-Clés
- **Technologie :** Algorithme KeyBERT.
- **Extraction :** Identification automatique des concepts clés (ex: "Management", "Salaire", "Télétravail").
- **Usage :** Visualisation des tendances et nuages de tags dynamiques.

---

## 🚀 Slide 10 : Recherche Sémantique & Vecteurs
- **Innovation :** Utilisation de **pgvector** dans Supabase.
- **Principe :** Recherche basée sur le **sens** des phrases (Embeddings) plutôt que sur les mots exacts.
- **Bénéfice :** Permet de trouver des expériences pertinentes même sans utiliser les mêmes termes.

---

## 📊 Slide 11 : Dashboard Entreprise & Insights
- **Visualisation :** Graphiques interactifs (Satisfaction, Sentiment, Thèmes).
- **Gestion :** Création d'événements (Tech Summits, Webinars) pour interagir avec la communauté.
- **Impact :** Aide les entreprises à améliorer leur culture interne basée sur les feedbacks réels.

---

## 🐳 Slide 12 : Ingestion & Déploiement
- **POC Data :** Script de seeding pour injecter 60+ expériences réalistes.
- **Monitoring :** Containers Docker isolés pour le Frontend et le Backend.
- **Scalabilité :** Préparé pour un déploiement Cloud (AWS/Vercel).

---

## 🏁 Slide 13 : Conclusion & Perspectives
- **Bilan :** Objectifs atteints avec une chaîne complète de traitement IA.
- **Futur :**
    - Ajout de notifications temps réel (WebSockets).
    - Modèle de Machine Learning pour la détection de "Fake News".
    - Version mobile native.

---
*Fin de la présentation - Merci de votre attention*
