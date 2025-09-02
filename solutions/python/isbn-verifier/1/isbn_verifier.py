def is_valid(isbn):
    i = 1
    accumulate = 0
    reversed_isbn = isbn[::-1].replace("-", "")
    if len(reversed_isbn) != 10:
        return False
        
    for n in reversed_isbn:
        if n.isalpha() and not ((n == 'x' or n == 'X') and i == 1) :
            return False
        
        n = 10 if (n == 'x' or n == 'X') else n
        accumulate += (i * int(n))
        i +=1
        
    return accumulate % 11 == 0
