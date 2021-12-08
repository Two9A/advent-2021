#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 15
import sys

def process(content):
    # I do enjoy the zip function
    signals, segs = zip(*[line.strip().split(' | ') for line in content])
    seglengths = [list(map(len, x.split(' '))) for x in segs]
    filtered = [[i for i in x if i in [2,3,4,7]] for x in seglengths]

    # And then a merge operator I don't quite understand...
    return len([y for x in filtered for y in x])

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
