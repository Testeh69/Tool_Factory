from xmlrpc.server import SimpleXMLRPCServer
import time
from functionJson import inJsonGetSpecificData, inJsonUpdateSpecificData

"""--------------------------------------------POST-----------------------------------------------------------"""
def sendNbParts(value:int):
    #sendTheNumberOf parts that the robots have loaded
    inJsonUpdateSpecificData("parts",int(value))
    return 1


def sendStateProgram():
    #update the state of the machine
    inJsonUpdateSpecificData("porte",0)
    inJsonUpdateSpecificData("statemachine",1)
    return 1

def sendHistorique(value:int):
    #update the historique parameter
    inJsonUpdateSpecificData("historique",int(value))
    return 1


def sendCycleProgram():
    #Simulation of the time of the machine that takes to make the parts
    if inJsonGetSpecificData("statemachine") == 1:
        print("Programme en Cours")
        cycle = inJsonGetSpecificData("cycle")
        if not isinstance(cycle,int):
            cycle = 2
        time.sleep(cycle)
        print('Programme Finis')
        inJsonUpdateSpecificData("statemachine",0)
        inJsonUpdateSpecificData("porte",1)
    return 1

  

"""--------------------------------------------GET-----------------------------------------------------------"""


def getNbParts()->int:
    return inJsonGetSpecificData("parts")

def getStateProgram()->int:
    #1 The machine work
    #0 The machine is in sleep
    return inJsonGetSpecificData("statemachine")


def getHistorique()->int:
    #1 to .... depending on the branch of the program the universal robot has failed
    return inJsonGetSpecificData("historique")



def getStatePorte()->int:
    #1 Porte Ouverte 
    #0 Porte Fermée
    return inJsonGetSpecificData("porte")

def getScan()->int:
    #1 Plan chargée 
    #0 Aucun plan
    return int(inJsonGetSpecificData("scan_status"))



server = SimpleXMLRPCServer(("169.254.163.6", 8000), allow_none=True)
server.register_function(sendCycleProgram,"sendCycleProgram")
server.register_function(getScan, "getScan")
server.register_function(sendStateProgram, "sendState")
server.register_function(getStateProgram, "getState")
server.register_function(getStatePorte, "getPorte")
server.register_function(getHistorique, "getHistorique")
server.register_function(sendHistorique, "sendHistorique")
server.register_function(getNbParts, "getParts")
server.register_function(sendNbParts, "sendParts")

server.serve_forever()