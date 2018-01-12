from random import randint
from statistics import mean, median, mode, pstdev


def pickfrom(*things):
	"""Returns a randomly chosen input."""
	output = things
	if len(things) == 1:
		if isinstance(things[0], (list, tuple, set, dict, str)):
			output = []
			for item in things[0]:
				output.append(item)
		else:
			pass
	else:
		pass
	return output[randint(0, len(output)-1)]


class Die:
	def __init__(self, *faces):
		if len(faces) == 1:
			self.faces = []
			if isinstance(faces[0], int):
				for i in range(faces[0]):
					self.faces.append(i+1)
			elif isinstance(faces[0], (tuple, list, set)):
				for item in faces[0]:
					self.faces.append(item)
			else:
				pass
		else:
			self.faces = faces
		self.numbered = True
		for item in self.faces:
			if not isinstance(item, (int, float)):
				self.numbered = False
				break
		self.results = []

	def roll(self, count=1):
		for i in range(count):
			self.results.append(pickfrom(self.faces))

	def clear_results(self):
		self.results = []

	def add_face(self, *new_faces):
		if len(new_faces) == 1 and isinstance(new_faces[0], (list, tuple, set)):
			new_faces = new_faces[0]
		else:
			pass
		for item in new_faces:
			self.faces.append(item)
		if self.numbered:
			for item in new_faces:
				if not isinstance(item, (int, float)):
					self.numbered = False
					break
				else:
					pass
		else:
			pass

	def remove(self, *faces):
		if len(faces) == 1 and isinstance(faces[0], (list, tuple, set)):
			faces = faces[0]
		else:
			pass
		for item in faces:
			try:
				self.faces.remove(item)
			except:
				pass
		if not self.numbered:
			self.numbered = True
			for item in self.faces:
				if not isinstance(item, (int, float)):
					self.numbered = False
					break
				else:
					pass
		else:
			pass

	def clear_faces(self):
		self.faces = []
		self.numbered = False

	def drop(self, count=1):
		if self.numbered:
			for i in range(count):
				self.results.remove(min(self.results))
		else:
			pass

	def analyze(self):
		print("Results:	", self.results)
		print("Dice Count:	", len(self.results))
		if self.numbered:
			self.results.sort()
			print("Minimum:	", self.results[0])
			print("Maximum:	", self.results[-1])
			print("Median:		", median(self.results))
			print("Mean:		", mean(self.results))
			print("Mode:		", mode(self.results))
			print("St. Dev:	", pstdev(self.results))
		else:
			pass
		print("Distribution:")
		for item in set(self.faces):
			print(str(item)+":	", self.results.count(item))

