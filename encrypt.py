import random

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


class encrypt():
    def __init__(self, str):
        self.string = str
        self.stringOrignal = str
        self.key = 0

    def out(self):
        print(self.string)

    def keyGenerator(self, length):
        key = 0
        while length > 0:
            key = key*10 + random.randrange(6)
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

    def encrypt(self):
        print("Want a Personalized Key?")
        choice = input("yo/nope : ")
        if choice == "yope" or choice == "y" or choice == "yes":
            self.key = int(input("Enter that goddamn key : "))
        else:
            length = int(input("Enter length of random key : "))
            self.key = self.keyGenerator(length)
        print("Your key is ", self.key)
        key = self.key
        while key > 0:
            d = key % 10
            if d == 0:
                self.increase()
            elif d == 1:
                self.increase(-1)
            elif d == 2:
                self.increase(2)
            elif d == 3:
                self.increase(-2)
            elif d == 4:
                self.reverse()
            elif d == 5:
                self.reverseWord()
            key = key // 10
        print("The encrypted string is :", self.string)
        print("The key to unlock is :", self.key)


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
        self.key = int(input("Enter that goddamn key : "))
        self.key = int(repr(self.key)[::-1])
        print("Your key is ", self.key)
        key = self.key
        while key > 0:
            d = key % 10
            if d == 0:
                self.increase()
            elif d == 1:
                self.increase(-1)
            elif d == 2:
                self.increase(2)
            elif d == 3:
                self.increase(-2)
            elif d == 4:
                self.reverse()
            elif d == 5:
                self.reverseWord()
            key = key // 10
        print("The decrypted string is :", self.string)

if __name__ == "__main__":
    choice = input("Wanna Encrypt or Decrypt : (e/d) : ")
    if choice == 'e':
        inst = encrypt(input("Enter Your String : "))
        inst.encrypt()
    elif choice == 'd':
        inst = decrypt(input("Enter Your String : "))
        inst.decrypt()
