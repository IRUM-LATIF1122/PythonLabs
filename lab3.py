# # Question 2 tempretaure converter from celcius to farenheit


# temp = float(input('Enter temprature : '))
# unit = input('celcius OR farenheit (enter c/f) :').lower()
# if unit == 'c':
#     converted_temp = temp * 1.8 + 32
#     print(f'temprature is  {converted_temp}F ')
# elif unit == 'f':
#     converted_temp = temp / 1.8 - 32
#     print(f'temprature is  {converted_temp}C ')
# else:
#     print('invalid unit .....')

# program to guess a number b/t 1-9 prompt show again & again untill user enter correct guess

# correct_guess  = 5
# while True:
#     guess_number = int(input('Guess a number : '))
#     if guess_number == correct_guess:
#         print('You gueesed correct congrats')
#         break

# input a word from user and reverse it

word = input(' Enter a word :')
print(word[:: -1 ])

# print pattern.................

counter = 1
while(counter <= 4):
    print('*' * counter)
    counter += 1
while(counter >= 0):
    print('*' * counter)
    counter -= 1





