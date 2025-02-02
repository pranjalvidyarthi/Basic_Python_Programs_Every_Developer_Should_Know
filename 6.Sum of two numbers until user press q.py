# Program to find sum of numbers inputtted by user
sum = 0
while(True):
    userinput = input("Enter your number :")
    if userinput !='q':
        sum = sum + int(userinput)
        print(f'Sum is {sum}')
    else:
        print(f'Thank you for using this program')
        break