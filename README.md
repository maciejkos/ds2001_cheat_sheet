Initially based on: https://learnxinyminutes.com/docs/python/

### Our online resources:

- DS2001 syllabus and
  schedule: https://docs.google.com/document/d/1KDv5eRDMsIv0cbXdks3B1SaTD-9BIEeoWduqn3NrkFU/edit?usp=sharing
- DS2000 lecture notes: https://course.ccs.neu.edu/ds2000/schedule.html
- Canvas: https://northeastern.instructure.com/courses/
- This cheat
  sheet: https://github.com/maciejkos/ds2001_cheat_sheet/blob/main/README.md

# **Weeks 1 and 2** (W1 and W2)

### **1. Python's `print()` Function**

- Use `print()` to display output to the console.

```python
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

name = "Alex"
print("And my name is:", name)  # => And my name is: Alex
```

### **2. Getting Input from the User**

- Use `input()` to receive input from the user. The input is returned as a
  string.

```python
input_string_var = input("Enter some data: ")
print(input_string_var)  # Output the entered data
print("Your data are:", input_string_var)  # => Your data are: some_data
```

### **3. Numbers**

- You can work with numbers in Python.

```python
3  # => 3
```

### **4. Types of Numbers**

- Python supports different types of numbers.

```python
type(1)  # => <class 'int'>
type(1.1)  # => <class 'float'>
```

### **5. Strings vs Numbers**

- Strings that represent numbers can be converted to actual numbers.

```python
type("1")  # => <class 'str'>
type(int("1"))  # => <class 'int'>
```

### **6. Basic Arithmetic Operations**

- You can perform arithmetic as you would expect.

```python
1 + 1  # => 2
8 - 1  # => 7
10 * 2  # => 20
35 / 5  # => 7.0
```

### **7. Floor Division**

- Floor division rounds towards negative infinity.

```python
5 // 3  # => 1
-5 // 3  # => -2
5.0 // 3.0  # => 1.0
-5.0 // 3.0  # => -2.0
```

### **8. Division Results in a Float**

- Division always produces a float.

```python
10.0 / 3  # => 3.3333333333333335
```

### **9. Rounding Numbers**

- You can round numbers to a specific number of decimal places.

```python
round(17 / 2.3, ndigits=2)  # => 7.39
```

### **10. Modulo Operation**

- The modulo operator `%` returns the remainder of a division.

```python
7 % 3  # => 1
-7 % 3  # => 2
```

### **11. Exponentiation**

- Use `**` for exponentiation (raising a number to the power of another).

```python
2 ** 3  # => 8
```

### **12. Operator Precedence**

- Use parentheses to enforce precedence in expressions.

```python
1 + 3 * 2  # => 7
(1 + 3) * 2  # => 8
```

### **13. Variable Assignment and References**

- Variables in Python store references to objects, not the objects themselves.

```python
a = 5  # Point a at 5
b = a  # Point b at what a is pointing to
```

### **14. Strings in Python**

- Strings can be created using either single or double quotes.

```python
"This is a string."
"This is also a string."
"John said 'Wow!'"  # Escape quotes properly.
```

### **15. String Concatenation**

- You can concatenate strings using the `+` operator.

```python
"Hello " + "world!"  # => "Hello world!", but don't print like this: print("Hello " + "world!")

text_to_print = "Hello " + "world!"
print(text_to_print)  # this should be ok
```

---

# **Week 3** (W3)

### **16. Math Functions**

- **Rounding**:
- Use `round()` to round numbers to a specific number of decimal places. (I
  showed this earlier.)

```python
round(10.111111111)  # => 10 (defaults to rounding to nearest integer)
round(10.111111111, ndigits=2)  # => 10.11
```

- **Finding Minimum and Maximum**:
    - Use the `min()` and `max()` functions to find the smallest or largest
      values.

```python
min(3, 1, 2)  # => 1
max(3, 1, 2)  # => 3
```

### **17. File Handling**

