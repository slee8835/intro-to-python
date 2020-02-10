"""
This program contrains two functions: get_input and calc_temp.
These functions are used to take in a temperature input in C
from user, then convert that temperature to Fahrenheit. 
"""

def get_input():
	"""
	this function gets temperature input from users in Celsius.
	"""
	cel_temp = float(input("Please enter a temperature in Celsius: "))
	return cel_temp

def calc_temp(cel):
	"""
	this function takes in a paramter "cel" which is degree Celsius, 
	and it will calculate the equivalent temperature in Fahrenheit 
	"""
	#to convert C to F: (°C × 9/5) + 32

	Far_temp = (cel*9/5)+32
	return Far_temp 


def main():
  	c = get_input()
  	f = calc_temp(c)
  	print(str(c) + " degrees Celsius is equivalent to " + str(f) + " degrees Fahrenheit.")
  	

if __name__== "__main__":
	main()