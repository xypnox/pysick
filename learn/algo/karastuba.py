# func multiply(m, n)
#   if len(m) == 1 or len(n) == 1:
#   	return m * n
#   k = 2 * (max(len(m), len(n)) / 2 + 1 )
#   a = m / 10 ** k
#   b = m % 10 ** k
#   c = n / 10 ** k
#   d = n % 10 ** k
#   ac = multiply(a, c)
#   bd = multiply(b, d)
#   mid = multiply(a+b, c+d) - ac -bd
#   return ac * 10 ** k + mid * 10 ** k/2 + bd


def multiply(m, n):
    if len(str(m)) == 1 or len(str(n)) == 1:
        return m * n
    k = max(len(str(m)), len(str(n))) // 2
    a = m // 10**k
    b = m % 10**k
    c = n // 10**k
    d = n % 10**k

    print(a, b, c, d, k)
    ac = multiply(a, c)
    bd = multiply(b, d)

    mid = multiply(a+b, c+d) - ac - bd

    return ac * 10 ** (2*k) + mid * 10 ** k + bd


n1 = 3141592653589793238462643383279502884197169399375105820974944592
n2 = 2718281828459045235360287471352662497757247093699959574966967627

print(multiply(n1, n2))
print(n1 * n2)
