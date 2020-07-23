
class Pokemon:
	
	total_available = 0		# total number of pokemon available

	def __init__(self, dex, name, available, line_available, locations):
		self.dex = dex
		self.name = name
		self.available = available
		self.line = line_available
		self.locations = locations
		if line_available == True:		#note: make sure there is a duplication check externally
			pokemon.total_available += 1

	# reference Python OOP Tutorial 3: classmethods and staticmethods

	def __repr__(self):
		return "Pokemon({}, {}, {}, {}, {})".format(self.dex, self.name, self.available, self.line, self.locations)

	def __str__(self):
		return "dex number: {}\npokemon name: {}\navailable?: {}\nline available?: {}\nlocations: {}".format(
			self.dex, self.name, self.available, self.line, self.locations)