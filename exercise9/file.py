def number_of_lines(filename):
    f = open(filename, 'r')
    num = len(f.readlines()) 
    f.close()
    return num

def number_frequency(filename):
    f = open(filename, 'r')
    frequencies = {}
    for line in f:
        try:
            frequencies[int(line)] += 1
        except KeyError:
            frequencies[int(line)] = 1
    f.close()
    return frequencies

numbers = number_frequency('nummer.txt')

for i in sorted(numbers.keys()):
    print("%i: %i" % (i, numbers[i]))
