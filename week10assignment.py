def delivery_report(raw_data, sla_str):
    cleaned = " ".join(raw_data.strip().split())
    orders_dict = {}
    entries = cleaned.split("|")
    for entry in entries:
        if ":" in entry: 
            order, hours = entry.split(":")
            orders_dict[order.strip()] = float(hours.strip())
    num_orders = len(orders_dict)
    total = sum(orders_dict.values())
    average = round(total/ num_orders, 1)
    fastest = None
    slowest = None
    min_time = float('inf')
    max_time = float('-inf')
    for order, hours in orders_dict.items():
        if hours < min_time:
            min_time = hours
            fastest= order
        if hours > max_time:
            max_time = hours
            slowest = order
    sla_target = float(sla_str)
    over_sla_count = 0
    for hours in orders_dict.values():
        if hours > sla_target:
            over_sla_count += 1
    ranking_tuples = []
    for order, hours in orders_dict.items():
        ranking_tuples.append((hours, order))    
    ranking_tuples.sort(reverse=True) 
    ranking = []
    for hours, order in ranking_tuples:
        ranking.append(f"{order} ({hours} hrs)")
    ranking_str = ", ".join(ranking)
    return {
        "orders": num_orders,
        "average": average,
        "fastest": fastest,
        "slowest": slowest,
        "over_24hrs": over_sla_count,
        "ranking": ranking_str
    }

