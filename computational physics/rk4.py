h = 0.1
x, y = [1], [5]


def f(x, y):
    return x*y


xn, yn = x[0], y[0]

while xn <= 2:
    k1 = f(xn, yn)
    k2 = f(xn+h/2, yn+k1/2)
    k3 = f(xn+h/2, yn+k2/2)
    k4 = f(xn+h, yn+k3)
    yn += h/6*(k1+2*k2+2*k3+k4)
    y.append(yn)
    xn += h
    x.append(xn)

print(x, y)

# for jio in range(1, 11):
#     with open("data"+jio+".dat", "a") as datafile:
#         for i in range(len(x)):
#             datafile.write(
#                 str(x[i])+" "+str(y[i])+"\n"
#             )
