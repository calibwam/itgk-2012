def fib_iter(n):
    fib = 0
    for i in range(n):
        fib+=i
    return fib

def fib_recur(n):
    if n < 2:
        return n
    return fib_recur(n-1)+fib_recur(n-2)
