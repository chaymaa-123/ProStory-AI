import sys
sys.path.insert(0, '/app')

from app.ai.pipeline import process_experiences
from app.repositories.repo_experience import RepositoryExperience

TECHNOVA_ID = '17ef1c45-e07a-48f2-bb6d-c1621015e32f'
ECOFUTURE_ID = '4fc1f7fa-5bcb-436c-ac95-49ea5db88dc5'

for company_name, company_id in [("TechNova", TECHNOVA_ID), ("EcoFuture", ECOFUTURE_ID)]:
    print(f"\n=== ANALYTICS {company_name} ({company_id}) ===")
    exps = RepositoryExperience.obtenir_par_entreprise(company_id, limit=30)
    print(f"Nb experiences recuperees: {len(exps)}")

    if not exps:
        print("Aucune experience trouvee!")
        continue

    result = process_experiences(exps, max_experiences=30)
    print(f"Positif  : {result['positive']}%")
    print(f"Negatif  : {result['negative']}%")
    print(f"Neutre   : {result['neutral']}%")
    print(f"Dominant : {result['dominant_sentiment']}")
    print(f"Total    : {result['total']} analyses")
    print(f"Keywords : {result['keywords'][:5]}")
    print(f"Summary  : {result['summary'][:100]}...")
