import items

# The main executable.
# Currently serves as the main frontend. Input is currently handled here and
# also all of the output.

# Checks for empty strings.
def getIntInput(str):
	try:
		return int(str)
	except ValueError:
		return 0

# Calculates the total value of all items in a list.
def totalValue(list):
	sum = 0

	for elements in list:
		sum += elements.amount * elements.price

	return sum

# Get amounts of minerals.
amountTritanium = getIntInput(input("How much Tritanium was refined? "))
amountPyerite = getIntInput(input("How much Pyerite was refined? "))
amountMexallon = getIntInput(input("How much Mexallon was refined? "))
amountIsogen = getIntInput(input("How much Isogen was refined? "))
amountNocxium = getIntInput(input("How much Nocxium was refined? "))
amountZydrine = getIntInput(input("How much Zydrine was refined? "))
amountMegacyte = getIntInput(input("How much Megacyte was refined? "))

# Set prices for minerals.
priceTritanium = 2.73
pricePyerite = 4.99
priceMexallon = 25.40
priceIsogen = 51.80
priceNocxium = 76.26
priceZydrine = 1596.88
priceMegacyte = 3009.63

# Creates a list and appends the minerals onto it.
minerals = []
minerals.append(items.Mineral("tritanium", amountTritanium, priceTritanium))
minerals.append(items.Mineral("pyerite", amountPyerite, pricePyerite))
minerals.append(items.Mineral("mexallon", amountMexallon, priceMexallon))
minerals.append(items.Mineral("isogen", amountIsogen, priceIsogen))
minerals.append(items.Mineral("nocxium", amountNocxium, priceNocxium))
minerals.append(items.Mineral("zydrine", amountZydrine, priceZydrine))
minerals.append(items.Mineral("megacyte", amountMegacyte, priceMegacyte))

print()
print("The total ISK value of the minerals would be: ",totalValue(minerals))
