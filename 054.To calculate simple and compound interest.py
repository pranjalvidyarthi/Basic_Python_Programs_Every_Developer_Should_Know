# To claculate simple and compound interest
p = int(input("Enter Principal Amount: "))
r = int(input('Enter rate (in %): '))
t = int(input('Enter time (in years) : '))
n = int(input('Enter no. of times interest applied: '))
#calculate simple interest
si = (p*r*t)/100
total_amt = p +si
#Display
print(F'Simple Interest: {si}')
print(f'Total Amount: {total_amt}')

#Compound interest
ci = p*((1 + (r/100)/n)**(n*t))
# Calculate total amount
t_a = ci
#display
print(f'Compound Interest : {ci}')
print(F'Total Amount: {t_a}')