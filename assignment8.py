"""
Maciej Kos
DS 2001 - Assignment 8
Oct 23/24, 2024

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
Terminology:

A 1D list is a collection of elements that themselves are not collections. In
other words, no element of a 1D list can be another list (or dictionary, set, 
etc.)

1d_list = ["a", "b", "c"]

In machine learning/AI, 1d lists are also called vectors. The terminology is
*very* confusing because a 1d list with 3 elements is called a 3-dimensional vector
(or a 3d vector).

A 2D list is a collection of collections.
2d_list = [
	1d_list,
	["d", "e", "f"],
	["g", "h", "i"]
	]

A 3D list is a collection of 2D collections

3d_list = [
	2d_list,
	[
        ["a", "b", "c"],
        ["d", "e", "f"],
		["g", "h", "i"]
    ] # this is another 2d lists
]

To make describing and reasoning about 2D list easier, we use two
conventions. (But there are more.)

1) A 2D list is a list of sublists; each sublist contains elements

list_of_sublist =	[
		["a", "b", "c"], # sublist 0 with 3 elements
		["d", "e", "f"], # sublist 1
		["g", "h", "i"]  # sublist 2
    ]

2) A 2D list is a grid (or a matrix) of rows; each row has columns

grid = [
	[1, 1, 2], # row 0, with 3 columns
	[3, 3, 0], # row 1
	[3, 5, 5] # row 2
	]

The value in row 1 column 2 is 0.

(In Machine Learning/AI, rows can be called vectors, so you have a matrix of
vectors or a grid of vectors or a matrix of rows. I find it very confusing
that, *most of the time*, they all mean the same thing.)

"""


"""
DEADLINE:
1. Submit your current version by the end of the class.
2. Submit the final version by 11:50 pm today. (Of course, if you complete 
everything in class, not need to submit it again.) 

—> IF YOU DON'T SUBMIT THE CURRENT VERSION BY THE END OF THE CLASS, YOU WILL 
LOSE 50% OF YOUR POINTS. <—

Below are many functions. Unfortunately, they are all broken! Your job is to
fix all functions based on their docstrings.

Good luck!
"""

"""
Easy problems; if you can't solve them, it means you are falling behind.
Ask Maciej or TAs for a consult during office hours.
"""

"""
Problem 1
"""


def create_simple_grid():
	"""
	[Concept: 2D Lists - Creation]
	Creates a simple 2x2 grid with zeros in first row and ones in second row.
	Hint: Create two separate lists first
	Hint: Append them to create the 2D list

	Example:
	->  create_simple_grid()
	[[0, 0], [1, 1]]

	Parameters
	----------
	None

	Returns
	-------
	list of lists
		A 2D list with [0,0] and [1,1]
	"""
	zeros =  # finish this line
	ones =  # finish this line
	grid = [] # this is a hint, leave it here


	return # finish this line

print("\nP1:") # don't change this
new_grid = create_simple_grid() # don't change this
print("new_grid:", new_grid) # don't change this

"""
Problem 2
"""

def print_matrix_elements(matrix):
	"""
	[Concept: 2D Lists - Printing]
	Prints each element of a 2D list on a separate line.
	Hint: Use nested loops - outer for rows, inner for elements

	Example:
	->  print_matrix_elements([[1, 2], [3, 4]])
	1
	2
	3
	4

	Parameters
	----------
	matrix: list of lists
		2D list of numbers

	Returns
	-------
	None. Prints to console.
	"""
	for row in # finish this loop
		for # finish this loop
			print(num) # don't change this


print("\nP2:") # don't change this
print("\nPrint_matrix_elements: ")  # don't change this
print_matrix_elements([[1, 2], [3, 4]])  # don't change this

"""
Problem 3
"""

def flatten_list(list_of_lists):
	"""
	[Concept: Nested Loops - List Flattening]
	Combines all sublists into a single list.
	Hint: Use nested loops to access each element

	Example:
	->  flatten_list([[1, 2], [3, 4], [5, 6, 7]])
	[1, 2, 3, 4, 5, 6, 7]

	Parameters
	----------
	list_of_lists: list of lists
		List containing sublists

	Returns
	-------
	list
		Single list containing all elements
	"""
	flat_list = [] # this is a hint, leave it here
	for sublist in # finish this loop
		# another loop goes here
			# one line missing
	return # finish this line


print("\nP3:") # don't change this
list_flattened = flatten_list([[1, 2], [3, 4], [5, 6, 7]]) # don't change this
print("list_flattened:", list_flattened) # don't change this


"""
Problem 4
"""

