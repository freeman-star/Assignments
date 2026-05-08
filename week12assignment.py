def run_tip_calculator():
    try:
        bill_amount=input("Enter bill amount in $ (or 'q' to quit): ")
        if bill_amount=="q":
            return print("Goodbye")
        float_bill=float(bill_amount)
        if float_bill<=0:
            raise ValueError("Bill amount must be greater than zero")
        tip_p=input("Enter tip percentage (e.g. 15 for 15%): ")
        tip_p=float(tip_p)
        if tip_p<0:
            raise ValueError("Tip percentage cannot be negative")
        diners=input("Enter number of diners: ")
        diners=int(diners)
        if diners <=0:
            raise ZeroDivisionError("Number of diners must be at least 1")
        tip=float_bill*tip_p/100
        total = float_bill + tip
        per_person = total / diners
        history=[]
    except ValueError as e:
        print(e)
        history.append(e)
    except ZeroDivisionError as z:
        print(z)
        history.append(z)
    else: 
        print(f"Tip: ${round(tip,2)} | Total: ${round(total,2)} | Per person: ${round(per_person,2)}")
        history.append("success")
    finally:
        print("---")
    return history
run_tip_calculator()