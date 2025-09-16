def sum_of_multiples(limit, multiples):
    multiples_calculated = [0]
    
    for e in multiples:
        x = [e*x for x in range(1, limit) if e*x < limit]
        multiples_calculated.extend(x)
        
    uniques = list(set(multiples_calculated))

    return sum(uniques)