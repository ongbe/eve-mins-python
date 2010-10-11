# The main executable.
# Currently serves as the main frontend. Input is handled here and also all of
# the output.
# TODO: Make a menu where one can choose all options from a numbered list.
# TODO: Give option to load predefined mineral amounts from file.

from __future__ import division
from __future__ import print_function
from optparse import OptionParser
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
# Parser
#

def parse_command_line_parameters():
	""" Parses command line arguments """
	usage = 'usage: %prog [options] output_filepath'
	version = 'Version: %prog 0.2'
	parser = OptionParser(usage=usage, version=version)

	# Binary 'verbose' flag
	parser.add_option('-v', '--verbose', action='store_true',
		dest='verbose', help='Print information during execution -- '+\
		'useful for debugging [default: %default]')

	# Pass a file name for non-interactive usage.
	parser.add_option('-f', '--file_to_use', action='store',
		type='string', dest='file_to_use', help='a filename with values '+\
		'file [default: %default]')

	# Binary flag for whether prices should be loaded.
	parser.add_option('-p', '--load_prices', action='store_true',
		dest='pricesLoaded', help='Load default prices from file -- '+\
		'[default: %default]')

	# An example int option
	parser.add_option('-i', '--int_value', action='store',
		type='int', dest='int_value', help='an integer value to store '+\
		'[default: %default]')

	# Set default values here if they should be other than None
	parser.set_defaults(verbose=False, string_to_write="Some example input.")

	opts, args = parser.parse_args()

	return opts,args

#
#	Methods
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

def prepare_ore_list(oreList):
"""Add potentially missing ore entries to the passed list.

This is to prevent KeyError's, where keys are missing due to the input
file (and subsequently the oreList) not having all possible ores.
"""
	for ore in ORENAMES:
		if ore not in oreList:
			oreList[ore] = 0
	return oreList

def prepare_mineral_list(mineralList):
"""Add potentially missing mineral entries to the passed list.

This is to prevent KeyError's, where keys are missing due to the input
file (and subsequently the mineralList) not having all possible minerals.
"""
	for mineral in MINERALNAMES:
		if mineral not in mineralList:
			mineralList[mineral] = 0
	return mineralList

def load_prices():
	mineralPrices = {}
	rawPrices = open('prices.data')

	for line in rawPrices:
		splitLine = line.split("=", 1)
		mineralPrices[splitLine[0].lower()] = splitLine[1].strip()
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

def load_amounts(amountFile, ores, minerals):
	inputOres = {}
	inputMinerals = {}
	rawAmounts = open(amountFile)

	for line in rawAmounts:
		material, amount = line.strip().split("=", 1)
		material = material.lower()
		amount = int(amount)
		if material in ores:
			inputOres[material] = amount
		elif material in minerals:
			inputMinerals[material] = amount
		else:
			raise ValueError("Incorrectly formated input file.")

	# Add potentially missing minerals/ores.
	inputOres = prepare_ore_list(inputOres)
	inputMinerals = prepare_mineral_list(inputMinerals)

	return inputOres, inputMinerals


#
#	Main method.
#
def main():
	opts, args = parse_command_line_parameters()
	verbose = opts.verbose

	minedMinerals = []
	mineralPrices = {}
	mineralAmounts = {}
	oreAmounts = {}

	# Price handling.
	if opts.pricesLoaded:
		mineralPrices = load_prices()
	else:
		mineralPrices = choice_mineral_prices_load_predefined()

	# Loading of amounts.
	if (opts.file_to_use != None):
		oreAmounts, mineralAmounts = load_amounts(
			opts.file_to_use, ORENAMES, MINERALNAMES)
		if len(oreAmounts) > 0:
			oreData = load_ores()
			convertedMinerals = calc.ores_to_minerals(oreAmounts, oreData,
				MINERALNAMES)
			for mineral in convertedMinerals:
				mineralAmounts[mineral] += convertedMinerals[mineral]

	else:
		if (prompt_bool("Do you wish to use ores as a basis for calculations?")):
			oreData = load_ores()
			oreAmounts = manual_input("How much {0} was mined? ",
				ORENAMES, prompt_int_input)
			mineralAmounts = calc.ores_to_minerals(oreAmounts, oreData,
				MINERALNAMES)
		else:
			mineralAmounts = manual_input("How much {0} was refined? ",
				MINERALNAMES, prompt_float_input)

	# Creates a list and appends the minerals (name, amount, price) onto it.
	for currentMineral in MINERALNAMES:
		minedMinerals.append(items.Mineral(currentMineral,
			float(mineralPrices[currentMineral])))

	print("The total ISK value of the minerals would be: ",
		locale.currency((calc.total_value(minedMinerals, mineralAmounts)),
		False, True, False), " ISK")


#
#	Execute main()
#
if __name__ == '__main__': main()
