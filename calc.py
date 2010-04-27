# This module provides functions for the calculations.

# Convert a given amount of ores to minerals.
# Returns a dictionary with Mineral objects.
def ores_to_minerals():
	# TODO: Add conversion code.
	pass

# Calculates the total ISK value of all items in a list.
def total_value(list):
	sum = 0
	for elements in list:
		sum += elements.amount * elements.price
	return sum
