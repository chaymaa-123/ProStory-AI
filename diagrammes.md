# Diagrammes du Projet Connex

## 1. Diagramme de Cas d'Utilisation (Use Case)

```mermaid
graph TD
    subgraph "Plateforme Connex"
        UC[Connex Platform]
    end
    
    subgraph "Acteurs"
        U[Utilisateur]
        E[Entreprise]
        A[Administrateur]
    end
    
    subgraph "Fonctionnalités Utilisateur"
        Auth[Authentification]
        Pub[Publication Expérience]
        Feed[Consultation Feed]
        Inter[Interactions Sociales]
        Rech[Recherche Avancée]
        Profil[Gestion Profil]
    end
    
    subgraph "Fonctionnalités Entreprise"
        Dashboard[Dashboard Analytics]
        Insights[Consultation Insights]
        Bench[Benchmarking]
        Percept[Analyse Perception]
    end
    
    subgraph "Fonctionnalités Administrateur"
        Mod[Moderation Contenu]
        GestUsers[Gestion Utilisateurs]
        Config[Configuration Système]
        Stats[Statistiques Globales]
    end
    
    U --> Auth
    U --> Pub
    U --> Feed
    U --> Inter
    U --> Rech
    U --> Profil
    
    E --> Dashboard
    E --> Insights
    E --> Bench
    E --> Percept
    
    A --> Mod
    A --> GestUsers
    A --> Config
    A --> Stats
    
    Auth --> UC
    Pub --> UC
    Feed --> UC
    Inter --> UC
    Rech --> UC
    Profil --> UC
    Dashboard --> UC
    Insights --> UC
    Bench --> UC
    Percept --> UC
    Mod --> UC
    GestUsers --> UC
    Config --> UC
    Stats --> UC
    
    style U fill:#e1f5fe
    style E fill:#f3e5f5
    style A fill:#fff3e0
```

## 2. Diagramme de Classes UML

```mermaid
classDiagram
    class Utilisateur {
        +int id
        +string email
        +string password_hash
        +string nom
        +string prenom
        +string role
        +datetime created_at
        +datetime updated_at
        +s'inscrire()
        +se_connecter()
        +modifier_profil()
        +publier_experience()
        +interagir()
    }
    
    class Experience {
        +int id
        +int utilisateur_id
        +int entreprise_id
        +string titre
        +text contenu
        +string secteur
        +datetime date_experience
        +datetime created_at
        +datetime updated_at
        +creer()
        +modifier()
        +supprimer()
        +analyser_ia()
    }
    
    class Entreprise {
        +int id
        +string nom
        +string secteur
        +string description
        +string logo_url
        +datetime created_at
        +datetime updated_at
        +get_insights()
        +get_analytics()
        +update_profil()
    }
    
    class Commentaire {
        +int id
        +int experience_id
        +int utilisateur_id
        +text contenu
        +datetime created_at
        +datetime updated_at
        +creer()
        +modifier()
        +supprimer()
    }
    
    class Like {
        +int id
        +int experience_id
        +int utilisateur_id
        +datetime created_at
        +ajouter()
        +retirer()
    }
    
    class Insight {
        +int id
        +int experience_id
        +int entreprise_id
        +float sentiment_score
        +string sentiment_label
        +array keywords
        +json themes
        +datetime created_at
        +generer()
        +analyser_sentiment()
        +extraire_keywords()
    }
    
    class Evenement {
        +int id
        +int entreprise_id
        +string titre
        +text description
        +date date_evenement
        +string type
        +datetime created_at
        +creer()
        +modifier()
        +supprimer()
    }
    
    class Sauvegarde {
        +int id
        +int utilisateur_id
        +int experience_id
        +datetime created_at
        +ajouter()
        +retirer()
    }
    
    Utilisateur ||--o{ Experience : publie
    Utilisateur ||--o{ Commentaire : écrit
    Utilisateur ||--o{ Like : donne
    Utilisateur ||--o{ Sauvegarde : sauvegarde
    Experience ||--o{ Commentaire : contient
    Experience ||--o{ Like : reçoit
    Experience ||--o{ Sauvegarde : est_sauvegardée
    Experience ||--|| Insight : génère
    Experience }o--|| Entreprise : concerne
    Insight }o--|| Entreprise : analyse
    Evenement }o--|| Entreprise : organisé_par
```

