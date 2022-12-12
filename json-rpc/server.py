#!/usr/bin/python
from jsonrpcserver import Success, method, serve, InvalidParams, Error
import json

# Write message
@method
def write(name, message):    
    if name == "":
        return Error(code=123, message="Empty name provided")

    elif len(name) == 1:
        return InvalidParams("Name cannot be len 1")

    elif message == "":
        return Error(code=123, message="Empty message provided")
    
    else:
        with open("messages-data.json", "r") as read_file:
            jason = json.load(read_file)
        
        id = len(jason.items())+1
        jason.setdefault(f"id{id}", { "name": f"{name}", "message": f"{message}" })

        with open("messages-data.json", "w") as write_file:
            json.dump(jason, write_file, indent=4)

        return Success("Mensaje recibido")

# Read all messages
@method
def readAll():
    with open("messages-data.json", "r") as read_file:
        jason_str = json.load(read_file)
    return Success(jason_str)

#Main
if __name__ == "__main__":
    with open("messages-data.json", "w") as write_file:
        json.dump({}, write_file)
    serve('localhost', 2000)