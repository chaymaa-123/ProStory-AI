# Rapport de Projet - Connex

## Remerciements

## Résumé 

Le projet Connex porte sur la conception et le développement d'une plateforme sociale innovante dédiée au partage d'expériences professionnelles, enrichie par l'intelligence artificielle pour l'extraction d'insights stratégiques. Dans un marché de l'emploi en quête de transparence, cette solution offre un espace sécurisé permettant de transformer des récits de carrière bruts en données exploitables pour les utilisateurs et les entreprises.

Sur le plan technique, l'application adopte une architecture Full-Stack robuste reposant sur un modèle de Façade (API Proxy). Le frontend est développé avec Next.js 16, assurant une interface utilisateur réactive et fluide, tandis que le backend est propulsé par FastAPI, garantissant des performances optimales et une sécurité accrue. La persistance des données est gérée par Supabase (PostgreSQL), et la protection des échanges est assurée par une authentification JWT associée à un hachage Bcrypt.

Le système intègre des fonctionnalités dynamiques telles qu'un fil d'actualité interactif, une gestion fine des rôles et des profils, ainsi qu'une infrastructure prête pour l'analyse automatisée par IA. Ce travail démontre la viabilité d'une architecture moderne pour répondre aux enjeux de sécurité et de scalabilité des réseaux sociaux thématiques actuels.

**Mots-clés :** Connex, Next.js, FastAPI, Intelligence Artificielle, Full-Stack, Partage d'expérience, Sécurité informatique, Pipeline IA.

## Abstract

The Connex project involves the design and development of an innovative social platform dedicated to sharing professional experiences, enhanced by Artificial Intelligence for strategic insight extraction. In a job market increasingly seeking transparency, this solution provides a secure space to transform raw career narratives into actionable data for both users and companies.

Technically, the application adopts a robust Full-Stack architecture based on an API Proxy (Facade) model. The frontend is developed with Next.js 16, ensuring a reactive and fluid user interface, while the backend is powered by FastAPI, guaranteeing optimal performance and enhanced security. Data persistence is managed by Supabase (PostgreSQL), and exchange protection is ensured by JWT authentication combined with Bcrypt hashing.

The system integrates dynamic features such as an interactive news feed, fine-grained role and profile management, and an infrastructure ready for automated AI analysis. This work demonstrates the viability of a modern architecture in meeting the security and scalability challenges of contemporary thematic social networks.

**Keywords:** Connex, Next.js, FastAPI, Artificial Intelligence, Full-Stack, Experience Sharing, Cybersecurity, AI Pipeline.

## Table des matières

- Introduction Générale
- Chapitre 1 : Contexte général du projet
  - 1.1 Introduction
  - 1.2. Contexte du projet
  - 1.3. Problématique
  - 1.4. Objectif du projet
  - 1.5. Spécification des besoins
    - 1.5.1. Besoins fonctionnels
    - 1.5.2. Besoins non fonctionnels
  - 1.6. Gestion de projet
    - 1.6.1. Cycle de vie du projet
    - 1.6.2. Planification du projet
    - 1.6.3. Diagramme de Gantt
  - 1.7. Entreprenariat
    - 1.7.1. Logo
    - 1.7.2. Commercialisation
    - 1.7.3. Financement
  - 1.8. Conclusion
- Chapitre 2 : Analyse et conception
  - 2.1. Introduction
  - 2.2. Étude de l'existant
  - 2.3. Benchmark
  - 2.4. Architecture de la solution
  - 2.5. Choix des technologies
  - 2.6. Conception
    - 2.6.1. Diagramme use case
    - 2.6.2. Diagramme de classe
    - 2.6.3. Diagramme d'activité
    - 2.6.4. Diagramme de séquence
  - 2.7. Conclusion
- Chapitre 3 : Réalisations
- Conclusion Générale
- Perspectives
- Webographie

## Table des figures

- Figure 1 : Next.js
- Figure 2 : FastAPI
- Figure 3 : PostgreSQL
- Figure 4 : Intelligence Artificielle
- Figure 5 : Diagramme use case
- Figure 6 : Diagramme de classe
- Figure 7 : Diagramme d'activité
- Figure 8 : Diagramme de séquence

## Table des tableaux

- Tableau 1 : Besoins fonctionnels
- Tableau 2 : Besoins non fonctionnels
- Tableau 3 : Planification du projet

