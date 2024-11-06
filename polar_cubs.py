"""
Maciej Kos
DS 2001 - Assignment 10
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
 ->>>> PLEASE UPLOAD BOTH assignment10.py AND polar_cubs.py <<<< -
"""

"""
Functions (and a class) that you can use. Please don't edit them. 
"""

class DataFrameValidationError(Exception):
	"""Custom exception for dataframe validation errors
	Used by validate_dataframe()
	You will not have any use for it, most likely.
	"""
	pass

def validate_dataframe(data):
	"""
	Validates a dictionary-based dataframe and raises DataFrameValidationError
	if any issues are found.

	Checks for:
	1. Empty data
	2. Inconsistent column lengths
	3. Missing values (None)
	4. Empty columns
	5. Non-list values
	"""
	issues = []

	# Check if data is empty
	if not data:
		raise DataFrameValidationError("Empty dataframe: no columns found")

	# Check if all values are lists
	for column_name, column_data in data.items():
		if not isinstance(column_data, list):
			raise DataFrameValidationError(
				f"Column '{column_name}' is not a list")

	# Check for empty columns
	empty_columns = [col for col, values in data.items() if len(values) == 0]
	if empty_columns:
		issues.append(f"Empty columns found: {', '.join(empty_columns)}")

	# Get lengths of all columns
	lengths = {col: len(values) for col, values in data.items()}

	# Check for inconsistent lengths
	if len(set(lengths.values())) > 1:
		issues.append("Inconsistent column lengths:")
		for col, length in lengths.items():
			issues.append(f"  - '{col}': {length} rows")

	# Check for None values
	for column_name, column_data in data.items():
		if None in column_data:
			none_indices = [i for i, x in enumerate(column_data) if x is None]
			issues.append(
				f"Column '{column_name}' contains None values at indices: {none_indices}")

	# If any issues were found, raise exception
	if issues:
		raise DataFrameValidationError("\n".join(issues))


def show(df, validate_df = False):
	"""
	Prints dictionary data in a tabular format with aligned columns.
	You will probably use it often in your final project.

	Parameters
	----------
	df : dict
		Dictionary where keys are column names and values are lists of df
	validate_df : bool
		If True: checks whether the df is properly formedTrue (
		default); if False (default), this check is skipped.

	Returns:
		Nothing.

	"""
	if not df:
		print("Empty dataset")
		return

	if validate_df:
		try:
			validate_dataframe(df)
		except DataFrameValidationError as e:
			print("Cannot show the dataframe due to following issues:")
			raise DataFrameValidationError(str(e))

	# Get column widths (maximum of column name and longest value)
	# We need it to make the table look nice and neat
	widths = {}
	for column in df:
		# Convert all values to strings and get their lengths
		value_lengths = [len(str(x)) for x in df[column]]
		# Get maximum length between column name and values
		widths[column] = max(len(column), max(value_lengths))

	# Print header
	header = ""
	separator = ""
	for column in df:
		header += f"{column:<{widths[column]}} "
		separator += "-" * widths[column] + " "
	print(header)
	print(separator)

	# Print rows
	num_rows = len(list(df.values())[0])
	for i in range(num_rows):
		row = ""
		for column in df:
			row += f"{str(df[column][i]):<{widths[column]}} "
		print(row)

	print()
	print(f"Your data have {num_rows} rows and {len(df.keys())} columns.")
	print()


def save_dict_df_as_csv(df, filename):
	"""
	Convert a dictionary-based dataframe to a CSV file and save it.
	Safely handles special characters.

	Parameters
	----------
	df : dict
		Dictionary where keys are column names and values are lists of df
	filename : str
		Name of the CSV file to create (should end with .csv)
	"""
	import csv
	# Get column names (dictionary keys)
	columns = list(df.keys())

	# Open file in write mode
	with open(filename, 'w', newline='') as f:
		writer = csv.writer(f)

		# Write header
		writer.writerow(columns)

		# Write rows
		for i in range(len(df[columns[0]])):
			row = [df[col][i] for col in columns]
			writer.writerow(row)

