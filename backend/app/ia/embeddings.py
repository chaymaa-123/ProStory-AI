"""
FICHIER : embeddings.py
OBJECTIF : Transformer le texte des expériences en vecteurs mathématiques (Embeddings).
CE QU'IL FAUT FAIRE ICI :
1. Remplacer le mock `[0.0] * 384` par un vrai appel de modèle NLP.
2. Soit utiliser `SentenceTransformer` (local, gratuit), soit l'API OpenAI (si budget alloué).
"""

"""
1. Objectif : Transformer le texte en vecteur pour les recommandations.
2. Contenu prévu : Modèle Sentence-Transformers local.
3. Responsable : IA.
4. Interactions : Appelé quand on crée une expérience.
5. Checklist :
   - [ ] Coder generer_embedding(texte: str) -> list[float]
"""

# Logique d'embeddings avec sentence-transformers
