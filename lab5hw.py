import math

## Ch 5:  3,6, 10, 11

##3
#give the logical opposites of these conditions 
"""
1. a < b 
2. a < b
3. a < 18 and day != 3 
4. a < 18 and day == 3 
"""

##6 
def exam_mark(grade):
	"""
	Write a function which is given an exam mark, 
	and it returns a string — the grade for that mark 
	"""

	first = "First"
	upper_second = "Upper Second"
	second = "Second"
	third = "Third"
	f1 = "F1 Supp"
	f2 = "F2"
	f3 = "F3"

	if grade >= 75:
		return first 
	elif grade >= 70 and grade < 75:
		return upper_second
	elif grade >= 60 and grade < 70:
		return second
	elif grade >= 50 and grade < 60:
		return third
	elif grade >= 45 and grade < 50:
		return f1
	elif grade >= 40 and grade < 45:
		return f2
	elif grade < 40:
		return f3


##10 
def find_hypot(side_a, side_b):
	"""
	Write a function find_hypot which, given the length of two sides 
	of a right-angled triangle, returns the length of the hypotenuse. 
	"""

	hypot = math.sqrt(side_a**2 + side_b**2)
	return hypot


##11
def is_rightangled(side_a, side_b, side_c):
	"""
	write a function which given the length of three sides of a triangle,
	will determine whether the triangle is right-angled. Assume that the
	third argument is always the longest side. The function will return True 
	if the triangle is right-angled, or False otherwise.
	"""
	two_sides_square = side_a**2 + side_b**2
	long_side_square = side_c**2

	if abs(long_side_square - two_sides_square) < 0.000001: 
		#if they are approximately equal
		return True
	return False

def main():

# for problem 6
	xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
	
	for i in xs:
		mark = exam_mark(i)
		print("my grade is " + str(i) + ", my exam mark is " + mark)

# for problem 10 
	a = 3.2
	b = 6.8
	c = find_hypot(a , b)
	print(str(c) + " is the hypotenuse for sides " + str(a) + " and " + str(b))

# for problem 11
	e = 13
	d = is_rightangled(a, b, e)
	print(d)

if __name__== "__main__":
	main()