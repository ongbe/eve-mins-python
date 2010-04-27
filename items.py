# TODO: Make the amounts a separate list.

# Module containing specifications for:
#	Minerals
#	Ores
# Planned:
#	Ships

class Mineral:
	def __init__(self, name, amount, price):
		self.name = name
		self.amount = amount
		self.price = price

class Ore:
	def __init__(self, name, amount, minBatch, refinedMinerals):
		self.name = name
		self.amount = amount

		self.refinedMinerals = refinedMinerals

