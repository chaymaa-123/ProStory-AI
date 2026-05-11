"""
Script leger - Cree les companies + evenements a venir dans Supabase
NE necessite PAS la service_role_key (utilise la cle anon)
Les comptes auth (email/password) seront a creer via la Dashboard Supabase.

Usage:
    .\\backend\\venv\\Scripts\\python.exe scripts\\seed_companies_events.py
"""

import os
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "backend"))

from dotenv import load_dotenv
load_dotenv(dotenv_path=ROOT_DIR / ".env")

from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
# Use service role key if available, otherwise anon key
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
if not SUPABASE_KEY or SUPABASE_KEY == "your-service-role-key-here":
    SUPABASE_KEY = os.getenv("SUPABASE_KEY") or os.getenv("SUPABASE_ANON_KEY")

print(f"[INFO] Using Supabase URL: {SUPABASE_URL}")
print(f"[INFO] Key type: {'service_role' if 'service_role' in str(os.getenv('SUPABASE_SERVICE_ROLE_KEY', '')) else 'anon'}")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

COMPANIES = [
    {
        "name":        "TechNova Solutions",
        "description": "Leader en innovation logicielle et intelligence artificielle.",
    },
    {
        "name":        "EcoFuture Group",
        "description": "Pionnier dans les solutions d'energie renouvelable et durable.",
    },
]

UPCOMING_EVENTS = [
    # TechNova (index 0)
    {
        "title":          "Tech Summit 2026 - Casablanca",
        "description":    "Le plus grand rassemblement d'innovation tech de la region MENA.",
        "date":           "2026-05-28T09:00:00+00:00",
        "location":       "Casablanca, Maroc",
        "category":       "Technologie",
        "is_virtual":     False,
        "max_attendees":  1500,
        "company_idx":    0,
    },
    {
        "title":          "AI & Data Day - Rabat",
        "description":    "Journee dediee a l'IA et a la data science.",
        "date":           "2026-06-18T10:00:00+00:00",
        "location":       "Rabat, Maroc",
        "category":       "Technologie",
        "is_virtual":     False,
        "max_attendees":  500,
        "company_idx":    0,
    },
    {
        "title":          "Hackathon Innovation 2026",
        "description":    "48h pour concevoir des solutions tech innovantes.",
        "date":           "2026-07-12T08:00:00+00:00",
        "location":       "Casablanca, Maroc",
        "category":       "Technologie",
        "is_virtual":     False,
        "max_attendees":  300,
        "company_idx":    0,
    },
    # EcoFuture (index 1)
    {
        "title":          "Webinar - Batiments a energie positive",
        "description":    "Comment concevoir des batiments qui produisent plus d'energie.",
        "date":           "2026-05-22T14:00:00+00:00",
        "location":       "En ligne",
        "category":       "Environnement",
        "is_virtual":     True,
        "max_attendees":  1000,
        "company_idx":    1,
    },
    {
        "title":          "Sustainability Week 2026",
        "description":    "Une semaine dediee aux energies propres et au developpement durable.",
        "date":           "2026-06-10T09:00:00+00:00",
        "location":       "Rabat, Maroc",
        "category":       "Environnement",
        "is_virtual":     False,
        "max_attendees":  800,
        "company_idx":    1,
    },
    {
        "title":          "Green Energy Forum",
        "description":    "Forum international sur les energies renouvelables.",
        "date":           "2026-07-05T10:00:00+00:00",
        "location":       "Marrakech, Maroc",
        "category":       "Environnement",
        "is_virtual":     False,
        "max_attendees":  600,
        "company_idx":    1,
    },
]


def get_or_create_company(name, description):
    try:
        res = supabase.table("companies").select("id").eq("name", name).execute()
        if res.data:
            c_id = res.data[0]["id"]
            print(f"   [REUSE] {name} -> {c_id}")
            return c_id
        ins = supabase.table("companies").insert({"name": name, "description": description}).execute()
        c_id = ins.data[0]["id"]
        print(f"   [CREATED] {name} -> {c_id}")
        return c_id
    except Exception as e:
        print(f"   [ERROR] Company '{name}': {e}")
        return None


def get_first_user():
    """Recupere un utilisateur existant pour servir de creator_id."""
    try:
        res = supabase.table("users").select("id, email, role").limit(5).execute()
        if res.data:
            # Prefere un user avec role entreprise
            for u in res.data:
                if u.get("role") == "entreprise":
                    print(f"   [INFO] Creator: {u['email']} (entreprise)")
                    return u["id"]
            # Sinon premier disponible
            u = res.data[0]
            print(f"   [INFO] Creator fallback: {u.get('email', u['id'])}")
            return u["id"]
    except Exception as e:
        print(f"   [ERROR] get_first_user: {e}")
    return None


