-- Activer l'extension pgvector pour les embeddings
CREATE EXTENSION IF NOT EXISTS vector;

-- Table utilisateurs
CREATE TABLE IF NOT EXISTS utilisateurs (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100),
    bio TEXT,
    avatar_url VARCHAR(500),
    role VARCHAR(20) DEFAULT 'user',
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_modification TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table experiences
CREATE TABLE IF NOT EXISTS experiences (
    id SERIAL PRIMARY KEY,
    utilisateur_id INTEGER NOT NULL,
    titre VARCHAR(255) NOT NULL,
    contenu TEXT NOT NULL,
    tags VARCHAR(255),
    domaine_activite VARCHAR(100),
    sentiment VARCHAR(20),
    score_qualite FLOAT DEFAULT 0,
    embedding vector(384),
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_modification TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(id) ON DELETE CASCADE
);

-- Index pour les performances
CREATE INDEX IF NOT EXISTS idx_experiences_utilisateur ON experiences(utilisateur_id);
CREATE INDEX IF NOT EXISTS idx_experiences_date ON experiences(date_creation DESC);
CREATE INDEX IF NOT EXISTS idx_experiences_embedding ON experiences USING ivfflat (embedding vector_cosine_ops);

-- Insérer un utilisateur de test
INSERT INTO utilisateurs (email, nom, prenom, avatar_url) VALUES 
('test@example.com', 'Test', 'User', 'https://avatar.placeholder.com/test')
ON CONFLICT DO NOTHING;