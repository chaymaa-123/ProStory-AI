# Composant CompanySearch (Frontend)

Ce composant permet de rechercher une entreprise dans la base de données via une interface d'autocomplétion fluide.

## Fonctionnalités
- **Recherche temps réel** : Appelle l'API `GET /api/company/search` avec un debounce de 300ms.
- **Sélection intelligente** : Permet de choisir une entreprise existante (utilise son UUID).
- **Création à la volée** : Si aucune entreprise n'est trouvée, l'utilisateur peut confirmer son texte saisi. Le backend se chargera de créer l'entrée correspondante dans la table `companies`.
- **Feedback visuel** : Indicateur de chargement et icônes d'état.

## Utilisation
```tsx
import { CompanySearch } from '@/components/CompanySearch'

// Dans votre composant de formulaire
<CompanySearch
  value={formData.company_id}
  onSelect={(id, name) => setFormData({ ...formData, company_id: id })}
  placeholder="Rechercher Capgemini..."
/>
```

## Intégration Backend
Le composant s'attend à ce que la route `/api/company/search` renvoie une liste d'objets `{ id: string, name: string }`.