def count_value(matrix, target):
	"""
	[Concept: 2D Lists - Counting]
	Counts how many times a value appears in a 2D list.
	Hint: Use nested loops and increment a counter

	Example:
	->  count_value([[1, 0, 1], [0, 1, 0], [0, 0, 0]], 1)
	3

	Parameters
	----------
	matrix: list of lists
		2D list to search through
	target: any
		Value to count

	Returns
	-------
	int
		Number of times target appears
	"""
	# one line missing
	for # finish this loop
		# one line missing
			# one line missing
				# one line missing

	return # finish this line

# don't change the below
print("\nP4:") # don't change this
occurrences_n =  count_value([[1, 0, 1], [0, 1, 0], [0, 0, 0]], 1)
print("occurrences_n:", occurrences_n)

"""
Problem 5
"""

def find_maximum(matrix):
	"""
	[Concept: 2D Lists - Finding Maximum]
	Finds the largest number in a 2D list.
	Hint: Start with first number and compare with all others

	Example:
	->  find_maximum([[1, 2], [3, 4]])
	4

	Parameters
	----------
	matrix: list of lists
		2D list of numbers

	Returns
	-------
	int or float
		Largest number found
	"""
	max_value =  # what was the max value equal to last week?
	# one for loop
		# another for loop
			# two lines missing; how did you find the max value last week?

	# one line missing


print("\nP5:") # don't change this
print("find_maximum:", find_maximum([[1, 2], [3, 4]])) # don't change this

""" Medium difficulty problems """

"""
Problem 6
"""

def is_sorted(numbers):
	"""
	[Concept: List Analysis]
	Checks if a list is sorted in ascending order.
	Hint: You will be iterating over list elements. What do you need to
	compare to decide whether a list is sorted in ascending order?

	Hint: You are likely to get the following error: 'list index out of range'.
	What does this error mean exactly?

	Example:
	->  is_sorted([1, 2, 3, 4, 5])
	True
	->  is_sorted([1, 3, 2, 4, 5])
	False

	Parameters
	----------
	numbers: list of int or float
		List to check

	Returns
	-------
	bool
		True if sorted, False otherwise
	"""
	for i # finish this loop
		# tricky conditional goes here
			return # finish this line
	return # finish this line


print("\nP6:") # don't change this
print("is_sorted: ", is_sorted([1, 2, 3, 4, 5])) # don't change this
print("is_sorted: ", is_sorted([1, 3, 2, 4, 5])) # don't change this



"""
Problem 7
"""

def create_index_sum_grid(size):
	"""
	[Concept: 2D Lists - Creation with Computation]
	Creates a grid where each value is sum of its row and column indices.
	Hint: Use nested loops with range(size)

	Example:
	->  create_index_sum_grid(3)
	[[0, 1, 2], [1, 2, 3], [2, 3, 4]]

    Hint: In the above example, what are the row and column indices of 4?

	Parameters
	----------
	size: int
		Size of the grid (size x size)

	Returns
	-------
	list of lists
		Grid where value at [i][j] equals i + j
	"""
	# one line missing
	for i # finish this loop
		row = []
		for j # finish this loop
			# one line missing
		# one line missing
	return grid

print("\nP7:") # don't change this
print("create_index_sum_grid: ", create_index_sum_grid(3)) # don't change this


"""
Problem 8
"""


def multiply_specific_positions(grid, factor, positions):
	"""
	[Concept: List Modification by Position]
	Multiplies values at specific positions by given factor.
	You CANNOT create any new lists.

	Hint: Use position-based access with range()
	Hint:
	->  fruit_1, fruit_2 = ["apple", "banana"]
	->  print(fruit_1) # What would this print?
	Hint: Modify values in place

	Example:
	->  grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	->  positions = [[0, 0], [1, 1], [2, 2]]
	->  multiply_specific_positions(grid, 2, positions)

	Explanation:
	[0, 0] in positions means to take the 0th column in the 0th row of the grid
	and multiply it by the factor. In this example, the factor is 2. (See
	function call.) Since grid[0][0] is 1, we multiply 1 by 2, which is 2.

	Original grid: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	Modified grid: [[2, 2, 3], [4, 10, 6], [7, 8, 18]]

	Parameters
	----------
	grid: list of lists
		2D list of numbers
	factor: int or float
		Number to multiply by
	positions: 2D list of numbers
		List of [row, column] positions to modify

	Returns
	-------
	None. Modifies original grid and prints result.
	"""
	print("Original grid:", grid) # don't change this
	# don't create any new lists
	for row, col in positions:
		# one line missing

		# hint: what would print(row, col) do? what are these values? where do
		# they come from?


	print("Modified grid:", grid)

