#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 27
import sys
from collections import Counter

def process(content):
    polymer = content[0].strip()
    replaces = {pair: rep for pair, rep in [l.strip().split(' -> ') for l in content[2:]]}
    for gen in range(10):
        tpl = polymer
        polymer = ''
        for i in range(len(tpl) - 1):
            polymer += tpl[i]
            polymer += replaces[tpl[i:i+2]]
        polymer += tpl[-1]
    counts = [v for k, v in Counter(polymer).most_common()]
    return max(counts) - min(counts)

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
