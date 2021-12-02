#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 03
import sys

def process(actions):
    totals = {}
    for action in actions:
        direction, amount = action.split(' ')

        # .has_key is deprecated, apparently...
        if direction in totals:
            totals[direction] += int(amount)
        else:
            totals[direction] = int(amount)
    return totals

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    fp = open(filename)

    changes = process(list(map(str.strip, fp.readlines())))
    fp.close()
    print(changes)

if __name__ == '__main__':
    main()
