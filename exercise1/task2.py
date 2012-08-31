from math import factorial

def binomial(n, k):
    if n>k:
        return factorial(n) / factorial(k)*factorial(n-k)

numOfTwoPairs = binomial(13,2)*binomial(4,2)*binomial(4,2)*binomial(11,1)*binomial(4,1)
numOfHands = 2598960

probOfTwoPairs = numOfHands / numOfTwoPairs

print("The probability of two pairs is %g" % probOfTwoPairs)
