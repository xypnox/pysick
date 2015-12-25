# our prime list is empty here
primes = []


def is_prime(x):
    # fxn to check prime

    # we assume no. to be prime
    a = 1

    # a loop to check divisibility with already known primes
    for i in primes:
        # if the num is divisible by prime known already
        # the condition turns 0 and it breaks the loop
        if x % i == 0:
            a = 0
            break
        # also breaks the loop if primes become greater than
        # sqrt of that num
        if i > int(x ** 0.5):
            break

    # if we do find a prime we add it to our collection
    if a == 1:
        primes.append(x)

    return a

# this loop simply runs the fxn to add newer primes
for i in range(2, 10000):
    is_prime(i)
    print("p>", i)

k = 0

for i in range(10000):
    if i not in primes:
        if i % 2 == 1:
            print(i)
            num = 0
            for x in primes:
                if x < i:
                    num = x
                    for j in range(1, i):
                        num = num + 2 * (j ** 2)
                        if num == i:
                            k = 0
                            break
                        else:
                            k = 1
                            num = x
                else:
                    break
            if k == 1:
                print("ans=>", i)
    if k == 1:
        break
