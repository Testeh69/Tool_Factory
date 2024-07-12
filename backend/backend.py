from fastapi import FastAPI, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from pydantic import BaseModel
app = FastAPI()

# Configuration pour permettre à toutes les origines d'accéder à l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

#Le fichier scan indique si un plan a été chargé dans la gravure
#1 plan chargé
#0 aucun plan

async def send_scan_status(websocket:WebSocket):
    await websocket.accept()
    try:
        while True:
            with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/scan.txt", mode="r", encoding="utf-8") as file:
                response = int(file.read())
                scan_status = response
                await websocket.send_json({"scan_status": scan_status})
            await asyncio.sleep(1)          
    except FileNotFoundError:
        await websocket.close(code=1011, reason="File not found")
    except Exception as e:
        await websocket.close(code=1011, reason=str(e))


@app.websocket("/scan")
async def websocket_scan(websocket:WebSocket):
    await send_scan_status(websocket)

class ScanState(BaseModel):
    state_scan:bool
    
@app.post("/scan")
def write_scan(loaded_layout: ScanState):
    loaded_layout_value = 1 if loaded_layout.state_scan else 0
    try:
        loaded_layout_str = str(loaded_layout_value)
        file_path = "C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/scan.txt"
        with open(file_path, mode="w+", encoding="utf-8") as file:
            file.write(loaded_layout_str)
        return {"success": True}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#Le fichier porte indique si la porte est ouverte
#1 porte ouverte
#0 porte fermée

async def send_porte_status(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/porte.txt", mode="r", encoding="utf-8") as file:
                response = int(file.read())
                porte_ouverte = response
                await websocket.send_json({"Porte_Ouverte": porte_ouverte})
            await asyncio.sleep(1)  
    except FileNotFoundError:
        await websocket.close(code=1011, reason="File not found")
    except Exception as e:
        await websocket.close(code=1011, reason=str(e))

@app.websocket("/porte")
async def websocket_porte(websocket: WebSocket):
    await send_porte_status(websocket)

class PorteState(BaseModel):
    porte_ouverte: bool

@app.post("/porte")
def write_porte(porte_state: PorteState):
    porte_ouverte = 1 if porte_state.porte_ouverte else 0
    try:
        porte_ouverte = str(porte_ouverte)
        file_path = "C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/porte.txt"
        with open(file_path, mode="w+", encoding="utf-8") as file:
            file.write(porte_ouverte)
            return {"success": True}
    except FileNotFoundError:
        return {"success": False}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

#Le fichier historique indique a qu'elle étape le robot se situe et si il y a un problème, le robot doit agir directement à cette étape
#0 à 6
async def send_historique(websocket:WebSocket):
    await websocket.accept()
    try:
        while True:
            with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/historique.txt", mode="r", encoding="utf-8") as file:
                response = int(file.read())
                historique = response
                await websocket.send_json({"historique": historique})
            await asyncio.sleep(1)  
    except FileNotFoundError:
        await websocket.close(code=1011, reason="File not found")
    except Exception as e:
        await websocket.close(code=1011, reason=str(e))



@app.websocket("/historique")
async def websocket_historique(websocket:WebSocket):
    await send_historique(websocket)

@app.post("/historique")
def write_historique(step_program:int):
    try:
        step_program = str(step_program)
        with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/historique.txt", mode="w+", encoding="utf-8") as file:
            response = file.write(step_program)
            return True
    except FileNotFoundError:
        return False
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Le fichier state machine indique si la machine effectue un programme ou est en pause
#1 Programme en cours
#0 Machine en pause

async def send_machine_status(websocket:WebSocket):
    await websocket.accept()
    try:
        while True:
            with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/statemachine.txt", mode="r", encoding="utf-8") as file:
                response = int(file.read())
                state_machine = response
                await websocket.send_json({"state_machine": state_machine})
            await asyncio.sleep(1)  
    except FileNotFoundError:
        await websocket.close(code=1011, reason="File not found")
    except Exception as e:
        await websocket.close(code=1011, reason=str(e))


@app.websocket("/statemachine")
async def websocket_machine(websocket:WebSocket):
    await send_machine_status(websocket)


class MachineState(BaseModel):
    state_machine:bool

@app.post("/statemachine")
def write_statemachine(state_machine: MachineState):
    value = 1 if state_machine.state_machine else 0
    try:
        value = str(value)
        file_path = "C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/statemachine.txt"
        with open(file_path, mode="w+", encoding="utf-8") as file:
            file.write(value)
        return {"success": True}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))