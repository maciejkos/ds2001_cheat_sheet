"""
Maciej Kos
DS 2001 - Assignment 9
Oct 30/31, 2024

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
︂
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


"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣤⡀⠀⠀⠍⠭⣔⣄⠀⠀⠀⠀⠀⢈⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⢂⣀⣀⣤⣀⣹⣷⣤⣀⣀⠀⢉⣿⣶⣶⣶⣶⣿⣿⣿⠷⠆⠀⠀⠀⠀⣀⣄⠀
⠀⠈⠉⠹⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠋⠀⠀⠀⡤⠀⠀⣿⣏⠀
⠀⠀⠀⠐⠹⢟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣽⣿⣿⠿⣆⠀⠀⠀⠀⢸⢀⣿⣿⠀
⠀⠀⠀⠀⠀⠠⢴⣿⠟⢛⣿⣿⣟⣩⣴⣾⣿⡉⠹⢦⡈⠳⢤⡀⠀⠈⢼⣿⣿⡄
⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠋⠀⣿⣿⣿⣿⣿⣿⣦⣀⡉⠶⡤⠈⠛⠂⠉⠁⠀⠀
⠀⠀⢺⣿⣿⣿⡿⠿⠿⣟⣛⣭⣽⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢉⠕⠺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠁⠛⢻⣿⠟⢑⡾⠁⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""

"""
Problem 1
"""


def create_witch_inventory():
	"""
	[Concept: Dictionary Creation]
	Creates a basic witch's inventory with items and their quantities. Prints it.
	Hint: Use curly braces to create dictionary
	Hint: Keys are strings, values are integers

	This function always returns the same dictionary.
	->  create_witch_inventory()
	{"wand": 1, "cauldron": 2, "black cat": 3}


	Parameters
	----
	None

	Returns
	----
	dict
		Dictionary with witch items and quantities
		{"wand": 1, "cauldron": 2, "black cat": 3}
	"""
	# <- create your inventory here in any way you like

	for item, quantity in inventory.items():  # do not change this
		print("Item: ", item, " in quantity of: ", quantity)  # do not change this
	return inventory  # do not change this


print("\nP1:")  # do not change this
witch_items = create_witch_inventory()  # do not change this
print("witch_items:", witch_items)  # do not change this


"""
Problem 2
"""

def count_spell_occurrences(spell_list):
	"""
	[Concept: Dictionary Creation and Value Access]
	Counts the occurrences of each spell in a list of spells cast during a witch
	gathering.

	Example:
	->  spell_list = [
			"Fizzlebroom", "Shadowmire", "Cackleroot", "Banshiver", "Vexfang",
			"Moonshade", "Nightspike", "Thornflicker", "Gravelight", "Vexshade",
			"Hexsong", "Wispwhisk", "Quakefang", "Shadowmire", "Fizzlebroom",
			"Duskmire", "Ghastgleam", "Craggle", "Vexblight", "Shadowquill",
			"Sablehex", "Nightthorn", "Slitherwhisp", "Drakeflame", "Quakefang",
			"Grumbleghast", "Cinderflare", "Nightmire", "Shadowmire", "Shriekspike",
			"Voidglint", "Flickershard", "Duskhorn", "Whispersong", "Nightshade",
			"Hexgleam", "Darkshade", "Blightwhisk", "Frostsinge", "Skulkshade",
			"Snapfang", "Murkgloom", "Quakefang", "Hexwhisper", "Voidfang",
			"Moonflicker", "Spiteblight", "Duskgloom", "Frostfang", "Thornsinge",
			"Ghostshade", "Driftspike", "Flickermire", "Darkmire", "Wraithshard",
			"Nightmire", "Shadowwhisk", "Skulkroot", "Dusksinge", "Vexfang",
			"Moonmire", "Shadegleam", "Crimsonwhisk", "Flickerquill", "Cinderthorn",
			"Banshiver", "Sablefang", "Spiteshard", "Dusksinge", "Hexroot",
			"Blightsong", "Nightflare", "Duskmire", "Gravelight", "Hexshade",
			"Shriekmire", "Grimquill", "Sablewhisk", "Fizzleshard", "Ghostthorn",
			"Voidgleam", "Whisperfang", "Ghastsong", "Duskmire", "Banspike",
			"Vexfang", "Shadowmire"]

	->  print(count_spell_occurrences(spell_list))
	{'Fizzlebroom': 2, 'Shadowmire': 4, 'Cackleroot': 1, 'Banshiver': 2,
	'Vexfang': 3, ...} # ... means I am only printing the beginning to the
	answer

	Hint: Use a dictionary to store each spell and the number of times it
	appears in the list.

	FYI: Rumor has it that if you read that list of spells out loud twice
	quickly, and without a slip of the tongue, Magrat Garlick's broomstick will
	appear under your bed. But if you make a mistake, Agatha's distant cackle
	will surprise you when you least expect it. And yes, it's been Agatha all
	along!

	Parameters
	----
	spell_list: list
		List of spells cast during a witch gathering.

	Returns
	----
	dict
		Dictionary where each spell is a key and its value is
		the count of its occurrences in the list.
		For example, {'Fizzlebroom': 2, 'Shadowmire': 4} means Fizzlebroom
		was cast 2 times and Shadowmire 4 times.

	"""

	# the spell_count dict with have spell names as keys and their counts as
	# values
	spell_count = {}  # do not edit this line
	for spell in spell_list:  # finish this loop, it will have conditionals


	return spell_count  # do not edit this line


print("\nP2:")  # do not change this
spell_list = [
	"Fizzlebroom", "Shadowmire", "Cackleroot", "Banshiver", "Vexfang",
	"Moonshade", "Nightspike", "Thornflicker", "Gravelight", "Vexshade",
	"Hexsong", "Wispwhisk", "Quakefang", "Shadowmire", "Fizzlebroom",
	"Duskmire", "Ghastgleam", "Craggle", "Vexblight", "Shadowquill",
	"Sablehex", "Nightthorn", "Slitherwhisp", "Drakeflame", "Quakefang",
	"Grumbleghast", "Cinderflare", "Nightmire", "Shadowmire", "Shriekspike",
	"Voidglint", "Flickershard", "Duskhorn", "Whispersong", "Nightshade",
	"Hexgleam", "Darkshade", "Blightwhisk", "Frostsinge", "Skulkshade",
	"Snapfang", "Murkgloom", "Quakefang", "Hexwhisper", "Voidfang",
	"Moonflicker", "Spiteblight", "Duskgloom", "Frostfang", "Thornsinge",
	"Ghostshade", "Driftspike", "Flickermire", "Darkmire", "Wraithshard",
	"Nightmire", "Shadowwhisk", "Skulkroot", "Dusksinge", "Vexfang",
	"Moonmire", "Shadegleam", "Crimsonwhisk", "Flickerquill", "Cinderthorn",
	"Banshiver", "Sablefang", "Spiteshard", "Dusksinge", "Hexroot",
	"Blightsong", "Nightflare", "Duskmire", "Gravelight", "Hexshade",
	"Shriekmire", "Grimquill", "Sablewhisk", "Fizzleshard", "Ghostthorn",
	"Voidgleam", "Whisperfang", "Ghastsong", "Duskmire", "Banspike",
	"Vexfang", "Shadowmire"]  # do not change this
print(count_spell_occurrences(spell_list))  # do not change this

"""
Guess what! Your previous code also works with emojis. Give it a try.
"""
# spell_list = [
#     '🎃', '👻', '💀', '☠️', '👾', '👻', '🧛','🎃',
#     '🦇', '🕷️', '🕸️', '🦉', '👻', '🕯️', '⚰️', '🩸', '🔮',
#     '⚗️', '🧪', '👻', '🕯️', '🎈', '😱', '🎃'
# ]
# print(count_spell_occurrences(spell_list))




"""
Problem 3
"""


def find_the_most_popular_spell(spell_count):
	"""
	[Concept: Iteration over items, Finding Maximum]
	Given the output of the `count_spell_occurrences()`
	function (i.e., spell_count), returns the most popular spell and how
	many times it was cast. The most popular spell is the spell with the with
	highest number of occurrences. You can assume there is only one such spell.

	Example:
	->  spell_count = count_spell_occurrences(spell_list)
	->  find_the_most_popular_spell(spell_count)
	{'Most popular spell': 'Shadowmire', 'Number of times cast': 4}


	Hint:

	Parameters
	----
	spell_count: dict
		Output of the `count_spell_occurrences()` function. For example:
		{'Fizzlebroom': 2, 'Shadowmire': 4, 'Cackleroot': 1, 'Banshiver': 2}

	Returns
	----
	dict
		Dictionary with keys "Most popular spell" and "Number of times cast"
		and their corresponding values.
	"""
	# first, create your dictionary (what should you call it?)
	# what keys should your dictionary have? and should their values be?
	# for now, the values can be None or False since you don't know what the
	# values should be exactly.

	occurrence_max = 0  # do not change this, you will need it
	for spell, occurrence in spell_count.items():  # do not change this
		# add lines of code here to find the
		# the name of the spell with max occurrences.
		# hint: whenever you find a new max, save the spell's name

	# once you know the answers, you can update your dictionary


	return most_popular_spell_info # do not change this


print("\nP3:")  # do not change this
spell_count = count_spell_occurrences(spell_list)  # do not change this
result = find_the_most_popular_spell(spell_count)  # do not change this
print(result["Most popular spell"],    # do not change this
      result["Number of times cast"])  # do not change this

"""
Problem 4

