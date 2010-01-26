# The main executable.
# Currently serves as the main frontend. Input is currently handled here and
# also all of the output.

# Checks for empty strings.
def getIntInput(str):
	try:
		return int(str)
	except ValueError:
		return 0

# Get amounts of minerals.
amountTritanium = getIntInput(input("How much Tritanium was mined? "))
amountPyerite = getIntInput(input("How much Pyerite was mined? "))
amountMexallon = getIntInput(input("How much Mexallon was mined? "))
amountIsogen = getIntInput(input("How much Isogen was mined? "))
amountNocxium = getIntInput(input("How much Nocxium was mined? "))
amountZydrine = getIntInput(input("How much Zydrine was mined? "))
amountMegacyte = getIntInput(input("How much Megacyte was mined? "))

# Set prices for minerals.
priceTritanium = 2.73
pricePyerite = 4.99
priceMexallon = 25.40
priceIsogen = 51.80
priceNocxium = 76.26
priceZydrine = 1596.88
priceMegacyte = 3009.63
