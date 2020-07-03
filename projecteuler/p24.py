"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import math


def getPerm(n=10 ** 6, a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    nn = n

    if len(a) == 0:
        return ''
    l = len(a)

    for num in a:
        print(num, l-1, math.factorial(l - 1), nn)
        if math.factorial(l - 1) >= nn:
            a.remove(num)
            print('Found digit: ', num, a, nn)
            return int(str(num) + str(getPerm(nn, a)))
        else:
            nn -= math.factorial(l - 1)


print(getPerm())
