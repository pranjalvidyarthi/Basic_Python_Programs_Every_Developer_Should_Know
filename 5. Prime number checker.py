# CHeck whether a number is prime or not
num = int(input("Enter your number : "))
Prime = False
if num < 1:
    print(f'{num} is invalid input')
elif num > 1:
    for i in range(2, num):
        if num % i ==0:
            Prime = True
            break
    if Prime:
        print(f'{num} is not a Prime Number')
    else:
        print(f'{num} is a Prime Number ')