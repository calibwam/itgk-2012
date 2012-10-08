from math import sqrt

def create_vector(a, b, c):
    return [a,b,c]

def print_vector(vec1):
    print("[%d %d %d]" % tuple(vec1))

def multiply_vector(vec1, c):
    return [x*c for x in vec1]

def vector_length(vec1):
    total = 0
    for x in vec1:
        total += x**2
    return sqrt(total)

def dot_product(vec1, vec2):
    total = 0
    for i in range(3):
        total += vec1[i]*vec2[i]
    return total

