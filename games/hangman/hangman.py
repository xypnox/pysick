from time import sleep
import os
from random import choice, seed

# import the hangman ascii model and dictionary
import data

# a seed for random.choice
seed()


def start():
    """
    Startup display function: slowly displays the hangman
    """
    for figure in data.hangman:
        os.system('clear')
        print(figure)
        sleep(0.4)

    os.system('clear')


def display(condition, letters, tletters):
    """
    Display fxn: displays the game UI
    """
    os.system('clear')

    print(data.hangman[5-condition])

    print('The clues are = ', end='\t')
    for l in letters:
        print(l, end='  ')

    print('\n')

    print('Tried letters = ', end='\t')
    for k in tletters:
        print(k, end='  ')

    print('\n')

    print("Chances Remaining = ", condition+1)

    print('\n')


def addletter(word, array, letter):
    i = 0

    for ltr in word:

        if ltr == letter:
            array[i] = letter

        i += 1


def compare(array, word):
    cond = False

    for i in range(len(word)):

        if array[i] == word[i]:
            cond = True

        else:
            cond = False
            break

    return cond


def play():
    randomword = choice(data.dictionary)
    knownletters = []
    triedletters = []
    win = False

    for l in randomword:
        knownletters.append('_')

    condition = 5

    while condition >= 0:
        display(condition, knownletters, triedletters)
        guess = input("Enter letter guess : ").lower()

        if guess in randomword:
            addletter(randomword, knownletters, guess)

            if compare(knownletters, randomword):
                win = True
                break

        else:
            triedletters.append(guess)
            condition -= 1

    if win:
        print("\nYou won, Word is", randomword)

    else:
        print('\nYou lost, The correct word is', randomword)


if __name__ == "__main__":
    start()
    while True:
        play()
        c = input("\nWanna play again: y/n :")
        if c == 'n' or c == 'no':
            exit()
