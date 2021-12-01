#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 02
import sys

WINDOW_SIZE = 3

def window(depths, i):
    # Ranges are up to but not including the stop value
    return sum(depths[i:i + WINDOW_SIZE])

def process(depths):
    increases = 0
    decreases = 0

    a = 0
    # You'd think the last value would be 3 off the end for a sliding window
    # of size 3, but it's only 2 off the end
    for x in range(1, len(depths) - (WINDOW_SIZE - 1)):
        window_a = window(depths, a)
        window_x = window(depths, x)
        if window_a < window_x:
            increases += 1
        elif window_a > window_x:
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

    # If we map int over the lines before using them, that's cleaner
    changes = process(list(map(int, map(str.strip, fp.readlines()))))
    fp.close()
    print(changes)

if __name__ == '__main__':
    main()
