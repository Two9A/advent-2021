#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 13
import sys

def process(content):
    positions = [int(x) for x in content[0].split(',')]
    return min([
        sum([abs(x - target) for x in positions])
        for target in range(max(positions))
    ])

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
