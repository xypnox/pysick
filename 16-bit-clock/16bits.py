from datetime import datetime
import time
import os
import sys


def printer(d):
    """
    used for output of clock
    """
    if d == 0:
        print(" .  .  .  .")
    elif d == 1:
        print(" .  .  .  o")
    elif d == 2:
        print(" .  .  o  .")
    elif d == 3:
        print(" .  .  o  o")
    elif d == 4:
        print(" .  o  .  .")
    elif d == 5:
        print(" .  o  .  o")
    elif d == 6:
        print(" .  o  o  .")
    elif d == 7:
        print(" .  o  o  o")
    elif d == 8:
        print(" o  .  .  .")
    elif d == 9:
        print(" o  .  .  o")
    elif d == 10:
        print(" o  .  o  .")
    elif d == 11:
        print(" o  .  o  o")
    elif d == 12:
        print(" o  o  .  .")
    elif d == 13:
        print(" o  o  .  o")
    elif d == 14:
        print(" o  o  o  .")
    elif d == 15:
        print(" o  o  o  o")


def bit_clock(condition=True):
    """
    Display a fancy clock with o and .
    """

    while condition:

        now = datetime.now()

        seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0,
                                  microsecond=0)).total_seconds()
        bit_seconds = int(round(seconds_since_midnight*2**16/86400))

        print("The 16-bit clock")
        print("BitSeconds now : ", bit_seconds)
        bit_list = []

        while bit_seconds > 0:
            d = bit_seconds % 16
            bit_list.append(d)
            printer(d)
            bit_seconds //= 16

        print()
        print("Time is :", bit_list)

        if condition is True:
            time.sleep(1.318359375)
            os.system("clear")

        if condition is not True:
            condition -= 1


def time_bit():
    """
    Return the time_list containg bit sections of current bit_seconds
    """

    now = datetime.now()

    seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0,
                              microsecond=0)).total_seconds()
    bit_seconds = int(round(seconds_since_midnight*2**16/86400))

    bit_list = []

    while bit_seconds > 0:
        d = bit_seconds % 16
        bit_list.append(d)
        bit_seconds //= 16

    return bit_list

if __name__ == "__main__":

    for arg in sys.argv[1:]:

        if arg == "time" or arg == "-t":
            print(time_bit())

        elif arg == "clock" or arg == "-c":
            bit_clock()

        elif arg == "clock-face" or arg == "-cf":
            bit_clock(1)

        elif arg == "help" or arg == "-h":
            print()
            print("16Bit Clock - Version 0.02 - alpha")
            print("This is 16 bit clock which divides the day in",
                  "2 ^ 16 \"bitseconds\"")
            print("The first bit is smallest and the last the largest")
            print("Each bitsecond is equal to 86400/2**16 real seconds")
            print("i.e. 1 bit second = ", 86400/2**16)
            print()
            print()
            print("Usage : ")
            print()
            print("python3 16bits.py time <or -t>")
            print("\t This prints the bit time in a python list")
            print()
            print("python3 16bits.py clock <or -c>")
            print("\t Prints the clock that shows bitseconds, updates itself!")
            print()
            print("python3 16bits.py help <or -h>")
            print("\t prints the help")
            print()
            print()
            print("Inspired by : https://github.com/lucasdnd/16-bit-clock/")
            print("Licensed under GNU GPL v3 found at :",
                  "http://www.gnu.org/licenses/gpl-3.0.en.html")
            print()
            print("By the way the time is : ", time_bit())

        else:
            bit_clock()
