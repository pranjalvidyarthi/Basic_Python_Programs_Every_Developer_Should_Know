# Find the Maximum of Three Numbers Without max()
a = int(input('enter first number: '))
b = int(input('enter second number: '))
c= int(input('enter third number: '))

if a>=b and a >=c:
    print('Maximum: ', a)
elif b >= a and b >= c:
    print(f'Maximum: {b}')
else:
    print(f'Maximum: {c}')