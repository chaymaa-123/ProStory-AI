@echo off
echo =======================================================
echo Installation des dependances pour ProStory-AI (Windows)
echo =======================================================

echo.
echo 1. Installation des dependances du Frontend (React)...
cd frontend
call npm install
cd ..

echo.
echo 2. Installation des dependances du Backend (FastAPI)...
cd backend
echo Creation de l'environnement virtuel (venv)...
python -m venv venv
echo Activation de l'environnement et installation des packages...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r exigences.txt
deactivate
cd ..

echo.
echo =======================================================
echo Installation terminee ! 
echo Vous pouvez maintenant utiliser scripts\demarrer_local.bat
echo =======================================================
pause
