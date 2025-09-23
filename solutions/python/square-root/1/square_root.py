"""
    To be honest, I saw this solution a few months ago in the Tour of Go: 
    https://go.dev/tour/flowcontrol/8
"""
def square_root(number):
    if number <= 0:
        return ValueError("sqrt input should be non-negative")
    z = 1
    i = 10
    while i > 0: 
        z -= (z*z - number) / (2*z)
        i -= 1
    return int(z)
    
