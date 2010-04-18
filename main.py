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
# Constants
#

ORES = ['veldspar', 'scordite', 'plagioclase', 'pyroxeres', 'omber', 'kernite',
		'jaspet', 'hemorphite', 'hedbergite', 'gneiss', 'dark ochre',
		'spodumain', 'crokite', 'bistot', 'arkonor', 'mercoxit']
MINERALS = ['tritanium', 'pyerite', 'mexallon', 'isogen', 'nocxium', 'zydrine',
			'megacyte', 'morphite']

#
#   Methods
#

def prompt_bool(prompt):
	choice = raw_input(prompt + ' (Y/N)? ').lower()
	while True:
		if choice in ['y']:
			return True
		elif choice in ['n']:
			return False
		else:
			choice = raw_input(
				"Your input was faulty. Try again. (Y/N) ").lower()

# Gets value and checks for empty strings.
def prompt_int_input(prompt):
	while True:
		try:
			value = int(raw_input(prompt))
		except ValueError:
			return 0
		else:
			return value

# Gets value and checks for empty strings.
def prompt_float_input(prompt):
	while True:
		try:
			value = float(raw_input(prompt))
		except ValueError:
			return 0
		else:
			return value

def choice_mineral_prices_load_predefined():
	if prompt_bool("Do you wish to load predifined mineral prices?"):
		print("\nPrices loaded.\n")
		mineralPrices = load_prices()
		return mineralPrices
	else:
		print("\nManual input selected.\n")
		mineralPrices = manual_input("{0}: ", MINERALS, prompt_int_input)
		return mineralPrices

def manual_input(question, iterationList, inputFunc):
    output = {}
    for item in iterationList:
        output[item] = inputFunc(question.format(item.capitalize()))
    return output

def load_prices():
	mineralPrices = {}
	rawPrices = open('prices.list')

	line = rawPrices.readline()
	while line != "":
		splitLine = line.split("=")
		mineralPrices[splitLine[0].lower()] = splitLine[1].strip()
		line = rawPrices.readline()
	return mineralPrices

#
#   Main method.
#

def main():
	minedMinerals = []
	mineralPrices = {}
	mineralAmounts = {}

	if (prompt_bool("Do you wish to use ores as a basis for calculations?")):
		raise NotImplementedError('Using ores is not implemented yet.')
		# TODO: Call an ore input function.
	else:
		mineralPrices = choice_mineral_prices_load_predefined()

		# TODO: Give option to load predefined amounts from file.
		mineralAmounts = manual_input("How much {0} was refined? ", MINERALS,
			prompt_float_input)

	# Creates a list and appends the minerals (name, amount, price) onto it.
	for currentMineral in MINERALS:
		minedMinerals.append(items.Mineral(currentMineral,
			int(mineralAmounts[currentMineral]),
			float(mineralPrices[currentMineral])))

	print()
	print("The total ISK value of the minerals would be: ",
		locale.currency((calc.total_value(minedMinerals)),
		False, True, False), " ISK")


#
#   Execute main()
#
if __name__ == '__main__': main()
