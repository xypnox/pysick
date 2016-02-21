j, ans = 0, 0
for x in range(2, 1000000):
    i = 0
    q = x
    print(x)
    while q != 1:
        if q % 2 == 0:
            q = q / 2
        else:
            q = 3 * q + 1
        i += 1
    if i > j:
        j, ans = i, x

print("ans = ", ans, i)
