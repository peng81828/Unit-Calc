print ("Peng81828's simple individual price calculator")
goodinput = False
while not goodinput:
	try:
		input_var = float(raw_input("Enter the total price of your item here: $ "))
		goodinput = True
	except ValueError:
		print ("Invalid Input! Are you sure that's a number?")
goodinput2 = False
while not goodinput2:
	try:
		individual = float(raw_input("How many units does your package bring? "))
		goodinput2 = True
	except ValueError:
		print ("Invalid Input! Are you sure that's a number?")
price= (input_var / individual)
price= round (price,2)
print ("The price per unit is $"),price
