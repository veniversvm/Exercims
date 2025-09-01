def score(x, y):
    position = x ** 2 + y ** 2
    if position > 100:
        return 0
    if position > 25:
        return 1
    if position > 1:
        return 5
    return 10
    