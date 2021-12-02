#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 04
import sys

def process(actions):
    distance = 0
    aim = 0
    depth = 0

    # Inner functions must declare use of outer variables
    def forward(amount):
        nonlocal distance, aim, depth
        distance += int(amount)
        depth += (aim * int(amount))
    def down(amount):
        nonlocal aim
        aim += int(amount)
    def up(amount):
        nonlocal aim
        aim -= int(amount)

    for action in actions:
        direction, amount = action.split(' ')
        # This is disgusting, I love it
        locals()[direction](amount)

    return {
        'distance': distance,
        'aim': aim,
        'depth': depth
    }

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    fp = open(filename)

    changes = process(list(map(str.strip, fp.readlines())))
    fp.close()
    print(changes)

if __name__ == '__main__':
    main()
