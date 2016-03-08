import os
from time import time
primes = []

os.system('rm primes.txt')
os.system('touch primes.txt')

f = open('primes.txt', 'r+')


def is_prime(x):
    # fxn to check prime

    # we assume no. to be prime
    a = True

    # a loop to check divisibility with already known primes
    for i in primes:
        # if the num is divisible by prime known already
        # the condition turns False and it breaks the loop
        if x % i == 0:
            a = False
            break
        # also breaks the loop if primes become greater than
        # sqrt of that num
        if i > int(x ** 0.5):
            break

    # if we do find a prime we add it to our collection
    if a:
        primes.append(x)

    return a

# this loop simply runs the fxn to add newer primes
t = time()
for i in range(2, int(input('Till where primes =] '))):
    is_prime(i)
t = time() - t
t = (t//0.001)/10000
print('\nPrimes found in', t, 's, Writing')

# the write loop
for i in range(len(primes)):
    f.write(str(primes[i])+'\n')


print('\nWritten\n')
