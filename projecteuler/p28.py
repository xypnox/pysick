"""
Calculates sum of diagonal elements of square
formed by putting numbers in a spiral format

for square of side 5 we get

21  22  23  24  25
20  7   8   9   10
19  6   1   2   11
18  5   4   3   12
17  16  15  14  13
"""

print("Enter the Size of square")
N = int(input().strip())

sum_of_diagonals = 1
# c = 0
counter = 1
leverage = 1
prevel = 1

for i in range(3, N*N+1):
    if i - prevel > counter:
        sum_of_diagonals += i
        prevel = i
        leverage += 1
        # print(i, leverage)
    if leverage > 4:
        # print("counter = ", counter)
        counter += 2
        leverage = 1

print("Sum of diagonals is ", sum_of_diagonals)
