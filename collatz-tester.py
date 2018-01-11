"""
The Collatz Conjecture is an un solved problem in Number Theory.
It claims that if you take any integer and repeat the following:
	• If the number is even, divide it by 2.
	• If the number is odd, multiply it by 3, then add 1.
You will eventually reach 1.

I wanted to play around with the concept and built a program to run the algorithm and keep track of a few things."""

TEST_VALUE = 7777777777777777777777777777777777777777777777


def test(integer, raw_data=False):
	check = integer
	output = []
	evens = []
	while check > 1:
		output.append(check)
		if check % 2 == 0:
			check = int(check/2)
			evens.append(True)
		else:
			check = 3*check+1
			evens.append(False)
		if check == 1:
			output.append(check)
			evens.append(False)
		else:
			pass
	print("Starting number:		", integer)
	print("Number of iterations:", len(output))
	if raw_data:
		print("Raw results:")
		for i in range(len(output)):
			if evens[i]:
				print("(Even)	", output[i])
			else:
				print("(Odd)	", output[i])


test(TEST_VALUE, True)
