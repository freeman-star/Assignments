def delivery_report(raw_data,sla_str):
    answer={}
    joined="".join(raw_data.strip().split())
    splitted=joined.split("|")
    for entry in splitted:
        a=entry.split(":")
        for i in a:
            i.strip()
        a[-1]=float(a[-1])
        answer[a[0]]=a[-1]
    total=0
    for value in answer.values():
        total+=value
    avarage=round(total/len(answer),1)
    return total
print(delivery_report("DADASA : 12|ahasgdf:      34|bababa:34",12))