#Total Purchase

item1 = int(input("Enter price for item1: "))
item2 = int(input("Enter price for item2: "))
item3 = int(input("Enter price for item3: "))
item4 = int(input("Enter price for item4: "))
item5 = int(input("Enter price for item5: "))

Sub_Total = item1 + item2 + item3 + item4 + item5
sales_tax = Sub_Total * 0.06

Total = Sub_Total + sales_tax
print("Total amount is {}".format(Total))