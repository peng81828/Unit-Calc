print ("Peng81828's simple individual price calculator")

totalPrice = raw_input("Enter the total price of your item here: $ ")
individual = raw_input("How many units does your package bring? ")

price = (int(totalPrice) / int(individual))
print "The price per unit is $" + str(price)
