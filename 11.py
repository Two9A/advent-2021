#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 11
import sys

def process(content):
    ages = [int(v) for v in content[0].split(',')]
    for day in range(0, 80):
        for i in range(0, len(ages)):
            ages[i] -= 1
            if ages[i] == -1:
                ages[i] = 6
                ages.append(8)
    return len(ages)

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
