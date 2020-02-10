import sys
import math
#Complete ch 7 (iteration):  exercises 1, 2, 10, 14, 15, 16,

def test(did_pass):
	""" Print the result of a test. """
	linenum = sys._getframe(1).f_lineno # Get the caller's line number.
	if did_pass:
		msg = "Test at line {0} ok.".format(linenum)
	else:
		msg = ("Test at line {0} FAILED.".format(linenum))
	print(msg)

#1 
def count_odd(num_list):
	odd_count = 0
	
	for i in num_list:
		if i %2 != 0:
			odd_count += 1 
	return odd_count

#2
def sum_even(num_list):
	even_sum = 0

	for i in num_list:
		if i%2 == 0:
			even_sum += i
	return even_sum

#10
def is_prime(my_int):
	"""
	returns True if the integer is a prime number.
	returns False if the integer is not a prime number.
	"""
	if my_int > 1:
		for i in range(2, my_int//2):	#the smallest divisible number is 2 
			if my_int%i == 0:			#start dividing my_int with i to find any divisible num
				return False
		return True

#14 
def num_digits(n):
	"""
	modify the function num_digits so that it will return the 
	correct number of digits for 0, positive and negative numbers.
	"""
	count = 0
	if abs(n) > 0:			#to encounter negative numbers
		while n != 0:	
			count = count + 1
			n = abs(n) // 10
		return count 
	elif n == 0:			#to encounter the number 0
		count += 1 
		return count 

#15 
def num_even_digits(n):
	"""
	the function counts the even digits of n 
	"""
	even_digits_count = 0
	if abs(n) > 0:
		while n != 0: 
			if n %2 == 0:
				even_digits_count +=1
			n = abs(n) //10 
		return even_digits_count
	elif n == 0:
		even_digits_count += 1 
		return even_digits_count

#16
def sum_of_squares(xs):
 	"""
 	 computes the sum of the squares of the numbers in 
 	 the list xs.
 	"""
 	square_sums = 0 
 	for i in xs:
 		square_sums += i**2 
 	return square_sums

def test_suite():
	test(count_odd([1, 2, 3, 4]) == 2)
	test(count_odd([3, 3, 9,1929491, 2, 3923948]) == 4)
	
	test(sum_even([2, 4, 1]) == 6)
	test(sum_even([10, 11, 12, 13]) == 22)

	test(is_prime(11))
	test(not is_prime(35))
	test(is_prime(19911121))
	
	test(num_digits(0) == 1)
	test(num_digits(-12345) == 5)
	
	test(num_even_digits(123456) == 3)
	test(num_even_digits(2468) == 4)
	test(num_even_digits(1357) == 0)
	test(num_even_digits(0) == 1)
	
	test(sum_of_squares([2, 3, 4]) == 29)
	test(sum_of_squares([ ]) == 0)
	test(sum_of_squares([2, -3, 4]) == 29)


if __name__== "__main__":
	test_suite()