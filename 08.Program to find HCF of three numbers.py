import math
# PRogram to find HCF of three numbers
num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number : "))
num3 = int(input("enter your third number : "))

def gcd_three_numbers(a,b,c):
    return math.gcd(math.gcd(a,b),c)
#CAlculate HCF (GCD)
hcf = gcd_three_numbers(num1,num2,num3)
print(f'THE HCF OF {num1} , {num2} and {num3} is :{hcf}')