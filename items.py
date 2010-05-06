# TODO: Make the amounts a separate list.

# Module containing specifications for:
#	Minerals
#	Ores
# Planned:
#	Ships

class Mineral:
	def __init__(self, name, price):
		self.name = name
		self.price = price

class Ore:
	def __init__(self, name, minBatch, refinedMinerals):
		self.name = name
		self.minBatch = minBatch
		self.refinedMinerals = refinedMinerals

