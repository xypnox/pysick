def linearSolver(params):
    # params -> array with a, b, c, p, q, r
    # result ->
    #   0 -> no solution
    #   1 -> infinite solutions
    #   [x, y] -> single solution
    a, b, c, p, q, r = params

    if a/p != b/q:
        y = (c*p-a*r)/(b*p-a*q)
        x = c/a - b/a*y
        return [x, y]
    elif a/p == c/r:
        return 1
    else:
        return 0


params = [int(x) for x in str(
    input("Enter parameters a, b, c, p, q, r seperated by commas:\n")
).split(',')]

print(params)
print(linearSolver(params))
