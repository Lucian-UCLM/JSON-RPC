#!/usr/bin/python
from jsonrpclib import Server
import sys

def main():
    server = Server('http://localhost:2000')

    name = "Lucian"
    message = "Hola"

    try:
        print(server.write(name, message))
        print(server.readAll())
    except:
        print("Error: ", sys.exc_info())

if __name__ == '__main__':
    main()