## 3. Diagramme d'Activité

```mermaid
flowchart TD
    Start([Début]) --> Auth{Authentifié?}
    
    Auth -->|Non| Login[Page de Connexion]
    Login --> Register[Page d'Inscription]
    Register --> Auth
    
    Auth -->|Oui| Feed[Fil d'Actualité]
    
    Feed --> Choice{Action Utilisateur}
    
    Choice -->|Publier| CreateExp[Créer Expérience]
    Choice -->|Rechercher| Search[Recherche Avancée]
    Choice -->|Consulter| ViewExp[Voir Expérience]
    Choice -->|Profil| Profile[Gestion Profil]
    
    CreateExp --> Form[Formulaire Expérience]
    Form --> Submit[Soumettre]
    
    Submit --> Fork{Traitement Parallèle}
    
    Fork -->|Stockage| SaveDB[Sauvegarder en BDD]
    Fork -->|Analyse IA| Pipeline[Pipeline IA]
    
    Pipeline --> Sentiment[Analyse Sentiment]
    Pipeline --> Keywords[Extraction Keywords]
    Pipeline --> Embeddings[Génération Embeddings]
    
    Sentiment --> Insights[Créer Insights]
    Keywords --> Insights
    Embeddings --> Insights
    
    SaveDB --> UpdateFeed[Mettre à jour Feed]
    Insights --> StoreInsights[Stocker Insights]
    
    UpdateFeed --> Feed
    StoreInsights --> NotifyEntreprise[Notifier Entreprise]
    
    Search --> Results[Afficher Résultats]
    Results --> Feed
    
    ViewExp --> Detail[Page Détail]
    Detail --> Interactions[Interactions Possibles]
    
    Interactions --> Like[Liker]
    Interactions --> Comment[Commenter]
    Interactions --> Save[Sauvegarder]
    
    Like --> Feed
    Comment --> Feed
    Save --> Feed
    
    Profile --> ProfileActions{Actions Profil}
    ProfileActions -->|Modifier| EditProfile[Modifier Profil]
    ProfileActions -->|Voir| ViewProfile[Voir Profil]
    
    EditProfile --> UpdateDB[Mettre à jour BDD]
    UpdateDB --> Feed
    
    ViewProfile --> Feed
    
    NotifyEntreprise --> Dashboard[Dashboard Entreprise]
    Dashboard --> Analytics[Visualiser Analytics]
    Analytics --> Feed
    
    End([Fin])
    
    style Start fill:#4caf50,color:#fff
    style End fill:#f44336,color:#fff
    style Fork fill:#ff9800,color:#fff
    style Pipeline fill:#2196f3,color:#fff
    style Dashboard fill:#9c27b0,color:#fff
```

## 4. Diagramme de Séquence

```mermaid
sequenceDiagram
    participant U as Utilisateur
    participant F as Frontend (Next.js)
    participant B as Backend (FastAPI)
    participant D as Database (Supabase)
    participant IA as Pipeline IA
    participant E as Entreprise
    
    Note over U,E: Flux d'authentification et création d'expérience
    
    U->>F: Accès à la plateforme
    F->>B: GET /api/auth/status
    B->>D: Vérifier session
    D-->>B: Session valide?
    B-->>F: Statut authentification
    F-->>U: Afficher page appropriée
    
    U->>F: Créer nouvelle expérience
    F->>U: Afficher formulaire
    U->>F: Soumettre formulaire
    F->>B: POST /api/experiences
    B->>D: Insérer expérience
    D-->>B: ID expérience créée
    B->>IA: Lancer analyse IA
    IA->>IA: Analyse sentiment
    IA->>IA: Extraction keywords
    IA->>IA: Génération embeddings
    IA-->>B: Insights générés
    B->>D: Insérer insights
    B-->>F: Expérience créée avec ID
    F-->>U: Confirmation création
    
    Note over U,E: Flux de consultation et interactions
    
    U->>F: Consulter feed
    F->>B: GET /api/experiences
    B->>D: Récupérer expériences
    D-->>B: Liste expériences
    B-->>F: Données formatées
    F-->>U: Afficher feed
    
    U->>F: Liker expérience
    F->>B: POST /api/experiences/{id}/like
    B->>D: Ajouter like
    D-->>B: Confirmation
    B-->>F: Like enregistré
    F-->>U: Mise à jour UI
    
    Note over U,E: Flux dashboard entreprise
    
    E->>F: Accès dashboard
    F->>B: GET /api/auth/entreprise/verify
    B->>D: Vérifier rôle entreprise
    D-->>B: Rôle confirmé
    B-->>F: Accès autorisé
    F->>B: GET /api/ai/company-insights/{id}
    B->>D: Récupérer insights entreprise
    D-->>B: Données analytics
    B-->>F: Insights formatés
    F-->>E: Afficher dashboard avec visualisations
```

