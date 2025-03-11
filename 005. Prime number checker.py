# CHeck whether a number is prime or not
number = int(input("Enter your number : "))
is_prime = False
if number < 1:
    print(f'{number} is invalid input')
elif number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = True
            break
    if is_prime == True:
        print(f'{number} is not a Prime Number')
    else:
        print(f'{number} is a Prime Number ')