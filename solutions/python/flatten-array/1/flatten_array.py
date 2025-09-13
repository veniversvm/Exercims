

def flattern_function(iterable):
    for element in iterable:
        if isinstance(element, int):
            yield element
        if isinstance(element, list):
            yield from flatten(element)

def flatten(iterable):
    return list(flattern_function(iterable))

