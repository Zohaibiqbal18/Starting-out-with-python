#Tip, Tax and Total

charge_for_food = int(input('Enter the charge of food: '))
tip = charge_for_food * 0.15
sales_tax = charge_for_food * 0.07
Total_amount = charge_for_food + tip + sales_tax


print('The charge for food is {}'.format(charge_for_food))
print('The tip is {}'.format(tip))
print('The sales tax is {}'.format(sales_tax))
print('The total amount is {}'.format(Total_amount))