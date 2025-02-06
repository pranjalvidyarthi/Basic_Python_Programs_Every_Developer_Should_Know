# Basic Calculator 
a =  float(input('enter the first number : '))
b = float(input('enter the second number :'))
operation = input("Choose operation (+,-,*,/): ")

if operation =='+':
    print(f'Result {a+b}')
elif operation =='-':
    print(f'Result {a-b}')
elif operation =="/":
    print(f"Result: {a/b if b != 0 else 'Cannot divide by zero'}")
elif operation =='*':
    print(f'Result {a*b}')
else:
    print("Invalid operation")