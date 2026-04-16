def water_usage_report(raw_data,threshold_str,delimiter):
    formatted="".join(raw_data.strip().split())
    data=formatted.split("|")
    name=data.pop(0)
    count=0
    float_data=[]
    for i in range(len(data)):
        float_data.append(float(data[i]))
        count+=1
    copy=float_data[::]
    copy.sort()
    best=copy[0]
    worst=copy[-1]
    threshold_str=float(threshold_str)
    above=0
    for a in float_data:
        if a>threshold_str:
            above+=1
    count=str(count)
    best=str(best)
    worst=str(worst)
    above=str(above)
    usage=delimiter.join(data)
    answer=f"Block: {name}\nCount: {count}\nBest: {best}\nWorst: {worst}\nOver {threshold_str}: {above}\nUsage: {usage}"
    return answer
