#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 19
import sys

def process(content):
    ends = {']': '[', ')': '(', '}': '{', '>': '<'}
    errors = []
    for line in [l.strip() for l in content]:
        blocks = []
        for char in line:
            if char in ends.values():
                blocks.append(char)
            elif char in ends.keys():
                if blocks[-1] == ends[char]:
                    blocks.pop()
                else:
                    errors.append(char)
                    break
    return sum([{')': 3, ']': 57, '}': 1197, '>': 25137}[e] for e in errors])

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
