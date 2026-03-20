def electricity_report(building_name,daily_kwh,high_kwh=150):
    total=0
    high_days=0
    change=[]
    for i in daily_kwh:
        total+=i
    avarage=total/len(daily_kwh)
    for n in daily_kwh:
        if n>high_kwh:
            high_days+=1
    for a in range(len(daily_kwh)-1):
        new=daily_kwh[a+1]-daily_kwh[a]
        change.append(new)
    print(f"Building     : {building_name}")
    print(f"Days         : {len(daily_kwh)}")
    print(f"Average      : {avarage}")
    print(f"Peak usage   : {max(daily_kwh)}")
    print(f"Lowest usage : {min(daily_kwh)}")
    print(f"High days    : {high_days}")
    print(f"Daily change : {change}")
electricity_report("University",[120,200,150,140,600],130)