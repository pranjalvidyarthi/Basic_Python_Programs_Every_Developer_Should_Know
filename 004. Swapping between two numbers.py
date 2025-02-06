# Swapping between two numbers 
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2: "))

#Swapping without using a temporary  variable
num1 , num2 = num2, num1
print(f'After swapping: num1 = {num1}, num2 = {num2}')