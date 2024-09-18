Initially based on: https://learnxinyminutes.com/docs/python/

### Our online resources:

- DS2001 syllabus and
  schedule: https://docs.google.com/document/d/1KDv5eRDMsIv0cbXdks3B1SaTD-9BIEeoWduqn3NrkFU/edit?usp=sharing
- DS2000 lecture notes: https://course.ccs.neu.edu/ds2000/schedule.html
- Canvas: https://northeastern.instructure.com/courses/
- This cheat sheet: https://github.com/maciejkos/ds2001_cheat_sheet/blob/main/README.md

### **1. Python's `print()` Function**

- Use `print()` to display output to the console.

```python
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

name = "Alex"
print("And my name is:", name)  # => And my name is: Alex
```

### **2. Getting Input from the User**

- Use `input()` to receive input from the user. The input is returned as a string.

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

# **New Material** (W3)

### **16. Math Functions**

- **Rounding**:
- Use `round()` to round numbers to a specific number of decimal places. (I showed this earlier.)

```python
round(10.111111111)  # => 10 (defaults to rounding to nearest integer)
round(10.111111111, ndigits=2)  # => 10.11
```

- **Finding Minimum and Maximum**:
    - Use the `min()` and `max()` functions to find the smallest or largest values.

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
    - Label axes using `plt.xlabel()` and `plt.ylabel()`, and add a title with `plt.title()`.

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
    - Use the `label` parameter in `plt.plot()` and then display the legend with `plt.legend()`.

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

- **Bar Chart**: Create a bar chart by specifying the x-position and height of each bar.

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
2024 Maciej Kos

version: 9/16/2024
