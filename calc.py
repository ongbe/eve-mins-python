# This module provides functions for the calculations.

def round_to_minimum_batch(amount, minBatch):
	roundedAmount = amount // minBatch * minBatch
	return roundedAmount

def amount_of_batches(amount, minBatch):
	roundedAmount = round_to_minimum_batch(amount, minBatch)
	amountOfBatches = roundedAmount // minBatch
	return amountOfBatches

# Convert a given amount of ores to minerals.
# Returns a dictionary with Mineral objects.
# TODO: Document the parameters.
def ores_to_minerals(oreAmounts, oreData, mineralList):
	outputMinerals = {}
	for mineral in mineralList:
		outputMinerals[mineral] = 0

	for ore in oreData:
		for mineral in mineralList:
			amountOfBatches = amount_of_batches(oreAmounts[ore.name],
				int(ore.minBatch))
			outputMinerals[mineral] += (amountOfBatches *
				int(ore.refinedMinerals[mineral]))
	return outputMinerals

# Calculates the total ISK value of all items in a list.
def total_value(list, amounts):
	sum = 0
	for element in list:
		sum += amounts[element.name] * element.price
	return sum
