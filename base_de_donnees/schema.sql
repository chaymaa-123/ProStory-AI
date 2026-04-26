-- Schema Supabase for ProStory-AI Experiences

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table (linked to auth.users)
CREATE TABLE IF NOT EXISTS public.users (
  id uuid NOT NULL DEFAULT auth.uid(),
  name text NOT NULL,
  email text NOT NULL UNIQUE,
  role text DEFAULT 'user' CHECK (role IN ('user', 'entreprise', 'admin')),
  created_at timestamp with time zone DEFAULT timezone('utc'::text, now()) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id) REFERENCES auth.users(id)
);

-- Experiences table
CREATE TABLE IF NOT EXISTS public.experiences (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  user_id uuid NOT NULL,
  title text NOT NULL,
  content text NOT NULL,
  category text,
  company_id uuid,
  event_id uuid,
  created_at timestamp with time zone DEFAULT timezone('utc'::text, now()) NOT NULL,
  updated_at timestamp with time zone DEFAULT timezone('utc'::text, now()) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE,
  FOREIGN KEY (company_id) REFERENCES public.companies(id) ON DELETE SET NULL,
  FOREIGN KEY (event_id) REFERENCES public.events(id) ON DELETE SET NULL
);

-- Tags table
CREATE TABLE IF NOT EXISTS public.tags (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  name text NOT NULL UNIQUE,
  PRIMARY KEY (id)
);

-- Experience-Tags junction
CREATE TABLE IF NOT EXISTS public.experience_tags (
  experience_id uuid NOT NULL,
  tag_id uuid NOT NULL,
  PRIMARY KEY (experience_id, tag_id),
  FOREIGN KEY (experience_id) REFERENCES public.experiences(id) ON DELETE CASCADE,
  FOREIGN KEY (tag_id) REFERENCES public.tags(id) ON DELETE CASCADE
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_experiences_user_id ON public.experiences(user_id);
CREATE INDEX IF NOT EXISTS idx_experiences_created ON public.experiences(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_experience_tags_exp ON public.experience_tags(experience_id);
CREATE INDEX IF NOT EXISTS idx_experience_tags_tag ON public.experience_tags(tag_id);

-- RLS policies (enable if needed)
ALTER TABLE public.experiences ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can view own experiences" ON public.experiences FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Users can insert own experiences" ON public.experiences FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Users can update own experiences" ON public.experiences FOR UPDATE USING (auth.uid() = user_id);

ALTER TABLE public.experience_tags ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Tags for own experiences" ON public.experience_tags FOR ALL USING (exists (SELECT 1 FROM public.experiences WHERE id = experience_id AND auth.uid() = user_id));

-- Companies table
CREATE TABLE IF NOT EXISTS public.companies (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  name text NOT NULL,
  description text,
  created_at timestamp with time zone DEFAULT timezone('utc'::text, now()) NOT NULL,
  PRIMARY KEY (id)
);

-- Events table (complete version)
CREATE TABLE IF NOT EXISTS public.events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    date TIMESTAMP WITH TIME ZONE NOT NULL,
    location VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL,
    is_virtual BOOLEAN DEFAULT FALSE,
    max_attendees INTEGER,
    creator_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    company_id UUID REFERENCES public.companies(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_events_creator ON public.events(creator_id);
CREATE INDEX IF NOT EXISTS idx_events_company ON public.events(company_id);
CREATE INDEX IF NOT EXISTS idx_events_date ON public.events(date);
CREATE INDEX IF NOT EXISTS idx_events_category ON public.events(category);

-- Experience-Company junction
CREATE TABLE IF NOT EXISTS public.experience_company (
  experience_id uuid NOT NULL,
  company_id uuid NOT NULL,
  PRIMARY KEY (experience_id, company_id),
  FOREIGN KEY (experience_id) REFERENCES public.experiences(id) ON DELETE CASCADE,
  FOREIGN KEY (company_id) REFERENCES public.companies(id) ON DELETE CASCADE
);

-- Experience-Event junction
CREATE TABLE IF NOT EXISTS public.experience_event (
  experience_id uuid NOT NULL,
  event_id uuid NOT NULL,
  PRIMARY KEY (experience_id, event_id),
  FOREIGN KEY (experience_id) REFERENCES public.experiences(id) ON DELETE CASCADE,
  FOREIGN KEY (event_id) REFERENCES public.events(id) ON DELETE CASCADE
);

-- Comments table
CREATE TABLE IF NOT EXISTS public.comments (
  id uuid NOT NULL DEFAULT uuid_generate_v4(),
  user_id uuid NOT NULL,
  experience_id uuid NOT NULL,
  content text NOT NULL,
  created_at timestamp with time zone DEFAULT timezone('utc'::text, now()) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE,
  FOREIGN KEY (experience_id) REFERENCES public.experiences(id) ON DELETE CASCADE
);

-- Likes table
CREATE TABLE IF NOT EXISTS public.likes (
  user_id uuid NOT NULL,
  experience_id uuid NOT NULL,
  created_at timestamp with time zone DEFAULT timezone('utc'::text, now()) NOT NULL,
  PRIMARY KEY (user_id, experience_id),
  FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE,
  FOREIGN KEY (experience_id) REFERENCES public.experiences(id) ON DELETE CASCADE
);

-- Insights table (AI analysis)
CREATE TABLE IF NOT EXISTS public.insights (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  experience_id UUID NOT NULL REFERENCES public.experiences(id) ON DELETE CASCADE,
  sentiment VARCHAR(20) NOT NULL CHECK (sentiment IN ('positif', 'neutre', 'negatif')),
  keywords TEXT[] DEFAULT '{}',
  score FLOAT DEFAULT 0.0 CHECK (score >= 0.0 AND score <= 1.0),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_insights_exp ON public.insights(experience_id);

-- Additional indexes
CREATE INDEX IF NOT EXISTS idx_experience_company_exp ON public.experience_company(experience_id);
CREATE INDEX IF NOT EXISTS idx_experience_company_comp ON public.experience_company(company_id);
CREATE INDEX IF NOT EXISTS idx_experience_event_exp ON public.experience_event(experience_id);
CREATE INDEX IF NOT EXISTS idx_experience_event_evt ON public.experience_event(event_id);
CREATE INDEX IF NOT EXISTS idx_comments_exp ON public.comments(experience_id);
CREATE INDEX IF NOT EXISTS idx_comments_user ON public.comments(user_id);
CREATE INDEX IF NOT EXISTS idx_likes_exp ON public.likes(experience_id);
CREATE INDEX IF NOT EXISTS idx_insights_exp ON public.insights(experience_id);

-- RLS policies for new tables
ALTER TABLE public.comments ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can manage own comments" ON public.comments FOR ALL USING (auth.uid() = user_id);

ALTER TABLE public.likes ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can manage own likes" ON public.likes FOR ALL USING (auth.uid() = user_id);

