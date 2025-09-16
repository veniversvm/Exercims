def sum_of_multiples(limit, multiples):
    multiples_calculated = [0]
    
    for e in multiples:
        if e == 0: continue
        x = [x for x in range(e, limit, e) if x < limit]
        multiples_calculated.extend(x)
        
    uniques = list(set(multiples_calculated))

    return sum(uniques)
