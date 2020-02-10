import sys
#4, 7,8, 8, 10, 11

def test(did_pass):
	""" Print the result of a test. """
	linenum = sys._getframe(1).f_lineno # Get the caller's line number.
	if did_pass:
		msg = "Test at line {0} ok.".format(linenum)
	else:
		msg = ("Test at line {0} FAILED.".format(linenum))
	print(msg)

#4 
def find(strng, ch, start=0):
    first_occur = start
    while first_occur < len(strng):
        if strng[first_occur] == ch:
            return first_occur
        first_occur += 1
    return -1

def count_letters(my_string, c):
	"""
	the function count_letters repeatedly calls the find function declared 
	above to find new occurrences of the letter being counted
	"""
	str_length = len(my_string)
	char_count = 0			#counter for the letter being counted
	index = 0				#using index to repeatedly call find function with new location in the string 

	while index < str_length:
		occur = find(my_string, c, index)	#start finding c in my_string at index 0
		if occur == -1:						#no c in my_string, break out of while loop 
			return char_count
		char_count += 1 
		index = occur + 1					#find first occurrences of c in string, look at next position 

	return char_count

#7 
def reverse(my_string):
	str_length = len(my_string)
	index = str_length-1
	reverse_list = []		#created an empty list so we can store char in reverse order
	curr_pos = 0			#position index for new reverse order list 

	#traverse through the string in decrementing order 
	for i in range (str_length-1, -1, -1):
		curr_char = my_string[i]		#start from last character of the string
		reverse_list.insert(curr_pos, curr_char)	#storing curr_char into a list starting from 0
		curr_pos += 1 

	reverse_str = ''.join(reverse_list)		#joining the list to turn into a string 
	return reverse_str

#8
def mirror(my_string):
	reverse_str = reverse(my_string)	#to make a reverse string 
	mirror_str = my_string + reverse_str

	return mirror_str

#9 
def remove_letter(c, my_string):
	"""
	function that removes all occurrences of a given letter from a string
	"""
	remove_str = my_string.replace(c, "")

	return remove_str

#10
def is_palindrome(my_word):	
	reverse_word = reverse(my_word)

	if my_word == reverse_word:			#if my_word and the reverse of it is the same, it's a palindrome
		return True
	return False

#11
def count(substr, my_string):
	sub_count = 0
	sub_length = len(substr)
	str_length = len(my_string)

	for i in range(0, str_length-1):
		temp_str = my_string[i: i+sub_length]	 	#creating a temp substring from string to compare with substr

		if temp_str == substr:
			sub_count += 1 

	return sub_count

def test_suite():

	test(count_letters("banana", "a") == 3)
	test(count_letters("hhhhhh", "h") == 6)
	test(reverse("happy") == "yppah")
	test(reverse("Python") == "nohtyP")
	test(reverse("") == "")
	test(reverse("a") == "a")
	test(mirror("good") == "gooddoog")
	test(mirror("Python") == "PythonnohtyP")
	test(mirror("") == "")
	test(mirror("a") == "aa")
	test(remove_letter("a", "apple") == "pple")
	test(remove_letter("a", "banana") == "bnn")
	test(remove_letter("z", "banana") == "banana")
	test(remove_letter("i", "Mississippi") == "Msssspp")
	test(remove_letter("b", "") == "")
	test(remove_letter("b", "c") == "c")
	test(is_palindrome("abba"))
	test(not is_palindrome("abab"))
	test(is_palindrome("tenet"))
	test(not is_palindrome("banana"))
	test(is_palindrome("straw warts"))
	test(is_palindrome("a"))
	test(is_palindrome(""))    # Is an empty string a palindrome?
	test(count("is", "Mississippi") == 2)
	test(count("an", "banana") == 2)
	test(count("ana", "banana") == 2)
	test(count("nana", "banana") == 1)
	test(count("nanan", "banana") == 0)
	test(count("aaa", "aaaaaa") == 4)


if __name__== "__main__":
	test_suite()

