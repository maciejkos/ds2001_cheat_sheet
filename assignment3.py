"""
Maciej Kos
DS 2001 - Assignment 3
Sept 17/18, 2024

Copyright 2024 Maciej Kos

This programming assignment is the intellectual property of Maciej Kos.
All rights reserved.

Students are prohibited from sharing, distributing, or making this assignment publicly
available in any form, including but not limited to posting on public repositories,
forums, or websites. Use of this assignment is restricted to the student it was
provided to for educational purposes only.

Unauthorized sharing or distribution of this assignment may result in academic
penalties and/or disciplinary action as determined by the author or Northeastern University.

Student's first and last name:
Date:
"""

# == GUIDELINES ==
# ONLY USE THE INSTRUCTIONS COVERED IN DS2000 and DS2001. DO NOT USE ANY OTHER INSTRUCTIONS, FUNCTIONS, ETC.
# If it is not in the cheat sheet, you probably shouldn't use it. Cheat sheet: https://github.com/maciejkos/ds2001_cheat_sheet/tree/main
# FOLLOW THE DS2000 STYLE GUIDE

# Feel free to discuss the assignment with the people around you and help each other out! It’s a great way to learn.
# If you have trouble with any step, raise your hand and ask a TA or Maciej for help!

import matplotlib.pyplot as plt


