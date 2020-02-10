def num_digits(n):
	"""
	modify the function num_digits so that it will return the 
	correct number of digits for 0, positive and negative numbers.
	"""
	count = 0
	if n == 0:			#to encounter the number 0
		count = 1 
		print(count)
		return count 
	else:
		while n != 0:	
			count = count + 1
			n = abs(n) // 10

	print(count)
	return count 

num_digits(0)
num_digits(-12345)

def reverse(my_string):
	rev_str = ""
	rev_lst = []

	for i in range(len(my_string)-1, -1, -1):
		rev_lst.append(my_string[i])
	rev_str = ''.join(rev_lst)
	print(rev_str)

reverse("hello")

def add_column(matrix):
	"""
	>>> m = [[0, 0], [0, 0]]
	>>> add_column(m)
	[[0, 0, 0], [0, 0, 0]]
	>>> n = [[3, 2], [5, 1], [4, 7]]
	>>> add_column(n)
	[[3, 2, 0], [5, 1, 0], [4, 7, 0]]
	>>> n
	[[3, 2], [5, 1], [4, 7]]
	"""
	if len(matrix[0]) != len(matrix[1]):
		return print("Error! matrix enter must have the same number of rows")

	matrix_len = len(matrix)
	new_matrix = matrix 

	for i in range(matrix_len):
		new_matrix[i].append(0)

	print(new_matrix)
	return new_matrix

m = [[0, 0], [0, 0]]
add_column(m)

str1 = "Data"
str2 = "Science"

if str1 == "Data":
	print(str1)
if str2 == "Data":
	print(str2)
elif str1 == "Data" and str2 == "Science":
	print(str1+str2)
else:
	print("neither")