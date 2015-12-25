primes = []


def is_prime(x):
    a = 1

    for i in primes:
        if x % i == 0:
            a = 0
            break
        if i > int(x ** 0.5):
            break

    if a == 1:
        primes.append(x)

    return a

# this loop simply runs the fxn to add newer primes
for i in range(2, 775122):
    is_prime(i)

# the output loop
for i in range(len(primes)):
    if 600851475143 % i == 0:
        pass

# additional endline
print()
