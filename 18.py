#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 18
import sys, math

SIZE = 100
# Because why slam this on the stack every time...
floor = []

def adj(x, y):
    global floor
    points = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
    return [p for p in points if p[0] >= 0 and p[0] < SIZE and p[1] >= 0 and p[1] < SIZE and floor[p[1]][p[0]] < 9]

def flood(l):
    points = [l[1] * SIZE + l[0]]
    npoints = 0
    while npoints < len(points):
        npoints = len(points)
        for p in points:
            # Lists don't have "merge and dedupe", but sets do
            points = list(set(points + [y * SIZE + x for x, y in adj(p % SIZE, int(p / SIZE))]))
    return points

def process(content):
    global floor
    floor = [list(map(int, list(l.strip()))) for l in content]
    basins = []
    for y in range(SIZE):
        for x in range(SIZE):
            p = floor[y][x]
            if len([a for a in adj(x, y) if floor[a[1]][a[0]] > p]) == len(adj(x, y)):
                basins.append(flood([x, y]))
    basins.sort(key=len)
    return math.prod([len(b) for b in basins[-3:]])

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
