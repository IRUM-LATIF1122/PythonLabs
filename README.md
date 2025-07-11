# Python Lab 1 - Basics

This repository contains my first Python lab, covering fundamental concepts like comments, input/output, data types, special characters, string operations, string slicing, lists, and list slicing.

## Lab Overview
- **Comments**: How to write comments in Python using `#`.  
- **Input/Output**: Using `input()` to take input and `print()` to display output.  
- **Data Types**: Introduction to integers, floats, complex numbers, strings, and booleans.  
- **List Operations**: Creating and printing lists with different data types.  
- **List Slicing**: Extracting sublists and reversing lists using slicing.

## How to Run
1. Ensure Python is installed on your system.  
2. Run the file in your terminal or any IDE (like PyCharm) using:  
   ```bash
   python lab1.py
   ```

# Python Basics: Arithmetic Operators, Conditional Statements & Logical Operators

### 1. Arithmetic Operators
Python supports the following arithmetic operators:
- **Addition (`+`)**: Adds two numbers
- **Subtraction (`-`)**: Subtracts one number from another
- **Multiplication (`*`)**: Multiplies two numbers
- **Division (`/`)**: Divides one number by another
- **Remainder (`%`)**: Returns the remainder of a division
- **Exponent (`**`)**: Raises one number to the power of another

The program includes examples of each arithmetic operation.

### 2. Operator Precedence
The precedence of operators in Python is:
1. Parentheses `()` - Highest precedence
2. Exponentiation `**`
3. Multiplication `*`, Division `/`
4. Addition `+`, Subtraction `-`

Examples in the code demonstrate how Python evaluates expressions based on these rules.

### 3. Predefined Functions
The program showcases built-in Python functions:
- **`round()`**: Rounds a floating-point number.
- **`abs()`**: Returns the absolute value of a number.

### 4. Conditional Statements
Conditional statements allow for decision-making in Python:
- **`if` Statement**: Executes a block of code if a condition is true.
- **`if-else` Statement**: Executes different blocks of code based on a condition.
- **`if-elif-else` Statement**: Evaluates multiple conditions sequentially.

Examples include:
- Weather conditions (hot, cold, pleasant)
- House purchase decision based on credit
- Pass/Fail grading system
- Name length validation

### 5. Logical Operators
Logical operators are used for multiple conditions:
- **`and`**: Returns `True` if both conditions are `True`
- **`or`**: Returns `True` if at least one condition is `True`
- **`not`**: Reverses the Boolean value

Examples include loan eligibility checks and weather conditions.

### 6. Weight Converter Program
This simple program converts weight between kilograms (`kg`) and pounds (`lbs`):
- Takes user input for weight.
- Asks for the unit (`kg` or `lbs`).
- Converts and displays the weight in the appropriate unit.

# Loops in Python
### 7. Loops Overview
Loops allow repeated execution of a block of code:
- **`for` Loop**: Iterates over a sequence (like a list, tuple, or range).
- **`while` Loop**: Repeats as long as a condition is `True`.

Examples include iterating over numbers, lists, and using loops for calculations.

### 8. Lists and Tuples
Lists and tuples store multiple items in a single variable:
- **Lists**: Mutable, ordered, and allow duplicates.
- **Tuples**: Immutable, ordered, and allow duplicates.

#### List Operations
- Accessing elements by index.
- Finding the maximum number in a list using a loop.
- Using 2D lists for matrix-like structures.
- Common list methods: `append()`, `insert()`, `remove()`, `pop()`, `count()`, and `clear()`.
- Removing duplicates from a list.

#### Tuple Operations
- Accessing elements.
- Unpacking tuples into variables.
- Using `*` to collect remaining values.
- Looping over tuples.

### 9. Dictionary Basics
A dictionary stores key-value pairs:
- **Mutable** and indexed by unique keys.
- Used for fast data retrieval.

#### Dictionary Operations
- Creating and accessing elements.
- Adding new key-value pairs.
- Using `.get()` to retrieve values safely.
- Example program: Converting a phone number to words using a dictionary.
  Python Functions Overview

#### 9. Functions 

- Function with parameters: Greeting with a name.
- Positional vs. Keyword Arguments: Shows how function arguments can be passed.
- Returning values: A function that calculates the area of a rectangle.
- Emoji Converter: A function that replaces text-based emojis with Unicode emojis.

#### 10 Python Exception Handling
- Prevents program crashes due to runtime errors.
- Provides meaningful error messages for better debugging.
- Ensures controlled execution with a `try-except-finally` structure.

#### How Exception Handling Works
- **try block**: Contains code that may cause an error.
- **except blocks**: Catch specific errors like:
  - `ZeroDivisionError`: Prevents division by zero.
  - `ValueError`: Ensures valid number input.
  - Generic `Exception`: Catches unexpected errors.
- **finally block**: Executes no matter what, ensuring program completion.

  #### Lab # 3
- Includes simple python problems and their solutions.
  #### Clases in python
  - this file covers the basic concepts of clases, constructer, destructor, methods in python. 
#### Stack:
 - basic implementation of class Stack using list.
 - Stack is a data structure that follows the LIFO (Last In, First Out) principle.
 - You push (add) elements to the top of the stack.
 - You pop (remove) the most recently added element.
 - You can also peek to look at the top item without removing it.
  
#### Queue:
- basic implementation of class Queue using list.
- Stack is a data structure that follows the FIFO (First In, First Out) principle.
- You enqueue (add) elements to the rear (end) of the queue.
 -You dequeue (remove) the  earliest added  element from front.
 -You can also peek to look at the front item without removing it.

# Pandas Practice File(pandaas_lib.py) 🐼

This file contains my beginner-level practice code for working with the **Pandas** library in Python. It includes examples and exercises that cover:

### ✅ Key Concepts Practiced:
- Creating and working with **Series**
- Creating **DataFrames** from dictionaries
- Selecting and filtering data using `loc[]` and `iloc[]`
- Reading from and writing to **CSV** files
- Cleaning data using `dropna()`, `fillna()`, and type casting
- Creating new columns and using `apply()` with functions
- Combining data with **concat** and **merge**

---

### 📁 File Structure

| File                 | Description                                 |
|----------------------|---------------------------------------------|
| `pandas_practice.py` | The main practice script                    |
| `CSV_data/`          | Folder for input and output CSV files       |

---

### 🚀 How to Run

1. Make sure you have Python installed (version 3.7+ recommended).
2. Install pandas:

## Author
This project was created as part of learning Python basics.

