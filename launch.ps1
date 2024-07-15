cd "C:\Users\Orefice\OneDrive\Bureau\IT\URSAFRAN\ToolFactory\frontend"

Start-Process npm -ArgumentList "run dev" -NoNewWindow

Start-Sleep -Seconds 5

cd "C:\Users\Orefice\OneDrive\Bureau\IT\URSAFRAN\ToolFactory\backend"

Start-Process uvicorn -ArgumentList "backend:app --reload --port 8081" -NoNewWindow

Start-Sleep -Seconds 2

cd "C:\Users\Orefice\OneDrive\Bureau\IT\URSAFRAN\ToolFactory\backend"

Start-Process python -ArgumentList "serverXMLRPC.py" -NoNewWindow


cd "C:\Users\Orefice\OneDrive\Bureau\IT\URSAFRAN\ToolFactory"
Start-Process python -ArgumentList "brave_launcher.py" -NoNewWindow