- **Reading from a File**:
    - Use `with open()` to read data from a file.
    - The `.readline()` method reads one line at a time.

```python
with open("vegetable_prices.txt", "r") as price_file:
	price_kale = float(price_file.readline())
	price_carrot = float(price_file.readline())
	price_broccoli = float(price_file.readline())

print(price_kale, price_carrot, price_broccoli)
```

### **18. Plotting with `matplotlib`**

- **Basic Plotting**:
    - Use `plt.plot(x, y, "marker")` to plot points.

```python
import matplotlib.pyplot as plt

plt.plot(100, 5, "x")  # Draws an x at position (100, 5)
plt.show()  # Displays the plot
```

- **Plotting User Input**:
    - Example of plotting based on user input.

```python
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

plt.plot(x1, y1, "o")  # Plot a circle at (x1, y1)
plt.plot(x2, y2, "x")  # Plot an x at (x2, y2)
plt.show()
```

- **Labeling Axes and Adding Titles**:
    - Label axes using `plt.xlabel()` and `plt.ylabel()`, and add a title with
      `plt.title()`.

```python
plt.xlabel("Description of the x-axis")
plt.ylabel("Description of the y-axis")
plt.title("Overall description of the plot")
plt.show()
```

- **Customizing Points**:
    - Customize the color, marker style, and size of points.

```python
# Red circle:
plt.plot(1, 2, "o", color="red")

# Blue square with custom size:
plt.plot(2, 4, "s", color="blue", markersize=25)
```

- **Adding a Legend**:
    - Use the `label` parameter in `plt.plot()` and then display the legend with
      `plt.legend()`.

```python
plt.plot(x1, y1, "s", color="blue", label="point one")
plt.plot(x2, y2, "d", color="orange", label="point two")
plt.legend()
plt.show()
```

- **Adjusting Axis Limits**:
    - Control the range of the axes using `plt.xlim()` and `plt.ylim()`.

```python
plt.xlim(0, 100)
plt.ylim(-100, 100)
plt.show()
```

- **Additional Plot Features**:
    - **Horizontal Line**: Draw a horizontal line at a specific y-value.

```python
plt.axhline(40, color="black")
```

- **Bar Chart**: Create a bar chart by specifying the x-position and height of
  each bar.

```python
plt.bar(1, 10, color="magenta")
```

```python
#  You can also use text lables instead of numbers for x-position
plt.bar("Northeastern U.", 10, color="red")
plt.bar("Boston U.", -2, color="gray")
```

- **Saving the Plot**:
    - Save the plot as an image file before displaying it with `plt.savefig()`.

```python
plt.savefig("example_plot.png", bbox_inches="tight")  # Save the plot as a PNG
plt.show()  # Display the plot
```

---

# **Week 4** (W4)

### **19. For-loops for File Handling and Iteration**