## 5. Diagramme de Gantt

```mermaid
gantt
    title Planification du Projet Connex - 7 Semaines
    dateFormat  YYYY-MM-DD
    axisFormat  %d/%m
    
    section Phase 1: Analyse
    Analyse des besoins     :a1, 2024-01-01, 7d
    Définition problématique :a2, after a1, 2d
    Benchmark              :a3, after a2, 3d
    Rédaction cahier charges:a4, after a3, 2d
    
    section Phase 2: Conception
    Modélisation UML       :c1, after a4, 5d
    Architecture système     :c2, after c1, 3d
    Schema BDD Supabase     :c3, after c2, 4d
    Validation technique     :c4, after c3, 2d
    
    section Phase 3: Développement Sprint 1
    Configuration Backend    :d1, after c4, 3d
    Auth JWT               :d2, after d1, 2d
    Triggers SQL           :d3, after d2, 2d
    Structure Frontend       :d4, after d3, 3d
    
    section Phase 4: Développement Sprint 2
    Fil d'actualité         :e1, after d4, 2d
    Pipeline IA complet     :e2, after e1, 3d
    Dashboard entreprise    :e3, after e2, 2d
    Intégration frontend    :e4, after e3, 2d
    
    section Phase 5: Tests & Corrections
    Tests unitaires         :t1, after e4, 2d
    Correction bugs         :t2, after t1, 2d
    Validation onboarding    :t3, after t2, 1d
    Tests intégration       :t4, after t3, 2d
    
    section Phase 6: Déploiement
    Configuration production :p1, after t4, 1d
    Mise en ligne          :p2, after p1, 2d
    Documentation technique :p3, after p2, 2d
    Préparation soutenance  :p4, after p3, 2d
```

## 6. Diagramme d'Architecture Système

```mermaid
graph TB
    subgraph "Frontend Layer"
        UI[Interface Utilisateur<br/>Next.js 16 + TailwindCSS]
        Comp[Composants React<br/>Radix UI + Lucide]
        Charts[Visualisations<br/>Recharts]
    end
    
    subgraph "API Gateway"
        Gateway[FastAPI Gateway<br/>JWT Authentication<br/>Rate Limiting]
    end
    
    subgraph "Backend Services"
        AuthSvc[Service Authentification<br/>JWT + Bcrypt<br/>Users + Companies]
        ExpSvc[Service Expériences<br/>CRUD Operations]
        IASvc[Service IA Pipeline<br/>Sentiment + Keywords]
        AnalyticsSvc[Service Analytics<br/>Dashboard Data<br/>Company Insights]
        EventSvc[Service Événements<br/>Company Events]
        CompanySvc[Service Entreprise<br/>B2B Features<br/>Profile Management]
    end
    
    subgraph "AI/ML Pipeline"
        Sentiment[Analyse Sentiment<br/>Transformers]
        Keywords[Extraction Keywords<br/>KeyBERT]
        Embeddings[Vector Embeddings<br/>Sentence-Transformers]
        Insights[Génération Insights<br/>PyTorch]
    end
    
    subgraph "Data Layer"
        Supabase[(Supabase<br/>PostgreSQL + pgvector)]
        VectorStore[(Vector Store<br/>Embeddings Storage)]
        Cache[(Redis Cache<br/>Session Data)]
    end
    
    subgraph "External Services"
        HuggingFace[Hugging Face<br/>Models Hub]
        Docker[Docker Containers<br/>Orchestration]
    end
    
    UI --> Gateway
    Comp --> Gateway
    Charts --> Gateway
    
    Gateway --> AuthSvc
    Gateway --> ExpSvc
    Gateway --> IASvc
    Gateway --> AnalyticsSvc
    Gateway --> EventSvc
    Gateway --> CompanySvc
    
    IASvc --> Sentiment
    IASvc --> Keywords
    IASvc --> Embeddings
    IASvc --> Insights
    
    AuthSvc --> Supabase
    ExpSvc --> Supabase
    AnalyticsSvc --> Supabase
    EventSvc --> Supabase
    CompanySvc --> Supabase
    
    Sentiment --> VectorStore
    Keywords --> VectorStore
    Embeddings --> VectorStore
    Insights --> Supabase
    
    AuthSvc --> Cache
    
    Sentiment --> HuggingFace
    Keywords --> HuggingFace
    Embeddings --> HuggingFace
    
    subgraph "Deployment"
        Docker --> Gateway
        Docker --> AuthSvc
        Docker --> ExpSvc
        Docker --> IASvc
        Docker --> AnalyticsSvc
        Docker --> EventSvc
        Docker --> CompanySvc
    end
    
    style UI fill:#e3f2fd
    style Gateway fill:#f3e5f5
    style Supabase fill:#e8f5e8
    style VectorStore fill:#fff3e0
    style HuggingFace fill:#fce4ec
```

