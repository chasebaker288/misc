from random import randint  # kind of wish randint was a vanilla/built-in function


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
	return output[randint(0,len(output)-1)]

