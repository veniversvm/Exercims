def square_of_sum(number):
    square_n = 0
    for n in range(number+1):
        square_n += n
    return square_n ** 2
    


def sum_of_squares(number):
    sum_square = 0
    for n in range(number+1):
        sum_square += n ** 2
    return sum_square


def difference_of_squares(number):
    return abs(sum_of_squares(number) - square_of_sum(number))
