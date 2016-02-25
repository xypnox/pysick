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

for i in range(2, 100000):
    is_prime(i)

print(primes[-1])

maxcounter = 0
result = []

for a in range(-1000, 1000):
    for b in range(1, 1000, 2):
        counter = 0
        for i in range(1000):
            val = i ** 2 + a * i + b
            counter += 1
            if val not in primes:
                break
            else:
                xval = val
        if counter > maxcounter:
            print([a, b], counter)
            maxcounter = counter
            result.append([a, b])

print(result)
