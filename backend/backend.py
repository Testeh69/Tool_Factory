from fastapi import FastAPI, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from pydantic import BaseModel
from functionJson import inJsonGetSpecificData, inJsonUpdateSpecificData

app = FastAPI()

# Configuration pour permettre à toutes les origines d'accéder à l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

#La donnée scan indique si un plan a été chargé dans la gravure
#1 plan chargé
#0 aucun plan

async def send_scan_status(websocket:WebSocket):
    await websocket.accept()
    try:
        while True:
            scan_status = inJsonGetSpecificData("scan_status")
            await websocket.send_json({"scan_status": scan_status})
            await asyncio.sleep(1)          
    except FileNotFoundError:
        await websocket.close(code=1011, reason="File not found")
    except Exception as e:
        await websocket.close(code=1011, reason=str(e))


@app.websocket("/scan")
async def websocket_scan(websocket:WebSocket):
    await send_scan_status(websocket)



@app.get("/scan")
def read_scan():
    result = inJsonGetSpecificData("scan_status")
    return{"scan_status":int(result)}

class ScanState(BaseModel):
    state_scan:bool   
   
@app.post("/scan")
def write_scan(loaded_layout: ScanState):
    loaded_layout_value = 1 if loaded_layout.state_scan else 0
    try:
        inJsonUpdateSpecificData("scan_status",loaded_layout_value)
        return {"success": True}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#La donnée porte indique si la porte est ouverte
#1 porte ouverte
#0 porte fermée

async def send_porte_status(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            porte_ouverte = inJsonGetSpecificData("porte")
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
        porte_ouverte = int(porte_ouverte)
        inJsonUpdateSpecificData("porte",porte_ouverte)
        return {"success": True}
    except FileNotFoundError:
        return {"success": False}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/porte")
def read_porte():
    result = inJsonGetSpecificData("porte")
    return{"Porte_Ouverte":int(result)}
    
#Le donnée historique indique a qu'elle étape le robot se situe et si il y a un problème, le robot doit agir directement à cette étape
#0 à 6
async def send_historique(websocket:WebSocket):
    await websocket.accept()
    try:
        while True:
            historique = inJsonGetSpecificData("historique")
            await websocket.send_json({"historique": historique})
            await asyncio.sleep(1)  
    except FileNotFoundError:
        await websocket.close(code=1011, reason="File not found")
    except Exception as e:
        await websocket.close(code=1011, reason=str(e))



@app.websocket("/historique")
async def websocket_historique(websocket:WebSocket):
    await send_historique(websocket)

class HistoriqueData(BaseModel):
    step_program: int

@app.post("/historique")
async def write_historique(data: HistoriqueData):
    step_program = data.step_program
    try:
        inJsonUpdateSpecificData("historique",step_program)
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# La donnée statemachine indique si la machine effectue un programme ou est en pause
#1 Programme en cours
#0 Machine en pause

async def send_machine_status(websocket:WebSocket):
    await websocket.accept()
    try:
        while True:
            state_machine = inJsonGetSpecificData("statemachine")
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
        inJsonUpdateSpecificData("statemachine",value)
        return {"success": True}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/statemachine")
def read_statemachine():
    result = inJsonGetSpecificData("statemachine")
    return{"state_machine":int(result)}


#La donnée cycle indique le temps de cycle de la machine
#1 to 60


class TimeCycle(BaseModel):
    time_cycle:int

@app.post("/cycle")
async def write_cycle(data: TimeCycle):
    time_cycle = data.time_cycle
    try: 
        inJsonUpdateSpecificData("cycle", time_cycle)
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def send_time_cycle(websocket:WebSocket):
    await websocket.accept()
    try:
        while True:
            time_cycle = inJsonGetSpecificData("cycle")
            await websocket.send_json({"time_cycle": time_cycle})
            await asyncio.sleep(1)  
    except FileNotFoundError:
        await websocket.close(code=1011, reason="File not found")
    except Exception as e:
        await websocket.close(code=1011, reason=str(e))


@app.websocket("/cycle")
async def websocket_time_cycle(websocket:WebSocket):
    await send_time_cycle(websocket)

@app.get("/cycle")
def read_time_cycle():
    result = inJsonGetSpecificData("cycle")
    return{"time_cycle":inJsonGetSpecificData("cycle")}


#La donnée parts indique le nombre de pièce qui a été chargée dans la graveuse
#0 to 4 parts

class NumberParts(BaseModel):
    number_parts:int

@app.post("/parts")
def write_number_parts(data:NumberParts):
    result = data.number_parts
    try:
        inJsonUpdateSpecificData("parts", result)
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/parts")
def read_number_parts():
    result = inJsonGetSpecificData("parts")
    return {"number_parts": int(result)}


async def send_parts(websocket:WebSocket):
    await websocket.accept()
    try:
        while True:
            number_parts = inJsonGetSpecificData("parts")
            await websocket.send_json({"number_parts": number_parts})
            await asyncio.sleep(1)  
    except FileNotFoundError:
        await websocket.close(code=1011, reason="File not found")
    except Exception as e:
        await websocket.close(code=1011, reason=str(e))



@app.websocket("/parts")
async def websocket_parts(websocket:WebSocket):
    await send_parts(websocket)