def crop_report(input_path,output_path,target_threshold):
    count=0
    farm_avr=0
    filds={}
    on_target=[]
    for line in input_path:
        count+=1
        splitted=line.split("|")
        numbers=splitted[1:]
        name=splitted[:1]
        total=0
        num_count=0
        numbers=numbers[0].split(",")
        for number in numbers:
            num_count+=1
            total+=number
        avr=total/num_count
        farm_avr+=avr
        f_avr=farm_avr/count
        filds[name]=avr
        if avr>=target_threshold:
            on_target.append(name)
        keys=[]
        values=[]
        for key,value in filds:
            keys.append(key)
            values.append(value)
        c=0
        for v in values:
            c+=1
            if v==max(values):
                maxim=v
        maxim_name=keys[c-1]
        s=0
        for m in values:
            s+=1
            if m==min(values):
                minem=m
        minem_name=keys[s-1]
    with open(output_path,"w") as f:
        f.write({
        "fields": count,
        "farm_avg": float(f_avr),
        "best_field": f'{maxim_name} ({maxim})',
        "lowest_field": f"{minem_name} ({minem})",
        "on_target":  on_target,
        })
crop_report("crop.txt","report.txt",9)