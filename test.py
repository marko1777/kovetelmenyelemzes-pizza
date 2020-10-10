import OrderingSystem as OS

ord = OS.OrderingSystem(10, 30)

ord.add(OS.PizzaType.PizzaMexicana)
ord.add(OS.PizzaType.PizzaRucolaXXL)
ord.add(OS.PizzaType.PizzaChicken)
ord.add(OS.PizzaType.Coke)
ord.add(OS.PizzaType.Beer)

if(ord.currentPrice() == 34.5):
	print("equals")

ord.delete(OS.PizzaType.PizzaMexicana)

if(ord.currentPrice() == 27.5):
	print("equals")

ord.delete(OS.PizzaType.PizzaMexicana)

ord.restart()

if(ord.currentPrice() == 0):
	print("equals")
