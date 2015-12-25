nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gem = []


def dgt(x):
    c = 0
    while x > 0:
        c += 1
        x = x//10
    return c


def getdigits(k, w, u):
    l = []
    while k > 0:
        l.append(k % 10)
        k = k//10
    while w > 0:
        l.append(w % 10)
        k = w//10
    while u > 0:
        l.append(u % 10)
        k = u//10
    return l

for i in range(1000):
    for j in range(1000):
        num = i*j
        if dgt(i)+dgt(j)+dgt(num) == 9:
            f = sorted(getdigits(i, j, num))
            if f == nums:
                gem.append((i, j, num))
    print(i)

print(gem)
