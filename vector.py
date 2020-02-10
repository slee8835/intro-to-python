
class Vector(object):
	"""
	A vector contains a numlist.
	The vector class has functions include len, mul, add, getitem and setitem
	return the string with the str function 
	"""
	def __init__(self, numlist = []):
		self.numlist = numlist

	def __str__(self):
		return str(self.numlist)

	def __len__(self):
		"""
		returns the length of the vector
		"""
		return len(self.numlist)

	def __mul__(self, v): 
		"""
		that takes two vectors of numbers of the same length, and returns the sum of 
		the products of the corresponding elements of each (the dot_product).
		"""
		dot = 0

		if len(self.numlist) != len(v.numlist):
			return "Error! 2 vectors must be the same length!"

		for i in range(len(self.numlist)):
			temp = self.numlist[i]*v.numlist[i]
			dot += temp

		return dot

	def __rmul__(self, s):
		""" 
		takes a number, s, and a vector, self, and returns the scalar multiple of self 
		by s.
		"""	
		scalar_vec = Vector([])

		for i in range(len(self.numlist)):
			scalar_vec.numlist.append(s * self.numlist[i])

		return scalar_vec

	def __add__(self, vec2):
		"""
	 	takes two vectors of the same length, and returns a new vector containing the 
	 	sums of the corresponding elements of each
	 	"""
		vec_sum = Vector([])
	
		if len(self.numlist) != len(vec2.numlist):
			return "Error! 2 vectors must be the same length!"

		for i in range(len(self.numlist)):
			vec_sum.numlist.append(self.numlist[i] + vec2.numlist[i])

		return vec_sum

	def __getitem__(self, idx):
		""" allows for indexing in accessing an element. Example:
		>>> v1 = Vector([1,2,3,4])
		>>> v1[0]
		1
		"""
		return self.numlist[idx]

	def __setitem__(self, idx, item):
		""" allows for indexing in asigning na element. Example:
		>>> v1 = Vector([1,2,3,4])
		>>> v1[0] = 100
		>>> print v1
		[100, 2, 3, 4]
		"""
		self.numlist[idx] = item


if __name__ == '__main__':

	numlist = [1, 2, 3]
	v1 = Vector(numlist)
	print(v1)
	print(len(v1))

	numlist2 = [5, 18, 2, 6, 3]
	v2 = Vector(numlist2)
	print(v2)
	print(len(v2))

	print(v1*v2)

	print(Vector([1, 1]) * Vector([1, 1]))
	print(Vector([1, 2]) * Vector([1, 4]))	

	v3 = Vector([4, 5, 11])
	print(v3)
	print(v1 * v3)

	print(5 * Vector([1, 2]))
	print(3 * Vector([1, 0, -1]))
	print(7 * Vector([3, 0, 5, 11, 2]))

	print(Vector([1, 1]) + Vector([1, 1])) 
	print(Vector([1, 2]) + Vector([1, 4]))
	print(Vector([1, 2, 1]) + Vector([1, 4, 3]))

	print(v1[0])
	print(v3[2])

	v1[0] = 2 
	print(v1[0])