#!/usr/bin/python
from jsonrpclib import Server
import sys


ip = 'localhost'
port = 2000
server = Server(f'http://{ip}:{port}')


if len(sys.argv) == 1:
    name = ""
    message = ""

elif len(sys.argv) == 2:
    name = sys.argv[1]
    message = ""

elif len(sys.argv) > 3:
    print("Error params <name> <message>")

else:
    name = sys.argv[1]
    message = sys.argv[2]


print(server.write(name, message))
#print(server.readAll())