- **Using for-loops to Read Files**:
    - A `for` loop can be used to iterate over each line in a file and process
      the data one line at a time. Example file is [here](https://raw.githubusercontent.com/maciejkos/ds2001_cheat_sheet/refs/heads/main/data_quant_small.txt).

```python
# Let's multiply numbers in a file by each other.

# Initialize a variable to store the multiplication result
# Right now, we set it to 1. We will update it later.
# We are not setting it to 0, because multiplying numbers by 0 always gives 0.
# (We would initialize to a different number if we were summing values.)

result_multiplication = 1

with open("data_quant_small.txt", "r") as infile:
	"""
	Let's assume the lines in data_quant_small.txt are:
	3
	1
	2
	"""
	# This loop with have as many iterations as there are lines in the file (3)
	for line in infile:
		# this print will print:
		# "3" on iteration 1
		# "1" on iteration 2
		# "2" on iteration 3
		print(line)

		# We can't multiply strings, so let's cast line to int and store it
		# (On other occasions you may need to cast to another data type.)
		current_value = int(line)

		# Now, we can update our result.
		result_multiplication = result_multiplication * current_value

		# this print will print:
		# 3 on iteration 1 (because 1*3 = 3)
		# 3 on iteration 2 (because 3*1 = 3)
		# 6 on iteration 3 (because 3*2 = 6)
		print("The multiplication results on this loop iteration is: ",
			result_multiplication)

print("The final multiplication results is: ", result_multiplication)



```


```python
with open("data_quant_small.txt", "r") as infile:
	previous_value = 0  # Set an initial value for comparison
	for line in infile:
		current_value = float(line)  # Convert the line to a float
		change = current_value - previous_value  # Calculate the change
		previous_value = current_value  # Update the previous value for the next iteration

		print("Current value:", current_value)
		print("Change from previous:", change, "\n")
```

- #### **Using `range()` in for-loops**

    - The `range()` function generates a sequence of numbers. You can use it in
      a `for` loop to repeat actions a specific number of times.
    - By default, `range(n)` generates numbers starting from 0 up to, but not
      including, `n`.

```python
for i in range(3):  # Loops 3 times (i will be 0, 1, 2)
	print("This is loop number:", i)
```
> If you want to know more about `range()`, here you go:
> - **Specifying a Start and End Value**:
>     - You can provide both a start and an end value with `range(start, end)`,
>       where `start` is included, but `end` is not.
> 
> ```python
> for i in range(2, 5):  # Loops with i = 2, 3, 4
>     print("Current value of i:", i)
> ```
> 
> - **Using a Step Value**:
>     - You can also specify a step value using `range(start, end, step)` to skip
>       numbers or count backwards.
> 
> ```python
> for i in range(0, 10, 2):  # Loops with i = 0, 2, 4, 6, 8
>     print("Even number:", i)
> ```
> 
> ```python
> for i in range(5, 0, -1):  # Loops with i = 5, 4, 3, 2, 1 (counts down)
>     print("Counting down:", i)
> ```

#### **For-loops with `matplotlib`**:

- You can manually plot multiple points by calling `plt.plot()` inside a `for`
  loop.

```python
import matplotlib.pyplot as plt

# Plot multiple points manually using a for-loop
for i in range(3):  # Loops with i = 0, 1, 2;

	# creates points: 0, 0 followed by 1, 2 followed by 2, 4
	point_x = i
	point_y = i * 2

	plt.plot(point_x, point_y, "o")  # Plot the point

plt.show()
```

### **20. Boolean Values: `True` and `False`**

- **What are Booleans?**
    - Booleans are a special data type that can have one of two values: `True`
      or `False`.
    - We will need them for comparisons and conditional statements.

```python
is_sunny = True
is_raining = False

print(is_sunny)  # Output: True
print(is_raining)  # Output: False
```

- **Booleans from Comparisons**:
    - Comparisons like `==`, `>`, `<`, `>=`,
      `<=` return `True` or `False`.

```python
x = 5
y = 10

print(x == y)  # Output: False (because 5 is not equal to 10)
print(x < y)  # Output: True (because 5 is less than 10)
```

### **21. Conditional Statements: `if`, `elif`, `else`**

- **Basic Conditional Logic**:
    - Use `if`, `elif`, and `else` to handle different conditions.

- **Using Booleans in Conditional Statements**:
    - Booleans can directly control the flow of your program in `if`, `elif`,
      and `else` statements.

```python
is_sunny = True

if is_sunny:
	print("It's sunny outside!")
else:
	print("It's cloudy outside!")
```

- **What is `if`?**
    - The `if` statement checks the first condition in a sequence of conditional
      statements.
    - If the condition in the `if` statement evaluates to `True`, the code
      inside the `if` block will execute, and Python will **skip any
      following `elif` or `else` blocks**.
    - If the condition is `False`, Python moves to the next condition (if any)
      in the sequence.

```python
x = 10

if x > 5:
	print("x is greater than 5")  # This code runs because x > 5
```

- **What is `elif`?**
    - `elif` (short for "else if") comes after an `if` statement and checks
      additional conditions if the `if` condition was `False`.
    - You can use multiple `elif` statements to handle different scenarios.
    - Once an `elif` condition is `True`, Python runs the code inside that block
      and **skips any further `elif` or `else` blocks**.

```python
x = 3

if x > 5:
	print("x is greater than 5")
elif x == 3:
	print("x is equal to 3")  # This code runs because x == 3
elif x < 5:
	print("x is less than 5")  # This is skipped because the previous elif was True
```

- **What is `else`?**
    - The `else` block is the "catch-all" for cases where none of the `if` or
      `elif` conditions are `True`.
    - It does **not** check any condition—if Python reaches an `else` block, it
      simply runs the code inside.

```python
x = 1

if x > 5:
	print("x is greater than 5")
elif x == 3:
	print("x is equal to 3")
else:
	print("x is not greater than 5 or equal to 3")  # This code runs because the other conditions were False
```

- **How `if`, `elif`, and `else` Work Together**

- Python checks conditions **from top to bottom**, and only the **first `True`
  condition** runs its block of code. After a condition is satisfied, Python *
  *skips the rest** of the `elif` and `else` blocks.
- If none of the conditions in `if` or `elif` statements are `True`, the `else`
  block (if present) will run.

```python
age = int(input("Enter your age: "))

if age < 13:
	print("You're a child.")  # This runs if age < 13
elif age < 20:
	print("You're a teenager.")  # This runs if age is 13-19
elif age < 65:
	print("You're an adult.")  # This runs if age is 20-64
else:
	print("You're an older adult.")  # This runs if none of the above conditions is true
```

- **Summary of Differences**

- **`if`**: Always comes first and checks the initial condition.
- **`elif`**: Comes after `if` (and can be repeated multiple times) to check
  more conditions if the previous ones were `False`.
- **`else`**: Comes at the end and runs only if none of the `if` or `elif`
  conditions were `True`. It does not check any conditions itself.

### **22. Boolean Operators: `and`, `or`, `not`**

- **Combining Conditions**:
    - Use boolean operators to combine conditions in a single `if` statement.
    - Here, we use `and` to check if both conditions are `True`

```python
age = int(input("Enter your age: "))

if age >= 18 and age < 65:
	print("You're an adult.")
elif age < 18:
	print("You're a minor.")
else:
	print("You're an older adult.")

# Thinking exercise: How would you re-write the above code to replace
# the `and` with two `if`s? Would it give the right answer?
```

- **Logical Operators with Booleans**:
    - Boolean values work with logical operators like `and`, `or`, and `not`.

```python
x = 10
y = 20
z = 30

print(x < y and y < z)  # Output: True (both comparisons are True)
print(not (x == z))  # Output: True (since x is not equal to z)
```
# **New Material** (W5)

### **23. Lists**

#### **Creating Lists**
- Lists are ordered collections of items in Python.
- You can create lists using square brackets `[]`.

```python
empty_list = [] # empty list 
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
```

#### **Creating Lists from Strings using `split()`**
- The `split()` method turns a string into a list of substrings.
- By default, it splits on whitespace. You can specify a different delimiter.

```python
line_from_a_file = "10,20,30"
numbers_list = line_from_a_file.split(",")
print(numbers_list)  # Output: ['10', '20', '30']

sentence = "The quick brown fox"
words = sentence.split()
print(words)  # Output: ['The', 'quick', 'brown', 'fox']

# but things can get tricky
clock_sounds = "tick, tock, tick, tock"

print(clock_sounds.split())  # Oopsie! Too many commas ['tick,', 'tock,', 'tick,', 'tock']
print(clock_sounds.split(", "))  # That's better: ['tick', 'tock', 'tick', 'tock']

clock_sounds_no_commas = "tick tock tick tock"
print(clock_sounds_no_commas.split(", ")) # what will this print?
```

```python
with open("my_file.txt", "r") as infile:
	# Let's assume these are the contents of "my_file.txt":
	# Alex likes long naps.
	# Jo likes lazy Sundays.
	for row in infile:
		words_as_list = row.split()
		print(words_as_list) # 1st: ['Alex', 'likes', 'long', 'naps.']
							#  2nd: ['Jo', 'likes', 'lazy', 'Sundays.']
```

#### **Accessing List Elements**
- Use indexing to access elements in a list.
- Indexing starts at 0 for the first element.
- Use negative indexing to access elements from the end of the list.

[//]: # (- You can also access a slice of a list using [:] )

```python
fruits = ["apple", "banana", "cherry", "pineapple", "kiwi"]
print(fruits[0])   # Output: "apple"
print(fruits[-1])  # Output: "kiwi" (last element)
print(fruits[1])   # Output: "banana"
```

#### **List Iteration (for loops with lists)**
- You can iterate through lists using `for` loops.

```python
# Iterating by value
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # 1st: "apple", 2nd: "banana", 3rd: "cherry"

# Iterating by index
for i in range(len(fruits)):
  print(f"Index {i}: {fruits[i]}")  # 1st: i=0, prints "Index 0: apple"
                                    # 2nd: i=1, prints "Index 1: banana"
                                    # 3rd: i=2, prints "Index 2: cherry"
```

#### **Modifying Lists**
- Lists are mutable, meaning you can change their contents.

```python
# Adding elements to a list using append()
numbers = []
numbers.append(1)
numbers.append(2)
print(numbers)  # Output: [1, 2]

# Modifying elements by index
fruits = ["apple", "banana", "cherry"]
fruits[1] = "grape"
print(fruits)  # Output: ["apple", "grape", "cherry"]
```

#### **Filtering Lists**

```python
# Using a for loop
numbers = [1, 2, 3, 4, 5]
evens = []
odds = []
for num in numbers:
  if num % 2 == 0:
      evens.append(num)  # 2nd: [2], 4th: [2, 4]
  else:
      odds.append(num)   # 1st: [1], 3rd: [1, 3], 5th: [1, 3, 5]
  # After each iteration:
  # 1st: evens=[], odds=[1]
  # 2nd: evens=[2], odds=[1]
  # 3rd: evens=[2], odds=[1, 3]
  # 4th: evens=[2, 4], odds=[1, 3]
  # 5th: evens=[2, 4], odds=[1, 3, 5]

print(f"Even numbers: {evens}")  # [2, 4]
print(f"Odd numbers: {odds}")   # [1, 3, 5]
```

#### **Counting Elements Based on a Condition**
- You can count occurrences in a list that meet certain conditions.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
for number in numbers:
	if number % 2 == 0:
		even_count = even_count + 1
print("There are", even_count, "even numbers.")  # Output: There are 5 even numbers.
```

#### **Converting List Elements**
- You can convert elements in a list from one type to another.

```python
#  Converting strings to integers
str_numbers = ['5', '4', '3', '2', '1']
for i in range(len(str_numbers)):
	str_numbers[i] = int(str_numbers[i])
print(str_numbers)  # [5, 4, 3, 2, 1]
```

#### **Conditional List Appending**

```python
numbers = [10, 25, 3, 40, 5]
even_numbers = []

for num in numbers:
	if num % 2 == 0:  # Condition: if the number is even
		even_numbers.append(num)

print("Even numbers:", even_numbers)  # Output: Even numbers: [10, 40]
```

### **24. Using the `random` Module**

- The `random` module in Python allows you to generate random numbers.
- It's useful for simulations, games, and making decisions based on chance.

```python
import random # first import random

# Generate a random integer between 1 and 10 (inclusive, so 1 and 10 possible) 
random_number = random.randint(1, 10)
print("The random number is:", random_number)
```

- **Create many random numbers and store in a list**

```python
import random

NUMBERS_TO_GENERATE = 10
BOUND_LOWER = 10
BOUND_UPPER = 50
random_ints = []

for i in range(NUMBERS_TO_GENERATE):
	random_int = random.randint(BOUND_LOWER, BOUND_UPPER)
	random_ints.append(random_int)
    
print(random_ints)
```
---
2024 Maciej Kos

version: 9/24/2024
