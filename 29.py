#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 29
import sys

SIZE = 100

def adj(p):
    x = p % SIZE; y = int(p / SIZE)
    points = [[x,y-1], [x-1,y], [x+1,y], [x,y+1]]
    return set([p[1] * SIZE + p[0] for p in points if p[0] >= 0 and p[0] < SIZE and p[1] >= 0 and p[1] < SIZE])

def process(content):
    nodes = [int(p) for p in [i for r in [list(l.strip()) for l in content] for i in r]]
    totals = [SIZE * SIZE for i in range(SIZE * SIZE)]
    visited = set(range(SIZE * SIZE))
    cur = 0; totals[0] = 0
    while True:
        for a in adj(cur):
            if totals[a] > totals[cur] + nodes[a]:
                totals[a] = totals[cur] + nodes[a]
        if len(visited) == 0:
            break
        cur = visited.pop()
    return totals[-1]

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
