"""Point d'entrée principal de l'API FastAPI"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello World'}
