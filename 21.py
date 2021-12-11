#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 21
import sys, time
from os import system

SIZE = 10

def adj(p):
    x = p % SIZE; y = int(p / SIZE)
    points = [[x-1,y-1], [x,y-1], [x+1,y-1], [x-1,y], [x+1,y], [x-1,y+1], [x,y+1], [x+1,y+1]]
    return [p[1] * SIZE + p[0] for p in points if p[0] >= 0 and p[0] < SIZE and p[1] >= 0 and p[1] < SIZE]

def printboard(board):
    system('clear')
    for y in range(SIZE):
        print(''.join(list(map(str, board[y * SIZE: y * SIZE + 10]))))
    time.sleep(0.05)

def process(content):
    board = []
    for y in range(SIZE):
        line = content[y].strip()
        for x in range(SIZE):
            board.append(int(line[x]))
    printboard(board)

    total = 0
    for gen in range(100):
        board = [p + 1 for p in board]
        flashes = []
        while True:
            nflashes = len(flashes)
            for p in range(SIZE * SIZE):
                if board[p] >= 10 and p not in flashes:
                    flashes.append(p)
                    for a in adj(p):
                        board[a] = board[a] + 1
            if len(flashes) == nflashes:
                total += nflashes
                break
        board = [0 if p > 9 else p for p in board]
        printboard(board)
    return total

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
