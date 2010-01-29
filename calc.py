# This module provides functions for the calculations.

# Calculates the total value of all items in a list.
def total_value(list):
	sum = 0
	for elements in list:
		sum += elements.amount * elements.price
	return sum
