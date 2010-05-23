# The main executable.
# Currently serves as the main frontend. Input is handled here and also all of
# the output.
# TODO: Make a menu where one can choose all options from a numbered list.

from __future__ import division
from __future__ import print_function
import locale
import items
import calc
import csv

locale.setlocale(locale.LC_ALL, ('sv_SE', 'UTF8'))

#
# Constants
#

# TODO: Currently there are two sources for these names. Make it one.
ORENAMES = ['veldspar', 'veldspar, concentrated', 'veldspar, dense', 'scordite',
            'scordite, condensed', 'scordite, massive', 'plagioclase',
            'plagioclase, azure', 'plagioclase, rich', 'pyroxeres',
            'pyroxeres, solid', 'pyroxeres, viscous', 'omber', 'omber, silvery',
            'omber, golden', 'kernite', 'kernite, luminous', 'kernite, fiery',
            'jaspet', 'jaspet, pure', 'jaspet, pristine', 'hemorphite',
            'hemorphite, vivid', 'hemorphite, radiant', 'hedbergite',
            'hedbergite, vitric', 'hedbergite, glazed', 'gneiss',
            'gneiss, iridescent', 'gneiss, prismatic', 'ochre, dark',
            'ochre, onyx', 'ochre, obsidian', 'spodumain',
            'spodumain, bright', 'spodumain, gleaming', 'crokite',
            'crokite, sharp', 'crokite, crystalline', 'bistot',
            'bistot, triclinic', 'bistot, monoclinic', 'arkonor',
            'arkonor, crimson', 'arkonor, prime', 'mercoxit', 'mercoxit, magma',
            'mercoxit, vitreous']

MINERALNAMES = ['tritanium', 'pyerite', 'mexallon', 'isogen', 'nocxium',
                'zydrine', 'megacyte', 'morphite']

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
		mineralPrices = manual_input("{0}: ", MINERALNAMES, prompt_int_input)
		return mineralPrices

def manual_input(question, iterationList, inputFunc):
    output = {}
    for item in iterationList:
        output[item] = inputFunc(question.format(item.capitalize()))
    return output

def load_prices():
	mineralPrices = {}
	rawPrices = open('prices.data')

	line = rawPrices.readline()
	while line != "":
		splitLine = line.split("=")
		mineralPrices[splitLine[0].lower()] = splitLine[1].strip()
		line = rawPrices.readline()
	return mineralPrices

def load_ores():
	ores = []
	rawOres = csv.reader(open('ores.data'), quotechar='"')

	for row in rawOres:
		refinedMinerals = {}
		colCount = 2
		for mineral in MINERALNAMES:
			refinedMinerals[mineral] = row[colCount]
			colCount += 1

		ores.append(items.Ore(row[0], row[1], refinedMinerals))
	return ores

#
#   Main method.
#
def main():
	minedMinerals = []
	mineralPrices = {}
	mineralAmounts = {}
	oreAmounts = {}

	mineralPrices = choice_mineral_prices_load_predefined()

	if (prompt_bool("Do you wish to use ores as a basis for calculations?")):
		oreData = load_ores()
		oreAmounts = manual_input("How much {0} was mined? ",
			ORENAMES, prompt_int_input)
		mineralAmounts = calc.ores_to_minerals(oreAmounts, oreData,
			MINERALNAMES)
	else:
		# TODO: Give option to load predefined amounts from file.
		mineralAmounts = manual_input("How much {0} was refined? ",
			MINERALNAMES, prompt_float_input)

	# Creates a list and appends the minerals (name, amount, price) onto it.
	for currentMineral in MINERALNAMES:
		minedMinerals.append(items.Mineral(currentMineral,
			float(mineralPrices[currentMineral])))

	print()
	print("The total ISK value of the minerals would be: ",
		locale.currency((calc.total_value(minedMinerals, mineralAmounts)),
		False, True, False), " ISK")


#
#   Execute main()
#
if __name__ == '__main__': main()
