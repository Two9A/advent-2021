#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Stars 33/34
import sys, re

def process(content):
    # So this is how you add tuples
    def addtuples(a, b): return tuple(map(sum, zip(a, b)))
    # findall returns a list of tuples
    minx, maxx, miny, maxy = map(int, re.findall(r'x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', content)[0])
    hits = 0; biggest_y = miny
    for x in range(1, maxx * 3):
        for y in range(-(maxy - miny) * 3, (maxy - miny) * 3):
            top = miny
            p = (0,0); v = (x,y)
            while p[0] < maxx and p[1] > miny:
                p = addtuples(p, v)
                v = addtuples(v, (-1 if v[0] > 0 else 0, -1))
                top = max(top, p[1])
                # A between operator, nice
                if minx <= p[0] <= maxx and miny <= p[1] <= maxy:
                    hits += 1
                    biggest_y = max(biggest_y, top)
                    break
    return [biggest_y, hits]

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()[0].strip()))

if __name__ == '__main__':
    main()
