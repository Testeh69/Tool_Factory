from xmlrpc.server import SimpleXMLRPCServer
#import fetchImage
import time

def getStatePorte():
    #1 Porte Ouverte 
    #0 Porte Fermée
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/porte.txt",mode = "r", encoding="utf-8") as file:
        x = file.read()
    print(x)
    return int(x)

def getScan():
    #1 Plan chargée 
    #0 Aucun plan
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/scan.txt",mode = "r", encoding="utf-8") as file:
        x = file.read()
    return int(x)

def sendStateProgram():
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/statemachine.txt",mode = "w+", encoding="utf-8") as file:
        file.write(str(1))
    print("Programme en Cours")
    time.sleep(2)
    print('Programme Finis')
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/statemachine.txt",mode = "w+", encoding="utf-8") as file:
        file.write(str(0))
    return True

def getStateProgram():
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/statemachine.txt",mode = "r", encoding="utf-8") as file:
        x = file.read()
    return int(x)


def getHistorique():
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/historique.txt",mode = "r", encoding="utf-8") as file:
        x = file.read()
    return int(x)



def sendHistorique(value:str):
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/historique.txt",mode = "w+", encoding="utf-8") as file:
        file.write(0)
    return True


server = SimpleXMLRPCServer(("169.254.163.6", 8000), allow_none=True)
server.register_function(getScan, "getScan")
server.register_function(sendStateProgram, "sendState")
server.register_function(getStateProgram, "getState")
server.register_function(getStatePorte, "getPorte")
server.register_function(getHistorique, "getHistorique")
server.register_function(sendHistorique, "sendHistorique")

server.serve_forever()