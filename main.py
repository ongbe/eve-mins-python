import locale
import items
import calc

# Set appropriate locale.
locale.setlocale(locale.LC_ALL, ('sv_SE', 'UTF8'))

# The main executable.
# Currently serves as the main frontend. Input is handled here and also all of
# the output.

# Checks for empty strings.
def get_int_input(str):
    try:
        return int(str)
    except ValueError:
        return 0

def check_choice(str):
    if str in ['y', 'Y', 'n', 'N']:
        return True
    else:
        return False

def check_loop(str):
    while True:
        if check_choice(str):
            return str
        else:
            str = input("Your input was faulty. Load predefined? (Y/N) ")

def get_prices():
    pass

def load_prices():
	mineralPrices = {}
	rawPrices = open('prices.list')

	line = rawPrices.readline()
	while line != "":
		splitLine = line.split("=")
		mineralPrices[splitLine[0].lower()] = splitLine[1].strip()
		line = rawPrices.readline()


# -----------------------
# User input starts here.
# -----------------------

# User is given choice to either load predefined mineral prices or input
# them manually.
priceChoice = input("Do you wish to load predifined mineral prices? (Y/N) ")
if check_loop(priceChoice) in ['y', 'Y']:
	load_prices()
	# TODO: Set the prices.
else:
    print("Manual input selected.")


# Get amounts of minerals.
amountTritanium = get_int_input(input("How much Tritanium was refined? "))
amountPyerite = get_int_input(input("How much Pyerite was refined? "))
amountMexallon = get_int_input(input("How much Mexallon was refined? "))
amountIsogen = get_int_input(input("How much Isogen was refined? "))
amountNocxium = get_int_input(input("How much Nocxium was refined? "))
amountZydrine = get_int_input(input("How much Zydrine was refined? "))
amountMegacyte = get_int_input(input("How much Megacyte was refined? "))

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
minerals.

print()
print("The total ISK value of the minerals would be: ", 
      locale.currency((calc.total_value(minerals)), False, True, False), " ISK")
