from operator import add, sub

def a_plus_abs_b(a, b):
	"""Return a+abs(b), but without calling abs.

	>>> a_plus_abs_b(2, 3)
	5
	>>> a_plus_abs_b(2, -3)
	5
	"""
	if b < 0: # b is negative. a + abs(b). a - (-b) = a + b
		f = sub
	else: # b is positive. a + b
		f = add # function NOT function call
	return f(a, b) # function call

def two_of_three(a, b, c):
	"""Return x*x + y*y, where x and y are the two largest members of the
	positive numbers a, b, and c.

	>>> two_of_three(1, 2, 3)
	13
	>>> two_of_three(5, 3, 1)
	34
	>>> two_of_three(10, 2, 8)
	164
	>>> two_of_three(5, 5, 5)
	50
	"""
	return a*a + b*b + c*c - min(a, b, c)*min(a, b, c)
	return max(a*a + b*b, b*b + c*c, c*c + a*a) # This will never get return
	"""
	Sum all the squares, then subtract the min squared. a*a + b*b + c*c - c*c where c is min
	Find all pair combinations, then take the max.
	"""

def largest_factor(n):
	"""Return the largest factor of n that is smaller than n.

	>>> largest_factor(15) # factors are 1, 3, 5
	5
	>>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
	40
	>>> largest_factor(13) # factor is 1 since 13 is prime
	1
	"""
	factor = n - 1
	while factor > 0: # This will break when 0 > 0. We will actually never hit this assuming n > 0
		if n % factor == 0: # If the number is prime, then factor = 1 and n % 1 == 0:
			return factor
		factor -= 1

	"""
	Start at n - 1. Try every number until you hit a factor.
	1. Counter (can be an input)
	2. Stop condition in the while statement. Breaks out when False
	3. Decrement/increment our counter (get closer to stop condition)
	"""

def if_function(condition, true_result, false_result):
	"""Return true_result if condition is a true value, and
	false_result otherwise.

	>>> if_function(True, 2, 3)
	2
	>>> if_function(False, 2, 3)
	3
	>>> if_function(3==2, 3+2, 3-2)
	1
	>>> if_function(3>2, 3+2, 3-2)
	5
	"""
	if condition:
		return true_result
	else:
		return false_result


def with_if_statement(): # This function needs to return 1
	"""
	>>> with_if_statement()
	1
	"""
	if c():
		return t() # Only go into suite of if statement when C() is TRUE
	else:
		return f() # Only go into else when all if/elif conditions are FALSE

def with_if_function(): # This function needs to do ANYTHING else
	return if_function(c(), t(), f()) # THIS IS A FUNCTION CALL
"""
Two steps to evaluating a call expression:
1. Evaluate the operator, then operands (left to right)
2. Apply operator to operands (going into the function)
with_if_function ALWAYS evaluates c(), t(), f() <- f() is not evaluated in with_if_statement
with_if_statement depends on c(). c() = True, then t(), c() = False, then f()
"""
def c():
	return True

def t():
	return 1

def f():
	return 1/0 # Cause an error, anything else
	while True: # Infinite Loop
		x = 1

def hailstone(n):
	"""Print the hailstone sequence starting at n and return its
	length.

	>>> a = hailstone(10) # set a equal to return value of hailstone(10)
	10
	5
	16
	8
	4
	2
	1
	>>> a
	7
	"""
	length = 1
	while n != 1: # Will break when n = 1
		print(n)
		if n % 2 == 0:
			n //= 2 # n = n // 2 We have to use // because regular / leaves decimals
		else:
			n = 3 * n + 1
		length += 1
	print(n)
	return length

	"""
	We start at n, if even divide by two, if odd multiply by 3 add 1
	stop at 1
	1. Counter (can be input)
	2. Stop condition
	3. Get closer to stop condition
