# This module provides functions for the calculations.

# Convert a given amount of ores to minerals.
# Returns a dictionary with Mineral objects.
def round_to_minimum_batch(amount, minBatch):
	refineAmount = amount // minBatch * minBatch
	return refineAmount

def ores_to_minerals(oreAmounts, oreData, mineralList):
	outputMinerals = {}
	for mineral in mineralList:
		outputMinerals[mineral] = 0

	for ore in oreData:
		for mineral in mineralList:
			outputMinerals[mineral] += (oreAmounts[ore.name] *
				int(ore.refinedMinerals[mineral]))
	return outputMinerals

# Calculates the total ISK value of all items in a list.
def total_value(list, amounts):
	sum = 0
	for element in list:
		sum += amounts[element.name] * element.price
	return sum