def sort_values(df, by_column):
	"""Sort df by a specific column, in ascending order

	Example:

	-> df = {
		'name': ['Maciej', 'Alice', 'Bob', 'Charlie', 'David', 'Eve'],
		'city': ['BOS', 'NY', 'LA', 'NY', 'LA', 'NY'],
		'score': [5, 85, 92, 88, 95, 90],
		'index': [0, 1, 2, 3, 4, 5]
	}
	-> print(sort_values(df, "name"))

	{
		'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Maciej'],
		'city': ['NY', 'LA', 'NY', 'LA', 'NY', 'BOS'],
		'score': [85, 92, 88, 95, 90, 5],
		'index': [1, 2, 3, 4, 5, 0]
	}

	Parameters
	----------
	df : dict
		Dictionary where keys are column names and values are lists of df
	by_column : str
		The column by which to group the data.

	Returns
	-------
	dict
		A dictionary (dataframe) sorted by `by_column`

	"""
	# Get the column to sort by
	sort_col = df[by_column]

	# Create list of indices and sort by values
	indices = list(range(len(sort_col)))
	indices.sort(key=lambda i: sort_col[i])

	# Reorder all columns
	result = {}
	for col in df:
		result[col] = [df[col][i] for i in indices]
	return result


def convert_column_type(df, column_name, new_type):
	"""
	Takes a dictionary-based dataframe and converts values in a specified column to a new type.
	Handles various error cases and provides informative messages.

	Parameters
	----------
	df : dict
	    A dictionary where keys are column names and values are lists of data
	column_name : str
	    The name of the column whose values should be converted
	new_type : type
	    The Python type to convert the values to (int, float, str, etc.)

	Returns
	-------
	dict
	    A new dictionary with the same structure but with converted values in the specified column

	Raises
	------
	KeyError
	    If column_name doesn't exist in df
	ValueError
	    If conversion fails for any value
	TypeError
	    If the type conversion is not supported
	"""
	if column_name not in df:
		raise KeyError(f"Column '{column_name}' not found in dataframe")

	result = {}
	for col in df:
		result[col] = df[col].copy()

	for i in range(len(result[column_name])):
		value = result[column_name][i]

		# Skip None values
		if value is None:
			continue

		try:
			# Special handling for certain type conversions
			if new_type == int:
				# Handle float strings for int conversion
				if isinstance(value, str) and '.' in value:
					value = float(value)
				result[column_name][i] = int(value)

			elif new_type == float:
				result[column_name][i] = float(value)

			elif new_type == str:
				result[column_name][i] = str(value)

			else:
				result[column_name][i] = new_type(value)

		except (ValueError, TypeError) as e:
			raise ValueError(
				f"Could not convert value '{value}' to {new_type.__name__} "
				f"at index {i}: {str(e)}"
			)

	return result


"""
Functions for you to write
"""

"""
P1: read_csv()
"""

