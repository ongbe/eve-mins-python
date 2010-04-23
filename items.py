# Module containing specifications for:
# 	Minerals
# Planned:
# 	Ships

# Template for a mineral.
class Mineral:
	def __init__(self, name, amount, price):
		self.name = name
		self.amount = amount
		self.price = price

class Ore:
	def __init__(self, name, amount, minerals):
		self.name = name
		self.amount = amount
		self.minerals = minerals
