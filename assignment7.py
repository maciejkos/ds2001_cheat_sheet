"""
Maciej Kos
DS 2001 - Assignment 7
Oct 16/17, 2024

Copyright 2024 Maciej Kos

This programming assignment is the intellectual property of Maciej Kos.
All rights reserved.

Students are prohibited from sharing, distributing, or making this assignment
publicly available in any form, including but not limited to posting on
public repositories,
forums, or websites. Use of this assignment is restricted to the student it was
provided to for educational purposes only.

Unauthorized sharing or distribution of this assignment may result in academic
penalties and/or disciplinary action as determined by the author or Northeastern
University.

Student's first and last name:
Date:
"""

# == GUIDELINES ==
# ONLY USE THE INSTRUCTIONS COVERED IN DS2000 and DS2001. DO NOT USE ANY OTHER
# INSTRUCTIONS, FUNCTIONS, ETC.
# FOLLOW THE DS2000 STYLE GUIDE

# Feel free to discuss the assignment with the people around you and help each
# other out! It's a great way to learn.
# If you have trouble with any step, raise your hand or ask a TA or
# Maciej for help!

# == GUIDELINES ==
# ONLY USE THE INSTRUCTIONS COVERED IN DS2000 and DS2001. DO NOT USE ANY OTHER
# INSTRUCTIONS, FUNCTIONS, ETC.
# FOLLOW THE DS2000 STYLE GUIDE

# If you have trouble with any step, ask a TA for help!


"""
#######################################
Core problems
#######################################
"""

"""
Below are many functions. Unfortunately, they are all broken! Your job is to
fix all functions based on their docstrings. You will also be asked to write 
a few functions from scratch.

Good luck!
"""


"""
Problem 1: print_hello_n_times()
"""

def print_hello_n_times(n_times):
	"""
	[Concept: Repeating Actions]
	Prints "Hello" n_times
	Hint: Use a loop that runs a fixed number of times.

	Example:
	>>> print_hello_n_times(3)
	Hello
	Hello
	Hello

	Parameters
	----------
	n_times : int
		The number of times "Hello" should be printed

	Returns
	-------
	Doesn't return anything. It just prints "Hello"
	"""

	for : # finish this loop
		print("Hello")

print_hello_n_times(3) # don't change this

"""
Problem 2: print_list_n_times()


# Write a function that prints a list n_times. Call it `print_list_n_times()`.
# Example:
# print_list_n_times(list_to_print = ["apples", "bananas"], n_times = 4)
# ["apples", "bananas"]
# ["apples", "bananas"]
# ["apples", "bananas"]
# ["apples", "bananas"]
# Make sure it has a docstring that describes what the function does, what
# parameters it takes, etc. (See other functions for what to include.)
"""

"""
Problem 3: print_list_indices_and_values()
"""

