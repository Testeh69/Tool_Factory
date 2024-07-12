
def write(x):
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/scan.txt", mode = "w", encoding= "utf-8") as file:
        file.write(x)

def read():
    with open("C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/outilArchitecture/backend/fichier_gravure_simulation/scan.txt", mode = "r", encoding= "utf-8") as file:
        x = file.read()
        x = x.split("\n")
        for word in x:
            result = word.split(":")
            print(result)
            print(type(result))   


write(str(1))
read()


