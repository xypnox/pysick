def f(x, y, z):
    return -x-y*z


def g(x, y, z):
    return -y-z*x


xi = 0
yi = 0
zi = 1

h = 0.1

xf = 10

xs, ys, zs = [xi], [yi], [zi]

while xi < xf:
    k1 = h*f(xi, yi, zi)
    l1 = h*g(xi, yi, zi)
    k2 = h*f(xi+h, yi+k1, zi+l1)
    l2 = h*g(xi+h, yi+k1, zi+l1)

    xi += h
    yi += 1/2*(k1 + k2)
    zi += 1/2*(l1 + l2)

    xs.append(xi)
    ys.append(yi)
    zs.append(zi)

print(xs, ys, zs)
