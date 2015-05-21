from __future__ import division
from random import random


def half_or_triple_plus_one(number):
    if number%2 == 0:
        return int(number/2)
    else:
        return int((3 * number) + 1)

def main_loop():
    number = int(100 + random() * (1000 - 100))
    points = []
    count = 0

    import pylab
    pylab.ion()       # Turn on interactive mode.

    while True:
        count += 1
        number = half_or_triple_plus_one(number)
        print count, number
        pylab.scatter([count], [number])
        pylab.draw()
        import time
        time.sleep(0.5)


if __name__ == "__main__":
    main_loop()