# A function in Python is a reusable block of code that performs a specific task.
# Functions help make code more modular, readable, and efficient by
# allowing you to execute the same logic multiple times without repetition.

def greeting():
    """Function to print a generic greeting message."""
    print("Hi Dear")
    print("Hope you are fine :) ")


# Function with a parameter to greet a specific person
def greeting_by_name(name):
    """Function to greet a person by their name."""
    print(f"Hi {name}")
    print("Hope you are fine :) ")


print('Start')
greeting()  # Calling function without parameters
greeting_by_name('IRUM')  # Calling function with a parameter
print('End')


# In functions, the order of parameters matters

def greeting_user(first_name, last_name):
    """Function to greet a user with their first and last name."""
    print(f'Hi {first_name} {last_name}')
    print("Hope you are fine :) ")


# Calling function with positional arguments
greeting_user('John', 'Smith')

# Calling function with keyword arguments (explicit order specification)
greeting_user(last_name='Noor', first_name='Irum')


# Example Function Returning a Result
def calculate_area(length, width):
    """Function to calculate the area of a rectangle."""
    return length * width


# Calling function and storing the result
area_result = calculate_area(length=5, width=6)
print(f'Area is {area_result}')


# Function for an emoji converter
def emoji_converter(message):
    """Function to convert text-based emojis into Unicode emojis."""
    words = message.split()  # Splitting the message into words
    emojis = {
        ":)": "😊",  # Happy face
        "):": "😪",  # Sad face
    }

    output = " "
    for item in words:
        output += emojis.get(item, item) + " "  # Replace if found, else keep original
    return output


# Taking user input for emoji conversion
user_message = input('> ')
print(emoji_converter(user_message))