Sadly, it wasn't exactly fun to be a witch. 
"""


def create_accused_record(name, age, occupation, accusers, verdict_date):
	"""
	[Concept: Dictionary Creation]
	Creates a record for an accused person during Salem Witch Trials.

	First see how messy it is with lists:
	accused = ["Bridget Bishop", 50, "tavern keeper"]
	# What if we need to update age? Which index was it again?
	accused[1] = 51  # Have to remember index 1 is age

	Then create a dictionary version that's more intuitive:
	accused_dict["age"] = 51  # Clear what we're updating!

	Example:
	->  create_accused_record("Sarah Good", 38, "beggar",
							["Mercy Lewis", "Ann Putnam Jr"],
							"July 19, 1692")
	{
		"name": "Sarah Good",
		"age": 38,
		"occupation": "beggar",
		"accusers": ["Mercy Lewis", "Ann Putnam Jr"],
		"verdict_date": "July 19, 1692"
	}

	Historical Note: Both Sarah Good and Bridget Bishop were among the first
	accused. While Bishop owned a tavern (unusual for a woman then), Good was
	a homeless beggar - showing how accusations crossed social classes.

	Parameters
	----
	name: str
		Name of the accused
	age: int
		Age at time of accusation
	occupation: str
		Person's occupation
	accusers: list
		List of people who made accusations
	verdict_date: str
		Date of final verdict

	Returns
	----
	dict
		Dictionary containing person's trial information
	"""

	return record  # do not change this


print("\n4:") # do not change this
print(
	create_accused_record("Sarah Good", 38, "beggar",
	                      ["Mercy Lewis", "Ann Putnam Jr"],
	                      "July 19, 1692")
) # do not change this

"""
Problem 5
"""


def combine_trial_records(record1, record2):
	"""
	[Concept: Dictionary Merging and Value Access]
	Combines information from two trial records, keeping track of total
	accusations per accuser.

	Example:
	->  rec1 = {
			"accused": "Martha Corey",
			"accusers": ["Ann Putnam Jr", "Mercy Lewis"],
			"date": "March 19, 1692"
		}
	->  rec2 = {
			"accused": "Rebecca Nurse",
			"accusers": ["Ann Putnam Jr", "Abigail Williams"],
			"date": "March 23, 1692"
		}
	->  combine_trial_records(rec1, rec2)
	{
		"Ann Putnam Jr": 2,
		"Mercy Lewis": 1,
		"Abigail Williams": 1
	}

	Historical Note: Ann Putnam Jr., only 12 years old, was one of the most
	active accusers, testifying against 62 people. She later apologized for her
	role in the trials.

	Parameters
	----
	record1: dict
		First trial record
	record2: dict
		Second trial record

	Returns
	----
	dict
		Dictionary with accusers as keys and their total accusations as values
	"""

	accuser_counts = {} # one line missing

	# Process accusers from first record
	for accuser in record1["accusers"]:  # do not change this


	# Process accusers from second record


	return accuser_counts  # do not change this


print("\nP5:") # do not change this
record1 = {
	"accused": "Martha Corey",
	"accusers": ["Ann Putnam Jr", "Mercy Lewis"],
	"date": "March 19, 1692"
} # do not change this
record2 = {
	"accused": "Rebecca Nurse",
	"accusers": ["Ann Putnam Jr", "Abigail Williams"],
	"date": "March 23, 1692"
} # do not change this
combined = combine_trial_records(record1, record2) # do not change this
print("Combined records:", combined) # do not change this

"""
Problem 6 - OPTIONAL, only if you want something a touch harder
"""


def analyze_trial_locations(trials_data):
	"""
	[Concept: Nested Dictionary Analysis]
	Analyzes which towns had the most accusations and executions.

	Example:
	->  data = [
			{
				"town": "Salem Village",
				"accused": ["Sarah Good", "Sarah Osborne"],
				"executed": ["Sarah Good"]
			},
			{
				"town": "Andover",
				"accused": ["Martha Carrier", "Mary Parker"],
				"executed": ["Martha Carrier"]
			}
		]
	->  analyze_trial_locations(data)
	{
		"Salem Village": {"total_accused": 2, "total_executed": 1},
		"Andover": {"total_accused": 2, "total_executed": 1}
	}

	Historical Note: While called the "Salem" witch trials, accusations spread
	to many towns. Andover actually had more accused than Salem Village.

	Parameters
	----
	trials_data: list of dict
		List of dictionaries containing town trial information

	Returns
	----
	dict
		Nested dictionary with statistics per town
	"""


	return town_stats # do not change this


print("\n6:") # do not change this
data = [
	{
		"town": "Salem Village",
		"accused": ["Sarah Good", "Sarah Osborne"],
		"executed": ["Sarah Good"]
	},
	{
		"town": "Andover",
		"accused": ["Martha Carrier", "Mary Parker"],
		"executed": ["Martha Carrier"]
	}
] # do not change this
print(analyze_trial_locations(data)) # do not change this



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
8) make sure the file is called assignmentN.py (e.g., assignment9.py)  
9) make sure to submit assignmentN.py (e.g., assignment9.py)
10) close PyCharm, open again, run the whole file and check that everything 
works correctly
"""
