# Check if a number is a perfect number
# Perfect number - A number is perfect if the sum of its factors (excluding itself) equals the number

num = int(input('Enter a number : '))
factors_sum = sum(i for i in range(1, num) if num % i == 0)
print(f'{num} is a Perfect Number' if factors_sum == num else f"{num} is not a perfect number")