# Let's write a weight converter program
# The user inputs a weight, and the program converts between kilograms and pounds

# Asking the user to enter weight as a floating-point number
weight = float(input('Enter your weight: '))

# Prompting the user to specify the unit of measurement
print('Enter unit: "l" for lbs AND "k" for kgs')
unit = input('lbs OR kgs: ')

# Checking if the input unit is kilograms (kg or K)
if unit == 'k' or unit == 'K':
    # Converting kg to lbs (1 kg = 2.20462 lbs)
    converted = weight * 2.20462
    # Displaying the converted weight with 2 decimal places
    print(f'Weight is {converted:.2f} lbs')

# Checking if the input unit is pounds (lb or L)
elif unit == 'l' or unit == 'L':
    # Converting lbs to kg (1 lb = 0.453592 kg)
    converted = weight / 2.20462
    # Displaying the converted weight with 2 decimal places
    print(f'Weight is {converted:.2f} kgs')

# If the user enters an invalid unit
else:
    print('Invalid unit. Please enter "k" for kg or "l" for lbs')
