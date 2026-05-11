"""
Script de creation des comptes entreprises + evenements a venir - ProStory-AI POC

Entreprises creees :
  1. TechNova Solutions  -> technova@prostory.ai  / TechNova2026!
  2. EcoFuture Group     -> ecofuture@prostory.ai / EcoFuture2026!

Usage (depuis le dossier racine prostory-ai/) :
    .\\backend\\venv\\Scripts\\python.exe scripts\\setup_enterprise_accounts.py
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

# ── Charger le .env ─────────────────────────────────────────────────────────────
ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT_DIR / ".env"

from dotenv import load_dotenv
load_dotenv(dotenv_path=ENV_PATH)

from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("[ERROR] SUPABASE_URL ou SUPABASE_KEY manquant dans le .env")
    sys.exit(1)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ── Definition des entreprises ───────────────────────────────────────────────────
ENTERPRISES = [
    {
        "name":        "TechNova Solutions",
        "email":       "technova@prostory.ai",
        "password":    "TechNova2026!",
        "description": "Leader en innovation logicielle et intelligence artificielle.",
    },
    {
        "name":        "EcoFuture Group",
        "email":       "ecofuture@prostory.ai",
        "password":    "EcoFuture2026!",
        "description": "Pionnier dans les solutions d'energie renouvelable et durable.",
    },
]

# ── Evenements a venir (apres aujourd'hui 11 mai 2026) ───────────────────────────
UPCOMING_EVENTS_TEMPLATES = [
    # TechNova events (index 0)
    {
        "title":          "Tech Summit 2026 - Casablanca",
        "description":    "Le plus grand rassemblement d'innovation tech de la region MENA. Keynotes, ateliers, networking.",
        "date":           "2026-05-28T09:00:00Z",
        "location":       "Casablanca, Maroc",
        "category":       "Technologie",
        "is_virtual":     False,
        "max_attendees":  1500,
        "enterprise_idx": 0,
    },
    {
        "title":          "AI & Data Day - Rabat",
        "description":    "Journee dediee a l'intelligence artificielle et a la data science.",
        "date":           "2026-06-18T10:00:00Z",
        "location":       "Rabat, Maroc",
        "category":       "Technologie",
        "is_virtual":     False,
        "max_attendees":  500,
        "enterprise_idx": 0,
    },
    {
        "title":          "Hackathon Innovation 2026",
        "description":    "48h pour concevoir des solutions tech innovantes. Equipes de 3-5 personnes.",
        "date":           "2026-07-12T08:00:00Z",
        "location":       "Casablanca, Maroc",
        "category":       "Technologie",
        "is_virtual":     False,
        "max_attendees":  300,
        "enterprise_idx": 0,
    },
    # EcoFuture events (index 1)
    {
        "title":          "Webinar - Batiments a energie positive",
        "description":    "Decouvrez comment concevoir des batiments qui produisent plus d'energie qu'ils n'en consomment.",
        "date":           "2026-05-22T14:00:00Z",
        "location":       "En ligne",
        "category":       "Environnement",
        "is_virtual":     True,
        "max_attendees":  1000,
        "enterprise_idx": 1,
    },
    {
        "title":          "Sustainability Week 2026",
        "description":    "Une semaine dediee aux energies propres, au developpement durable et aux solutions climatiques.",
        "date":           "2026-06-10T09:00:00Z",
        "location":       "Rabat, Maroc",
        "category":       "Environnement",
        "is_virtual":     False,
        "max_attendees":  800,
        "enterprise_idx": 1,
    },
    {
        "title":          "Green Energy Forum",
        "description":    "Forum international sur les energies renouvelables - solaire, eolien, hydrogene vert.",
        "date":           "2026-07-05T10:00:00Z",
        "location":       "Marrakech, Maroc",
        "category":       "Environnement",
        "is_virtual":     False,
        "max_attendees":  600,
        "enterprise_idx": 1,
    },
]


def get_or_create_company(name, description):
    """Retourne l'ID d'une entreprise existante ou la cree."""
    existing = supabase.table("companies").select("id").eq("name", name).execute()
    if existing.data:
        c_id = existing.data[0]["id"]
        print(f"   [REUSE] Entreprise existante: {name} ({c_id})")
        return c_id
    res = supabase.table("companies").insert({"name": name, "description": description}).execute()
    c_id = res.data[0]["id"]
    print(f"   [OK] Entreprise creee: {name} ({c_id})")
    return c_id


def create_auth_user_and_profile(enterprise, company_id):
    """Cree un utilisateur Supabase Auth + entree dans public.users."""
    email    = enterprise["email"]
    password = enterprise["password"]
    name     = enterprise["name"]

    # Verifier si l'utilisateur existe deja dans public.users
    existing_user = supabase.table("users").select("id").eq("email", email).execute()
    if existing_user.data:
        user_id = existing_user.data[0]["id"]
        print(f"   [REUSE] Compte auth deja existant: {email} ({user_id})")
        return user_id

    # Creer le compte Supabase Auth via admin API
    try:
        auth_res = supabase.auth.admin.create_user({
            "email":         email,
            "password":      password,
            "email_confirm": True,
            "user_metadata": {
                "full_name":    name,
                "role":         "entreprise",
                "company_name": name,
            }
        })
        user_id = auth_res.user.id
        print(f"   [OK] Compte Supabase Auth cree: {email} ({user_id})")
    except Exception as e:
        print(f"   [WARN] Impossible de creer le compte auth: {e}")
        # Essayer de recuperer via l'API admin list
        try:
            users_page = supabase.auth.admin.list_users()
            for u in users_page:
                if u.email == email:
                    user_id = u.id
                    print(f"   [REUSE] Compte recupere: {email} ({user_id})")
                    break
            else:
                print(f"   [ERROR] Compte introuvable pour: {email}")
                return None
        except Exception as e2:
            print(f"   [ERROR] Impossible de recuperer l'utilisateur: {e2}")
            return None

    # Attendre que le trigger cree la ligne dans public.users
    time.sleep(0.6)

    # Upsert manuel dans public.users
    try:
        supabase.table("users").upsert({
            "id":    user_id,
            "name":  name,
            "email": email,
            "role":  "entreprise",
        }).execute()
        print(f"   [OK] Profil public.users upsert: {email}")
    except Exception as e:
        print(f"   [WARN] Upsert public.users: {e}")

    return user_id


def delete_outdated_events():
    """Supprime les evenements dont la date est dans le passe."""
    now_iso = datetime.now(timezone.utc).isoformat()
    try:
        res = supabase.table("events").delete().lt("date", now_iso).execute()
        deleted = len(res.data) if res.data else 0
        if deleted:
            print(f"   [CLEAN] {deleted} evenement(s) perime(s) supprime(s).")
        else:
            print("   [INFO] Aucun evenement perime trouve.")
    except Exception as e:
        print(f"   [WARN] Impossible de supprimer les anciens events: {e}")


def create_event(evt_template, company_id, creator_id):
    """Cree un evenement si le titre n'existe pas deja."""
    title = evt_template["title"]
    existing = supabase.table("events").select("id").eq("title", title).execute()
    if existing.data:
        e_id = existing.data[0]["id"]
        print(f"   [REUSE] Evenement existant: {title} ({e_id})")
        return e_id

    payload = {
        "title":         title,
        "description":   evt_template["description"],
        "date":          evt_template["date"],
        "location":      evt_template["location"],
        "category":      evt_template["category"],
        "is_virtual":    evt_template.get("is_virtual", False),
        "max_attendees": evt_template.get("max_attendees"),
        "creator_id":    creator_id,
        "company_id":    company_id,
    }
    try:
        res = supabase.table("events").insert(payload).execute()
        e_id = res.data[0]["id"]
        print(f"   [OK] Evenement cree: {title} ({e_id})")
        return e_id
    except Exception as e:
        print(f"   [ERROR] Creation evenement '{title}': {e}")
        return None


