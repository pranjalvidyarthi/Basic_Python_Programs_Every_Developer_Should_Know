# Program to find sale price of an item with given cost and discount (%)
cost = float(input('Enter the cost of the item: '))
discount_percent = float(input('Enter discount percentage: '))

discount_amount = (cost*discount_percent)/100
#Calculate sale price
sale_price = cost - discount_amount

print('Sale Price: ' , sale_price)