def delete_old_events():
    now_iso = datetime.now(timezone.utc).isoformat()
    try:
        res = supabase.table("events").delete().lt("date", now_iso).execute()
        n = len(res.data) if res.data else 0
        print(f"   [CLEAN] {n} event(s) perime(s) supprimes.")
    except Exception as e:
        print(f"   [WARN] delete old events: {e}")


def create_event(evt, company_id, creator_id):
    title = evt["title"]
    try:
        existing = supabase.table("events").select("id").eq("title", title).execute()
        if existing.data:
            e_id = existing.data[0]["id"]
            print(f"   [REUSE] {title} -> {e_id}")
            return e_id
    except Exception as e:
        print(f"   [WARN] Check existing: {e}")

    # Full payload - try different column combinations
    payloads = [
        # 1. Full payload (schema.sql version)
        {
            "title":         title,
            "description":   evt["description"],
            "date":          evt["date"],
            "location":      evt["location"],
            "category":      evt["category"],
            "is_virtual":    evt.get("is_virtual", False),
            "max_attendees": evt.get("max_attendees"),
            "creator_id":    creator_id,
            "company_id":    company_id,
        },
        # 2. Without is_virtual and max_attendees
        {
            "title":       title,
            "description": evt["description"],
            "date":        evt["date"],
            "location":    evt["location"],
            "category":    evt["category"],
            "creator_id":  creator_id,
            "company_id":  company_id,
        },
        # 3. Without category (minimal)
        {
            "title":       title,
            "description": evt["description"],
            "date":        evt["date"],
            "location":    evt["location"],
            "creator_id":  creator_id,
            "company_id":  company_id,
        },
        # 4. Absolute minimum
        {
            "title":       title,
            "description": evt["description"],
            "date":        evt["date"],
            "creator_id":  creator_id,
        },
    ]

    for i, payload in enumerate(payloads):
        try:
            res = supabase.table("events").insert(payload).execute()
            if res.data:
                e_id = res.data[0]["id"]
                print(f"   [CREATED] {title} -> {e_id} (variant {i+1})")
                return e_id
        except Exception as e:
            err_msg = str(e)
            if i < len(payloads) - 1:
                # Extract the missing column name from error message
                import re
                m = re.search(r"'(\w+)' column", err_msg)
                col = m.group(1) if m else "unknown"
                print(f"   [RETRY] Column '{col}' not found, trying simpler payload...")
            else:
                print(f"   [ERROR] All variants failed for '{title}': {err_msg}")
    return None


def main():
    print("\n" + "="*60)
    print("  Seed Companies + Events - ProStory-AI")
    print("="*60)

    # Step 1: Companies
    print("\n[1/3] Companies...")
    company_ids = []
    for c in COMPANIES:
        c_id = get_or_create_company(c["name"], c["description"])
        company_ids.append(c_id)

    # Step 2: Clean old events
    print("\n[2/3] Cleaning old events...")
    delete_old_events()

    # Step 3: Events (need a creator_id)
    print("\n[3/3] Creating upcoming events...")
    creator_id = get_first_user()
    if not creator_id:
        print("   [WARN] No user found in public.users - events need a creator_id.")
        print("   [WARN] Create a user first (register on the app), then re-run this script.")
    else:
        for evt in UPCOMING_EVENTS:
            idx = evt["company_idx"]
            c_id = company_ids[idx] if idx < len(company_ids) else None
            if c_id:
                create_event(evt, c_id, creator_id)
            else:
                print(f"   [SKIP] No company_id for event: {evt['title']}")

    # Summary
    print("\n" + "="*60)
    print("  DONE - Summary")
    print("="*60)
    print("\n  Companies in DB:")
    for i, name in enumerate([c["name"] for c in COMPANIES]):
        cid = company_ids[i] if i < len(company_ids) else "N/A"
        print(f"    {name} -> {cid}")

    print("\n  Enterprise Login Credentials (to create via Supabase Dashboard):")
    print("    1. TechNova Solutions")
    print("       Email   : technova@prostory.ai")
    print("       Password: TechNova2026!")
    print("       Role    : entreprise")
    print()
    print("    2. EcoFuture Group")
    print("       Email   : ecofuture@prostory.ai")
    print("       Password: EcoFuture2026!")
    print("       Role    : entreprise")
    print()
    print("  -> To create auth accounts, go to:")
    print("     https://supabase.com/dashboard/project/pbiafmzrdzsxfnyogvwp/auth/users")
    print("     Click 'Add user' > 'Create new user' for each enterprise.")
    print()


if __name__ == "__main__":
    main()
