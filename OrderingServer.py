import json
import socketserver

import OrderingSystem


class OrderingServer:
    def start(self, HOST="localhost", PORT="8089"):
        with socketserver.TCPServer((HOST, PORT), OrderHandler) as server:
            server.serve_forever()


class OrderHandler(socketserver.BaseRequestHandler):
    def __init__(self, orderingSystem: OrderingSystem.OrderingSystem):
        self.orderingSystem = orderingSystem

    def handle(self):
        data = self.request.recv(1024).strip()
        dataDict = json.loads(data)

        if dataDict["action"] == "add":
            self.orderingSystem.add(dataDict["orderType"])
        elif dataDict["action"] == "delete":
            self.orderingSystem.delete(dataDict["orderType"])
        elif dataDict["action"] == "restart":
            self.orderingSystem.restart()

        self.request.sendall(self.orderingSystem.packToJson())
