# the game surface
surface = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

# co-ordinates for insertion
coords = [0, 0, 0, 0, 0, 0, 0]


def display():
    # display fxn
    print('  0   1   2   3   4   5   6')
    for i in range(0, 7):
        print('|', end=' ')
        for j in range(0, 7):
            print(surface[6 - i][j], end=' | ')
        print('\n')

display()
# counter for alternative moves
count = 0


def win():
    a = False
    for i in range(7):
        for j in range(4):
            if surface[i][j] == "X" or surface[i][j] == "O":
                if surface[i][j] == surface[i][j + 1] == surface[i][j + 2] == surface[i][j + 3]:
                    a = True
    for i in range(4):
        for j in range(7):
            if surface[i][j] == "X" or surface[i][j] == "O":
                if surface[i][j] == surface[i + 1][j] == surface[i + 2][j] == surface[i + 3][j]:
                    a = True
    for i in range(4):
        for j in range(4):
            if surface[i][j] == "X" or surface[i][j] == "O":
                if surface[i][j] == surface[i + 1][j + 1] == surface[i + 2][j + 2] == surface[i + 3][j + 3]:
                    a = True
    for i in range(4):
        for j in range(3, 7):
            if surface[i][j] == "X" or surface[i][j] == "O":
                if surface[i][j] == surface[i + 1][j - 1] == surface[i + 2][j - 2] == surface[i + 3][j - 3]:
                    a = True
    return a


def insert(x, count):
    # fxn for insertion
    if x < 7:
        if count % 2 == 0:
            surface[coords[x]][x] = 'X'
            coords[x] += 1
        else:
            surface[coords[x]][x] = 'O'
            coords[x] += 1
    else:
        print("Invalid Input")

while True:
    # sample input
    insert(int(input("Move :")), count)
    count += 1
    display()
    if win():
        print("Win")
        break
