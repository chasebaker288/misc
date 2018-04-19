"""Based on an idea for distributing damage semi-randomly among multiple enemies in a video game"""

from random import randint

TESTNUMBER = 100

def distribute(integer):
	goal = integer
	results = []
	counter = 0
	while goal > integer*0.1:
		test = 0
		for i in range(2**counter):
			test = max(test, randint(1, goal))
		goal -= test
		results.append(test)
		counter += 1
	if goal > 0:
		results.append(goal)
	return results

distribute(TESTNUMBER)
