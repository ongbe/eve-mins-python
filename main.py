# The main executable.
# Currently serves as the main frontend. Input is handled here and also all of
# the output.
# TODO: Make a menu where one can choose all options from a numbered list.

import locale
import items
import calc

locale.setlocale(locale.LC_ALL, ('sv_SE', 'UTF8'))

#
#   Methods
#
def price_input_method_choice():
	choice = input("Do you wish to load predifined mineral prices? (Y/N) ")
	if check_input_loop(choice) in ['y', 'Y']:
		print("\nPrices loaded.\n")
		mineralPrices = load_prices()
		return mineralPrices
	else:
		print("\nManual input selected.\n")
		mineralPrices = manual_prices()
		return mineralPrices

def ore_or_minerals_choice():
	choice = input("Do you wish to use ores as a basis for calculations? (Y/N) ")
	if check_input_loop(choice) in ['y', 'Y']:
		print("\nOres selected.\n")
		# TODO: add actual functionality.
	else:
		print("\nUsing minerals.\n")
		# TODO: add actual functionality.

# Checks for empty strings.
def get_int_input(str):
	try:
		return int(str)
	except ValueError:
		return 0

# Checks for empty strings.
def get_float_input(str):
	try:
		return float(str)
	except ValueError:
		return 0

def check_boolchoice_input(str):
	if str in ['y', 'Y', 'n', 'N']:
		return True
	else:
		return False

def check_input_loop(str):
	while True:
		if check_boolchoice_input(str):
			return str
		else:
			str = input("Your input was faulty. Try again. (Y/N) ")

def load_prices():
	mineralPrices = {}
	rawPrices = open('prices.list')

	line = rawPrices.readline()
	while line != "":
		splitLine = line.split("=")
		mineralPrices[splitLine[0].lower()] = splitLine[1].strip()
		line = rawPrices.readline()
	return mineralPrices

def manual_prices():
	mineralPrices = {}

	print("Please enter the price of each mineral.")
	mineralPrices['tritanium'] = get_float_input(input("Tritanium: "))
	mineralPrices['pyerite'] = get_float_input(input("Pyerite: "))
	mineralPrices['mexallon'] = get_float_input(input("Mexallon: "))
	mineralPrices['isogen'] = get_float_input(input("Isogen: "))
	mineralPrices['nocxium'] = get_float_input(input("Nocxium: "))
	mineralPrices['zydrine'] = get_float_input(input("Zydrine: "))
	mineralPrices['megacyte'] = get_float_input(input("Megacyte: "))
	
	return mineralPrices

def manual_amounts():
	mineralAmounts = {}
	mineralAmounts['tritanium'] = get_int_input(input(
		"How much Tritanium was refined? "))
	mineralAmounts['pyerite'] = get_int_input(input(
		"How much Pyerite was refined? "))
	mineralAmounts['mexallon'] = get_int_input(input(
		"How much Mexallon was refined? "))
	mineralAmounts['isogen'] = get_int_input(input(
		"How much Isogen was refined? "))
	mineralAmounts['nocxium'] = get_int_input(input(
		"How much Nocxium was refined? "))
	mineralAmounts['zydrine'] = get_int_input(input(
		"How much Zydrine was refined? "))
	mineralAmounts['megacyte'] = get_int_input(input(
		"How much Megacyte was refined? "))

	return mineralAmounts


#
#   User interaction.
#

ore_or_minerals_choice()

mineralPrices = price_input_method_choice()

# TODO: Give option to load predefined amounts from file.
mineralAmounts = manual_amounts()

# Creates a list and appends the minerals (name, amount, price) onto it.
minerals = []
minerals.append(items.Mineral("tritanium", int(mineralAmounts['tritanium']),
                float(mineralPrices['tritanium'])))
minerals.append(items.Mineral("pyerite", int(mineralAmounts['pyerite']),
                float(mineralPrices['pyerite'])))
minerals.append(items.Mineral("mexallon", int(mineralAmounts['mexallon']),
                float(mineralPrices['mexallon'])))
minerals.append(items.Mineral("isogen", int(mineralAmounts['isogen']),
                float(mineralPrices['isogen'])))
minerals.append(items.Mineral("nocxium", int(mineralAmounts['nocxium']),
                float(mineralPrices['nocxium'])))
minerals.append(items.Mineral("zydrine", int(mineralAmounts['zydrine']),
                float(mineralPrices['zydrine'])))
minerals.append(items.Mineral("megacyte", int(mineralAmounts['megacyte']),
                float(mineralPrices['megacyte'])))

print()
print("The total ISK value of the minerals would be: ",
      locale.currency((calc.total_value(minerals)), False, True, False), " ISK")
