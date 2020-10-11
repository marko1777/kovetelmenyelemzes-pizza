import json
import socketserver

from OrderingSystem import OrderingSystem

orderingSystem = OrderingSystem(10, 30)


class OrderingServer:
    def start(self, HOST="localhost", PORT=8089):
        with socketserver.TCPServer((HOST, PORT), OrderHandler) as server:
            print("started")
            server.serve_forever()


class OrderHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        data = b'{' + data.split(b'{')[1]
        print(data)
        dataDict = json.loads(data)
        print(dataDict)

        if dataDict["action"] == "add":
            orderingSystem.add(int(dataDict["orderType"]))
        elif dataDict["action"] == "remove":
            orderingSystem.remove(int(dataDict["orderType"]))
        elif dataDict["action"] == "restart":
            orderingSystem.restart()

        print(orderingSystem.packToJson())
        # self.request.sendall(orderingSystem.packToJson())


if __name__ == "__main__":
    orderingServer = OrderingServer()
    orderingServer.start()
