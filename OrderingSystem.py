import enum

class PizzaType(enum.Enum):
	PizzaMexicana = 0
	PizzaRucolaXXL = 1
	PizzaChicken = 2
	Coke = 3
	Beer = 4


class PizzaDescription:
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
            PizzaType.PizzaMexicana : PizzaDescription(7, False),
            PizzaType.PizzaRucolaXXL : PizzaDescription(14, False),
            PizzaType.PizzaChicken : PizzaDescription(8.5, False),
            PizzaType.Coke : PizzaDescription(2, True),
            PizzaType.Beer : PizzaDescription(3, True)}

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
