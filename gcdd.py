def gccd(x, y):
    if x > y:
        x, y = y, x
    rem = y
    while rem >= 0:
        if rem > x:
            rem = rem - x
        elif rem < x:
            rem, x = x, rem
        else:
            return x

print(gccd(3426, 4563))
