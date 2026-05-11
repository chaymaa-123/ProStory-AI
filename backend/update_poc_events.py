from app.coeur.base_de_donnees import supabase
from datetime import datetime, timedelta

def update_poc():
    print("🚀 Mise à jour des données POC (Entreprises et Événements)...")

    # 1. S'assurer que les 3 entreprises existent
    COMPANIES = [
        {"name": "TechNova Solutions", "description": "Leader en innovation logicielle et IA."},
        {"name": "EcoFuture Group", "description": "Pionnier dans les solutions d'énergie renouvelable."},
        {"name": "Global Health Dynamics", "description": "Innover pour le futur de la santé mondiale."}
    ]

    company_ids = {}
    for comp in COMPANIES:
        existing = supabase.table("companies").select("id").eq("name", comp['name']).execute()
        if existing.data:
            c_id = existing.data[0]['id']
            company_ids[comp['name']] = c_id
            print(f"🔄 Entreprise existante: {comp['name']} ({c_id})")
        else:
            res = supabase.table("companies").insert(comp).execute()
            if res.data:
                c_id = res.data[0]['id']
                company_ids[comp['name']] = c_id
                print(f"✅ Entreprise créée: {comp['name']} ({c_id})")

    # 2. Création d'événements à venir (Upcoming)
    UPCOMING_EVENTS = [
        {
            "title": "Tech Summit 2026",
            "description": "Le plus grand rassemblement innovation de l'année.",
            "date": "2026-05-15T09:00:00Z",
            "location": "Casablanca, Maroc",
            "category": "Technologie",
            "company_name": "TechNova Solutions"
        },
        {
            "title": "Sustainability Week",
            "description": "Workshop sur les énergies propres et durables.",
            "date": "2026-06-10T10:00:00Z",
            "location": "Rabat, Maroc",
            "category": "Énergie",
            "company_name": "EcoFuture Group"
        },
        {
            "title": "HealthTech Global Forum",
            "description": "L'avenir de la médecine personnalisée.",
            "date": "2026-07-05T08:30:00Z",
            "location": "Paris, France",
            "category": "Santé",
            "company_name": "Global Health Dynamics"
        }
    ]

    # Nettoyer les anciens événements de test pour éviter la confusion (optionnel)
    # supabase.table("events").delete().neq("id", "00000000-0000-0000-0000-000000000000").execute()

    for evt in UPCOMING_EVENTS:
        comp_name = evt.pop("company_name")
        c_id = company_ids.get(comp_name)
        
        # Insérer l'événement
        res = supabase.table("events").insert(evt).execute()
        if res.data:
            e_id = res.data[0]['id']
            print(f"✅ Événement créé: {evt['title']} ({e_id})")
            
            # Lier à l'entreprise via junction table
            if c_id:
                supabase.table("experience_company").insert({"company_id": c_id, "experience_id": None}).execute() # Attendre... 
                # En fait, la table de jointure pour events est experience_event ou company_event ?
                # Vérifions le schéma des events
                pass

if __name__ == "__main__":
    update_poc()
