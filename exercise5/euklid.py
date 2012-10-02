def gcd(a, b):
    while b:
        old_b = b
        b = a%b
        a = old_b

    return a

def reduce_fraction(a, b):
    div = gcd(a,b)
    return int(a/div) , int(b/div)
