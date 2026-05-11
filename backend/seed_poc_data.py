import os
import uuid
import random
from app.coeur.base_de_donnees import supabase
from app.recommendations import analyze_text

# --- CONFIGURATION ---
COMPANIES = [
    {"name": "TechNova Solutions", "description": "Leader en innovation logicielle et intelligence artificielle."},
    {"name": "EcoFuture Group", "description": "Pionnier dans les solutions d'énergie renouvelable et durable."}
]

CATEGORIES = ["Technologie", "Management", "Bien-être", "Carrière", "Environnement"]

GOOD_TEMPLATES = [
    "Une expérience incroyable chez {company}. L'équipe est soudée et le projet est passionnant.",
    "J'ai adoré travailler sur le dernier événement de {company}. Une organisation parfaite.",
    "Le management chez {company} est vraiment exemplaire. On se sent écouté.",
    "Superbe opportunité de croissance. J'ai beaucoup appris en peu de temps.",
    "La culture d'entreprise chez {company} est ce qui se fait de mieux."
]

BAD_TEMPLATES = [
    "Déçu par la gestion de projet chez {company}. Trop de pression inutile.",
    "Ambiance toxique dans l'équipe. Je ne recommanderais pas de postuler.",
    "Manque de reconnaissance flagrant. Les efforts ne sont jamais récompensés.",
    "Processus administratifs trop lourds qui ralentissent tout le travail.",
    "Mauvaise communication entre les départements, c'est frustrant au quotidien."
]

NEUTRAL_TEMPLATES = [
    "Travail classique de bureau, rien de spécial à signaler.",
    "Journée de formation habituelle sur les nouveaux outils.",
    "Réunion hebdomadaire pour faire le point sur les dossiers en cours.",
    "Documentation des processus en cours de finalisation.",
    "Participation à un séminaire interne sur la sécurité informatique."
]

def seed_data():
    print("🚀 Démarrage du seeding pour le POC...")

    # 1. Création d'un utilisateur de test
    user_id = str(uuid.uuid4())
    user_data = {
        "id": user_id,
        "name": "Test User POC",
        "email": f"test_poc_{random.randint(1000, 9999)}@example.com",
        "role": "user"
    }
    
    # On insère directement dans public.users (bypass auth.users check si possible)
    # Note: Dans un vrai environnement, il faudrait créer un auth.user d'abord.
    # Ici on assume que le trigger ou la politique permet l'insertion pour le POC.
    try:
        supabase.table("users").upsert(user_data).execute()
        print(f"✅ Utilisateur de test créé: {user_id}")
    except Exception as e:
        print(f"⚠️ Erreur insertion utilisateur (peut-être déjà existant ou RLS): {e}")
        # On essaie de récupérer un utilisateur existant
        res = supabase.table("users").select("id").limit(1).execute()
        if res.data:
            user_id = res.data[0]['id']
            print(f"🔄 Utilisation de l'utilisateur existant: {user_id}")
        else:
            print("❌ Aucun utilisateur disponible. Abandon.")
            return

    # 2. Création des Entreprises (get-or-create pour éviter les doublons)
    company_ids = []
    for comp in COMPANIES:
        # Chercher d'abord si elle existe déjà
        existing = supabase.table("companies").select("id").eq("name", comp['name']).execute()
        if existing.data:
            c_id = existing.data[0]['id']
            company_ids.append(c_id)
            print(f"🔄 Entreprise existante réutilisée: {comp['name']} ({c_id})")
        else:
            res = supabase.table("companies").insert(comp).execute()
            if res.data:
                c_id = res.data[0]['id']
                company_ids.append(c_id)
                print(f"✅ Entreprise créée: {comp['name']} ({c_id})")

    # 3. Création des Événements
    event_ids = []
    for c_id in company_ids:
        event_data = {
            "title": f"Hackathon Annuel {random.randint(2025, 2026)}",
            "description": "Un événement majeur pour l'innovation interne.",
            "date": "2026-06-15T09:00:00Z",
            "location": "Paris, France",
            "category": "Technologie",
            "creator_id": user_id,
            "company_id": c_id
        }
        try:
            res = supabase.table("events").insert(event_data).execute()
            if res.data:
                e_id = res.data[0]['id']
                event_ids.append(e_id)
                print(f"✅ Événement créé pour l'entreprise {c_id}")
        except Exception as e:
            print(f"⚠️ Erreur insertion événement avec tous les champs, tentative simplifiée: {e}")
            # Tentative sans 'category' au cas où le schéma diffère
            simple_event = {
                "title": event_data["title"],
                "description": event_data["description"],
                "date": event_data["date"],
                "location": event_data["location"],
                "creator_id": user_id,
                "company_id": c_id
            }
            try:
                res = supabase.table("events").insert(simple_event).execute()
                if res.data:
                    e_id = res.data[0]['id']
                    event_ids.append(e_id)
                    print(f"✅ Événement créé (version simplifiée) pour {c_id}")
            except Exception as e2:
                print(f"❌ Échec total création événement: {e2}")

    # 4. Génération des 60 Expériences (30 par entreprise)
    for i, c_id in enumerate(company_ids):
        comp_name = COMPANIES[i]['name']
        print(f"✍️ Génération de 30 expériences pour {comp_name}...")
        
        for j in range(30):
            # 10 bonnes, 10 mauvaises, 10 neutres
            if j < 10:
                content = random.choice(GOOD_TEMPLATES).format(company=comp_name)
                title = "Une superbe expérience"
            elif j < 20:
                content = random.choice(BAD_TEMPLATES).format(company=comp_name)
                title = "Assez déçu"
            else:
                content = random.choice(NEUTRAL_TEMPLATES).format(company=comp_name)
                title = "Retour d'expérience"

            exp_data = {
                "user_id": user_id,
                "title": f"{title} #{j+1}",
                "content": content,
                "category": random.choice(CATEGORIES)
            }

            res = supabase.table("experiences").insert(exp_data).execute()
            if res.data:
                exp_id = res.data[0]['id']
                
                # Liaison junction tables
                supabase.table("experience_company").insert({"experience_id": exp_id, "company_id": c_id}).execute()
                
                # Liaison event si disponible
                if len(event_ids) > i and j % 5 == 0:
                    try:
                        supabase.table("experience_event").insert({"experience_id": exp_id, "event_id": event_ids[i]}).execute()
                    except:
                        pass

                # ANALYSE IA (Très important pour les analytics)
                try:
                    analysis = analyze_text(content)
                    insight_data = {
                        "experience_id": exp_id,
                        "sentiment": analysis['sentiment'],
                        "keywords": analysis['keywords'],
                        "score": analysis['confidence']
                    }
                    supabase.table("insights").insert(insight_data).execute()
                except Exception as ia_e:
                    print(f"⚠️ Erreur IA pour exp {exp_id}: {ia_e}")

        print(f"✅ 30 expériences terminées pour {comp_name}")

    print("🏁 Seeding terminé avec succès !")

if __name__ == "__main__":
    seed_data()
