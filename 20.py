#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 20
import sys
from statistics import median

def process(content):
    ends = {']': '[', ')': '(', '}': '{', '>': '<'}
    scores = []
    for line in [l.strip() for l in content]:
        blocks = []
        err = False
        for char in line:
            if char in ends.values():
                blocks.append(char)
            elif char in ends.keys():
                if blocks[-1] == ends[char]:
                    blocks.pop()
                else:
                    err = True
                    break
        if not err:
            score = 0
            # Reverse happens in-place, and doesn't return
            blocks.reverse()
            for b in blocks:
                score *= 5
                score += {'(': 1, '[': 2, '{': 3, '<': 4}[b]
            scores.append(score)
    return median(scores)

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
