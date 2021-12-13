#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 25
import sys

def process(content):
    # readlines has an analogue in string terms...
    points = [[int(p) for p in l.strip().split(',')] for l in content[0].splitlines()]
    folds = [0 if l.split(' ')[2].split('=')[0] == 'x' else 1 for l in content[1].splitlines()]
    dims = [max([p[0] for p in points]) + 1, max([p[1] for p in points]) + 1]
    for f in folds:
        dims[f] = int(dims[f] / 2)
        for p in range(len(points)):
            if points[p][f] > dims[f]:
                points[p][f] -= (points[p][f] - dims[f]) * 2
        break

    # We may's well use the deduping of sets
    return len(list(set([p[1] * dims[0] + p[0] for p in points])))

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.read().split("\n\n")))

if __name__ == '__main__':
    main()
