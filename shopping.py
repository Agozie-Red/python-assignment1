import item_price
print("List of Avialable Products")
print("milk, coffee, bread, cake, oats, choclate, cornflakes, sugar, malt, egg")
item = input("Enter the item you wish to buy: ")
qty = input("Enter the quantity: ")

if item == "milk":
	price=item_price.milk
	print("The price of ",item," is: ",item_price.milk)
	total = int(qty)*price
	print("Total is: ", total)
if item == "coffee":
	price=item_price.coffee
	print("The price of ",item," is: ",item_price.coffee)
	total = int(qty)*price
	print("Total is: ", total)
if item == "bread":
	price=item_price.bread
	print("The price of ",item," is: ",item_price.bread)
	total = int(qty)*price
	print("Total is: ", total)
if item == "cake":
	price=item_price.cake
	print("The price of ",item," is: ",item_price.cake)
	total = int(qty)*price
	print("Total is: ", total)
if item == "oats":
	price=item_price.oats
	print("The price of ",item," is: ",item_price.oats)
	total = int(qty)*price
	print("Total is: ", total)
if item == "choclate":
	price=item_price.choclate
	print("The price of ",item," is: ",item_price.choclate)
	total = int(qty)*price
	print("Total is: ", total)		
if item == "cornflakes":
	price=item_price.cornflakes
	print("The price of ",item," is: ",item_price.cornflakes)
	total = int(qty)*price
	print("Total is: ", total)				
if item == "sugar":
	price=item_price.sugar
	print("The price of ",item," is: ",item_price.sugar)
	total = int(qty)*price
	print("Total is: ", total)
if item == "malt":
	price=item_price.malt
	print("The price of ",item," is: ",item_price.malt)
	total = int(qty)*price
	print("Total is: ", total)	
