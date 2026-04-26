import requests

def test_feed():
    url = "http://127.0.0.1:8000/api/experience/feed"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            experiences = response.data if hasattr(response, 'data') else response.json()
            for exp in experiences[:3]:
                print(f"ID: {exp.get('id')}")
                print(f"Titre: {exp.get('title')}")
                print(f"Company ID: {exp.get('company_id')}")
                print(f"Company Name: {exp.get('company_name')}")
                print("-" * 20)
        else:
            print(f"Erreur API: {response.status_code}")
    except Exception as e:
        print(f"Erreur connexion: {e}")

if __name__ == "__main__":
    test_feed()
