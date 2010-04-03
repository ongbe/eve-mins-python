# The main executable.
# Currently serves as the main frontend. Input is handled here and also all of
# the output.
# TODO: Make a menu where one can choose all options from a numbered list.

from __future__ import print_function
import locale
import items
import calc

locale.setlocale(locale.LC_ALL, ('sv_SE', 'UTF8'))

#
#   Methods
#

def use_ores_bool():
	choice = raw_input(
		"Do you wish to use ores as a basis for calculations? (Y/N) ")
	if check_boolchoice_input(choice) in ['y', 'Y']:
		print("\nOres selected.\n")
		return True
	else:
		print("\nUsing minerals.\n")
		return False

def prices_load_predefined_choice():
	choice = raw_input("Do you wish to load predifined mineral prices? (Y/N) ")
	if check_boolchoice_input(choice) in ['y', 'Y']:
		print("\nPrices loaded.\n")
		mineralPrices = load_prices()
		return mineralPrices
	else:
		print("\nManual input selected.\n")
		mineralPrices = manual_input_prices()
		return mineralPrices

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
	while True:
		if str in ['y', 'Y', 'n', 'N']:
			return str
		else:
			str = raw_input("Your input was faulty. Try again. (Y/N) ")

def load_prices():
	mineralPrices = {}
	rawPrices = open('prices.list')

	line = rawPrices.readline()
	while line != "":
		splitLine = line.split("=")
		mineralPrices[splitLine[0].lower()] = splitLine[1].strip()
		line = rawPrices.readline()
	return mineralPrices

def manual_input_ore():
	oreAmounts = {}
	oreAmounts['tritanium'] = get_int_input(raw_input(
		"How much Tritanium was refined? "))
	oreAmounts['pyerite'] = get_int_input(raw_input(
		"How much Pyerite was refined? "))
	oreAmounts['mexallon'] = get_int_input(raw_input(
		"How much Mexallon was refined? "))
	oreAmounts['isogen'] = get_int_input(raw_input(
		"How much Isogen was refined? "))
	oreAmounts['nocxium'] = get_int_input(raw_input(
		"How much Nocxium was refined? "))
	oreAmounts['zydrine'] = get_int_input(raw_input(
		"How much Zydrine was refined? "))
	oreAmounts['megacyte'] = get_int_input(raw_input(
		"How much Megacyte was refined? "))

	return oreAmounts

def manual_input_prices():
	mineralPrices = {}

	print("Please enter the price of each mineral.")
	mineralPrices['tritanium'] = get_float_input(raw_input("Tritanium: "))
	mineralPrices['pyerite'] = get_float_input(raw_input("Pyerite: "))
	mineralPrices['mexallon'] = get_float_input(raw_input("Mexallon: "))
	mineralPrices['isogen'] = get_float_input(raw_input("Isogen: "))
	mineralPrices['nocxium'] = get_float_input(raw_input("Nocxium: "))
	mineralPrices['zydrine'] = get_float_input(raw_input("Zydrine: "))
	mineralPrices['megacyte'] = get_float_input(raw_input("Megacyte: "))
	
	return mineralPrices

def manual_input_amounts():
	mineralAmounts = {}
	mineralAmounts['tritanium'] = get_int_input(raw_input(
		"How much Tritanium was refined? "))
	mineralAmounts['pyerite'] = get_int_input(raw_input(
		"How much Pyerite was refined? "))
	mineralAmounts['mexallon'] = get_int_input(raw_input(
		"How much Mexallon was refined? "))
	mineralAmounts['isogen'] = get_int_input(raw_input(
		"How much Isogen was refined? "))
	mineralAmounts['nocxium'] = get_int_input(raw_input(
		"How much Nocxium was refined? "))
	mineralAmounts['zydrine'] = get_int_input(raw_input(
		"How much Zydrine was refined? "))
	mineralAmounts['megacyte'] = get_int_input(raw_input(
		"How much Megacyte was refined? "))

	return mineralAmounts

#
#   Main method.
#
def main():
	minerals = []
	mineralPrices = {}
	mineralAmounts = {}

	if (use_ores_bool()):
		print("Not implemented!")
		# TODO: call an ore input function.
	else:
		mineralPrices = prices_load_predefined_choice()

		# TODO: Give option to load predefined amounts from file.
		mineralAmounts = manual_input_amounts()

	# Creates a list and appends the minerals (name, amount, price) onto it.
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
		locale.currency((calc.total_value(minerals)),
		False, True, False), " ISK")

#
#   Execute main()
#
if __name__ == '__main__': main()
