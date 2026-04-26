# Triggers et Logique SQL (Supabase)

Ce dossier documente la logique métier déportée directement dans la base de données PostgreSQL pour garantir l'intégrité et la performance.

## ⚡ Trigger d'Inscription (`handle_new_user_with_company`)

Ce trigger est la pièce maîtresse du flux d'inscription des entreprises.

### Script SQL :
```sql
CREATE OR REPLACE FUNCTION public.handle_new_user_with_company()
RETURNS trigger AS $$
DECLARE
    existing_company_id uuid;
    company_name_val text;
BEGIN
    company_name_val := new.raw_user_meta_data->>'company_name';

    -- 1. Création Identity
    INSERT INTO public.users (id, name, email, role, created_at)
    VALUES (new.id, new.raw_user_meta_data->>'full_name', new.email, COALESCE(new.raw_user_meta_data->>'role', 'user'), now());

    -- 2. Logique Entreprise (Revendication intelligente)
    IF (new.raw_user_meta_data->>'role' = 'entreprise') AND (company_name_val IS NOT NULL) THEN
        SELECT id INTO existing_company_id FROM public.companies WHERE name ILIKE company_name_val LIMIT 1;
        IF existing_company_id IS NOT NULL THEN
            UPDATE public.companies SET owner_id = new.id WHERE id = existing_company_id AND owner_id IS NULL;
        ELSE
            INSERT INTO public.companies (name, owner_id, created_at) VALUES (company_name_val, new.id, now()) RETURNING id INTO existing_company_id;
        END IF;
    END IF;

    -- 3. Profil lié
    INSERT INTO public.profiles (id, current_company_id, created_at, is_onboarding_complete)
    VALUES (new.id, existing_company_id, now(), false);

    RETURN new;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
```

## 📋 Pourquoi cette approche ?
- **Atomicité** : Soit tout est créé (User + Entreprise + Profil), soit rien ne l'est. Pas de données orphelines.
- **Vitesse** : Pas d'allers-retours entre le backend et la DB.
- **Consistance** : Même si on change de backend (ex: passer de Python à Node), la logique d'inscription reste identique.

---

## 🛡️ Configuration de Sécurité Backend

Le backend FastAPI utilise une configuration spécifique pour interagir avec Supabase tout en respectant ou bypassant les politiques RLS (Row Level Security).

### Utilisation de la `SERVICE_ROLE_KEY`
Pour les opérations de gestion (comme la création d'expériences ou la mise à jour de profils), le backend utilise la **Service Role Key**. 
- **Pourquoi ?** Cette clé possède des privilèges élevés qui permettent de bypasser les politiques RLS. C'est essentiel car le serveur FastAPI agit comme un middleware de confiance et gère sa propre logique d'autorisation.
- **Fallback** : Si la clé de service n'est pas configurée, le système retombe sur la clé `anon` par défaut, mais de nombreuses opérations d'écriture risquent d'échouer si le RLS est activé sur les tables cibles.
