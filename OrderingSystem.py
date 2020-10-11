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
            OrderType.PizzaMexicana : OrderDescription(7, False),
            OrderType.PizzaRucolaXXL : OrderDescription(14, False),
            OrderType.PizzaChicken : OrderDescription(8.5, False),
            OrderType.Coke : OrderDescription(2, True),
            OrderType.Beer : OrderDescription(3, True)}

	def add(self, pizzaType):
		if(self._orders.get(pizzaType) == None):
			self._orders[pizzaType] = 1
		else:
			++self._orders[pizzaType]

		self._currentPrice += self._pizzaPrices[pizzaType]._cost

	def delete(self, pizzaType):
		orderCount = self._orders.get(pizzaType)
		if(orderCount == None):
			return
		elif(orderCount == 1):
			self._orders.pop(pizzaType)
		else:
			--self._orders[pizzaType]

		self._currentPrice -= self._pizzaPrices[pizzaType]._cost

	def currentPrice(self):
		return self._currentPrice

	def restart(self):
		self._orders = {}
		self._currentPrice = 0

	def packToJson(self):
		dataDict = {"orders": self._orders.keys(), "price": self._currentPrice}
		return json.dumps(dataDict)
