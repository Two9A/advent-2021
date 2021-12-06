#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 10
import sys

def process(content):
    SIZE = 1000
    routes = [v.replace(' -> ', ',') for v in content]
    board = {}
    for route in routes:
        x1, y1, x2, y2 = [float(v) for v in route.split(',')]
        xdiff = (x2 - x1) / float(max(abs(x2 - x1), abs(y2 - y1)))
        ydiff = (y2 - y1) / float(max(abs(x2 - x1), abs(y2 - y1)))
        x = x1
        y = y1
        while int(abs(x - x2)) or int(abs(y - y2)):
            px = int(x)
            py = int(y)
            if (py * SIZE + px) not in board:
                board[py * SIZE + px] = 0
            board[py * SIZE + px] += 1
            while int(x) == px and int(y) == py:
                x += xdiff
                y += ydiff

        px = int(x)
        py = int(y)
        if (py * SIZE + px) not in board:
            board[py * SIZE + px] = 0
        board[py * SIZE + px] += 1

    return len([x for x in board.values() if x > 1])

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
