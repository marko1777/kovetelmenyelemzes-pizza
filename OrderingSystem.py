import enum
import json


class OrderType(enum.Enum):
    PizzaMexicana = 0
    PizzaRucolaXXL = 1
    PizzaChicken = 2
    Coke = 3
    Beer = 4


class OrderDescription:
    def __init__(self, cost, isBeverage):
        self._cost = cost
        self._isBeverage = isBeverage


class OrderingSystem:
    def __init__(self, priceMinimum, bonusMinimum):
        self._priceMinimum = priceMinimum
        self._bonusMinimum = bonusMinimum
        self._orders = {}
        self._currentPrice = 0

    _pizzaPrices = {
        OrderType.PizzaMexicana.value: OrderDescription(7, False),
        OrderType.PizzaRucolaXXL.value: OrderDescription(14, False),
        OrderType.PizzaChicken.value: OrderDescription(8.5, False),
        OrderType.Coke.value: OrderDescription(2, True),
        OrderType.Beer.value: OrderDescription(3, True)}

    def add(self, orderType):
        if orderType not in self._orders.keys():
            self._orders[orderType] = 1
        else:
            self._orders[orderType] += 1

        self._currentPrice += self._pizzaPrices[orderType]._cost

    def remove(self, orderType):
        if orderType not in self._orders.keys():
            return

        orderCount = self._orders.get(orderType)
        if orderCount == 1:
            self._orders.pop(orderType)
        else:
            self._orders[orderType] -= 1

        self._currentPrice -= self._pizzaPrices[orderType]._cost

    def currentPrice(self):
        return self._currentPrice

    def restart(self):
        self._orders = {}
        self._currentPrice = 0

    def packToJson(self):
        dataDict = {"orders": self._orders, "price": self._currentPrice}
        return json.dumps(dataDict).encode('utf-8')