## Introduction Générale

À l'ère de la transformation numérique, le marché du travail traverse une mutation profonde où la transparence et le partage d'informations authentiques sont devenus des enjeux stratégiques. Si des plateformes professionnelles existent déjà, il subsiste un besoin croissant pour des espaces dédiés au partage de récits d'expérience concrets, capables de transformer des témoignages vécus en connaissances exploitables.

C'est dans ce contexte que s'inscrit le projet Connex. Cette plateforme sociale innovante a pour mission de centraliser les expériences professionnelles tout en exploitant la puissance de l'Intelligence Artificielle pour en extraire des "insights" métier pertinents. L'objectif est double : offrir aux utilisateurs un espace d'échange structuré et fournir aux entreprises une vision analytique des tendances de carrière et des retours d'expérience.

Le développement de cette solution repose sur des choix technologiques de pointe visant la performance et la sécurité. En utilisant une architecture Full-Stack composée de Next.js pour une interface utilisateur réactive, de FastAPI pour un backend robuste avec pipeline IA intégré, et de Supabase pour une gestion de données scalable, le projet Connex se veut une réponse technique moderne aux défis des réseaux sociaux thématiques.

Ce rapport détaille les étapes clés de la réalisation du projet. Le premier chapitre présentera le contexte, les objectifs et la planification. Le deuxième chapitre sera consacré à l'analyse fonctionnelle et à la conception technique (cas d'utilisation et diagrammes). Enfin, le troisième chapitre exposera l'architecture logicielle, les technologies de sécurité mises en œuvre ainsi que les interfaces finales de la solution.

## Chapitre 1 : Contexte général du projet

### 1.1 Introduction

Ce chapitre présente le cadrage du projet Connex en définissant son contexte, sa problématique et ses objectifs principaux. Dans un environnement professionnel où les informations sont souvent dispersées et peu structurées, il devient essentiel de proposer une solution capable de valoriser les expériences réelles. Ce chapitre permet ainsi d'identifier les besoins des utilisateurs, de justifier la pertinence du projet et de poser les bases nécessaires pour sa conception et son développement.

### 1.2. Contexte du projet

Avec la transformation digitale du marché de l'emploi, les professionnels ne se contentent plus de profils ou d'offres classiques, mais recherchent des retours d'expérience concrets et fiables. Aujourd'hui, ces informations existent, mais elles sont dispersées sur plusieurs plateformes (forums, réseaux sociaux, témoignages informels) et restent difficilement exploitables.

Dans ce contexte, le projet Connex propose une plateforme dédiée au partage structuré d'expériences professionnelles. L'objectif est non seulement de centraliser ces récits, mais aussi de les valoriser grâce à l'intelligence artificielle, capable d'en extraire des insights utiles pour les utilisateurs et les entreprises. Cette approche permet de transformer des données brutes en informations stratégiques, apportant ainsi une réelle valeur ajoutée dans la compréhension du marché professionnel.

### 1.3. Problématique

Aujourd'hui, les expériences professionnelles sont largement partagées sur différentes plateformes numériques, mais elles restent souvent désorganisées, informelles et difficiles à exploiter. Les utilisateurs publient des témoignages riches en contenu, mais sans structure ni analyse, ce qui limite leur utilité réelle. Par conséquent, il devient difficile pour les étudiants, les chercheurs d'emploi ou les entreprises d'en tirer des informations fiables et pertinentes.

De plus, les plateformes existantes se concentrent principalement sur le réseautage ou les profils, sans offrir de véritable valorisation des récits d'expérience. Dans ce contexte, il est nécessaire de repenser la manière dont ces données sont collectées et utilisées.

**Comment concevoir une plateforme capable de centraliser ces expériences, tout en utilisant l'intelligence artificielle pour les transformer en informations analytiques exploitables, sécurisées et utiles à la prise de décision ?**

### 1.4. Objectif du projet

Le projet Connex a pour objectif principal de concevoir et développer une plateforme web innovante permettant le partage structuré d'expériences professionnelles, tout en exploitant l'intelligence artificielle pour en extraire des informations à forte valeur ajoutée.

Sur le plan technique, l'objectif est de mettre en place une architecture Full-Stack moderne et sécurisée, basée sur :
- un frontend réactif (Next.js),
- un backend performant (FastAPI),
- et une base de données scalable (Supabase/PostgreSQL).

