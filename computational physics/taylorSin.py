PI = 3.14159265359


def factorial(x):
    if x == 0:
        return 1
    return factorial(x-1)*x


def taylorSin(x, n=10):
    return sum([(-1)**i/factorial(2*i+1)*x**(2*i+1) for i in range(0, n+1)])


def taylorSinRecur(x, n=10):
    # This function returns array of [ith term, sum till ith term]
    # The sum till ith term is the final value of sin
    i = n-1
    if i == 0:
        return [x, x]
    else:
        iMinusTerm, summation = taylorSinRecur(x, i)
        iTerm = iMinusTerm*(-(x)**2 / ((2*i)*(2*i+1)))
        return [iTerm, summation+iTerm]


print(taylorSin(PI/4))

print(taylorSin(float(input('Enter the value for x: '))))
print(taylorSinRecur(float(input('Enter the value for x: ')))[1])
