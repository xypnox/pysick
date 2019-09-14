#!/bin/python3

import os
import sys


def timeConversion(s):
    time = s.split(':')
    if time[2][2:3] == 'PM':
        time[0] += 12
    time[2] = time[2][0:1]
    return ':'.join(time)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
