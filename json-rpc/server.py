#!/usr/bin/python
from jsonrpcserver import Success, method, serve, InvalidParams, Error
import json


# Write message
@method
def write(name, message):    
    if name == "":
        return Error(code=123, message="El nombre esta vacío")

    elif len(name) == 1:
        return InvalidParams("El nombre no puede ser de un único carácter")

    elif message == "":
        return Error(code=123, message="El mensaje esta vacío")

    elif len(message) == 1:
        return InvalidParams("El mensaje no puede ser de un único carácter")
    
    else:
        with open("data_file.json", "r") as read_file:
            jason = json.load(read_file)
        
        id = len(jason.items())+1
        jason.setdefault(f"id{id}", { "name": f"{name}", "message": f"{message}" })

        with open("data_file.json", "w") as write_file:
            json.dump(jason, write_file, indent=4)

        return Success(f"Mensaje recibido. Gracias {name}!!")


# Read all messages
@method
def readAll():
    with open("data_file.json", "r") as read_file:
        jason_str = json.load(read_file)
    return Success(jason_str)


#Main
if __name__ == "__main__":
    with open("data_file.json", "w") as write_file:
        json.dump({}, write_file)
    
    serve('localhost', 2000)