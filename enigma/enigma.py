import random
from os import system

# small letters
char = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# BIG Letters
Char = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# variables for key-making
keyvars = ['0', '1', '2', '3', '4', '5', '6']


class encrypt():
    """Encrypt class:
    This class
    """

    def __init__(self, str):
        self.string = str
        self.stringOrignal = str
        self.key = 0

    def keyGenerator(self, length):
        key = ""
        while length > 0:
            key += random.choice(keyvars)
            length -= 1
        return key

    def increase(self, counter=1):
        newstring = ""

        for letter in self.string:

            if letter in char:
                index = char.index(letter) + counter

                if index > 25:
                    index = index - 26

                letter = char[index]

            elif letter in Char:
                index = Char.index(letter) + counter

                if index > 25:
                    index = index - 26

                letter = Char[index]

            newstring += letter

        self.string = newstring

    def reverse(self):
        self.string = self.string[::-1]

    def reverseWord(self):
        newstring = ""

        for word in self.string.split(" "):
            newstring += word[::-1]
            newstring += " "

        self.string = newstring[:-1]

    def countReverse(self):
        newstring = ""

        for letter in self.string:

            if letter in char:
                letter = char[25 - char.index(letter)]

            elif letter in Char:
                letter = Char[25 - Char.index(letter)]

            newstring += letter

        self.string = newstring

    def execute(self, key):
        for letter in key:
            if letter == '0':
                self.increase()
            elif letter == '1':
                self.increase(-1)
            elif letter == '2':
                self.increase(2)
            elif letter == '3':
                self.increase(-2)
            elif letter == '4':
                self.reverse()
            elif letter == '5':
                self.reverseWord()
            elif letter == '6':
                self.countReverse()

    def encrypt(self):
        print("\nWanna a Personalized Key?")
        choice = input("yope/nope : ")

        if choice == "yope" or choice == "y" or choice == "yes":
            self.key = input("\nEnter that dizzle of a key : ")

        else:
            length = int(input("\nLength o' key you can put 'n ur brain: "))
            self.key = self.keyGenerator(length)

        self.execute(self.key)

        print("\n3ncrypt3d str!ng !z :", self.string)
        print("\nk3y 2 un10c|< !z :", self.key, '\n')


class decrypt(encrypt):
    """
    Decrypt Class :
    This class inherits from encrypt class and contains functions of same name
    So as to ease developement. It should be noted though that their
    functionality is completely opposite to the ones of encrypt class.
    """

    def increase(self, counter=1):
        newstring = ""

        for letter in self.string:

            if letter in char:
                index = char.index(letter) - counter
                if index > 25:
                    index = index - 26
                letter = char[index]

            elif letter in Char:
                index = Char.index(letter) - counter
                if index > 25:
                    index = index - 26
                letter = Char[index]

            newstring += letter

        self.string = newstring

    def decrypt(self):
        self.key = input("\nEnter that key you nearly forgot : ")[::-1]
        self.execute(self.key)
        print("\nd3crypt3d string !z :", self.string, '\n')


if __name__ == "__main__":
    system("clear")
    choice = input("\nWanna Encrypt or Decrypt : (e/d) : ")

    if choice == 'e':
        inst = encrypt(input("\nEnter Your String : "))
        inst.encrypt()

    elif choice == 'd':
        inst = decrypt(input("\nEnter Your String : "))
        inst.decrypt()
