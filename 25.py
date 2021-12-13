#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 25
import sys, re

def process(content):
    # readlines has an analogue in string terms...
    # This is apparently the syntax for transposing, too
    points = list(zip(*[[int(p) for p in l.strip().split(',')] for l in content[0].splitlines()]))
    folds = [0 if re.search(r'(\w)=', l).group(1) == 'x' else 1 for l in content[1].splitlines()]
    dims = [max(d) + 1 for d in points]
    for f in folds:
        dims[f] = int(dims[f] / 2)
        points[f] = [(2 * dims[f] - p) if p > dims[f] else p for p in points[f]]
        break

    # We may's well use the deduping of sets
    return len(set([p[1] * dims[0] + p[0] for p in zip(*points)]))

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.read().split("\n\n")))

if __name__ == '__main__':
    main()
