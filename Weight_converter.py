# Lets write a weight converter program input weight if its in kilos display in lbs and vice versa

weight = float(input('Enter your weight : '))
print('Enter unit l for lbs AND k for kgs ')
unit = input('lbs OR kgs : ')

if unit == 'k' or unit == 'K':
    converted =  weight * 2.20462
    print(f'weight is {converted: .2f}lbs')
elif unit == 'l' or unit == 'L':
    converted =  weight / 2.20462
    print(f'weight is {converted : .2f}kgs')
else:
    print('invalid unit , Please enter kg/k or lb/l')

