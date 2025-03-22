# Following are the arithmatic operators in python
# addition(+), subtraction(-) , multiplication(*) , division(/), remainder(%), exponent(**)

# Addition add and return result
num1 = 10
num2 = 5
sum = num1 + num2
print('Addition result  is ' , sum)

# subtraction subtract and return result
subtraction = num1 - num2
print('subtraction result is ', subtraction)

# multiplication  nultiplies two numbers
multiplication = num1 * num2
print("multiplication result is ", multiplication)

# division  divides and return Quotient
div = num1 / num2
print('division result is ', div)

# remainder divides and return remainder of division
rem = num1 % num2
print("remainder result is : ", rem)

# exponent makes second number power of first
expo = num1 ** num2
print("exponent result is :", expo)

# Operator precedence
# parenthesis                   --> highest precedence
# exponent                      --> after parenthesis
# multiplication & division     --> after exponent
# addition & subtraction        --> after multiplication & division

# lets check from an expression

x = 10 ** 2 + (5+7 ) * 5
print(x)                    # ouput = 160

y = 45 - 5 * 10 ** 2
print(y)                    #output = -455

# Now lets see some predefined functions in python

# round()  it will round of floating point number

num = 2.7
print(round(num))       # 3

num = 2.3
print(round(num))       # 2

num = 2.5
print(round(num))       # 2

num = 2.6
print(round(num))       # 3

# abs()  convert negative number into positive make number an absolute number

num = -7.6
print(abs(num))         # 7.6