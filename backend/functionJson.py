import json
from typing import Union



file_path = "C:/Users/Orefice/OneDrive/Bureau/IT/URSAFRAN/ToolFactory/backend/fichier_gravure_simulation/data.json"


def inJsonGetSpecificData(key:str, file_path_json:str = file_path) -> Union[int,bool,str]:
    try:
        if isinstance(key,str):
            with open(file_path_json, "r") as file:
                data = json.load(file)
        return data[key]
    except:
        return "Error, the key need to be a string"
    


def inJsonUpdateSpecificData(key:str,value: Union[int,str,bool], file_path_json: str = file_path) ->bool:
    try:
        with open(file_path_json, mode = "r") as file:
            data = json.load(file)
        data[key] = value
        with open(file_path_json, "w") as file:
            json.dump(data, file,indent= 4)
            return True
    except:
        return False