print("\nP8:") # don't change this
grid_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # don't change this
positions = [[0, 0], [1, 1], [2, 2]] # don't change this
multiply_specific_positions(grid=grid_2d, factor=2, positions=positions) # don't change this

""" Hard problems """

"""
Problem 9 
"""

def find_matching_pairs(grid):
	"""
	[Concept: Nested For-Loops with Position]
	Given a list of sublists, finds pairs of matching numbers that are next to
	each other horizontally within a sublist.
	Hint: Outer loop for rows, inner loop for positions
	Hint: Whenever you hear `position` or `index` it usually means "use range()"
	Hint: Compare current position with next position

	Example:
	>  grid = [
	[1, 1, 2],
	[3, 3, 3],
	[3, 5, 5]]
	->  find_matching_pairs(grid)

	Matching pairs found:
	Row 0: positions 0-1 (value: 1)
	Row 1: positions 0-1 (value: 3)
	Row 1: positions 1-2 (value: 3)
	Row 2: positions 1-2 (value: 5)

	Parameters
	----------
	grid: list of lists
		2D list of numbers

	Returns
	-------
	None. Prints results to console.
	"""
	print("Matching pairs found:") # don't change this
	for i # finish this line
		for j # finish this line
			# tricky conditional goes here
				# below is a hint; don't change this, leave it there
				print(f"Row {i}: positions {j}-{j + 1} (value: {grid[i][j]})")

print("\nP9:") # don't change this

grid = [
	[1, 1, 2],
	[3, 3, 3],
	[3, 5, 5]] # don't change this

find_matching_pairs(grid) # don't change this


"""
Problem 10
"""

def find_value_locations(grid, target):
	"""
	[Concept: 2D List Searching and Counting]
	Counts and locates all occurrences of a value in a 2D list.
	Hint: Keep track of both row and column positions
	Hint: What comes to our mind whenever we hear "position"?
	Hint: Use a counter for total occurrences

	Example:
	->  grid = [["A", "B", "A"], ["B", "A", "A", "A"]]
	->  find_value_locations(grid, "A")
	Value 'A' found 5 times:
	- Row 0, Column 0
	- Row 0, Column 2
	- Row 1, Column 1
	- Row 1, Column 2
	- Row 1, Column 3

	Parameters
	----------
	grid: list of lists
		2D list to search; sublists can be of different lengths and there can
		be many of them
	target: any
		Value to find

	Returns
	-------
	None. Prints analysis to console.
	"""
	count = 0 # this is a hint, leave it here
	locations = [] # this is a hint, leave it here

	# your code, including nested for-loops goes here
	# it should count how many times the target value was found.

	print(f"Value '{target}' found {count} times:") # don't change this

	for row, col in locations: # don't change this
		print(f"- Row {row}, Column {col}") # don't change this

print("\nP10:") # don't change this
grid = [["A", "B", "A"], ["B", "A", "A", "A"]] # don't change this
find_value_locations(grid, "A") # don't change this


"""
Problem 11 
"""

def convert_and_filter(grid_string_numbers):
	"""
	[Concept: List Modification During Iteration]
	Converts strings to floats and creates new list with values above average.
	Hint: First convert all strings to floats
	Hint: Then calculate average
	Hint: Finally filter values
	Hint: If you wrote functions to filter and/or compute average last week,
	feel free to reuse them here.

	Example:
	->  grid = [["1.5", "4.5"], ["3.5", "2.5"]]
	->  convert_and_filter(grid)
	Original values converted to floats: [[1.5, 2.5], [3.5, 4.5]]
	Average value: 3.0
	Values above average: [4.5, 3.5]

	Parameters
	----------
	grid_string_numbers: list of lists
		2D list of string numbers

	Returns
	-------
	list
		List of float values above average
	"""
	# Convert to floats
	grid_floats = [] # this is a hint, leave it here
	# your code, including nested for-loops goes here

	# don't change the below
	print("Original values converted to floats:", grid_floats)

	# Calculate average using nested for-loops

	print("Average value:", average) # don't change this

	# Filter values
	# your code, including nested for-loops goes here
	# it should filter our values that are above average.

	print("Values above average:", above_average_values) # don't change this
	return above_average_values # don't change this

print("\nP11:") # don't change this
grid = [["1.5", "4.5"], ["3.5", "2.5"]] # don't change
values_above_average = convert_and_filter(grid) # don't change
print("Returned values above average:", values_above_average) # don't change



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

"""