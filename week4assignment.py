def restaurant_bill(food_total,service_quality,num_diners,has_voucher,voucher_percent=0):
    tip=0
    total_bill=food_total+tip
    if service_quality=="exelent":
        tip=0.15*food_total
    elif service_quality=="good":
        tip=0.10*food_total
    elif service_quality=="fair":
        tip=0.05*food_total
    elif service_quality=="none":
        tip=0*food_total
    if has_voucher==True:
        if voucher_percent>0:
            total_bill=total_bill*((100-voucher_percent)/100)
    if total_bill<0:
        total_bill=0
    per_person=round(total_bill/num_diners)
    return per_person
print(restaurant_bill(45000,"excellent",3,False))