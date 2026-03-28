@echo off
echo =======================================================
echo Lancement du projet prostory-ai (Mode Windows)
echo =======================================================

echo 1. Lancement de la base de donnees (Docker)...
start "prostory-ai - Base de Donnees (Docker)" cmd /c "docker-compose up"

echo 2. Lancement du Backend FastAPI...
start "prostory-ai - Backend (FastAPI)" cmd /c "cd backend && call venv\Scripts\activate.bat && uvicorn app.main:app --reload"

echo 3. Lancement du Frontend React...
start "prostory-ai - Frontend (React)" cmd /c "cd frontend && npm run dev"

echo =======================================================
echo Tous les processus ont ete lances dans de nouvelles fenetres !
echo Pour les arreter, fermez simplement leurs fenetres respectives.
echo =======================================================
pause
