#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 06
import sys

def process(v, f):
    values = [int(x, 2) for x in v]
    for i in range(11, -1, -1):
        criterion = (1 if (sum([x >> i & 1 for x in values]) > (len(values) / 2)) else 0) << i
        # We need to account for the evenly-divided case...
        if len([x for x in values if (x & (1 << i)) == criterion]) == (len(values) / 2):
            if f:
                values = [x for x in values if (x & (1 << i)) > 0]
            else:
                values = [x for x in values if (x & (1 << i)) == 0]
        else:
            if f:
                values = [x for x in values if (x & (1 << i)) == criterion]
            else:
                values = [x for x in values if (x & (1 << i)) != criterion]
        if len(values) == 1:
            return values[0]

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        ox = process(fp.readlines(), True)
    with open(filename) as fp:
        co = process(fp.readlines(), False)
    print(ox * co)

if __name__ == '__main__':
    main()