Sur le plan fonctionnel, la plateforme vise à :
- offrir un espace sécurisé où les utilisateurs peuvent publier et consulter des expériences professionnelles,
- permettre des interactions sociales (likes, commentaires, sauvegardes),
- proposer un système de recherche et de filtrage efficace.

Enfin, un objectif clé du projet est d'intégrer une dimension intelligente, en préparant une infrastructure capable d'exploiter l'IA pour :
- analyser les contenus publiés,
- extraire des insights (tendances, sentiments, thèmes),
- fournir des indicateurs utiles aux utilisateurs et aux entreprises.

Ainsi, Connex ne se limite pas à un réseau social, mais se positionne comme un outil d'analyse et d'aide à la décision dans le domaine professionnel.

### 1.5. Spécification des besoins

La spécification des besoins permet d'identifier les fonctionnalités attendues du système ainsi que les contraintes techniques à respecter. Elle constitue une base essentielle pour la conception et le développement de la solution.

#### 1.5.1. Besoins fonctionnels

Les besoins fonctionnels décrivent les actions que les utilisateurs peuvent effectuer sur la plateforme Connex.

| Fonctionnalité | Description |
|----------------|-------------|
| Authentification | Inscription et connexion sécurisées des utilisateurs. |
| Publication | Création et partage de récits d'expériences professionnelles. |
| Fil d'actualité | Consultation dynamique des expériences partagées par la communauté. |
| Interaction | Système de likes, commentaires et sauvegarde en favoris. |
| Recherche | Filtrage avancé des contenus par secteur ou mots-clés. |
| Analyse IA | Extraction d'insights métier et dashboard pour les entreprises. |

*Tableau 1 : Besoins fonctionnels*

#### 1.5.2. Besoins non fonctionnels

Ils garantissent la viabilité technique et la qualité de l'expérience utilisateur.

| Critère | Exigence |
|---------|----------|
| Sécurité | Protection stricte des données via JWT et hachage Bcrypt. |
| Performance | Temps de réponse minimal de l'API et chargement rapide. |
| UX/UI | Interface intuitive, fluide et totalement responsive. |
| Scalabilité | Capacité du système à supporter une montée en charge (Cloud). |
| Disponibilité | Accès stable et permanent aux services de la plateforme. |

*Tableau 2 : Besoins non fonctionnels*

### 1.6. Gestion de projet

La gestion de projet vise à organiser et structurer les différentes étapes de développement de Connex, en définissant un cycle de vie adapté ainsi qu'une planification claire des tâches à réaliser.

#### 1.6.1. Cycle de vie du projet

Pour le développement de Connex, nous avons adopté un modèle Agile, permettant une évolution progressive du projet et une meilleure adaptation aux changements.

Le cycle de vie se décompose en plusieurs phases :
- Analyse des besoins : identification des fonctionnalités et des contraintes
- Conception : modélisation du système (UML, architecture)
- Développement : implémentation des fonctionnalités
- Tests : validation du bon fonctionnement
- Déploiement : mise en production de l'application

#### 1.6.2. Planification du projet

Pour mener à bien le développement de la plateforme Connex, nous avons adopté une approche structurée divisée en cinq grandes phases chronologiques. Cette organisation permet de garantir le respect des délais tout en assurant une qualité technique optimale.

| Phase | Tâches Principales | Durée | Période |
|-------|-------------------|-------|---------|
| Analyse & Cadrage | Étude du besoin, définition de la problématique, benchmark et rédaction du cahier des charges. | 1 semaine | Semaine 1 |
| Conception | Modélisation UML (Use Cases Zero Trust), architecture système et schéma de base de données Supabase. | 2 semaines | Semaines 2 - 3 |
| Développement (Sprint 1) | Configuration du Backend (FastAPI), Auth JWT, Triggers SQL et structure de base du Frontend. | 1 semaine | Semaine 4 |
| Développement (Sprint 2) | Gestion du fil d'actualité (Feed), intégration de l'IA (pipeline complet avec transformers, KeyBERT) et dashboard entreprise. | 1 semaine | Semaine 5 |
| Tests & Corrections | Tests unitaires, correction des bugs (ex: erreurs de cache/refresh), et validation du tunnel d'onboarding. | 1 semaine | Semaine 6 |
| Déploiement | Mise en ligne de la solution, rédaction de la documentation technique et préparation de la soutenance. | 1 semaine | Semaine 7 |