## 7. Diagramme de Flux de Données IA

```mermaid
flowchart LR
    subgraph "Input"
        Text[Texte Expérience<br/>Récit Utilisateur]
    end
    
    subgraph "Preprocessing"
        Clean[Nettoyage Texte<br/>Suppression ponctuation<br/>Normalisation]
        Token[Tokenisation<br/>Découpage en tokens]
    end
    
    subgraph "AI Models"
        SentimentModel[Modèle Sentiment<br/>Transformers<br/>nlptown/bert-base]
        KeywordModel[KeyBERT<br/>all-MiniLM-L6-v2]
        EmbedModel[Sentence-Transformers<br/>all-MiniLM-L6-v2]
    end
    
    subgraph "Processing"
        SentimentScore[Score Sentiment<br/>Positif/Négatif/Neutre]
        KeywordExtraction[Extraction Mots-clés<br/>Top 10 keywords]
        VectorGeneration[Génération Vecteurs<br/>384 dimensions]
    end
    
    subgraph "Output & Storage"
        InsightsDB[Insights en BDD<br/>Supabase]
        VectorDB[Vecteurs Stockés<br/>pgvector]
        Dashboard[Dashboard Visualisation<br/>Graphiques & Stats]
    end
    
    Text --> Clean
    Clean --> Token
    Token --> SentimentModel
    Token --> KeywordModel
    Token --> EmbedModel
    
    SentimentModel --> SentimentScore
    KeywordModel --> KeywordExtraction
    EmbedModel --> VectorGeneration
    
    SentimentScore --> InsightsDB
    KeywordExtraction --> InsightsDB
    VectorGeneration --> VectorDB
    
    InsightsDB --> Dashboard
    VectorDB --> Dashboard
    
    style Text fill:#e1f5fe
    style SentimentModel fill:#f3e5f5
    style KeywordModel fill:#e8f5e8
    style EmbedModel fill:#fff3e0
    style InsightsDB fill:#fce4ec
    style Dashboard fill:#f1f8e9
```

---

## Instructions pour utiliser ces diagrammes

### Dans Markdown
Copiez-collez le code Mermaid correspondant dans vos fichiers Markdown. La plupart des éditeurs modernes (VS Code, GitHub, GitLab) afficheront automatiquement les diagrammes.

### Dans le rapport
Pour inclure ces diagrammes dans votre rapport.md :
1. Copiez le code Mermaid souhaité
2. Ajoutez-le dans une section avec le titre approprié
3. Les diagrammes seront rendus automatiquement

### En ligne
Vous pouvez visualiser et modifier ces diagrammes sur :
- [Mermaid Live Editor](https://mermaid.live)
- [Mermaid Diagrams](https://mermaid-js.github.io/mermaid-live-editor)

### Pour la présentation
Exportez les diagrammes en images PNG/SVG depuis l'éditeur Mermaid pour les intégrer dans vos présentations PowerPoint ou Google Slides.
