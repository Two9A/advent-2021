#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 16
import sys

def process(content):
    signals, segs = zip(*[line.strip().split(' | ') for line in content])
    # So you can't join a list, you have to call ''.join
    signals = [[''.join(sorted(i)) for i in x] for x in [l.split(' ') for l in signals]]
    segs = [[''.join(sorted(i)) for i in x] for x in [l.split(' ') for l in segs]]
    out = 0
    # Turns out there's no easy way to get the key on a for/in
    for idx in range(len(signals)):
        signal = signals[idx]
        mapping = {
            1: [i for i in signal if len(i) == 2][0],
            4: [i for i in signal if len(i) == 4][0],
            7: [i for i in signal if len(i) == 3][0],
            8: [i for i in signal if len(i) == 7][0]
        }
        # And you can't easily diff lists, but sets can be diff'd
        mapping[3] = [i for i in signal if len(i) == 5 and len(list(set(i) - set(mapping[7]))) == 2][0]
        mapping[2] = [i for i in signal if len(i) == 5 and len(list(set(i) - set(mapping[4]))) == 3][0]
        mapping[5] = [i for i in signal if len(i) == 5 and i not in [mapping[2], mapping[3]]][0]
        mapping[9] = [i for i in signal if len(i) == 6 and len(list(set(i) - set(mapping[3]))) == 1][0]
        mapping[6] = [i for i in signal if len(i) == 6 and len(list(set(i) - set(mapping[5]))) == 1 and i != mapping[9]][0]
        mapping[0] = [i for i in signal if i not in mapping.values()][0]
        mapping = {v:k for k,v in mapping.items()}

        out += int(''.join([str(mapping[i]) for i in segs[idx]]))
    return out

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
