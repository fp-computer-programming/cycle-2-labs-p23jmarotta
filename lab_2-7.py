# Creator JM 9/20/22 lab2-7

a = 5
b = 10
c = 0
d = -4

variables = [a,b,c,d]

for num in variables:
    if num%2 == 0:
        print('Number is even')
    else:
        print('Number is odd')

    if num < -5:
        print('- less than -5')
    elif num < 5:
        print('- number is between -5 and 5')
    else:
        print('- number is greater than 5')