def main():
    print("\n" + "="*62)
    print("  ProStory-AI - Setup des comptes entreprises + evenements")
    print("="*62 + "\n")

    company_ids = []
    user_ids    = []

    # 1. Creer/recuperer les entreprises et leurs comptes auth
    for enterprise in ENTERPRISES:
        print(f"\n[STEP] Traitement: {enterprise['name']}")
        c_id = get_or_create_company(enterprise["name"], enterprise["description"])
        u_id = create_auth_user_and_profile(enterprise, c_id)
        company_ids.append(c_id)
        user_ids.append(u_id)

    # 2. Nettoyer les evenements perimes
    print("\n[STEP] Nettoyage des evenements perimes...")
    delete_outdated_events()

    # 3. Creer les evenements a venir
    print("\n[STEP] Creation des evenements a venir...")
    for evt in UPCOMING_EVENTS_TEMPLATES:
        idx  = evt["enterprise_idx"]
        c_id = company_ids[idx]
        u_id = user_ids[idx]
        if u_id:
            create_event(evt, c_id, u_id)
        else:
            print(f"   [SKIP] Pas de creator_id pour l'index {idx}: {evt['title']}")

    # 4. Recapitulatif
    print("\n" + "="*62)
    print("  SETUP TERMINE - Identifiants de connexion")
    print("="*62)
    for i, ent in enumerate(ENTERPRISES):
        print(f"\n  Entreprise : {ent['name']}")
        print(f"  Email      : {ent['email']}")
        print(f"  Password   : {ent['password']}")
        print(f"  Role       : entreprise")
        if i < len(company_ids):
            print(f"  Company ID : {company_ids[i]}")
        if i < len(user_ids):
            print(f"  User ID    : {user_ids[i]}")
    print()


if __name__ == "__main__":
    main()
