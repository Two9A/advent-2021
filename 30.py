#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 30
import sys

SIZE = 500
SQSIZE = 100

def adj(p):
    x = p % SIZE; y = int(p / SIZE)
    points = [[x,y-1], [x-1,y], [x+1,y], [x,y+1]]
    return set([p[1] * SIZE + p[0] for p in points if p[0] >= 0 and p[0] < SIZE and p[1] >= 0 and p[1] < SIZE])

def process(content):
    nodes = [int(p) for p in [i for r in [list(l.strip()) for l in content] for i in r]]
    def nodeval(p):
        nonlocal nodes
        y = p // SIZE; x = p % SIZE
        sy = y // SQSIZE; py = y % SQSIZE
        sx = x // SQSIZE; px = x % SQSIZE
        v = nodes[py * SQSIZE + px]
        v += sy; v += sx
        v = (v - 1) % 9 + 1
        return v

    totals = [-1 for i in range(SIZE * SIZE)]
    unvisited = set(range(1, SIZE * SIZE))
    cur = 0; totals[0] = 0
    while True:
        if len(unvisited) == 0:
            break
        for a in adj(cur):
            if totals[a] == -1 or totals[a] > totals[cur] + nodeval(a):
                totals[a] = totals[cur] + nodeval(a)
                unvisited.add(a)
        cur = unvisited.pop()
    return totals[-1]

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
