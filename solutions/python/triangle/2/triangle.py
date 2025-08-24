def equilateral(sides):
    set_side = set(sides)
    return len(set_side) == 1 and 0 not in set_side


def isosceles(sides):
    set_side = set(sides)
    return len(set_side) < 3 and (0 not in set_side and 1 not in set_side)


def scalene(sides):
    set_side = set(sides)
    if len(set_side) != 3:
        return False
    side_a, side_b, side_c = sides
    return side_a + side_b > side_c and side_b + side_c > side_a and side_c + side_a > side_b 
