"""
Maciej Kos
DS 2001 - Assignment 6 v2: parameter names made less confusing
Oct 09/10, 2024

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

import random
import matplotlib.pyplot as plt


##########################################################################
# Pre-defined functions for you to use; do not edit, move, or copy this code.
# Simply use it to figure out what these functions return and how to call them.
# You do not have to understand the code inside these functions.

def grow_grass(previous_grass):
	"""
	Simulate the growth of grass over time.

	This function calculates the new amount of grass based on the previous
	amount, with the growth rate being a random factor between 10% and 20%.
	The total grass amount is capped at 100 units to simulate a natural upper
	limit (e.g., space or resource constraints).

	Parameters
	----------
	previous_grass : float
		The previous amount of grass.

	Returns
	-------
	float
		The new (current) amount of grass after growth, capped at 100 units.
		If the calculated growth exceeds 100, the value is set to 100.
	"""
	growth = previous_grass * random.uniform(0.1, 0.2)
	if previous_grass + growth > 100:
		return 100
	else:
		return previous_grass + growth


def update_rabbits(previous_rabbits, current_grass):
	"""
	Update the rabbit population based on the available grass.

	The function models rabbit population changes depending on the amount of grass
	available. If there is sufficient grass (more than 10 units), the rabbit population
	grows by a random factor between 5% and 10%. If the grass is insufficient, the
	population decreases by a random factor between 0% and 5%.

	Parameters
	----------
	previous_rabbits : int
		The previous number of rabbits.
	current_grass : float
		The current amount of grass available.

	Returns
	-------
	int
		The new (current) number of rabbits after accounting for growth or
		decline.
	"""
	if current_grass > 10:
		return int(previous_rabbits * (1 + random.uniform(0.05, 0.1)))
	else:
		return int(previous_rabbits * (1 - random.uniform(0, 0.05)))


def rabbits_eat_grass(current_grass, current_rabbits):
	"""
	Simulate grass consumption by rabbits.

	This function calculates the amount of grass consumed by rabbits based on
	the current number of rabbits and the current grass amount. Each rabbit
	consumes 0.1 units of grass, up to the total amount available.

	Parameters
	----------
	current_grass : float
		The current amount of grass.
	current_rabbits : int
		The current number of rabbits.

	Returns
	-------
	float
		The amount of grass remaining after the rabbits have eaten.
	"""
	grass_eaten = min(current_grass, current_rabbits * 0.1)
	return current_grass - grass_eaten


def wolf_attack(current_rabbits):
	"""
	Simulate a wolf attack on the rabbit population.

	The function randomly reduces the rabbit population by a factor between
	10% and 20%, representing the number of rabbits eaten by a wolf during
	an attack.

	Parameters
	----------
	current_rabbits : int
		The current number of rabbits.

	Returns
	-------
	float
		The number of rabbits remaining after the wolf attack, with a minimum of
		zero.
	"""
	rabbits_eaten = int(current_rabbits * random.uniform(0.1, 0.2))
	return max(0, current_rabbits - rabbits_eaten)


def plot_part_1(time_steps, grass_amounts):
	"""
	Plot the growth of grass over time.

	This function generates a line plot that shows how the amount of grass changes
	over a given number of time steps. The x-axis represents the time steps, and
	the y-axis represents the amount of grass. A legend, grid, and labels are added
	to the plot for better readability.

	Parameters
	----------
	time_steps : int
		The number of time steps in the simulation.
	grass_amounts : list of float
		A list containing the amount of grass at each time step.

	Returns
	-------
	None
		The function displays the plot and does not return any value.
	"""
	plt.figure(figsize=(10, 6))
	plt.plot(range(time_steps), grass_amounts, label='Grass')
	plt.title('Grass Growth Over Time')
	plt.xlabel('Time Steps')
	plt.ylabel('Grass Amount')
	plt.legend()
	plt.grid(True)
	plt.show()


def plot_part_2(time_steps, grass_amounts, rabbit_population):
	"""
	Plot the changes in grass and rabbit populations over time.

	This function generates a line plot showing the amount of grass and the rabbit
	population across a specified number of time steps. The x-axis represents the
	time steps, while the y-axis shows the amount of grass and rabbit population.
	A legend, grid, and labels are added to enhance readability.

	Parameters
	----------
	time_steps : int
		The number of time steps in the simulation.
	grass_amounts : list of float
		A list containing the amount of grass at each time step.
	rabbit_population : list of int
		A list containing the rabbit population at each time step.

	Returns
	-------
	None
		The function displays the plot and does not return any value.
	"""
	plt.figure(figsize=(10, 6))
	plt.plot(range(time_steps), grass_amounts, label='Grass')
	plt.plot(range(time_steps), rabbit_population, label='Rabbits')
	plt.title('Grass and Rabbit Population Over Time')
	plt.xlabel('Time Steps')
	plt.ylabel('Amount / Population')
	plt.legend()
	plt.grid(True)
	plt.show()


def plot_part_3(time_steps, grass_amounts, rabbit_population):
	"""
	Plot the changes in grass and rabbit populations over time, accounting for
	consumption.

	This function generates a line plot that illustrates how the amount of grass
	and rabbit population change over a given number of time steps, taking into
	consideration the effects of rabbits consuming grass. The plot displays the
	time steps on the x-axis and the amount of grass and rabbit population on the
	y-axis. A legend, grid, and labels are added for clarity.

	Parameters
	----------
	time_steps : int
		The number of time steps in the simulation.
	grass_amounts : list of float
		A list containing the amount of grass at each time step.
	rabbit_population : list of int
		A list containing the rabbit population at each time step.

	Returns
	-------
	None
		The function displays the plot and does not return any value.
	"""
	plt.figure(figsize=(10, 6))
	plt.plot(range(time_steps), grass_amounts, label='Grass')
	plt.plot(range(time_steps), rabbit_population, label='Rabbits')
	plt.title('Grass and Rabbit Population Over Time (Rabbits Eating Grass)')
	plt.xlabel('Time Steps')
	plt.ylabel('Amount / Population')
	plt.legend()
	plt.grid(True)
	plt.show()


def plot_part_4(time_steps, grass_amounts, rabbit_population, wolf_attacks):
	"""
	Plot the changes in grass and rabbit populations over time, including wolf attacks.

	This function generates a line plot showing the dynamics of grass and rabbit
	populations across a given number of time steps. It also marks the occurrences
	of wolf attacks as vertical dashed lines, indicating significant population
	events. The x-axis represents the time steps, and the y-axis shows the amount
	of grass and the rabbit population.

	Parameters
	----------
	time_steps : int
		The number of time steps in the simulation.
	grass_amounts : list of float
		A list containing the amount of grass at each time step.
	rabbit_population : list of int
		A list containing the rabbit population at each time step.
	wolf_attacks : list of int
		A list of time steps where wolf attacks occurred.

	Returns
	-------
	None
		The function displays the plot and does not return any value.
	"""
	plt.figure(figsize=(10, 6))
	plt.plot(range(time_steps), grass_amounts, label='Grass')
	plt.plot(range(time_steps), rabbit_population, label='Rabbits')
	plt.vlines(wolf_attacks, ymin=0, ymax=max(rabbit_population), color='red',
	           label='Wolf Attack', linestyle='dashed')
	plt.title('Grass and Rabbit Population Over Time (With Wolf Attacks)')
	plt.xlabel('Time Steps')
	plt.ylabel('Amount / Population')
	plt.legend()
	plt.grid(True)
	plt.show()


##########################################################################

def main():
	"""
	## DS2001 In-Class Assignment (Week 6)
	### Objective:
	- Practice working with loops and lists
	- Call functions and update variables
	"""

	"""
	High-level Overview:
	In this assignment, you'll build a simple ecosystem simulation using Python. 
	You'll start with a basic model of grass growth and gradually increase its 
	complexity by adding more elements and interactions. The assignment is 
	divided into four parts:
	
	1. Basic Grass Simulation: You'll model the growth of grass over time.
	2. Adding Rabbits: You'll introduce rabbits to your ecosystem and see how 
	their population changes alongside the grass.
	3. Rabbits Eating Grass: You'll create an interaction between rabbits and 
	grass, where rabbits consume the grass.
	4. Wolf Attacks (Stretch Goal): You'll add periodic wolf attacks that 
	affect the rabbit population.
	
	Throughout these parts, you'll practice working with loops, lists, and 
	functions. You'll also learn how to call functions, update variables, and 
	visualize your results using plots. This assignment will help you understand 
	how simple rules can create complex behaviors in a system, which is a 
	fundamental concept in many areas of science and computing.

	### Part 1: Basic Grass Simulation
	Task: Simulate the growth of grass over a number of time steps and plot it. 
	
	Overview:
	At every step, grass will grow by an amount returned by one of the helper 
	functions. To plot it, we need two lists. One list will contain time 
	steps (0, 1, 2, ...). These will be xs on our plot. The other list will 
	contain the amount of grass at every step. These will be ys.   
	
	At every step, you will be adding the amount of grass to the
	list. 
	
	The plotting function is already written for you `plot_part_1()`. 
	You can always visualize your results by calling it to check if your code 
	works correctly. You plot should be similar to this one:
	https://raw.githubusercontent.com/maciejkos/ds2001_cheat_sheet/refs/heads/as/a6q1.png
	
	What to do:
	1. Our simulation will run for 100 steps. Create a `time_steps` variable 
	and set it to 100. 
	2. We need to start with some initial amount of grass. Create a variable 
	`grass_initial` and set it to 50.
	3. Create a list called `grass_amounts`. At every step, we will be 
	appending the new amount of grass to it. 

	4. Use a for loop to simulate grass growth for the specified number of 
	time steps. This loop will repeat as many times as the 
	value of `time_steps`
	5. At time step 0, append the initial amount of grass (50) to the 
	`grass_amounts` list.
		- This is our starting condition and is handled separately because there 
		is no previous value to use.
	6. For all other time steps (1 to 99), calculate the current amount of 
	grass based on the amount of grass in the previous time step. 
		a. Get the previous amount of grass from `grass_amounts`.
		b. Use this value and the relevant helper function to calculate the 
		current amount of grass. 
		c. Append this current amount of grass to the `grass_amounts` list.
	
	7. Plot the result using `plot_part_1()`
	
	"""
	time_steps = 100
	grass_initial = 50
	# Empty list to store grass amounts
	grass_amounts = []

	# Loop for each time step
	for step in range(time_steps):
		if step == 0:
			# At time step 0, start with the initial amount of grass
			grass_amounts.append(grass_initial)
		else:
			# For all other time steps, calculate the new amount of grass based on the previous step
			grass_previous = grass_amounts[-1]
			grass_current = grow_grass(grass_previous)

			# Add the new grass amount to the list
			grass_amounts.append(grass_current)

	# Plot the grass growth over time
	plot_part_1(time_steps, grass_amounts)


	"""
	### Part 2: Adding Rabbits
	
	This part builds upon the code from Part 1.
	
	Overview:
	In this part, we'll extend our simulation to include rabbits alongside the 
	grass. We'll track both grass and rabbit populations over time. At each 
	step, the grass will grow, and the rabbit population will change based on 
	the available grass. We'll need two lists: one for grass amounts 
	(which we already have from Part 1) and a new one for rabbit population. 
	These will represent the y-values on our plot, while the time steps will be 
	our x-values. At every step, we'll calculate and add new values for both 
	grass and rabbits to their respective lists.
	
	What to do:
	1. Copy your code from Part 1 and paste it here.
	2. Create a new variable `rabbits_initial` and set it to 20.
	3. Create a new empty list called `rabbit_population` to keep track of the 
		rabbit population over time.
	4. Modify your existing for loop to simulate both grass growth and rabbit 
	population changes:
	   a. At time step 0:
	      - Append the initial amount of grass (50) to the `grass_amounts` list.
	      - Append the initial number of rabbits (20) to the `rabbit_population` 
	      list.
	   b. For all other time steps (1 to 99):
	      - Get the previous amount of grass from `grass_amounts`.
	      - Get the previous number of rabbits from `rabbit_population`.
	      - Use the `grow_grass()` function to calculate the current amount of 
	      grass.
	      - Use the `update_rabbits()` function to calculate the current 
	      number of rabbits.
	      - Append the current amount of grass to `grass_amounts`.
	      - Append the current number of rabbits to `rabbit_population`.
	5. After the loop, plot the results. The plotting function is already 
	written for you `plot_part_2()`. 
	You can always visualize your results by calling it to check if your code 
	works correctly. You plot should be similar to this one:
	https://raw.githubusercontent.com/maciejkos/ds2001_cheat_sheet/refs/heads/as/a6q2.png
	"""



	"""
	### Part 3: Rabbits Eating Grass
	
	In this part, you will build upon the code from Part 2.
	
	Overview:
	Now we'll make our simulation more realistic by having the rabbits eat the grass. 
	This introduces a direct interaction between the two populations. At each 
	step, we'll first grow the grass, then update the rabbit population, 
	and finally have the rabbits eat some of the grass. 
	This eating process will reduce the amount of grass after the rabbits have 
	fed. We'll continue to use our two lists for grass amounts and rabbit 
	population, updating them at each step to reflect these new interactions.
	
	What to do:
	1. Copy your code from Part 2 and paste it here.
	2. Modify your existing for loop to include the rabbits eating grass:
	   a. At time step 0:
	      - Keep it the same as in Part 2.
	   b. For all other time steps (1 to 99):
	      - Get the previous amount of grass from `grass_amounts`.
	      - Get the previous number of rabbits from `rabbit_population`.
	      - Use the `grow_grass()` function to calculate the current amount of 
	      grass.
	      - Use the `update_rabbits()` function to calculate the current number
	      of rabbits.
	      - Use the `rabbits_eat_grass()` function to update the current 
	      grass amount after the rabbits have eaten.
	      - Append the final current amount of grass to `grass_amounts`.
	      - Append the current number of rabbits to `rabbit_population`.
	3. After the loop, plot the results. The plotting function is already 
	written for you `plot_part_3()`. 
	You can always visualize your results by calling it to check if your code 
	works correctly. You plot should be similar to this one:
	https://raw.githubusercontent.com/maciejkos/ds2001_cheat_sheet/refs/heads/as/a6q3.png
	"""




	"""
	### Stretch Goal: Wolf Attacks (Optional)
	
	In this part, you will extend the code from Part 3.
	
	Overview:
	In this final part, we'll add another layer of complexity to our ecosystem: 
	periodic wolf attacks. These attacks will occur at regular intervals and 
	reduce the rabbit population. We'll need to track when these attacks happen. 
	In addition to our grass and rabbit lists, we'll create a new list to 
	record the time steps when wolf attacks occur. At each step, we'll grow 
	the grass, update the rabbit population, have the rabbits eat the grass, 
	and then check if it's time for a wolf attack. This will give us a more 
	dynamic and complex simulation of our small ecosystem.
	
	What to do:
	1. Copy your code from Part 3 and paste it here.
	2. Create a new variable `wolf_attack_interval` and set it to 10.
	3. Create a new empty list called `wolf_attacks` to keep track of when wolf 
	attacks occur.
	4. Modify your existing for loop to include wolf attacks:
	   a. At time step 0:
	      - Keep it the same as in Part 3.
	   b. For all other time steps (1 to 99):
	      - Get the previous amount of grass from `grass_amounts`.
	      - Get the previous number of rabbits from `rabbit_population`.
	      - Use the `grow_grass()` function to calculate the current amount of 
	      grass.
	      - Use the `update_rabbits()` function to calculate the current number 
	      of rabbits.
	      - Use the `rabbits_eat_grass()` function to update the current 
	      grass amount after the rabbits have eaten.
	      - Use an `if-statement`, `step`, and `wolf_attack_interval` to decide 
	      whether the wolf attacks at this step.
	        - If it is, use the `wolf_attack()` function to update the 
	            number of rabbits.
	        - Add the current step to the `wolf_attacks` list.
	      - Append the final current amount of grass to `grass_amounts`.
	      - Append the current number of rabbits to `rabbit_population`.
	5. After the loop, plot the results. The plotting function is already 
	written for you `plot_part_3()`. 
	You can always visualize your results by calling it to check if your code 
	works correctly. You plot should be similar to this one:
	https://raw.githubusercontent.com/maciejkos/ds2001_cheat_sheet/refs/heads/as/a6q4.png
	
	"""




	"""
	Great job! You've learned more about loops, functions, and plotting. 
	Remember to submit your completed script.
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
