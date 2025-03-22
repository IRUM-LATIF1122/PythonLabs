# Conditional statement allows a program to execute different blocks of code based on a specified condition.
# it helps in decision making , control flow ....

# lets see an example

is_hot = True
is_cold = False

if is_hot:
    print("its hot outside ")
    print("drint plenty of water")
elif is_cold:
    print('its cold outside wear warm clothes')
else:
    print('wearther is pleaseant')
print('Weather updates ...')

# lets see another example house price = 1M$ if buyer has good credit down payement = 10%  else downpayment = 20%

buyer_credit = True

if buyer_credit:
    down_payment = 10 / 100 * 1000000
else:
    down_payment = 20 / 100 * 100000
print(f'Downpayment is: ${down_payment}')

# lets see another example
# input marks if marks>40 print pass else fail

marks = int(input(' Enter your marks '))
if marks >= 40:
    print('Congratulation you have passed')
else:
    print("No worries you will be passed next time ")

# lets see an example input name if name is less than 3 character display name should be atleast 3 charachters
# else if name is more than 50 characters display name should be less than 50 char else looks good

print('\n ')
name = input("Enter name :")
if len(name)<3:
    print("Name should be more than 3 characters ")
elif len(name)>50:
    print("Name should be less than 50 characters ")
else:
    print("Name looks good")