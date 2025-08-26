def is_armstrong_number(number):
    n_str = str(number)
    length = len(n_str)
    total = 0
    for element in n_str:
        total += int(element) ** length
    return number == total