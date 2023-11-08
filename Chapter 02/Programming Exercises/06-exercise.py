#Sales Tax

Amount_of_purchase = float(input("Enter the amount of purchase: "))
state_sales_tax = Amount_of_purchase * 0.04
country_sales_tax = Amount_of_purchase * 0.02
Total_sales_tax = state_sales_tax + country_sales_tax
Total_of_sale = Amount_of_purchase + Total_sales_tax

print('Amount of the purchase is {}'.format(Amount_of_purchase))
print('State sales tax is {}'.format(state_sales_tax))
print('Country sales tax is {}'.format(country_sales_tax))
print('Total Sales tax is {}'.format(Total_sales_tax))
print('Total of the sale is {}'.format(Total_of_sale))