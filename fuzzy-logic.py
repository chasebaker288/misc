"""A series of functions designed to perform basic logic gate operations on "fuzzy" booleans."""


def fzparse(fuzzy_boolean):
    """Forces out-of-bound values within boolean range."""
    if fuzzy_boolean > 1:
        fuzzy_boolean = 1.0
    elif fuzzy_boolean < 0:
        fuzzy_boolean = 0.0
    else:
        pass
    return fuzzy_boolean


def fznot(fuzzy_boolean):
    return 1.0 - fzparse(fuzzy_boolean)


def fzand(*fuzzy_booleans):
    output = 1.0
    if len(fuzzy_booleans) == 1 and isinstance(fuzzy_booleans[0], (list, tuple, set)):
        # Allows arguments to be fed in through an iterable
        fuzzy_booleans = fuzzy_booleans[0]
    else:
        pass
    for item in fuzzy_booleans:
        output *= fzparse(item)
    return output


def fzor(*fuzzy_booleans):
    return fznot(fzand([fznot(x) for x in fuzzy_booleans]))


def fzxor(*fuzzy_booleans):
    return fzor(fuzzy_booleans) * fznot(fzand(fuzzy_booleans))


def fznor(*fuzzy_booleans):
    return fzand([fznot(x) for x in fuzzy_booleans])


def fznand(*fuzzy_booleans):
    return fznot(fzand(fuzzy_booleans))


def fzxnor(*fuzzy_booleans):
    return fznot(fzxor(fuzzy_booleans))


def fzcomplete(*fuzzy_booleans):
    """Checks if a series of fuzzy booleans is Complete / Complementary."""
    output = 0.0
    if len(fuzzy_booleans) == 1 and isinstance(fuzzy_booleans[0], (list, tuple, set)):
        # Allows arguments to be fed in through an iterable
        fuzzy_booleans = fuzzy_booleans[0]
    else:
        pass
    for x in fuzzy_booleans:
        output += fzparse(x)
    if output > 1:
        return 0.0
    else:
        return output
