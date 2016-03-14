def factor(x):
    'Returns prime factors of a integer'
    factors = []
    i = 2
    while(x >= i):
        if x % i == 0:
            x = x/i
            factors.append(i)
            i = 1
        i += 1

    return factors


def factorcount(x):
    'Returns number of factors'
    factors = []
    i = 2
    while(x >= i):
        if x % i == 0:
            k = 0
            while x % i == 0:
                x = x/i
                k += 1
            factors.append(k)
            # print(x, i, k)
        i += 1

    facn = 1

    for f in factors:
        facn *= (f + 1)

    return facn


def powsum(x, n):
    ret = 0
    for i in range(n):
        ret += x ** n
    return ret


def sumofdivisors(x):
    'Returns Sum of divisors'
    a = []
    i = 2
    while(x > i):
        if x % i == 0:
            k = 0
            xn = x
            while xn % i == 0:
                xn = xn/i
                k += 1
            a.append(i)
        i += 1

    ret = sum(a) + 1

    return ret


# print(sumofdivisors(220))

# // For problem # 12
# triangnum, i = 0, 1
# while True:
#     triangnum += i
#     i += 1
#     print(triangnum, factorcount(triangnum))
#     if factorcount(triangnum) >= 500:
#         print("found : ", triangnum)
#         break

# // for problem 21
am = []

for i in range(1, 10000):

    di = sumofdivisors(i)
    if sumofdivisors(di) == i:
        if i not in am and di not in am and i != di:
            am.append(i)
            am.append(di)
            print("amicable :", i)

print('\n Sum =', sum(am))
