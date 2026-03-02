init_min=int(input("Enter initial minutes:"))
while init_min>0:
    if init_min>120:
        status="Permit holder"
    else:
        status="Pay & Display"
    print(f"Meter loaded. Initial time:{init_min}")
    print(f"Status:{status}")
    choice=int(input("[1] Add time  [2] Advance clock  [3] Check time  [4] Exit\nYour choice:"))
    if choice==1:
        addtime=int(input("Enter the time amount:"))
        while addtime<=0:
            addtime=int(input("Invalid amount. Please enter a positive value:"))
        init_min=init_min+addtime
        print(f"{addtime}minutes added. Updated time:{init_min}.")
        continue
    elif choice==2:
        advtime=int(input("Minutes to advance:"))
        while advtime<=0:
            advtime=int(input("Invalid amount. Please enter a positive value:"))
        init_min=init_min-advtime
        print(f"Clock advanced{advtime}. Time remaining:{init_min}")
        continue
    elif choice==3:
        print(f"Time remaining:{init_min}")
        continue
    else:
        break