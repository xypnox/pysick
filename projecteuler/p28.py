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
