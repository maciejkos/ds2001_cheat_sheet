"""
Maciej Kos
DS 2001 - Assignment 5
Sept 25/26, 2024

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

import matplotlib.pyplot as plt


def main():
	"""
	## DS2001 In-Class Assignment (Week 5)
	### Objective:
	- Practice working with lists
	- Apply string manipulation techniques
	- Use for-loops to process data
	- Create basic visualizations
	"""


	"""
	### Q1. Reading from File and Splitting (10 minutes)

	Task: Load data from a file. Print the first and the last fruit from its
	last line.

	a. In your Python script, open and read `fruits.txt`.
	b. For each line in the file:
		- Use the `split()` method to convert the line into a list.
		- Print the resulting list.
	c. After processing all lines, print the first and last fruit from the
	last line you processed.
	Hint: Not all prints need to be in the for loop.
	"""

	# Your code should go here

	"""
	### Q2. Random Number Generation and Plotting (15 minutes)
	
	Task: Create 20 random numbers and plot them.
	
	a. Import the random module. Remember that imports go above def main().
	b. Create a loop that runs 20 times. In each iteration:
		- Generate two random integers for x and y coordinates.
			- x coordinates should be between 5 and 10 (inclusive) 
			- y coordinates should be between 0 and 20 (inclusive) 
		- Use `plt.plot()` to add the point to the plot.
	c. After the loop, use `plt.show()` to display the plot.
	"""

	# Your code should go here

	"""
	### Q3. Simulating Die Rolls and List Operations (15 minutes)
	
	Task: Simulate rolling a six-sided die 50 times and count odd rolls 
	using a list.
	
	STOP and THINK. What answer do you expect? How many of the 50 die rolls 
	should be an odd number (1, 3, or 5)?
	
	a. Import the `random` module if you haven't already. Remember that 
	imports go above def main().
	b. Create an empty list called `odd_rolls`.
	c. Simulate rolling a six-sided die 50 times. In other words: 
	select a random integer between 1 and 6; repeat it 50 times.
	d. For each roll, if the result is an odd number, append it to 
	`odd_rolls`. You should use the modulo operator for checking if a number 
	is odd.
	e. After all rolls, check the length of your list to count how many odd 
	numbers were rolled.
	f. Print the count of odd numbers rolled.
	
	STOP and THINK. What was the answer? Does it make sense? Is it what you
	expected? Run your code again a few time and consider whether the 
	answer is close to what you expected or not.
	"""

	# Your code should go here

	"""
	[OPTIONAL] Stretch goal for a sticker. 

	If you are finished and oh sooo bored, consider one addition to your code.

	a. Write a for loop that would repeat 1000 times.
	b. Copy and paste your Q3 code inside that loop, including the for-loop 
	statement. By nesting your Q3 code inside the loop from (a), we make the 
	Q3 code run 1000 times. 
	c. Further explanation: after writing code for (a) and (b) above, you will 
	have two loops. The loop from (b) will be nested inside the loop from (a). 
	On each of the 1000 iterations of loop (a), your code from the (b) loop will 
	iterate 50 times. In total, there will be 50,000 iterations.
	d. Store your answer (the number of odd rolls in this loop iteration) 
	in a new list called "answers". After the loop finishes, we want this 
	list to have 1000 answers in it.
	e. Uncomment the code that is commented out below. It should print the 
	average of your answers. Is the answer closer to what you expected in Q3? 
	"""

	# Your code should go here

	# Uncomment the code below when you finish writing your stretch goal code.
	# from statistics import mean
	# print("The mean of number of odd rolls is: ", mean(answers))
	# print("Come for a sticker!")

	"""
	Great job! You've just practiced working with lists, string manipulation,
	random number generation, and basic data visualization!

	Submission:
		- Complete this core assignment.
		- Go through the list under the main() function
		- Submit file to Canvas/Gradescope.
	"""


# REMINDER
# ONLY USE THE INSTRUCTIONS COVERED IN DS2000 and DS2001. DO NOT USE ANY OTHER
# INSTRUCTIONS, FUNCTIONS, ETC.
# FOLLOW THE DS2000 STYLE GUIDE

"""
Before submitting the assignment:

0) have you used ONLY the Python instructions that were covered in lectures and 
nothing else? Did you follow the style guide?
1) fill out lines 19 and 20
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

main()
