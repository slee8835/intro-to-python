#11,12,13, 14, 15, 16, 17  in the text at the end of chapter 6.
import sys
import math

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

#11 
def compare(a, b):
	"""
	Write a compare function that returns 1 if a > b, 0 if a == b, and -1 if a < b
	"""
	if a > b:
		return 1 
	elif a == b:
		return 0
	elif a < b:
		return -1

#12
def hypotenuse(side_a, side_b):

	"""
	Write a function find_hypot which, given the length of two sides 
	of a right-angled triangle, returns the length of the hypotenuse. 
	"""

	hypot = math.sqrt(side_a**2 + side_b**2)
	return hypot

#13
def slope(x1, y1, x2, y2):
	"""
	Write a function slope(x1, y1, x2, y2) that returns the slope of the line 
	through the points (x1, y1) and (x2, y2)
	"""
	a = (y1-y2)/(x1-x2)
	return a 

def intercept(x1, y1, x2, y2):
	"""
	returns the y-intercept of the line through the points (x1, y1) and (x2, y2)
	"""
	slope_num = slope(x1, y1, x2, y2)
	b = y1 - x1*slope_num
	return b 

#14
def is_even(n):
	"""
	 takes an integer as an argument and returns True if the argument is an even 
	 number and False if it is odd
	 """
	if n%2 == 0:
		return True
	return False

#15
def is_odd(n):
	"""
	returns True when n is odd and False otherwise. 
	Finally, modify it so that it uses a call to is_even to determine if its argument is 
	an odd integer, and ensure that its test still pass.
	"""
	if is_even(n):
		return False
	return True

#16
def is_factor(f, n):

	if n%f == 0:
		return True
	return False 

#17 
def is_multiple(f, n):

	if f%n == 0:
		return True
	return False

#find a way to use is_factor in your definition of is_multiple

def is_multiple2(f, n):

	if is_factor(f, n):
		return False 
	elif not(is_factor(f, n)) and f%n == 0:
		return True
	return False 

def test_suite():
	""" 
	Run the suite of tests for code in this module (this file).
	"""
	test(compare(5, 4) == 1)
	test(compare(7, 7) == 0)
	test(compare(2, 3) == -1)
	test(compare(42, 1) == 1)

	test(hypotenuse(3, 4) == 5.0)
	test(hypotenuse(12, 5) == 13.0)
	test(hypotenuse(24, 7) == 25.0)
	test(hypotenuse(9, 12) == 15.0)

	test(slope(5, 3, 4, 2) == 1.0)
	test(slope(1, 2, 3, 2) == 0.0)
	test(slope(1, 2, 3, 3) == 0.5)
	test(slope(2, 4, 1, 2) == 2.0)
	test(intercept(1, 6, 3, 12) == 3.0)
	test(intercept(6, 1, 1, 6) == 7.0)
	test(intercept(4, 6, 12, 8) == 5.0)

	test(is_even(0) == True)
	test(is_even(15) == False)
	test(is_even(-4) == True)
	test(is_even(9) == False)
	test(is_odd(0) == False)
	test(is_odd(15) == True)
	test(is_odd(-4) == False)
	test(is_odd(9) == True)

	test(is_factor(3, 12))
	test(not is_factor(5, 12))
	test(is_factor(7, 14))
	test(not is_factor(7, 15))
	test(is_factor(1, 15))
	test(is_factor(15, 15))
	test(not is_factor(25, 15))

	test(is_multiple(12, 3))
	test(is_multiple(12, 4))
	test(not is_multiple(12, 5))
	test(is_multiple(12, 6))
	test(not is_multiple(12, 7))

	test(is_multiple2(12, 3))
	test(is_multiple2(12, 4))
	test(not is_multiple2(12, 5))
	test(is_multiple2(12, 6))
	test(not is_multiple2(12, 7))

test_suite()    
