import math


def factors(x):
    if x == 1:
        return [1]
    fs = [1]
    for i in range(2, math.ceil(x**(1/2))):
        if x % i == 0:
            fs.append(int(i))
            fs.append(int(x/i))
    if math.ceil(x**(1/2))**2 == x:
        fs.append(int(x**(1/2)))
    fs.sort()
    return fs


for i in range(100):
    print(i, factors(i))
