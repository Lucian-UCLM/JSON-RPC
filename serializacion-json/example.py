#!/usr/bin/python
import json

# Datos
data = {
    "payload0":{
        "method": "method0",
        "params":"password",
        "id": "0"
    },
    "payload1":{
        "method": "method1",
        "params":"1, 2, 3, 4",
        "id": "1"
    }
}

# Relleno de datos
for i in range(2, 10):
    method = f"method{i}"
    params = "1, 2, 3"
    data.setdefault(f"payload{i}", {"method": f"{method}", "params": f"{params}", "id": f"{i}"})

# Serializar
with open("data_file.json", "w") as write_file:
    write_file.write("{}")
    json.dump(data, write_file, indent=4)

# Deserializar
with open("data_file.json", "r") as read_file:
    jason = json.load(read_file)

# Editar objeto json
jason.setdefault(f"payload{10}", {"method": f"{10}", "params": f"{10}", "id": f"{10}"})

# Serializar de nuevo
with open("data_file.json", "w") as write_file:
    json.dump(jason, write_file, indent=4)