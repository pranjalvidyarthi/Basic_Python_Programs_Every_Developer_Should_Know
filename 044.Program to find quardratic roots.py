# Program to find quardratic roots
a = int(input('Enter coefficent of x\u00B2:'))
b = int(input('Enter coefficent of x: '))
c = int(input("Enter c: "))
#calculation of d
d = (b**2)-4*a*c
if d<0:
    print('Roots are imagniary')
elif d>0:
    x1 = -b+(d**0.5)/2*a
    x2 = -b-(d**0.5)/2*a
    print("Roots are", x1, "and" , x2, "value of d is", d)
else:
    print("Error")