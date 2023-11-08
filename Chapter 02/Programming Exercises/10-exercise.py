#Stock transaction program

#Purchase Section
No_of_shares_purchased = 1000
price_of_one_share = 32.98
Total_amount = No_of_shares_purchased * price_of_one_share
commission_paid = Total_amount * 0.02

#Sale section
No_of_shares_sold = 1000
price_of_onee_share = 33.92             #different varible from price_of_one_share
Total_amountt = No_of_shares_sold * price_of_onee_share     #different variable from Total_amount
commission_paidd = Total_amount * 0.02           #different variable from commision_paid
Amount_of_money_left = Total_amountt - (commission_paid + commission_paidd)

#For outputs
print('The total amount paid for stocks is {}'.format(Total_amount))
print('The commission paid to broker when bought the stock is {}'.format(commission_paid))
print('The total amount from selling stock is {}'.format(Total_amountt))
print('The commision paid to broker when sold the stock is {}'.format(commission_paidd))
print('The amount of money left is {}'.format(Amount_of_money_left))