from xmlrpc.server import SimpleXMLRPCServer
#import fetchImage
import time

"""--------------------------------------------POST-----------------------------------------------------------"""

def sendStateProgram():
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/ToolFactory/backend/fichier_gravure_simulation/statemachine.txt",mode = "w+", encoding="utf-8") as file:
        file.write(str(1))

def sendHistorique(value:int):
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/ToolFactory/backend/fichier_gravure_simulation/historique.txt",mode = "w+", encoding="utf-8") as file:
        file.write(str(value))
    
def sendCycleProgram():
    print("Programme en Cours")
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/ToolFactory/backend/fichier_gravure_simulation/statemachine.txt",mode = "r+", encoding="utf-8") as file:
        cycle = file.read()
    if isinstance(cycle,int):
        cycle = int(cycle)
    else:
        cycle = 2
    time.sleep(cycle)
    print('Programme Finis')
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/ToolFactory/backend/fichier_gravure_simulation/statemachine.txt",mode = "w+", encoding="utf-8") as file:
        file.write(str(0))

"""--------------------------------------------GET-----------------------------------------------------------"""

def getStateProgram():
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/ToolFactory/backend/fichier_gravure_simulation/statemachine.txt",mode = "r", encoding="utf-8") as file:
        x = file.read()
    return int(x)


def getHistorique():
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/ToolFactory/backend/fichier_gravure_simulation/historique.txt",mode = "r", encoding="utf-8") as file:
        x = file.read()
    return int(x)



def getStatePorte():
    #1 Porte Ouverte 
    #0 Porte Fermée
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/ToolFactory/backend/fichier_gravure_simulation/porte.txt",mode = "r", encoding="utf-8") as file:
        x = file.read()
    return int(x)

def getScan():
    #1 Plan chargée 
    #0 Aucun plan
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/ToolFactory/backend/fichier_gravure_simulation/scan.txt",mode = "r", encoding="utf-8") as file:
        x = file.read()
    return int(x)



server = SimpleXMLRPCServer(("169.254.163.6", 8000), allow_none=True)
server.register_function(sendCycleProgram,"sendCycleProgram")
server.register_function(getScan, "getScan")
server.register_function(sendStateProgram, "sendState")
server.register_function(getStateProgram, "getState")
server.register_function(getStatePorte, "getPorte")
server.register_function(getHistorique, "getHistorique")
server.register_function(sendHistorique, "sendHistorique")

server.serve_forever()