import os
from pathlib import Path
from supabase import create_client
from dotenv import load_dotenv

# Chemin absolu vers le .env à la racine
env_path = Path("C:/Users/hp/Desktop/prostory-ai/.env")
load_dotenv(dotenv_path=env_path)

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_KEY")

if not url or not key:
    print("Erreur: Identifiants introuvables.")
    exit(1)

supabase = create_client(url, key)

def inspect_events():
    try:
        # On tente de provoquer une erreur descriptive
        supabase.table("events").select("non_existent").execute()
    except Exception as e:
        print(f"Colonnes: {str(e)}")

if __name__ == "__main__":
    inspect_events()
