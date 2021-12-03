#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 05
import sys

def process(v):
    values = [int(x, 2) for x in v]
    gamma = 0
    for i in range(0, 12):
        # Python doesn't have ternaries? Come now
        gamma += (1 if (sum([x >> i & 1 for x in values]) > (len(values) / 2)) else 0) << i
    return gamma * (4095 - gamma)

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    fp = open(filename)

    changes = process(list(map(str.strip, fp.readlines())))
    fp.close()
    print(changes)

if __name__ == '__main__':
    main()
