# A series of functions designed to perform basic logic gate operations on "fuzzy" booleans.


def fuzparse(fuzzy_boolean):
	"""Forces out-of-bound values within boolean range."""
	if fuzzy_boolean > 1:
		fuzzy_boolean = 1.0
	elif fuzzy_boolean < 0:
		fuzzy_boolean = 0.0
	else:
		pass
	return fuzzy_boolean


def fuznot(fuzzy_boolean):
	return 1.0-fuzparse(fuzzy_boolean)


def fuzand(*fuzzy_booleans):
	output = 1.0
	if len(fuzzy_booleans) == 1 and isinstance(fuzzy_booleans[0], (list, tuple, set)):  # Allows arguments to be fed in through an iterable
		fuzzy_booleans = fuzzy_booleans[0]
	else:
		pass
	for item in fuzzy_booleans:
		output *= fuzparse(item)
	return output


def fuzor(*fuzzy_booleans):
	return fuznot(fuzand([fuznot(x) for x in fuzzy_booleans]))


def fuzxor(*fuzzy_booleans):
	return fuzor(fuzzy_booleans) * (1.0-fuzand(fuzzy_booleans))


def fuznor(*fuzzy_booleans):
	return fuzand([fuznot(x) for x in fuzzy_booleans])


def fuznand(*fuzzy_booleans):
	return 1.0-(fuzand(fuzzy_booleans))


def fuzxnor(*fuzzy_booleans):
	return 1.0-(fuzxor(fuzzy_booleans))


def fuzcomplete(*fuzzy_booleans):
	"""Checks if a series of fuzzy booleans is Complete / Complementary."""
	output = 0.0
	if len(fuzzy_booleans) == 1 and isinstance(fuzzy_booleans[0], (list, tuple, set)):  # Allows arguments to be fed in through an iterable
		fuzzy_booleans = fuzzy_booleans[0]
	else:
		pass
	for x in fuzzy_booleans:
		output += fuzparse(x)
	if output > 1:
		return 0.0
	else:
		return output
