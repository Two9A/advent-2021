#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 14
import sys

def process(content):
    positions = [int(x) for x in content[0].split(',')]

    def gauss(x):
        return (x * (x + 1)) / 2

    return min([
        sum([gauss(abs(x - target)) for x in positions])
        for target in range(max(positions))
    ])

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
