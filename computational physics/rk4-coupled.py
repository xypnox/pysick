def f(x, y, z):
    return z


def g(x, y, z):
    return x*z**2-y**2


xi = 0
yi = 1
zi = 0

h = 0.1

xf = 10

xs, ys, zs = [xi], [yi], [zi]

while xi < xf:
    k1 = f(xi, yi, zi)
    l1 = g(xi, yi, zi)
    k2 = f(xi+h/2, yi+h*k1/2, zi+h*l1/2)
    l2 = g(xi+h/2, yi+h*k1/2, zi+h*l1/2)
    k3 = f(xi+h/2, yi+h*k2/2, zi+h*l2/2)
    l3 = g(xi+h/2, yi+h*k2/2, zi+h*l2/2)
    k4 = f(xi+h, yi+h*k3, zi+h*l3)
    l4 = g(xi+h, yi+h*k3, zi+h*l3)

    xi += h
    yi += h/6*(k1 + 2*k2 + 2*k3 + k4)
    zi += h/6*(l1 + 2*l2 + 2*l3 + l4)

    xs.append(xi)
    ys.append(yi)
    zs.append(zi)

print(xs, ys, zs)