*Tableau 3 : Planification du projet*

#### 1.6.3. Diagramme de Gantt

*(À insérer ici le diagramme de Gantt du projet)*

### 1.7. Entreprenariat

#### 1.7.1. Logo

*(À insérer ici le logo du projet Connex)*

#### 1.7.2. Commercialisation

La plateforme Connex adopte un modèle économique freemium :
- Version gratuite pour les utilisateurs particuliers avec accès aux fonctionnalités de base
- Version premium pour les entreprises avec dashboard analytique avancé et API d'accès aux insights

#### 1.7.3. Financement

Le projet est financé par :
- Fonds propres des fondateurs
- Subventions innovation numériques
- Pré-vente de licences aux entreprises partenaires

### 1.8. Conclusion

Ce chapitre a permis de cadrer les enjeux de Connex. En transformant des récits informels en données exploitables grâce à l'IA, le projet s'affirme comme un véritable outil d'aide à la décision. L'alliance d'une méthodologie Agile et d'une stack moderne (Next.js, FastAPI, Supabase) garantit une solution sécurisée et évolutive. Ce socle étant posé, nous pouvons aborder la phase de Conception pour traduire ces besoins en modèles techniques.

## Chapitre 2 : Analyse et conception

### 2.1. Introduction

Ce chapitre expose la stratégie technique adoptée pour concrétiser la vision de Connex. L'objectif est de transformer les besoins identifiés en une architecture logicielle robuste, capable de traiter et de valoriser les expériences professionnelles.

Pour ce faire, nous détaillerons d'abord une étude de l'existant afin de situer notre valeur ajoutée, avant de présenter l'architecture globale du système. Enfin, nous justifierons les choix technologiques (Next.js, FastAPI, Supabase) qui garantissent la performance, la sécurité et la scalabilité de la plateforme.

Cette étape de conception est le socle indispensable pour assurer la transition entre le concept théorique et la réalisation technique finale.

### 2.2. Étude de l'existant

Dans le domaine du partage d'expériences professionnelles, plusieurs plateformes existent déjà, chacune offrant certaines fonctionnalités mais présentant aussi des limites.

Les réseaux professionnels comme LinkedIn permettent aux utilisateurs de publier des contenus liés à leur parcours, de développer leur réseau et d'accéder à des opportunités d'emploi. Cependant, ces publications restent souvent générales, peu structurées et orientées vers la valorisation personnelle plutôt que vers un retour d'expérience détaillé et exploitable.

D'autres plateformes comme Glassdoor se concentrent sur les avis concernant les entreprises (salaires, conditions de travail), mais les informations restent limitées, parfois anonymes et difficilement vérifiables. De plus, elles ne permettent pas une analyse approfondie des expériences partagées.

Les forums et blogs offrent quant à eux une liberté d'expression plus large, mais les contenus y sont dispersés, non organisés et peu exploitables pour une utilisation analytique ou stratégique.

Ainsi, l'étude de l'existant met en évidence un manque de solutions capables de centraliser, structurer et analyser les expériences professionnelles de manière intelligente. C'est dans ce contexte que s'inscrit Connex, en proposant une plateforme innovante combinant partage d'expérience et exploitation des données par intelligence artificielle.

### 2.3. Benchmark

| Plateforme | Forces | Faiblesses | Opportunités pour Connex |
|------------|--------|------------|-------------------------|
| LinkedIn | Large base d'utilisateurs, réseau professionnel | Contenus peu structurés, orienté CV | Structuration des récits, analyse IA |
| Glassdoor | Avis d'entreprises, données salariales | Anonymat limité, pas d'analyse de contenu | Expériences détaillées, insights qualitatifs |
| Forums spécialisés | Contenus authentiques, communauté engagée | Difficile à exploiter, pas de centralisation | Centralisation avec analyse automatisée |

### 2.4. Architecture de la solution

La solution Connex repose sur une architecture Full-Stack moderne organisée en plusieurs couches, garantissant performance, sécurité et évolutivité.

L'architecture est basée sur un modèle de microservices où le backend FastAPI orchestre les échanges entre le frontend, la base de données Supabase et les modules d'intelligence artificielle.

