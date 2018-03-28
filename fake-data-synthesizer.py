"""Based on a 'what if' idea I had. """

from random import randint


def corr(variable1, variable2):
""" Returns the correlation coefficient between two variables. The function assumes both sets of data are in the same order - that is, the first data point in list 1 is linked to the first data point in list 2."""
	n = len(variable1)
	if n != len(variable2):
		return "ERROR - dataset sizes do not match"
	x = variable1
	y = variable2
	return (n*(sum([(x[i]*y[i]) for i in range(n)])) - sum(x)*sum(y)) / ((n*sum([i**2 for i in x]) - sum(x)**2) * (n*sum([i**2 for i in y]) - sum(x)**2))**0.5


def stdev(listofvalues):
""" Returns the standard deviation of a set of numbers."""
	xbar = sum(listofvalues)/len(listofvalues)
	output = [pow((x - xbar), 2) for x in listofvalues]
	return (sum(output)/len(listofvalues))**0.5


def psuedogauss():
""" Returns a value from -3.0 to 3.0, with probabilities roughly matching a normal distribution."""
	return (randint(-100, 100) + randint(-100, 100) + randint(-100, 100))/100


def generate(dataset1, dataset2):
	if len(dataset1) != len(dataset2):
		return "ERROR - dataset sizes do not match"
	min1 = min(dataset1)
	min2 = min(dataset2)
	max1 = max(dataset1)
	max2 = max(dataset2)
	scale = (max2-min2)/(max1-min1)
	chaos1 = stdev(dataset1)
	chaos2 = stdev(dataset2)
	fakedata1 = [((max1+min1)/2)+chaos1*psuedogauss() for i in range(2*len(dataset1))]
	if corr(dataset1, dataset2) < 0:  # To fix the issue of positive correlations for things that should be negatively correlated
		fakedata2 = [max2-scale*(fakedata1[i]-min1)+(chaos2*psuedogauss()) for i in range(len(fakedata1))]
	else:
		fakedata2 = [min2+scale*(fakedata1[i]-min1)+(chaos2*psuedogauss()) for i in range(len(fakedata1))]
	return [[round(fakedata1[i], 1), round(fakedata2[i])] for i in range(len(fakedata1)) if 0.85*min2 <= fakedata2[i] <= 1.15*max2]  # Trims results to only those with realistic bounds. E.G. no negatives for number of cars owned 


DATA = [  # Placeholder data, via Wikipedia.  Population growth rate  VS  cars owned per capita.
	[0.4, 154],  # China
	[1.1, 151],  # India
	[0.7, 795],  # USA
	[1.1, 68],  # Indonesia
	[0.8, 249],  # Brazil
	[2.0, 18],  # Pakistan
	[2.6, 61],  # Nigeria
	[1.1, 3],  # Bangladesh
	[0.0, 293],  # Russia
	[1.3, 275],  # Mexico
	[-0.2, 591],  # Japan
	[2.5, 8],  # Ethiopia
	[1.5, 30],  # Philippines
	[1.9, 45],  # Egypt
	[1.0, 23],  # Vietnam
	[0.2, 572],  # Germany
	[3.3, 5],  # DR Congo
	[1.1, 256],  # Iran
	[1.6, 253],  # Turkey
	[0.3, 206],  # Thailand
	[0.6, 519],  # UK
	[0.4, 578],  # France
	[-0.1, 679],  # Italy
	[3.1, 7],  # Tanzania
	[1.3, 165],  # South Africa
	[0.9, 7],  # Myanmar
	[0.4, 459],  # South Korea
	[0.8, 148],  # Colombia
	[2.6, 24],  # Kenya
	[0.0, 593]  # Spain
	]


print(generate([DATA[i][0] for i in range(len(DATA))], [DATA[i][1] for i in range(len(DATA))]))


