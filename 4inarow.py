# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This is the classic four in a row game by                                 #

#      █████  ██████  ██ ██    ██ ██   ████████ ██████   █████
#    ██   ██ ██   ██ ██ ██    ██ ██      ██    ██   ██ ██   ██
#   ███████ ██   ██ ██ ██    ██ ██      ██    ██████  ███████
#  ██   ██ ██   ██ ██ ██    ██ ██      ██    ██   ██ ██   ██
# ██   ██ ██████  ██  ██████  ███████ ██    ██   ██ ██   ██

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               TODO
#            [ ] Create AI
#            [ ] Document the project
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import time
from random import randint


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

# counter for alternative moves
count = 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                           The display fxn                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def display():
    """
    Display the Surface of
    """
    # display fxn
    print('  0   1   2   3   4   5   6')
    for i in range(0, 7):
        print('|', end=' ')
        for j in range(0, 7):
            print(surface[6 - i][j], end=' | ')
        print('\n')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                           The Win checking fxn                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def win():
    """
    Winning condition checking function

    This checks for rows coloumns and diagonals for
    similar value for winning
    """
    a = False

    # check row - win
    for i in range(7):
        for j in range(4):
            if surface[i][j] == "X" or surface[i][j] == "O":
                if surface[i][j] == surface[i][j + 1] == surface[i][j + 2] == surface[i][j + 3]:
                    a = True

    # check coloumn | win
    for i in range(4):
        for j in range(7):
            if surface[i][j] == "X" or surface[i][j] == "O":
                if surface[i][j] == surface[i + 1][j] == surface[i + 2][j] == surface[i + 3][j]:
                    a = True

    # check diagonal / win
    for i in range(4):
        for j in range(4):
            if surface[i][j] == "X" or surface[i][j] == "O":
                if surface[i][j] == surface[i + 1][j + 1] == surface[i + 2][j + 2] == surface[i + 3][j + 3]:
                    a = True

    # check diagonal \ win
    for i in range(4):
        for j in range(3, 7):
            if surface[i][j] == "X" or surface[i][j] == "O":
                if surface[i][j] == surface[i + 1][j - 1] == surface[i + 2][j - 2] == surface[i + 3][j - 3]:
                    a = True

    return a


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                              The low ai game                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def playai():
    """
    Low Artificial Inteligence function

    This simulates simple randomly selected moves so the player
    can feel easy to win
    """
    count = 0
    while True:
        coords = [0, 0, 0, 0, 0, 0, 0]
        display()

        if count % 2 == 0:
            a = int(input("Move :"))
            if -1 < a < 7:
                insert(a, count)
                count += 1

        inpt = 1
        while inpt:
            if count % 2 == 1:
                er = randint(0, 6)
                if coords[er] < 7:
                    insert(er, count)
                    inpt = 0
                    count += 1

        if a == 10:
            break

        if a == 11:
            surface = [
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ']
            ]
            coords = [0, 0, 0, 0, 0, 0, 0]

        if win():
            os.system("clear")
            if count % 2 == 0:
                print("Mr. Computer wins")
            else:
                print("Mr. Player wins")
            display()
            surface = [
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ']
            ]
            coords = [0, 0, 0, 0, 0, 0, 0]
            print("Restarting Game in 10 seconds")
            time.sleep(10)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                           The 2 player game                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def play2():
    count = 0
    coords = [0, 0, 0, 0, 0, 0, 0]
    while True:
        display()
        a = int(input("Move :"))

        if -1 < a < 7:
            insert(a, count)
            count += 1

        if a == 10:
            break

        if a == 11:
            surface = [
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ']
            ]
            coords = [0, 0, 0, 0, 0, 0, 0]

        if win():
            os.system("clear")
            if count % 2 == 0:
                print("Mr. O wins")
            else:
                print("Mr. X wins")
            display()
            surface = [
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ']
            ]
            coords = [0, 0, 0, 0, 0, 0, 0]
            print("Restarting Game in 10 seconds")
            time.sleep(10)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                            The Insert fxn                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


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


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                           The main game loop                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


while True:
    choice = int(input("Enter game mode : "))
    os.system("clear")
    if choice == 1:
        play2()
    elif choice == 2:
        playai()
    elif choice == 3:
        break
