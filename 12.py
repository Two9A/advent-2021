#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 12
import sys

def process(content):
    # Yep, the brute-force algorithm isn't going to work
    ages = [0,0,0,0,0,0,0,0,0]
    for i in [int(v) for v in content[0].split(',')]:
        ages[i] += 1
    for day in range(0, 256):
        ages = ages[1:] + [ages[0]]
        ages[-3] += ages[-1]
    return sum(ages)

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
