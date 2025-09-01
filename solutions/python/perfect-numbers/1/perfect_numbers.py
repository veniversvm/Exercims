def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
        
    divisors = [1]
    i = 2
    
    while number > i:
        if number % i == 0:
            divisors.append(i)
        i += 1
        

    aliquot = sum(divisors)
    if aliquot == number:
        return "perfect"
    if number < aliquot:
        return "abundant"
    return "deficient"
