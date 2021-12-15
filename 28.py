#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 28
import sys
from collections import Counter

def process(content):
    polymer = content[0].strip()
    replaces = {pair: [pair[0]+rep, rep+pair[1]] for pair, rep in [l.strip().split(' -> ') for l in content[2:]]}
    # I'm told this is how you do a merge...
    pairs = [i for l in [[k, v[0], v[1]] for k, v in list(replaces.items())] for i in l]
    polypairs = {p: 0 for p in pairs}
    chars = {c: 0 for c in [i for c in [[p[0], p[1]] for p in polypairs.keys()] for i in c]}
    for i in range(len(polymer) - 1):
        polypairs[polymer[i:i+2]] += 1
        chars[polymer[i]] += 1
    chars[polymer[-1]] += 1
    for gen in range(40):
        pairs = polypairs.copy()
        for pair, cnt in pairs.items():
            polypairs[pair] -= cnt;
            polypairs[replaces[pair][0]] += cnt;
            polypairs[replaces[pair][1]] += cnt;
            chars[pair[0]] -= cnt
            chars[pair[1]] -= cnt
            chars[replaces[pair][0][0]] += cnt;
            # Don't double-count the middle char
            chars[replaces[pair][1][0]] += cnt;
            chars[replaces[pair][1][1]] += cnt;
    return max(chars.values()) - min(chars.values())

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
