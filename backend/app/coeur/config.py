"""
FICHIER : config.py
OBJECTIF : Gestion des variables d'environnement.
CE QU'IL FAUT FAIRE ICI :
1. Ajouter toute nouvelle clé secrète, URL externe ou paramètre de configuration (ex: API_KEY_OPENAI, URL_FRONTEND).
2. Utiliser `pydantic-settings` si la validation des variables devient complexe.
"""

"""
1. Objectif : Charger et valider les variables d'environnement.
2. Contenu prévu : Classe Pydantic Settings.
3. Responsable : Backend.
4. Interactions : Lu par base_de_donnees.py et securite.py.
5. Checklist :
   - [ ] Importer .env et exposer un objet settings
"""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = ''
    
    class Config:
        env_file = '.env'

settings = Settings()
