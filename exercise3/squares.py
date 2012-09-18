a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b**2 - 4*a*c

if d < 0:
    print("two complex roots")
elif d > 0:
    print("two real roots")
else:
    print("one real double root")
