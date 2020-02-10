
## methods need to return type fraction for + - * /
class Fraction(object):
	"""
	A fraction contains a numerator and a denominator.
	Contains add and mult functions and overload operators.
	return the string with the str function 
	"""
	def __init__(self, numerator = 1, denominator = 1):
		self.numerator = numerator
		self.denominator = denominator

	def __str__(self):
		return str(self.numerator) + "/" + str(self.denominator) 

	def mult(self, f2):
		num = self.numerator * f2.numerator
		dem = self.denominator * f2.denominator
		newfrac = Fraction(num, dem)
		return newfrac

	def __mul__(self, f2):
		num = self.numerator * f2.numerator
		dem = self.denominator * f2.denominator
		newfrac = Fraction(num, dem)
		return newfrac

	def add(self, f2):
		num =self.numerator * f2.denominator + f2.numerator * self.denominator
		dem = self.denominator * f2.denominator
		newfrac = Fraction(num, dem)
		return newfrac

	def __add__(self, f2):
		num =self.numerator * f2.denominator + f2.numerator * self.denominator
		dem = self.denominator * f2.denominator
		newfrac = Fraction(num, dem)
		return newfrac



if __name__ == '__main__':

	f = Fraction(1, 2)
	print(f)

	print(f.mult(Fraction(2, 4)))

	a = Fraction(5, 8)
	b = Fraction(2, 7)
	c = a * b 
	print(c)

	d = Fraction(1, 8)
	e = Fraction(1, 4)

	print(d.add(e))

	f = d + e 
	print(f)

	g = Fraction(6, 16)
	h = a + g * d
	print(h)
