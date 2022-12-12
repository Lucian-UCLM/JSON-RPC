# JSON-RPC

Implementación de ejemplos para el trabajo teórico de sistemas distribuidos sobre JSON-RPC

## Autores

- Lucian Andrei Farcas
- Sergio García Muñoz

## Archivos

- [serializacion-json.md](./serializacion-json.md): Carpeta que contiene el ejemplo de serialización y des-serialización en json
- [json-rpc.md](./json-rpc.md): Carpeta que contiene el ejemplo de json-rpc

## Testing de server

- Para testear el server se puede usar el siguitente comando:

```curl -X POST http://localhost:2000 -d '{"jsonrpc": "2.0", "method": "write", "params": {"name": "Lucian", "message": "Hola"}, "id": 1}'```

- Puedes cambiar los campos ```name``` y ```message``` para hacer el experimento más único.

- Hay dos posibles metodos:
    -  ```write```: Para registrar un mensaje con un nombre y el propio mensaje
    -  ```readAll```: Para recibir todos los mensajes que se han escrito