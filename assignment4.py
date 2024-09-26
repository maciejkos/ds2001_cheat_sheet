"""
Maciej Kos
DS 2001 - Assignment 4
Sept 25/26, 2024

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
	## DS2001 In-Class Assignment (Week 4)
	### Objective:
		Apply conditional statements
	- Practice reading data from a file
	- Use for-loops to process data
	- Perform basic calculations on data

	### Q1. Number Categorizer:

	—> Please refer to "21. Conditional Statements: if, elif, else" in the cheat
	sheet to guide your work.

	In this question, you will:

	- Write a program that takes a number as input.
	- Categorize the number based on its value:
		- If the number is greater than zero, print "Positive".
		- If the number is less than zero, print "Negative".
		- If the number is equal to zero, print "Zero".

	You’ll use `if`, `elif`, and `else` statements to achieve this.
	Follow the steps carefully:

	1. Take user input:
		- Use the `input()` function to get a number from the user.

	2. Categorize the number:
		- Use an `if` statement to check if the number is greater than zero.
			- If it is, print "Positive".
		- Use an `elif` statement to check if the number is less than zero.
			- If it is, print "Negative".
		- Use an `else` statement to handle the case where the number is exactly
		zero.
			- In this case, print "Zero".

	3. Run your code and test:
		- Test your program by running it with different inputs:
			a positive number, a negative number, and zero.
			Make sure it works correctly for all cases.

	### Example tests:

	- If the user inputs `5.3`, the program should print:
		Positive

	- If the user inputs `-0.2`, the program should print:
		Negative

	- If the user inputs `0`, the program should print:
		Zero


	### Summary of Steps:
	1. Use `input()` to get a number from the user and convert it to a float.
	2. Use `if-elif-else` to check whether the number is positive, negative, or zero.
	3. Print the correct message based on the number’s value.

	Please write your code under relevant comments below. For example, your
	code for deciding whether a number is Positive should go under comment
	'# If the number is greater than zero, print "Positive"'
	"""
	# Step 1: Take user input and convert it to a float

	# Step 2: Categorize the number using if-elif-else
	# If the number is greater than zero, print "Positive"

	# If the number is less than zero, print "Negative"

	# If the number is equal to zero, print "Zero"


	"""
	==Q2. File Reading and Temperature Analysis==
	—> Please refer to "19. For-loops for File Handling and Iteration" in the
	cheat sheet to guide your work.

	You are provided with a file named `temperature_data.txt` containing daily
	maximum temperatures (in °C) for a city over a 30-day period.
	Each line in the file represents one day's maximum temperature.

	The file is here:
	https://raw.githubusercontent.com/maciejkos/ds2001_cheat_sheet/refs/heads/as/temperature_data.txt

	In this question, you will read data from a file and
	find the number of hot and cold days.

	Definitions:
	- Hot day is a day with temperature >= 30°C
	- Cold day is a day with temperature <= 10°C

	Logic overview:
	https://raw.githubusercontent.com/maciejkos/ds2001_cheat_sheet/refs/heads/as/q2.png

	The data file contains lines with daily temperatures. Each line is one
	temperature reading.

	The code fairy already initialized two variables for you. You will use later
	use these variables in the for-loop.

	- Open the file `temperature_data.txt` using the `with open()` method.
	- Using a for-loop, iterate over the file contents.
	- On each loop iteration load new temperature reading and:
		1) make sure it is of the correct data type
		2) if it is a hot day, increment hot_days_count by 1
		2) if it is a cold day, increment cold_days_count by 1

	- After the loop:
		1) print the number of hot days; if your code works correctly,
			"Number of hot days: 2"
		1) print the number of cold days; if your code works correctly,
			"Number of cold days: 3"
	"""

	# store the count of hot days; will get updated in the for-loop
	hot_days_count = 0

	# store the count of hot days; will get updated in the for-loop
	cold_days_count = 0

	"""
	===Q3. File Reading and Data Processing:===

	—> Please refer to "19. For-loops for File Handling and Iteration" in the
	cheat sheet to guide your work.

	In this question, you will read data from a file and
	calculate the average temperature. HOWEVER, you will do it differently from
	the previous assignment.

	The data file contains lines with daily temperatures. Each line is one
	temperature reading. To compute the average, you need to know the sum of
	all temperature readings and the count of readings. (To get the average, you
	will divide the sum by the count.) You will use a for-loop to get
	this sum and count.

	Logic overview:
	https://raw.githubusercontent.com/maciejkos/ds2001_cheat_sheet/refs/heads/as/q3.png

	- Initialize variables for storing the sum and the count or readings
	- Just like in Q2:
		1. Open the file `temperature_data.txt` using the `with open()` method.
		2. Using a for-loop, iterate over the file contents.
	- On each loop iteration:
		1) variable storing the sum of temperatures: update it by adding the
		current reading to it
		2) variable storing the count of temperatures: increment it by 1

	- After the loop,
		1) calculate the average temperature for the month.
		2) print the average temperature. Don't round it.
	"""

	# initialize variable to store the sum of temperature readings

	# initialize variable to store the count of temperature readings

	# Open the file `temperature_data.txt` using the `with open()` method.
	# Using a for-loop, iterate over the file contents.
	# On each loop iteration:
	# 1) update temperature_sum by adding the current reading to it
	# 2) increment temperature_count by 1

	"""

	Great job! You’ve just learned how to use conditionals and for-loops!
	These skills are critical for implementing complex business or analysis logic.

	Submission:
		- Complete this core assignment.
		- Go through the list under the main() function
		- Submit file to Canvas/Gradescope.

	"""
	# Core assignment ends here

	"""
	=== Stretch Goals (Optional for Volunteers for EXTRA CREDIT 1 point):===

	DON'T START IF YOU HAVEN'T COMPLETED Q1 – Q3.

	If you’ve completed the core assignment and are looking for a challenge or
	more practice, you can work on  the following stretch goals. These tasks
	will give you the chance to further improve your plotting and logic
	skills.

	Notes:
	- These stretch goals are optional and meant to provide extra practice.
	- They are not mandatory for all students, but highly recommended for those
	who finish early or want more of a challenge.
	- You can receive 1 extra credit point for completing both goals.

	Stretch Goals
	### Q4. Plotting the Temperature Data:

	In this question, you will create a plot of daily temperatures using
	Matplotlib. You’ll also add a horizontal line representing
	the average temperature (which has already been computed in a previous
	question) and customize the plot with labels, a title,
	and save the chart as an image file.

	Logic overview:
	https://raw.githubusercontent.com/maciejkos/ds2001_cheat_sheet/refs/heads/as/q4.png

	### Steps:

	1. Opening the file:
		- First, you'll open the `temperature_data.txt` file using the
		`with open()` method.
		- This file contains daily temperature readings, with one
		temperature value per line.

	2. Creating the plot:
		- Use a for-loop to go through each line in the file.
		- For each temperature value in the file, you will plot it on a graph.
		- The x-axis will represent the day (starting from 1), and the y-axis
		will represent the temperature for that day.

		Plot the daily temperatures:
		- Use `plt.plot()` to add points to the plot. You’ll use `"bo"`
		as the style for blue circle markers, representing each day's
		temperature.

	3. Adding the average temperature:
		- After your loops finishes, you will add a horizontal line
		across the plot to show the average temperature.
		- Use `plt.axhline()` to draw the line. The color of the line will be
		red (`"r"`).

	4. Customizing the plot:
		- Label the x-axis as `"Day"` using `plt.xlabel()`, since
		the x-axis represents the day of the month.
		- Label the y-axis as `"Temperature (°C)"` using `plt.ylabel()`,
		because the y-axis represents the temperature in degrees Celsius.
		- Add a title to the plot using `plt.title()`. The title should be
		`"Daily Temperatures Over 30 Days"`.

	5. Saving and displaying the plot:
		- Save the plot as an image file called `"temperature_analysis.png"`
		using `plt.savefig()`.
		- After saving the file, use `plt.show()` to display
		the plot on the screen.

	### Detailed Instructions:

	1. Open the file:
		- Use the `with open()` method to open `"temperature_data.txt"`.
	2. Initialize variables:
		- Create a variable `day = 0` to keep track of which day the temperature
		corresponds to. The first line in the file will correspond to day 1,
		the second line to day 2, and so on.

	3. Iterating through the file and plotting points:
		- Use a for-loop to iterate through each line in the file:
		- Inside the loop, Increment the `day` counter by 1 for each line you
		read.
		- Plot the temperature for each day using `plt.plot()`.
		 x is day and y is temperature
		- The `"bo"` argument stands for blue circle markers,
		which will be used to represent each data point.

	4. After the for-loop add the average temperature line:
		- Use `plt.axhline()` to add a horizontal line across the plot at the
		value of `temperature_average` from the previous question. See cheat sheet
		for how to use plt.axhline()

	5. Labeling the axes and adding a title:
		- Label the x-axis `"Day"` using `plt.xlabel()`
		- Label the y-axis `"Temperature (C)"` using `plt.ylabel()`
		- Add the title `"Daily Temperatures Over 30 Days"` using `plt.title()`

	6. Saving and displaying the plot:
		- Save the plot to a file called `"temperature_analysis.png"` using
		`plt.savefig()`
		- Finally, use `plt.show()` to display the plot on the screen.

	"""
	# your code goes here

	"""
	Q5. Temperature Change:

	—> Please refer to "19. For-loops for File Handling and Iteration" in the
	cheat sheet to guide your work.

	In this question, you will:

	- Count how many times the temperature increased from one day to the next.
	- You will use a for-loop to go through the temperatures and compare each
	day’s temperature to the previous day’s temperature.
	- Print the total number of temperature increases at the end.

	Logic overview:
	https://raw.githubusercontent.com/maciejkos/ds2001_cheat_sheet/refs/heads/as/q5.png

	To determine if the temperature increased from one day to the next, you will
	use a for-loop. On every iteration except for the first one, you will
	compare each day's temperature to the previous day's temperature. If
	the current day's temperature is greater than the previous day's, you
	will count it as an increase. The first iteration will be a bit different
	since there is no "previous" temperature to compare with, so we will skip
	the comparison for that first day.


	The code fairy has already initialized two variables for you:
	- `temperature_increases_count`: This will store the number of times the
	temperature increases.
	- `is_first_reading`: This variable helps us manage the first temperature
	reading (since there is no previous value to compare it to).

	### Detailed Instructions:

	- Write logic for determining if temperature increased.
		1. initialize variable temperature_previous and set it 30
		2. initialize variable temperature_current and set it 20
		3. write an if-statement that checks whether temperature_current
		is greater then temperature_previous.
		- If this is true, increment temperature_increases_count by 1. (This
		variable was created for you below.)
		- If this is not true, don't do anything (no need for an if-statement).
	- Make sure this logic works correctly with different values of
	temperature_previous and temperature_current.


	1. Just like in Q2:
		- Open the file `temperature_data.txt` using the `with open()` method.
		- Using a for-loop, iterate over the file contents.

	2. In the for-loop, processing each temperature reading:
		- Before determining if temperature increased, we need to make sure
		that this is not our first temperature reading. This is because we can't
		compare the first reading with the previous one. The previous one doesn't
		exist. If it is NOT the first reading, we can do the comparison.
		The variable `is_first_reading` is used to track this.

		Write an if-statement to ensure that this is not the first reading.

		- Under the if-statement, copy and paste the logic code you wrote at the
		beginning of this question. This is the end of your conditional.
		- After processing the temperature, set `is_first_reading` to
		`False` so that future iterations can perform the comparison.
		- For subsequent iterations, compare the current temperature
		(`temperature_current`) with the previous day's temperature
		(`temperature_previous`).
		- If the current temperature is greater than the previous day’s
		temperature, this means the temperature increased,
		and you should increase the count (`temperature_increases_count`) by 1.
		- Update the value of `temperature_previous`
		at the end of each loop to store the current temperature for the next
		comparison.

	4. After the loop ends:
		- Once you’ve finished iterating through all the lines in the file, the
		total number of temperature increases will be stored in
		`temperature_increases_count`.
		- Use the `print()` function to display the result in the following format:
		  Number of temperature increases: number_of_increases

	"""

	temperature_increases_count = 0
	is_first_reading = True


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
4) do you use comments and are they above the code they reference, not next to it?
5) are there spaces around items? (e.g., x = y not x=y, and # comment not #comment)
6) do you use whitespace to separate code into logical chunks?
8) make sure the file is called assignment4.py
9) make sure to submit assignment4.py
10) close PyCharm, open again, run the whole file and check that everything
works correctly

Finally, when submitting it to Gradescope, make sure there aren't any errors.
"""

main()
