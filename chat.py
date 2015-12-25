import random


class vocab:
    """Creates Vocabulary for the chat-bot"""
    def __init__(self):
        self.happy = []
        self.greet = []
        self.sad = []
        self.fstP = []
        self.secP = []
        self.otrP = []


def extract(x):
    wdlist = []
    x += " "
    wd = ''
    for i in range(len(x)):
        if x[i] != ' ':
            wd += x[i]
        else:
            wdlist.append(wd)
            wd = ''
    return wdlist


def richc(x, voc):
    """Rich Compare :
    This function comares a list with the Vocabulary and hence returns
    The amount of words used in the list that are in the array
    """
    ret = [0, 0, 0, 0, 0]
    for word in x:
        if word in voc.happy:
            ret[0] += 1
        elif word in voc.sad:
            ret[1] += 1
        elif word in voc.fstP:
            ret[2] += 1
        elif word in voc.secP:
            ret[3] += 1
        elif word in voc.otrP:
            ret[4] += 1
    return ret

simple = vocab()

simple.happy = ["Amaze", "Delight"]
simple.sad = ["Damn", "No", "Never", "Yucks"]
simple.greet = ["Hi", "Hello", "Yo", "What's Up", "Hey"]
simple.fstP = [""]
print(random.choice(simple.greet))
print(richc(extract("So happy i am Yo No Yucks"), simple))
