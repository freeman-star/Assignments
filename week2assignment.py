oil=input("Do you need oil change?(for 160$):")
oil_change=(oil=="yes")
oil_price=oil_change and 160 
wash=input("Do you need washing service?(for 110$):")
wash_service=(wash=="yes")
wash_price=wash_service and 110
premium=input("Is it your first time using our workshop?")
premium_answer=(premium=="yes")
before_dis=oil_price+wash_price
dis=(before_dis>250)
dis_0=(before_dis<=250)
discount=before_dis*0.08
dis_amount=dis*discount
premium_amount=premium_answer*before_dis*0.11
total=before_dis-dis_amount+premium_amount
print(f"Total amount you should pay is :{total}\nDiscount amount:{dis_amount}\nFirst time user fee amount:{premium_amount}")