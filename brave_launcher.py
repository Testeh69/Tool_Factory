import webbrowser
import os
import subprocess



brave_path:str = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
if not os.path.exists(brave_path):
    raise FileNotFoundError(f"Brave executable not found at {brave_path}")

# URL à ouvrir
url:str = "http://localhost:8080/"

# Ouvrir Brave avec l'URL spécifiée
subprocess.Popen([brave_path, url])
