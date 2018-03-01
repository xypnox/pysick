#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    div = 0
    n = int(input().strip())
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            div += i
    print(div)
