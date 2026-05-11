-- ============================================================
-- Connex - Setup Entreprises (Version Robuste)
-- A executer dans le SQL Editor de Supabase
-- ============================================================

DO $$
DECLARE
    tn_id UUID;
    ef_id UUID;
BEGIN
    -- 1. Création des Entreprises dans public.companies
    -- On vérifie par le nom pour éviter les doublons
    IF NOT EXISTS (SELECT 1 FROM public.companies WHERE name = 'TechNova Solutions') THEN
        INSERT INTO public.companies (name, description)
        VALUES ('TechNova Solutions', 'Leader en innovation logicielle et intelligence artificielle.')
        RETURNING id INTO tn_id;
    ELSE
        SELECT id INTO tn_id FROM public.companies WHERE name = 'TechNova Solutions';
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.companies WHERE name = 'EcoFuture Group') THEN
        INSERT INTO public.companies (name, description)
        VALUES ('EcoFuture Group', 'Pionnier dans les solutions d energie renouvelable et durable.')
        RETURNING id INTO ef_id;
    ELSE
        SELECT id INTO ef_id FROM public.companies WHERE name = 'EcoFuture Group';
    END IF;

    -- 2. Création des comptes Auth (si nécessaire)
    -- Note: Les mots de passe sont hashés en MD5/Bcrypt par Supabase via crypt()
    
    -- TechNova Auth
    IF NOT EXISTS (SELECT 1 FROM auth.users WHERE email = 'technova@prostory.ai') THEN
        INSERT INTO auth.users (id, instance_id, email, encrypted_password, email_confirmed_at, raw_app_meta_data, raw_user_meta_data, role, aud)
        VALUES (
            gen_random_uuid(),
            '00000000-0000-0000-0000-000000000000',
            'technova@prostory.ai',
            crypt('TechNova2026!', gen_salt('bf')),
            NOW(),
            '{"provider":"email","providers":["email"]}',
            '{"full_name":"TechNova Solutions","role":"entreprise"}',
            'authenticated',
            'authenticated'
        );
    END IF;

    -- EcoFuture Auth
    IF NOT EXISTS (SELECT 1 FROM auth.users WHERE email = 'ecofuture@prostory.ai') THEN
        INSERT INTO auth.users (id, instance_id, email, encrypted_password, email_confirmed_at, raw_app_meta_data, raw_user_meta_data, role, aud)
        VALUES (
            gen_random_uuid(),
            '00000000-0000-0000-0000-000000000000',
            'ecofuture@prostory.ai',
            crypt('EcoFuture2026!', gen_salt('bf')),
            NOW(),
            '{"provider":"email","providers":["email"]}',
            '{"full_name":"EcoFuture Group","role":"entreprise"}',
            'authenticated',
            'authenticated'
        );
    END IF;

    -- 3. Synchronisation avec public.users
    INSERT INTO public.users (id, name, email, role)
    SELECT id, raw_user_meta_data->>'full_name', email, 'entreprise'
    FROM auth.users
    WHERE email IN ('technova@prostory.ai', 'ecofuture@prostory.ai')
    ON CONFLICT (id) DO UPDATE SET role = 'entreprise';

    -- 4. Création des Événements
    -- TechNova Events
    IF NOT EXISTS (SELECT 1 FROM public.events WHERE title = 'Tech Summit 2026 - Casablanca') THEN
        INSERT INTO public.events (title, description, date, location, category, creator_id, company_id)
        SELECT 'Tech Summit 2026 - Casablanca', 'Le plus grand rassemblement tech.', '2026-05-28T09:00:00Z', 'Casablanca', 'Technologie', id, tn_id
        FROM public.users WHERE email = 'technova@prostory.ai';
    END IF;

    IF NOT EXISTS (SELECT 1 FROM public.events WHERE title = 'AI & Data Day - Rabat') THEN
        INSERT INTO public.events (title, description, date, location, category, creator_id, company_id)
        SELECT 'AI & Data Day - Rabat', 'Journee IA et Data.', '2026-06-18T10:00:00Z', 'Rabat', 'Technologie', id, tn_id
        FROM public.users WHERE email = 'technova@prostory.ai';
    END IF;

    -- EcoFuture Events
    IF NOT EXISTS (SELECT 1 FROM public.events WHERE title = 'Webinar - Batiments Green') THEN
        INSERT INTO public.events (title, description, date, location, category, creator_id, company_id)
        SELECT 'Webinar - Batiments Green', 'Innovation durable.', '2026-05-22T14:00:00Z', 'En ligne', 'Environnement', id, ef_id
        FROM public.users WHERE email = 'ecofuture@prostory.ai';
    END IF;

END $$;

-- Vérification finale
SELECT name, email, role FROM public.users WHERE role = 'entreprise';
SELECT title, date, company_id FROM public.events WHERE date > NOW();