def main():
	"""
	## DS2001 In-Class Assignment (Week 3)

	### Objective:
	- Practice reading data from a file
	- Perform mathematical operations on the data
	- Create a basic plot with `matplotlib` (Visualizing data is an important skill in almost any
	field—whether you’re a data analyst, scientist, or even in marketing.)

	### Instructions:

	You are provided with a file named `city_temperatures.txt` containing the average temperatures (in °F)
	of three cities over the past week: Boston, New York, and San Francisco.

	Your task is to:
	1. Read the temperatures from the file.
	2. Calculate some statistics: the average, the minimum, and the maximum temperature.
	3. Visualize the data by creating a bar chart comparing the temperatures of the three cities.
	4. Customize the plot: add labels, title, and save the plot to a file.

	Steps:

	===Q1. File Reading:===
	  - Open the file `city_temperatures.txt` and read the temperatures of Boston, New York, and San Francisco. [Hint:
	  use the "with open(...) as ..." pattern.]
	  - To get the temperatures you will need to READ (each) LINE separately; (hint hint)
	  - Store these temperatures in three variables: `temp_boston`, `temp_ny`, and `temp_sf`.
	  - Print these values to confirm you've read them correctly.
	"""

	### --> Your code goes under each comment below
	# Open the file using the "with open(...) as ..." pattern.

	# Store these temperatures in three variables: `temp_boston`, `temp_ny`, and `temp_sf`

	# Print these values to confirm you've read them correctly.

	"""
	Q2. Math Operations:
	   - Calculate the average temperature of the three cities.
	   - Find the minimum and maximum temperature using the `min` and `max` functions.
	   - Print the results.
	"""
	### --> Your code goes under each comment below

	# Calculate the average temperature of the three cities.

	# Find the minimum and maximum temperature using the `min` and `max` functions.

	# Print the results.

	"""
	Q3. Plotting:
	   - Create a bar chart to visually compare the temperatures of the three cities.
	   - Customize the chart by adding labels, a title. (This helps make your data more readable and meaningful.)
	   - Save the plot as `city_temperatures.png`.
	"""
	### --> Your code goes under each comment below

	# Make a single bar with temperature in Boston; make it green

	# Make a single bar with temperature in New York; make it blue

	# Make a single bar with temperature in San Francisco; make it red

	# Add labels for x and y axes and add a title

	# Save the plot as a file

	# Show the plot

	# ==REMINDER==
	# ONLY USE THE INSTRUCTIONS COVERED IN DS2000 and DS2001. DO NOT USE ANY OTHER INSTRUCTIONS, FUNCTIONS, ETC.
	# FOLLOW THE DS2000 STYLE GUIDE

	"""
	
	Great job! You’ve just learned how to manipulate data, calculate key statistics, and 
	create visualizations—all critical skills in Python that we’ll build on.
	
	Submission:
	   - Complete this core assignment and save your plot as `city_temperatures.png`.
	   - Go through the list under the main() function
	   - Submit both files to Canvas/Gradescope.
	   
	"""
	# Core assignment ends here

	"""
	=== Stretch Goals (Optional for Volunteers):===
	
	DON'T START IF YOU HAVEN'T COMPLETED Q1 – Q3.
	
	If you’ve completed the core assignment and are looking for a challenge or more practice, you can work on 
	the following stretch goals. These tasks will give you the chance to further improve your plotting 
	skills by adding more customization.
	
	Notes:
	- These stretch goals are optional and meant to provide extra practice. They are not mandatory for all students, 
	but highly recommended for those who finish early or want more of a challenge.
	
	Stretch Goal 1: Bar Plot Customization
	
	You are provided with a basic bar plot comparing the scores of three students. Customize it by:
	1. Adding a legend to indicate which color corresponds to which student.
	2. Naming the x-axis as "Students" and the y-axis as "Scores".
	3. Giving the plot a title: "Student Scores".
	
	"""

	##################### BEGIN: Starter Code (don't change it, don't copy it, don't move it)

	# Scores of students
	student_1 = 88
	student_2 = 92
	student_3 = 79

	# Create a bar plot
	plt.bar("Alex", student_1, color="blue", label="Alex")
	plt.bar("Aspen", student_2, color="green", label="Aspen")
	plt.bar("Angel", student_3, color="red", label="Angel")

	##################### END: Starter Code (don't change it, don't copy it, don't move it)

	### --> Your code goes under each comment below

	# Add a legend to indicate which color corresponds to which student.

	# Name the x-axis as "Students" and the y-axis as "Scores".

	# Give the plot a title: "Student Scores".

	# Show your plot

	"""
	Stretch Goal 2: Scatter Plot Customization
	
	Now, you’re provided with a basic scatter plot that compares the heights (cm) and weights (kg) of five individuals. 
	Customize it by:
	1. Adding a legend, naming the x-axis and y-axis, and giving the plot a title.
	2. Changing the colors and markers of the points:
	   - For the first three individuals, use blue squares.
	   - For the last two individuals, use orange circles.

    	NOTE: plt.scatter() hasn't been introduced in DS2000 yet. Don't use it in DS2000 HW,
     	until it is introduced, please.
	"""

	##################### BEGIN: Starter Code (don't change it, don't copy it, don't move it)

	# Heights and weights
	height_1, weight_1 = 160, 60
	height_2, weight_2 = 165, 65
	height_3, weight_3 = 170, 70
	height_4, weight_4 = 175, 75
	height_5, weight_5 = 180, 80

	# Create a scatter plot
	plt.scatter(height_1, weight_1, color="blue", marker="s", label="Person 1")
	plt.scatter(height_2, weight_2, color="blue", marker="s", label="Person 2")
	plt.scatter(height_3, weight_3, color="blue", marker="s", label="Person 3")
	plt.scatter(height_4, weight_4, color="orange", marker="o", label="Person 4")
	plt.scatter(height_5, weight_5, color="orange", marker="o", label="Person 5")

	##################### END: Starter Code (don't change it, don't copy it, don't move it)

	### --> Your code goes under each comment below

	# Add a legend, name the x-axis and y-axis, and give the plot a title

	# Show your plot

	"""
	Stretch Goal 3: Bar Plot with Mean Line
	
	Create a new bar plot that compares the monthly sales of five stores and:
	1. Add a horizontal line representing the average sales across all stores.
	2. Customize the plot by adding axis labels, a title, and a legend.
	"""

	##################### BEGIN: Starter Code (don't change it, don't copy it, don't move it)

	# Sales data
	store_A = 120
	store_B = 150
	store_C = 100
	store_D = 180
	store_E = 130


	##################### END: Starter Code (don't change it, don't copy it, don't move it)
	
	### --> Your code goes under each comment below
	# Calculate the mean sales
	
	# Create a bar plot with different colors for each store
	
	# Add a horizontal line representing the mean sales
	
	# Show your plot


"""
Before submitting the assignment:

0) have you used ONLY the Python instructions that were covered in lectures and nothing else? Did you follow 
the style guide?
1) fill out lines 19 and 20
2) are variables named correctly?
3) are all lines of code < 80 characters?
4) do you use comments and are they above the code they reference, not next to it?
5) are there spaces around items? (e.g., x = y not x=y, and # comment not #comment)
6) do you use whitespace to separate code into logical chunks?
8) make sure the file is called assignment3.py  
9) make sure to submit assignment3.py AND the plot
10) close PyCharm, open again, run the whole file and check that everything works correctly

Finally, when submitting it to Gradescope, make sure there aren't any errors.
"""

main()
