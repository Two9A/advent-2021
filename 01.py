#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 01
import sys

def process(depths):
    increases = 0
    decreases = 0

    # Sneaky string comparisons...
    a = int(depths[0])
    for x in depths[1:]:
        x = int(x)
        if a < x:
            increases += 1
        elif a > x:
            decreases += 1
        a = x
    return {
        'increases': increases,
        'decreases': decreases
    }

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    fp = open(filename)

    # A map isn't directly iterable...
    changes = process(list(map(str.strip, fp.readlines())))
    fp.close()
    print(changes)

if __name__ == '__main__':
    main()
