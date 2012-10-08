n = 0
try:
    n = int(input("Give your n: "))
except:
    pass

s = 0
num = 0

for i in range(1, n+1):
    s += i**2
    num +=1

print(s, num)