**🔹Couche Frontend**
Le frontend est développé avec Next.js, permettant de créer une interface utilisateur moderne, rapide et réactive.
Il assure :
- L'affichage du fil d'actualité
- La gestion des interactions (publication, likes, commentaires)
- La communication avec le backend via des requêtes API sécurisées

**🔹Couche Backend**
Le backend est implémenté avec FastAPI, assurant :
- La gestion de la logique métier
- L'authentification des utilisateurs (JWT)
- La sécurisation des données (Bcrypt)
- L'orchestration du pipeline IA (analyse de sentiment, extraction de mots-clés, embeddings)
- L'exposition d'API RESTful avec documentation Swagger automatique

**🔹Base de données**
La persistance des données est assurée par Supabase (PostgreSQL), permettant :
- Le stockage des utilisateurs et des expériences
- La gestion des relations (posts, commentaires, entreprises)
- Une structure évolutive et performante

**🔹Module Intelligence Artificielle**
Un pipeline IA complet est intégré pour :
- L'analyse sémantique des expériences avec transformers et sentence-transformers
- L'analyse de sentiment avancée
- L'extraction de mots-clés avec KeyBERT
- La génération d'embeddings pour la recherche sémantique
- La création d'insights synthétiques pour les entreprises

**🔹Communication entre les composants**
Le flux de fonctionnement est le suivant :
1. L'utilisateur interagit avec le frontend Next.js
2. Le frontend envoie une requête au backend FastAPI
3. Le backend traite la demande et interagit avec Supabase
4. Pour les analyses, le backend déclenche le pipeline IA complet
5. Les résultats structurés sont renvoyés au frontend pour affichage
6. Les insights sont stockés pour analyses futures

### 2.5. Choix des technologies

Le choix des technologies adoptées dans le cadre du projet ProStory-AI repose sur une analyse approfondie des besoins fonctionnels et techniques. L'objectif est de garantir une application performante, sécurisée et évolutive, tout en facilitant le développement et la maintenance.

**Frontend : Next.js**
Le développement de la partie frontend a été réalisé à l'aide du framework Next.js, basé sur React.
Next.js offre une excellente performance grâce au rendu côté serveur (SSR) et à la génération de pages statiques, ce qui améliore considérablement le temps de chargement et l'expérience utilisateur. De plus, il permet une structuration claire du projet et facilite la gestion des routes et des composants. Son intégration avec des outils modernes de design permet également de concevoir une interface fluide, responsive et intuitive.

*Figure 1 : Next.js*

**Backend : FastAPI**
Le backend de l'application est développé avec FastAPI, un framework Python moderne et performant.
FastAPI se distingue par sa rapidité d'exécution grâce à la programmation asynchrone, ce qui le rend adapté aux applications nécessitant un grand nombre de requêtes. Il permet également de créer facilement des API REST sécurisées et bien structurées. Un autre avantage majeur est la génération automatique de documentation interactive (Swagger), facilitant les tests et la collaboration. Enfin, son écosystème Python le rend idéal pour l'intégration future de modules d'intelligence artificielle.

*Figure 2 : FastAPI*

**Base de données : Supabase (PostgreSQL)**
La gestion des données repose sur Supabase, utilisant le système PostgreSQL.
PostgreSQL est une base de données relationnelle robuste, fiable et largement utilisée dans les applications professionnelles. Supabase simplifie sa gestion en offrant des services prêts à l'emploi comme l'authentification et les API automatiques. Cette solution permet une bonne organisation des données (utilisateurs, expériences, interactions) tout en garantissant la scalabilité du système.

*Figure 3 : PostgreSQL*

**Intelligence Artificielle**
Un pipeline IA complet est développé avec des technologies open source de pointe :
- **sentence-transformers** pour les embeddings sémantiques
- **transformers** (Hugging Face) pour l'analyse de texte
- **KeyBERT** pour l'extraction de mots-clés pertinents
- **PyTorch** comme framework d'apprentissage profond
L'intégration de ces technologies permet d'analyser automatiquement les expériences professionnelles afin d'en extraire des informations pertinentes telles que les thèmes récurrents, les sentiments exprimés et les insights stratégiques. Cela transforme des données textuelles brutes en informations exploitables, apportant ainsi une réelle valeur ajoutée à la plateforme.

*Figure 4 : Intelligence Artificielle*