def print_list_indices_and_values(data):
	"""
	[Concept: Basic Iteration]
	Prints each index and its corresponding value in the list.
	Hint: Use `range()` to get the indices.

	Example:
	>>> print_list_indices_and_values([10, 20, 30, 40, 50])
	Index 0 Value 10
	Index 1 Value 20
	Index 2 Value 30
	Index 3 Value 40
	Index 4 Value 50

	Parameters
	----------
	data : list
		A list of any data type.

	Returns
	-------
	None. Prints output to console.


	"""
	for i in range( # finish this loop
		print("Index", i , "Value", data[i])
		# no other lines of code needed

# don't change this:
print_list_indices_and_values(data = [10, 20, 30, 40, 50])

"""
Problem 4: print_two_lists_side_by_side()
"""

def print_two_lists_side_by_side(list1, list2):
	"""
	[Concept: Basic Iteration]
	Prints the elements of two lists side by side.
	Hint: Use `range()` and indices.  Assume lists are of the same length.

	Example:
	>>> print_two_lists_side_by_side([1, 2, 3], ['A', 'B', 'C'])
	1 A
	2 B
	3 C

	Parameters
	----------
	list1: list
		The first list.
	list2: list
		The second list.

	Note:
		You can assume both lists always have the same length.

	Returns
	-------
	None. Prints output to console.

	"""
	for i in range( # finish this loop
		print(STUFF MISSING HERE)
		# no other lines of code needed

# don't change this:
print_two_lists_side_by_side([1, 2, 3], ['A', 'B', 'C'])

"""
Problem 5: search_for_item()
"""

def search_for_item(): # HMMM, SOMETHING SEEMS TO BE MISSING HERE
	"""
	[Concept: Searching]
	Checks if the target is present in the list. If found, prints "Found!",
	else prints "Not found!".
	Hint: Use a variable to keep track of whether you've found the number.

	Example:
	>>> search_for_item([1, 3, 5, 7, 9], 7)
	Found!
	>>> search_for_item([1, 3, 5, 7, 9], 8)
	Not found!

	Parameters
	----------
	data: list
		A list of any data type
	target: The element you're looking for. Can be any data type as long as
	it's comparable to elements in the list. In other words, if you pass a list
	of ints, the target should also be an int.

	Returns
	-------
	None. Prints to console.
	"""

	found = False # this is a hint, leave it here

	for item  # finish this loop
		# a few lines of code needed here

	if found:
		print("Found!")
	else:
		print("Not found!")

search_for_item([1, 3, 5, 7, 9], 7) # don't change this
search_for_item([1, 3, 5, 7, 9], 8) # don't change this

"""
Problem 6: count_item_in_list()
"""

def count_item_in_list(data, target):
	"""
	[Concept: Counting and Summing]
	Counts how many times the target appears in the list.
	Hint: Use a variable to keep track of the count as you loop through the list.

	Example:
	>>> count_item_in_list([5, 3, 5, 7, 5, 9], 5)
	Number 5 appears 3 times.

	Parameters
	----------
	data : list
		The list you want to check. Can be a list of any data type.
	target:
		The element you're counting. Can be any data type as long as it's
		comparable to elements in the list.

	Returns
	-------
	None. Prints output to console.

	"""
	count = 0

	for candidate in # finish this loop
		# a few lines of code missing here

	print("Number", target, "appears", count, "times.") # don't change this

count_item_in_list([5, 3, 5, 7, 5, 9], 5) # don't change this

"""
Problem 7: sum_list_elements()
"""

def sum_list_elements(numbers):
	"""
	[Concept: Counting and Summing]
	Calculates the sum of all numbers in the list. Do NOT use sum().
	Hint: Use a variable to keep track of the running total.

	Example:
	>>> sum_list_elements([1, 2, 3, 4, 5])
	Sum: 15

	Parameters
	----------
	numbers : list of int or float
		The list of numbers you want to sum.

	Returns
	-------
	None. Prints to console.
	"""
	total = 0 # this is a hint, leave it here
	for # finish this loop
		# one line of code missing here

	print("Sum: ", total) # don't change this

sum_list_elements([1, 2, 3, 4, 5])

"""
Problem 8: find_maximum()
"""

def find_maximum(numbers):
	"""
	[Concept: Finding Max/Min]
	Finds and prints the maximum number in the given list of numbers.
	Hint: Use a variable to keep track of the current maximum as you loop through the list.

	Example:
	>>> find_maximum([3, 5, 7, 2, 9])
	Maximum number: 9

	Parameters
	----------
	numbers : list of int or float
		A list of numbers. You can assume it is not empty.

	Returns
	-------
	None. Prints output to console.
	"""
	maximum =  # this should be the first element in the list, use the
	# right index, don't hardcode the number 3.

	for num  # finish this loop
		# a few lines of code missing here

	print(f"Maximum number: {maximum}") # don't change this

find_maximum([3, 5, 7, 2, 9])

"""
Problem 9: get_non_negative_numbers()
"""

def get_non_negative_numbers(numbers):
	"""
	[Concept: Filtering]
	Creates a new list that contains only the non-negative numbers from the
	original list.
	Hint: Use a new list and append items that meet the condition.

	Example:
	>>> get_non_negative_numbers([-2, 1, -4, 3, -6, 5])
	[1, 3, 5]

	Parameters
	----------
	numbers: list of int or float
		List of numbers to filter.

	Returns
	-------
	list of int or float
		List containing only non-negative numbers.
	"""
	non_negative_numbers = [] # don't change this

	for # finish this loop
		# one line of code missing here
			# one line of code missing here

	return # finish this line

print(get_non_negative_numbers([-2, 1, -4, 3, -6, 5])) # don't change this

"""
Problem 10: remove_all_occurrences()
"""

def remove_all_occurrences(data, target):
	"""
	[Concept: Filtering]
	Removes all instances of a target value from a list. Do NOT use remove().
	Hint: what does this return: "apple" in ["banana", "apple", "cherry"]
	Hint: what does this return: "eggs" in ["banana", "apple", "cherry"]
	(Check in console if unsure.)

	Example:
	Here, we will remove all numbers 2 from the list.
	>>> remove_all_occurrences([1, 2, 3, 2, 4, 2, 5], 2)
	Updated list: [1, 3, 4, 5]

	Parameters
	----------
	data: list
		List of any data type.
	target:
		Value to remove.  Can be any data type found in data.

	Returns
	-------
	list
		Updated list with all target occurrences removed.
	"""
	updated_list_without_target_value = [] # this is a hint, leave it here

	for # finish this loop
		# one line of code missing here
			# one line of code missing here


	return # finish this line

# don't change this:
print(f"Updated list: {remove_all_occurrences([1, 2, 3, 2, 4, 2, 5], 2)}")

"""
#######################################
Stretch goals for 2 extra credits
#######################################
"""

"""
Stretch goal 1

Write a function that takes a list and returns True if this list has
duplicates; otherwise, if returns False.
Here are two test cases for you.
	has_duplicates([1, 2, 3, 2, 5])
	True
	has_duplicates([1, 2, 3, 4, 5])
	False
Make sure it to add a docstring.
"""


"""
Stretch goal 2

Write a function that takes two lists and returns a list of common
elements. If there are no common elements, it returns an empty list.
Here are two test cases for you.
	find_common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
	[4, 5]
	find_common_elements([1, 2, 3], [4, 5, 6])
	[]
Make sure it to add a docstring.
"""

"""
#######################################
Extra problems for additional practice
#######################################
"""

"""
Extra problem 0:
"""

def get_squares(numbers):
	"""
	[Concept: Transforming]
	Creates a new list containing the squares of the numbers in the input list.

	Example:
	>>> get_squares([1, 2, 3, 4, 5])
	Squares: [1, 4, 9, 16, 25]

	Parameters
	----------
	numbers: list of int or float
		List of numbers to be squared.

	Returns
	-------
	list of int or float
		List containing squares.
	"""
	squares = [] # this is a hint, leave it here

	for # finish this loop
	# one line of code missing here

	return # finish this line

squared_numbers = get_squares([1, 2, 3, 4, 5]) # don't change this
print(f"Squares: {squared_numbers}") # don't change this

"""
Extra problem 1: calculate_average_grade()
"""

def calculate_average_grade(grades):
	"""
	[Concept: Averaging]
	Calculates the average of all grades in the list. Do NOT use sum().
	Hint: Sum all grades and divide by the number of grades.
	Hint: The number of grades is the same as the length of your list.

	Example:
	>>> calculate_average_grade([85, 92, 78, 95, 88])
	Average grade: 87.6

	Parameters
	----------
	grades: list
		A list of grades (numbers).

	Returns
	-------
	None. Prints output to console.
	"""
	total = 0 # this is a hint, leave it here

	for grade # finish this loop
		# one line of code missing here

	average = # finish this.
	print(f"Average grade: {average}") # don't change this

"""
Extra problem 2: find_longest_word()
"""

def find_longest_word(words):
	"""
	[Concept: Max/Min]
	Finds the longest word in the list.
	Hint: Compare the length of each word with the current longest word.

	Example:
	>>> find_longest_word(['apple', 'banana', 'cherry', 'date', 'elderberry'])
	Longest word: elderberry

	Parameters
	----------
	words: list of str
		List of words.

	Returns
	-------
	None. Prints output to console.
	"""
	longest_word = ""  # Initialize to an empty string

	for word # finish this loop
		# a few lines of code missing here

	print(f"Longest word: {longest_word}") # don't change this

# don't change this:
find_longest_word(['apple', 'banana', 'cherry', 'date', 'elderberry'])

"""
Extra problem 3: calculate_cumulative_sum()
"""

def calculate_cumulative_sum(numbers):
	"""
	[Concept: Cumulative Sum]
	Creates and returns a list where each element is the sum of all previous
	elements.
	Hint: Keep a running total and add it to the new list in each iteration.

	Example:
	>>> calculate_cumulative_sum([1, 2, 3, 4, 5])
	Cumulative sum: [1, 3, 6, 10, 15]

	Parameters
	----------
	numbers : list of int or float
		A list of numbers.

	Returns
	-------
	list of int or float
		List representing the cumulative sum.
	"""
	cumulative_sum = [] # this is a hint, leave it here
	current_sum = 0 # this is a hint, leave it here

	for # finish this loop
		# a few lines of code missing here

	return # finish this line

cumul_sum = calculate_cumulative_sum([1, 2, 3, 4, 5]) # don't change this
print(f"Cumulative sum: {cumul_sum}") # don't change this

"""
Extra problem 4: print_list_in_reverse()
"""

def print_list_in_reverse(): # HMMM, SOMETHING SEEMS TO BE MISSING HERE
	"""
	[Concept: Reverse Iteration]
	Prints the elements of the list in reverse order.
	Hint: Use a for-loop with `range()` in reverse.
	Hint: Start from the last element.

	Example:
	>>> print_list_in_reverse([1, 2, 3, 4, 5])
	5
	4
	3
	2
	1

	Parameters
	----------
	data : list
		The list to be printed in reverse.

	Returns
	-------
	None. Prints output to console.
	"""
	# fix the line below by replacing XXX and YYY with something that makes
	# sense
	for i in range(range(data[-1], XXX, YYY):
		print() # what should you print here?

print_list_in_reverse([1, 2, 3, 4, 5]) # don't change this


# REMINDER
# ONLY USE THE INSTRUCTIONS COVERED IN DS2000 and DS2001. DO NOT USE ANY OTHER
# INSTRUCTIONS, FUNCTIONS, ETC.
# FOLLOW THE DS2000 STYLE GUIDE

"""
Before submitting the assignment:

0) have you used ONLY the Python instructions that were covered in lectures and 
nothing else? Did you follow the style guide?
1) fill out lines 21 and 22A
2) are variables named correctly? (snake_case and informative names?)
3) are all lines of code < 80 characters?
4) do you use comments and are they above the code they reference, not next 
to it?
5) are there spaces around items? (e.g., x = y not x=y, 
and # comment not #comment)
6) do you use whitespace to separate code into logical chunks?
8) make sure the file is called assignment5.py  
9) make sure to submit assignment5.py
10) close PyCharm, open again, run the whole file and check that everything 
works correctly

Finally, when submitting it to Gradescope, make sure there aren't any errors.
"""