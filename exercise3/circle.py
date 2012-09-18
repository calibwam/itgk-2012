from math import pi,sqrt

def circle(radi):
    print("Area: %.2f" % (pi * radi * radi))
    print("Circumference: %.2f" % (2 * pi * radi))

circle(1)

def inverseCircle(area, circumference):
    if circumference > 0:
        print("Radi: %.2f" % (circumference/(2*pi)))
    else:
        print("Radi: %.2f" % (sqrt(area/pi)))

inverseCircle(3,0)
inverseCircle(3,3)
