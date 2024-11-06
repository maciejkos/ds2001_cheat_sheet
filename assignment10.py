"""
Maciej Kos
DS 2001 - Assignment ︂10
Nov 6/7, 2024

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
This week you will implement your own data science utilities. Let's call it 
polar_cubs or pc for short. It will live in a separate file polar_cubs.py and 
you will be able to use it in your final project. To use it, just place it in 
the same folder as the current file an import it like I do below. 

This will help you a lot in your final project.

In polar_cubs.py there are a few functions already. You can use them.
Additionally, polar_cubs.py contains unfinished functions with docstrings and 
some skeleton code. 

Like in previous weeks, your objective is to complete these functions.
Unlike in previous weeks, these functions will stay in polar_cubs.py. This 
file (assignment10.py), contains 
1) basic tests to ensure your code works (you will use it for testing)
2) one basic exercise at the very end to get you comfortable calling your 
functions from polar_cubs.py. It is very easy.

The groupify() and groupby() functions can be pretty hard. I recommend one or 
two most experienced team members focus on them, while less experienced 
programmers focus on describe(). You can share code once done.


In summary:
(Please read the above before reading the summary.)
- Go to polar_cubs.py and write the first first function.
- Run this file (assignment10.py) to test it.
- When it working, write the next function. 
- Decide who on your team writes groupify() and groupby() and who write 
describe(). You can share code once done.

Finally, 
- work as a team and help each other out,
- feel free to reuse any of the code *you* wrote for DS2000 homework and DS2001 
assignments.

Good luck!
"""


"""
P1: read_csv()
"""

from pprint import pprint as pp
import polar_cubs as pc # this is how we import polar_cubs; don't edit this line


"""
P1: read_csv()
"""
print("\nP1:") # don't change this
df = pc.read_csv("score_by_city.csv")
pc.show(df)

# P1:
# name    city score index
# ------- ---- ----- -----
# Alice   NY   85    0
# Bob     LA   92    1
# Charlie NY   None  2
# David   LA   95    3
# Eve     NY   90    4
#
# Your data have 5 rows and 4 columns.


"""
P2: filter_df()
"""
print("\nP2:") # don't change this
df = {
	'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
	'city': ['NY', 'LA', 'NY', 'LA', 'NY'],
	'score': [85, 92, 88, 95, 90],
	'index': [0, 1, 2, 3, 4]
}

df_score_gt_90 = pc.filter_df(df, 'score', 90, condition=">")
print(df_score_gt_90)
# {'name': ['Bob', 'David'],
# 'city': ['LA', 'LA'],
# 'score': [92, 95],
# 'index': [1, 3]}

"""
P3: groupify()
"""
print("\nP3:") # don't change this
df = {
	'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
	'city': ['NY', 'LA', 'NY', 'LA', 'NY'],
	'score': [85, 92, 88, 95, 90],
	'index': [0, 1, 2, 3, 4]
}

df_by_city = pc.groupify(df, 'city')
pp(df_by_city)

# {'LA': {'city': ['LA', 'LA'],
#         'index': [1, 3],
#         'name': ['Bob', 'David'],
#         'score': [92, 95]},
#  'NY': {'city': ['NY', 'NY', 'NY'],
#         'index': [0, 2, 4],
#         'name': ['Alice', 'Charlie', 'Eve'],
#         'score': [85, 88, 90]}}


"""
P4: groupby()
"""
print("\nP4:") # don't change this
df = {
	'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
	'city': ['NY', 'LA', 'NY', 'LA', 'NY'],
	'score': [85, 92, 88, 95, 90]
}

df_sum_by_city = pc.groupby(df, 'city', 'sum')
pp(df_sum_by_city)
# {'city': ['NY', 'LA'], 'score': [263, 187]}
"""
P5: describe()
"""
print("\nP5:") # don't change this
df = {
	'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
	'city': ['NY', 'LA', 'NY', 'LA', 'NY'],
	'score': [85, 92, 88, 95, 90]
} # don't change this

summary_of_score = pc.describe(df, ["score"]) # don't change this
pp(summary_of_score) # don't change this
# {'score': {'count': 5, 'max': 95, 'mean': 90.0, 'min': 85}}

