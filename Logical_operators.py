# Logical operators in Python: and, or, not

# 'and' operator: Returns True if both conditions are True, otherwise False
x = 5
y = 10
if x > 0 and y > 5:
    print("Both conditions are True")  # This will execute

# 'or' operator: Returns True if at least one condition is True
a = 7
b = -3
if a > 0 or b > 0:
    print("At least one condition is True")  # This will execute

# 'not' operator: Reverses the Boolean value (True → False, False → True)
is_raining = False
if not is_raining:
    print("You can go outside")  # This will execute since not False = True

# Logical operators are commonly used in conditional statements and loops

# lets see some more examples

# logical and
has_good_credit = True
has_good_income = False

if has_good_credit and has_good_income:
    print("Eligible for loan")
else:
    print('Not eligible for loan')

# logical or
has_good_credit = True
has_good_income = False
if has_good_credit or has_good_income:
    print("Eligible for loan")
else:
    print('Not eligible for loan')

# logical not
is_raining = False
if not is_raining:
    print('You can go outside')

