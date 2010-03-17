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

def get_float_input(str):
    try:
        return float(str)
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

# -----------------------
# User input starts here.
# -----------------------

# User is given choice to either load predefined mineral prices or input
# them manually.
priceChoice = input("Do you wish to load predifined mineral prices? (Y/N) ")
if check_loop(priceChoice) in ['y', 'Y']:
    mineralPrices = load_prices()
else:
    print("\nManual input selected.\n")
    mineralPrices = manual_prices()

# Get amounts of minerals.
amountTritanium = get_int_input(input("How much Tritanium was refined? "))
amountPyerite = get_int_input(input("How much Pyerite was refined? "))
amountMexallon = get_int_input(input("How much Mexallon was refined? "))
amountIsogen = get_int_input(input("How much Isogen was refined? "))
amountNocxium = get_int_input(input("How much Nocxium was refined? "))
amountZydrine = get_int_input(input("How much Zydrine was refined? "))
amountMegacyte = get_int_input(input("How much Megacyte was refined? "))

# Creates a list and appends the minerals (name, amount, price) onto it.
minerals = []
minerals.append(items.Mineral("tritanium", amountTritanium,
                float(mineralPrices['tritanium'])))
minerals.append(items.Mineral("pyerite", amountPyerite,
                float(mineralPrices['pyerite'])))
minerals.append(items.Mineral("mexallon", amountMexallon,
                float(mineralPrices['mexallon'])))
minerals.append(items.Mineral("isogen", amountIsogen,
                float(mineralPrices['isogen'])))
minerals.append(items.Mineral("nocxium", amountNocxium,
                float(mineralPrices['nocxium'])))
minerals.append(items.Mineral("zydrine", amountZydrine,
                float(mineralPrices['zydrine'])))
minerals.append(items.Mineral("megacyte", amountMegacyte,
                float(mineralPrices['megacyte'])))

print()
print("The total ISK value of the minerals would be: ",
      locale.currency((calc.total_value(minerals)), False, True, False), " ISK")
