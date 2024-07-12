# Déplacer dans le répertoire du frontend
cd "C:\Users\Orefice\OneDrive\Bureau\IT\URSAFRAN\outilArchitecture\frontend"

# Lancer npm run dev en arrière-plan
Start-Process npm -ArgumentList "run dev" -NoNewWindow

# Attendre quelques secondes pour que le serveur npm démarre
Start-Sleep -Seconds 5

# Revenir au répertoire frontend
cd "C:\Users\Orefice\OneDrive\Bureau\IT\URSAFRAN\outilArchitecture\backend"

# Démarrer uvicorn pour le serveur FastAPI sur le port 8081 avec rechargement automatique
Start-Process uvicorn -ArgumentList "backend:app --reload --port 8081" -NoNewWindow

# Attendre quelques secondes pour que uvicorn démarre
Start-Sleep -Seconds 2

# Revenir au répertoire frontend (optionnel, si nécessaire pour votre script Python)
cd "C:\Users\Orefice\OneDrive\Bureau\IT\URSAFRAN\outilArchitecture\backend"

# Démarrer votre script Python (serverXMLRPC.py)
Start-Process python -ArgumentList "serverXMLRPC.py" -NoNewWindow
