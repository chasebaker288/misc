"""
A work in progress
"""

class Polynomial:
	def __init__(self, list_of_coefficients, list_of_exponents=()):
		self.coefficients = list_of_coefficients
		if len(list_of_exponents) == 0:
			self.exponents = list(range(len(list_of_coefficients)))[::-1]
		else:
			if len(list_of_exponents) != len(set(list_of_exponents)):
				print("Error: Duplicate exponent values.")
			elif len(list_of_coefficients) > len(list_of_exponents):
				print("Error: More coefficients than exponents.")
			elif len(list_of_coefficients) < len(list_of_exponents):
				print("Error: More exponents than coefficients.")
			else:
				self.exponents = list_of_exponents
		self.sort()

	def sort(self):
		self.coefficients = [x for _, x in sorted(zip(self.exponents, self.coefficients))][::-1]
		self.exponents = sorted(self.exponents)[::-1]

	def calc(self, x):
		output = 0
		for i in range(len(self.coefficients)):
			output += self.coefficients[i]*x**self.exponents[i]
		return output

	def add(self, new_coefficient, new_exponent):
		if new_exponent in self.exponents:
			self.coefficients[self.exponents.index(new_exponent)] = new_coefficient
		else:
			self.coefficients.append(new_coefficient)
			self.exponents.append(new_exponent)
		self.sort()

	def remove(self, exponent):
		try:
			index = self.exponents.index(exponent)
			self.exponents[index:index+1] = []
			self.coefficients[index:index+1] = []
		except:
			print("Error: Exponent not found")
