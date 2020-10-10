import OrderingSystem as OS

ord = OS.OrderingSystem(10, 30)

ord.add(OS.OrderType.PizzaMexicana)
ord.add(OS.OrderType.PizzaRucolaXXL)
ord.add(OS.OrderType.PizzaChicken)
ord.add(OS.OrderType.Coke)
ord.add(OS.OrderType.Beer)

if(ord.currentPrice() == 34.5):
	print("equals")

ord.delete(OS.OrderType.PizzaMexicana)

if(ord.currentPrice() == 27.5):
	print("equals")

ord.delete(OS.OrderType.PizzaMexicana)

ord.restart()

if(ord.currentPrice() == 0):
	print("equals")
