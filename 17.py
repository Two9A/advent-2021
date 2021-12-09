#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 17
import sys

SIZE = 100

def adj(x, y):
    points = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
    return [p for p in points if p[0] >= 0 and p[0] < SIZE and p[1] >= 0 and p[1] < SIZE]

def process(content):
    floor = [list(map(int, list(l.strip()))) for l in content]
    lows = []
    for y in range(SIZE):
        for x in range(SIZE):
            p = floor[y][x]
            if len([a for a in adj(x, y) if floor[a[1]][a[0]] > p]) == len(adj(x, y)):
                lows.append(p + 1)
    return sum(lows)

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