def read_csv(filename):
	"""
	Reads a CSV file and returns a dictionary ("dataframe") where:
	- Keys are column names (from the header row)
	- Values are lists containing the column data
	- An 'index' column is added automatically with values 0, 1, 2, ...

	Handles cases where the file is empty or where rows have missing values.

	Example:
	--------
	Given a file "score_by_city.csv" with:
		name,city,score
		Alice,NY,85
		Bob,LA,92
		Charlie,NY,88
		David,LA,95
		Eve,NY,90

	-> df = read_csv("score_by_city.csv")
	-> print(df)
	{
		'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
		'city': ['NY', 'LA', 'NY', 'LA', 'NY'],
		'score': [85, 92, 88, 95, 90],
		'index': [0, 1, 2, 3, 4]
	}

	Parameters
	----------
	filename : str
		The name of the CSV file to read.

	Returns
	-------
	dict
		A dictionary where:
		- Keys are column names (strings)
		- Values are lists containing the column data
		- An added 'index' key contains row indices starting from 0.
	"""
	# Initialize an empty dictionary to store column data
	df = {}

	# Step 1: Open the file and read all lines using .readlines()
	with # finish this line
		lines = # finish this line

		# Check if the file is empty. Ff it is empty, return an empty dict.
		if # finish this conditional
			print("Error: The file is empty.")
			return {}

		# Step 2: Process the first line as headers
		headers = # finish this line
		for header in headers:
			# Initialize a list for each column in `df`

		# Example after Step 2 (if headers are "name", "city", "score"):
		# df = {'name': [], 'city': [], 'score': []}

		# Step 3: Process each subsequent line as a data row
		for line in lines[1:]:
			values_to_process = # strip whitespace and convert to a
			# list
			values = [] # this is a hint, leave it here; don't change this; use this

			# `values_to_process` may contain empty strings ''
			# Iterate over values in the `values_to_process` list. If a value
			# is not an empty string, append it to `values`. If it is an empty
			# string, append None instead.
			# Write a for loop to do this.

			# Assign each value from `values` to its respective column based on
			# headers
			for i in range(len(headers)):
				df[headers[i # finish this statement

			# Example after Step 3 (with 3 rows of data):
			# df = {
			#     'name': ['Alice', 'Bob', 'Charlie'],
			#     'city': ['NY', 'LA', 'NY'],
			#     'score': ['85', '92', '88']
			# }

	# Step 4: Here, we add an 'index' column with sequential integers from 0 to
	# num_rows - 1. You don't have to write any code here.
	num_rows = len(df[headers[0]]) # don't change this
	df["index"] = list(range(num_rows)) # don't change this

	# Example after Step 4:
	# df = {
	#     'name': ['Alice', 'Bob', 'Charlie'],
	#     'city': ['NY', 'LA', 'NY'],
	#     'score': ['85', '92', '88'],
	#     'index': [0, 1, 2]
	# }

	# Step 5: Return the completed `df` dictionary with the added 'index' column
	return


"""
P2: filter_df()
"""

def filter_df(df, column, value, condition="=="):
	"""
	Filters a dictionary ("dataframe") to only include rows where the specified column
	meets a given condition. A new dictionary is returned containing only the rows
	that match the condition.

	Example:
	--------
	-> df = {
		'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
		'city': ['NY', 'LA', 'NY', 'LA', 'NY'],
		'score': [85, 92, 88, 95, 90],
		'index': [0, 1, 2, 3, 4]
	}

	-> df_score_gt_90 = filter_df(df, 'score', 90, condition=">")
	-> print(df_score_gt_90)
	{
		'name': ['Bob', 'David'],
		'city': ['LA', 'LA'],
		'score': [92, 95],
		'index': [1, 3]
	}

	Overview:
	---------
	1. The function initializes an empty dictionary, `filter_df`, with the same
	   column structure as `df`, but with empty lists to hold filtered values.
	2. It iterates over each row in the specified column and applies the condition:
	   - Supported conditions are '==', '>', and '<'.
	   - Rows that match the condition are kept in `filter_df`.
	3. The filtered rows are returned as `filter_df`.

	Parameters
	----------
	df : dict
		A dictionary representing tabular data where:
		- Keys are column names (strings)
		- Values are lists containing the column data

	column : str
		The name of the column to filter by.

	value : any
		The value to compare against in the specified column.

	condition : str, optional
		The condition for filtering (default is '==').
		- '==': Include rows where `column` equals `value`.
		- '>': Include rows where `column` is greater than `value`.
		- '<': Include rows where `column` is less than `value`.

	Returns
	-------
	dict
		A new dictionary (dataframe) containing only rows that meet the
		condition.
	"""
	# Step 1: Initialize an empty dictionary `filter_df` with the same structure as `df`
	# No need to write any code.
	filtered_df = {col: [] for col in df} # leave it here; don't change this;
	# at this point filtered_df is {'name': [], 'city': [], 'score': [], 'index': []}

	# Step 2: Iterate over each row of the selected column in the df and apply
	# the filter condition
	for i in range(len(df[column])): # don't change this
		# Check if the row meets the specified condition
		# It will be a very long if-statement that checks different things
		# depending on the condition parameter. We started you off
		# condition = "==".
		if (condition == "==" and df[column][i] == # finish this line

			# Step 3: Add the data for this row to `filter_df`
			for col in df:
				filtered_df[col]# finish this statement

	# Step 4: Return `filter_df` with only the rows that matched the condition
	return

"""
P3: groupify()
"""

def groupify(df, by_column):
	"""
	Groups rows of data based on unique values in a specified column and returns
	a dictionary where:
	- Keys are unique values from `by_column`
	- Values are dictionaries with lists of values from all columns for each group

	Example:
	--------
	-> df = {
		'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
		'city': ['NY', 'LA', 'NY', 'LA', 'NY'],
		'score': [85, 92, 88, 95, 90],
		'index': [0, 1, 2, 3, 4]
	}

	-> df_by_city = groupify(df, 'city')
	-> print(df_by_city)
	{
		'NY': {
			'name': ['Alice', 'Charlie', 'Eve'],
			'city': ['NY', 'NY', 'NY'],
			'score': [85, 88, 90],
			'index': [0, 2, 4]
		},
		'LA': {
			'name': ['Bob', 'David'],
			'city': ['LA', 'LA'],
			'score': [92, 95],
			'index': [1, 3]
		}
	}

	Overview:
	---------
	1. Identify all unique values in `by_column` to define groups.
	2. Initialize `result` with a sub-dictionary for each unique value.
	3. Populate each group by adding rows to the appropriate sub-dictionary in `result`.

	Parameters
	----------
	df : dict
		A dictionary representing tabular data with column names as keys.

	by_column : str
		The column by which to group the data.

	Returns
	-------
	dict
		A dictionary where each unique value in `by_column` is a key,
		and each value is a dictionary with grouped data for each column.
	"""
	# Step 1: Identify all unique values in the specified column
	# The unique values should end up being ['NY', 'LA'], if using the example
	# from the docstring.
	unique_values = [] # leave it here; don't change this;
	for value in df[by_column]: # leave it here; don't change this;
		# finish this loop


	# Step 2: Initialize the `result` dictionary for each unique group
	# At the end of this step, the result should be:
	# 	{'NY':
	# 		 {'name': [], 'city': [], 'score': [], 'index': []},
	# 	'LA': {
	# 		'name': [], 'city': [], 'score': [], 'index': []}}
	result = {} # leave it here; don't change this;


	# Step 3: Populate each group with corresponding rows from `df`
	for i in range(len(df[by_column])): # leave it here; don't change this;
		group_val = df[by_column][i] # leave it here; don't change this;
		for col in df: # leave it here; don't change this;
			# on the first iteration, this loop should append 'Alice' from df
			# to group `NY` column `name` in the result dictionary

	return result

"""
P4: groupby()
"""

def groupby(df, by_column, agg_function='mean'):
	"""
	Groups data by a specified column and applies an aggregation function
	(mean, sum, or count) to each group for the remaining columns.

	Example:
	--------
	-> df = {
		'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
		'city': ['NY', 'LA', 'NY', 'LA', 'NY'],
		'score': [85, 92, 88, 95, 90]
	}

	-> df_mean_by_city = groupby(df, 'city', 'sum')
	-> print(df_mean_by_city)

	{
		'city': ['NY', 'LA'],
		'score': [263, 187],
	}
	In this example, the function groups df by unique values in `city`.
	For each unique city ('NY' and 'LA'), it calculates the sum of scores.
	The aggregation function could also be 'mean' or 'count' for different
	aggregation results.

	Supported aggregation functions:
	- 'mean': Computes the average of values in each group.
	- 'sum': Computes the sum of values in each group.
	- 'count': Counts the number of rows in each group.

 Overview:
	---------
	1. The function calls `groupify` to create groups of rows based on unique values
	   in the specified `by_column`. Each group contains only the rows where `by_column`
	   matches the group’s unique value.
	   - Example: If `by_column` is "city", `groupify` will group all rows with
		 'NY' together and all rows with 'LA' together.

	2. The function initializes a result dictionary, `result`, where:
	   - `by_column` contains the unique values from `by_column`, one per group.
	   - Each other column will store aggregated values for each group.
	   - Example: With `by_column` "city", the initial `result` is
		 `{'city': ['NY', 'LA']}`.

	3. The function iterates over each unique value (group) and applies the
	   specified aggregation function to the other columns.
	   - Example: For each unique city, calculate the mean score and add it
		 to `result['score']`.

	4. Finally, the function returns the `result` dictionary, which contains
	   grouped data for `by_column` and aggregated data for the remaining columns.

	Parameters
	----------
	df : dict
		A dictionary representing tabular data where:
		- Keys are column names (strings)
		- Values are lists containing the column data.

	by_column : str
		The column name by which to group the data.

	agg_function : str, optional
		The aggregation function to apply to each group in other columns.
		Supported values are 'mean', 'sum', and 'count'. Default is 'mean'.

	Returns
	-------
	dict
		A dictionary where:
		- The key `by_column` contains unique values from `by_column`.
		- Each other key contains a list of aggregated values for the corresponding group.
	"""
	# Step 1: Group data by the specified column using `groupify`
	# Example: If `by_column` is 'city', `grouped_data` will contain data grouped by each city.
	grouped_df = groupify(df, by_column)

	# Step 2: Initialize the result dictionary with the unique values in `by_column`
	# - The `by_column` key in `result` stores these unique values
	# - Each remaining column will later store aggregated values for each group
	# - Using our example, if `by_column` is "city", the initial result would look like:
	#   {'city': ['NY', 'LA']}
	result = {} # leave it here; don't change this;
	keys_list = [] # leave it here; don't change this;
	for key in grouped_df.keys(): # leave it here; don't change this;
		# finish this for loop
	result[by_column] = # finish this line

	# Step 3: Apply the aggregation function to each group for all columns except `by_column`
	# We aggregate the remaining columns based on the group structure from
	# `groupify`.
	# A) We need to decide what columns to analyze. We need to ignore the
	# following columns: 1) the `by_column`, 2) columns that do not contain
	# floats or ints, if the `agg_function` is `mean` or `sum`

	column_names_to_analyze = [] # leave it here; don't change this;

	# You will need to write a for-loop that appends columns to
	# `column_names_to_analyze`.
	# This if-statement will be somewhere in your for-loop. It is here to
	# help you.

	if agg_function == 'mean' or agg_function == 'sum':
		if type(df[column_name][0]) in [int, float]:
			column_names_to_analyze.append(column_name)

	# B) Now, we need to iterate over all column names that we want to
	# analyze.

	for column_name in # finish this line
		# C) For the columns that we analyze, we need to set their
		# values in the `result` dict to an empty list. We will be appending to
		# that list later.
		result            # finish this line

		# Step 4: Compute the aggregation for each unique group
		for group_key, group_values in grouped_df.items():
			# For each group, retrieve the values for the current column `col`
			values = # finish this line
			# Example for Step 4:
			# If `column_name` is "score" and `group_key` is "NY", `values` would be:
			# values = [85, 88, 90] for group 'NY' in the "score" column
			# This list will be aggregated to produce a single value.

			# Apply the specified aggregation function to these values
			if agg_function == 'mean':
				aggregate_result = sum(values) / len(values) if values else 0
			# add the handling of the remaining aggregation functions

			else: # leave it here; don't change this;
				raise ValueError( # leave it here; don't change this;
					f"Unsupported aggregation function: {agg_function}") # leave it here; don't change this;

			# Append the `aggregate_result` for this group to the `result`
			# dictionary.
			# Using the example, if `agg_function` is 'mean', the `result` after
			# processing all groups for `score` would look like:
			# {'city': ['NY', 'LA'], 'score': [87.67, 93.5]}
			result # finish this line

	return result

def describe(df, numeric_columns):
	"""
	Calculate basic statistics for specified numeric columns.
	The basic statistics are mean, min, max, count. You can use the built-in
	functions like sum().

	None values are ignored.

	Example:
	-> df = {
		'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
		'city': ['NY', 'LA', 'NY', 'LA', 'NY'],
		'score': [85, 92, 88, 95, 90]
	}

	-> summary_of_score = describe(df, ["score"])
	-> print(summary_of_score)
	{'score': {'mean': 90.0, 'min': 85, 'max': 95, 'count': 5}}

	Parameters
	----------
	df : dict
		A dictionary where keys are column names and values are lists of data
	numeric_columns : list
		List of column names that should be treated as numeric

	Returns
	-------
	dict
		A dictionary where keys are column names and values are dictionaries
		containing the statistics for each numeric column
	"""
	result = {}



		return result

"""
 ->>>> PLEASE UPLOAD BOTH assignment10.py AND polar_cubs.py <<<< -
"""
