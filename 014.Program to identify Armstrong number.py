# Program to identify Armstrong number 
num = int(input("Enter a number : "))

num_str = str(num)
num_digits = len(num_str)
#Calculate the sum of each digit raised to the power of num_digits
sum_of_powers = 0

for digit in num_str:
    sum_of_powers += int(digit) ** num_digits

#CHeck if the sum matches the original number
if sum_of_powers == num:
    print(f'{num} is an Armstrong number!')
else:
    print(f'{num} is not an Armstrong number!')