"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from math import ceil
import math

# from multiprocessing.dummy import Pool as ThreadPool


def get_factors(x):
    if x == 1:
        return 1
    fs = [1]
    for i in range(2, math.ceil(x**(1/2))):
        if x % i == 0:
            fs.append(int(i))
            fs.append(int(x/i))
    if math.ceil(x**(1/2))**2 == x:
        fs.append(int(x**(1/2)))
    fs.sort()
    return sum(fs)


def is_abundant(n):
    if get_factors(n) > n:
        return True
    return False


abundant = []

for n in range(1, 28123):
    if is_abundant(n):
        abundant.append(n)

# print(abundant)

add_perms = set([])

for i in abundant:
    for j in abundant:
        if i + j > 28123:
            break
        add_perms.add(i+j)

# print("Calculated Permuations")
# print(len(add_perms), add_perms)

sumX = 0
for n in range(1, 28123):
    if n not in add_perms:
        sumX += n

# # pool = ThreadPool(200)
# # results = pool.map(check, range(1, 28123))

print(sumX)