### 2.6. Conception

#### 2.6.1. Diagramme use case

Ce diagramme de cas d'utilisation présente les interactions entre les différents acteurs (utilisateur, entreprise, administrateur) et la plateforme Connex.

*Figure 5 : Diagramme use case*

Il met en évidence les principales fonctionnalités telles que la gestion du profil, la consultation et la publication de contenu, ainsi que l'analyse pour les entreprises. Toutes ces actions nécessitent une authentification préalable afin d'assurer la sécurité et le contrôle d'accès au système.

#### 2.6.2. Diagramme de classe

Le diagramme de classes UML de Connex structure les données nécessaires au fonctionnement de la plateforme.

*Figure 6 : Diagramme de classe*

Au centre, la classe Utilisateur gère les accès (via le rôle et l'email) et est liée à l'Expérience, qui représente le récit professionnel partagé. Chaque expérience peut être enrichie par des Commentaires pour favoriser l'aspect social, et rattachée de manière optionnelle à une Entreprise ou un Événement pour donner du contexte au récit.

L'aspect innovant réside dans la classe Insight, générée par l'intelligence artificielle. Elle analyse le contenu des expériences pour en extraire des thèmes et des scores de sentiment. Ces analyses sont directement liées aux entreprises, leur permettant ainsi de suivre les tendances et les retours d'expérience les concernant. Cette structure garantit une base de données organisée et évolutive, prête pour l'intégration des fonctionnalités d'analyse automatique.

#### 2.6.3. Diagramme d'activité

Ce diagramme illustre le flux opérationnel de la plateforme Connex, depuis l'accès de l'utilisateur jusqu'à la génération d'analyses stratégiques.

*Figure 7 : Diagramme d'activité*

Le processus débute par une vérification de l'authentification, orientant l'utilisateur vers le fil d'actualité ou vers l'inscription. L'aspect central réside dans la création d'une "expérience" : lors de la soumission, le système déclenche une exécution parallèle (fork). D'un côté, il assure le stockage et la mise à jour des recommandations ; de l'autre, il lance instantanément l'analyse par l'intelligence artificielle pour extraire les sentiments et les thèmes du récit. Enfin, le diagramme montre la boucle de valeur finale où les entreprises accèdent à un tableau de bord enrichi par ces insights. Cette modélisation souligne la capacité du système à traiter des tâches complexes en arrière-plan tout en maintenant une navigation fluide pour l'utilisateur.

#### 2.6.4. Diagramme de séquence

Ce diagramme de séquence illustre le fonctionnement dynamique de l'application Connex depuis l'authentification de l'utilisateur jusqu'à la consultation du contenu, la création d'expériences et les interactions. Il montre également l'intégration d'un service d'intelligence artificielle pour analyser les expériences et enrichir les données.

*Figure 8 : Diagramme de séquence*

### 2.7. Conclusion

Ce chapitre a permis de présenter la solution proposée à travers une étude de l'existant, un benchmark des plateformes similaires ainsi que la définition de l'architecture du système. L'analyse a mis en évidence les limites des solutions actuelles, justifiant ainsi la conception de Connex.

Le choix des technologies a été réalisé de manière stratégique afin de garantir une application performante, sécurisée et évolutive. Cette approche offre une base solide pour le développement et l'intégration des fonctionnalités avancées, notamment celles liées à l'intelligence artificielle.

## Chapitre 3 : Réalisations

*(Ce chapitre détaillera la mise en œuvre technique du projet, les captures d'écran de l'application, les défis rencontrés et les solutions apportées.)*

## Conclusion Générale

Le projet Connex est né du constat qu'il manquait, sur le marché actuel, une passerelle structurée entre le récit professionnel brut et l'analyse de données stratégiques. Au terme de ce travail, nous avons conçu et développé une plateforme sociale innovante capable de combler ce fossé en automatisant l'extraction d'insights grâce à l'intelligence artificielle.

Sur le plan fonctionnel, l'application répond aux exigences de partage, d'interaction et de recherche définies lors de la phase d'analyse. Elle offre aux utilisateurs un espace sécurisé pour valoriser leur parcours et aux entreprises un outil d'aide à la décision basé sur des retours d'expérience réels.

Sur le plan technique, la réalisation de ce projet a permis de valider la pertinence d'une architecture moderne :
- La réactivité de Next.js pour une expérience utilisateur fluide.
- La robustesse de FastAPI, avec pipeline IA intégré et orchestration des microservices.
- La fiabilité de Supabase pour une gestion de données scalable et sécurisée.

L'intégration du pipeline IA complet (transformers, sentence-transformers, KeyBERT) constitue la pierre angulaire du projet, transformant une simple base de témoignages en un actif informationnel riche. Bien que la solution actuelle soit pleinement fonctionnelle, elle ouvre des perspectives d'évolution passionnantes, telles que la génération automatique de recommandations de carrière personnalisées ou l'analyse prédictive des tendances sectorielles à plus grande échelle.

Pour conclure, ce projet de fin d'études a été une expérience formatrice majeure, nous permettant de maîtriser l'ensemble du cycle de vie d'une application Full-Stack, de la phase de conception UML jusqu'au déploiement, tout en intégrant les enjeux cruciaux de la cybersécurité et de l'intelligence artificielle dans le web moderne.

## Perspectives

Bien que la plateforme Connex soit aujourd'hui fonctionnelle et réponde aux objectifs initiaux, plusieurs axes d'amélioration peuvent être envisagés pour accroître son impact et sa robustesse :

### 1. Évolution de l'Intelligence Artificielle
- **Analyse prédictive :** Passer d'une analyse descriptive (sentiments, thèmes) à une analyse prédictive capable d'anticiper les évolutions de carrière ou les besoins en compétences d'un secteur donné.
- **Agent conversationnel dédié :** Intégrer un "Coach IA" capable de répondre aux questions des utilisateurs en se basant sur la base de connaissances accumulée par les récits d'expérience.

### 2. Fonctionnalités et Gamification
- **Système de certification :** Mettre en place un mécanisme de validation des expériences (via les entreprises ou les pairs) pour renforcer la fiabilité des témoignages.
- **Badges et Récompenses :** Introduire des éléments de gamification pour encourager les experts à partager des récits de haute qualité et à interagir davantage avec la communauté.

### 3. Sécurité et Confidentialité
- **Anonymisation dynamique :** Utiliser l'IA pour détecter et flouter automatiquement les noms propres ou données sensibles dans les récits afin de garantir un anonymat total si l'utilisateur le souhaite.
- **Architecture décentralisée :** Explorer l'utilisation de technologies blockchain pour la vérification immuable des parcours professionnels.

### 4. Expansion B2B
- **Dashboard analytique avancé :** Développer une interface payante pour les départements RH, leur offrant des outils de "benchmarking" social pour comparer la perception de leur marque employeur par rapport à la concurrence.

## Webographie

### Documentation technique
- **Next.js Documentation** : https://nextjs.org/docs
- **FastAPI Documentation** : https://fastapi.tiangolo.com/
- **Supabase Documentation** : https://supabase.com/docs
- **PostgreSQL Documentation** : https://www.postgresql.org/docs/

### Intelligence Artificielle et Machine Learning
- **Hugging Face Transformers** : https://huggingface.co/docs/transformers/
- **Sentence Transformers** : https://www.sbert.net/
- **KeyBERT Documentation** : https://maartengr.github.io/KeyBERT/
- **PyTorch Documentation** : https://pytorch.org/docs/
- **NumPy Documentation** : https://numpy.org/doc/

### Sécurité et Authentification
- **JWT Handbook** : https://jwt.io/introduction/
- **OWASP Security Guidelines** : https://owasp.org/
- **Bcrypt Documentation** : https://www.npmjs.com/package/bcrypt
- **Python-JOSE** : https://python-jose.readthedocs.io/

### Architecture et Design
- **UML 2.5 Specification** : https://www.omg.org/spec/UML/
- **API Design Guidelines** : https://restfulapi.net/
- **Microservices Patterns** : https://microservices.io/

### Articles de recherche
- "Professional Experience Sharing in Social Networks" - Journal of Computer-Mediated Communication
- "AI-Powered Career Insights: A Systematic Review" - IEEE Transactions on Artificial Intelligence
- "Zero Trust Architecture for Social Platforms" - ACM Computing Surveys

### Références académiques
- "Design Patterns: Elements of Reusable Object-Oriented Software" - Gamma et al.
- "Clean Architecture" - Robert C. Martin
- "Building Microservices" - Sam Newman
