#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 08
import sys, re

def process(lines):
    SIZE = 5
    draws = [int(x) for x in lines[0].split(',')]
    boards = [[]]
    board_index = 0
    boards_won = []

    def unmarked(board):
        return sum([v for v in board if v & 1024 == 0])

    # Read the boards first...
    for line in lines[2:]:
        cells = [int(x) for x in re.split('\s+', line.strip(' ')) if len(x)]
        if len(cells) > 0:
            boards[board_index] += cells
        else:
            board_index += 1
            boards.append([])

    # And now we can play Bingo
    for draw in draws:
        for i in range(0, len(boards)):
            boards[i] = [1024|x if x == draw else x for x in boards[i]]
            for y in range(0, SIZE):
                if (i not in boards_won and len([v for v in boards[i][y * SIZE : y * SIZE + SIZE] if v&1024]) == SIZE):
                    boards_won.append(i)
                if (i not in boards_won and len([v for v in boards[i][y : SIZE * SIZE : SIZE] if v&1024]) == SIZE):
                    boards_won.append(i)
        # It's not the last board left, it's the last board to win...
        if len(boards_won) == len(boards):
            return unmarked(boards[boards_won[-1]]) * draw

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
