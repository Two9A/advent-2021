#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 31
import sys

TYPE_LITERAL = 4

def readbits(stream, pos, num):
    out = 0
    while num > 0:
        idx = pos // 8
        bitidx = 8 - (pos & 7)
        nbits = 8 if (bitidx == 8 and num >= 8) else bitidx if num > bitidx else num
        out <<= nbits
        out += (stream[idx] & ((1 << bitidx) - 1)) >> (bitidx - nbits)
        pos += bitidx
        num -= bitidx
    return out

sumver = 0
def parse(stream, pos):
    global sumver
    origpos = pos
    ver = readbits(stream, pos, 3); pos += 3
    sumver += ver
    typ = readbits(stream, pos, 3); pos += 3
    if (typ == TYPE_LITERAL):
        literal = 0
        done = False
        while not done:
            l = readbits(stream, pos, 5); pos += 5
            done = (l & 16) == 0
            literal <<= 4
            literal += (l & 15)
        return {"type": "literal", "version": ver, "value": literal, "len": pos - origpos}
    else:
        ltyp = readbits(stream, pos, 1); pos += 1
        if ltyp:
            npack = readbits(stream, pos, 11); pos += 11
            literals = []
            for i in range(0, npack):
                p = parse(stream, pos); pos += p['len']
                literals.append(p)
        else:
            lenpack = readbits(stream, pos, 15); pos += 15
            literals = []
            prepos = pos
            while pos < (prepos + lenpack):
                p = parse(stream, pos); pos += p['len']
                literals.append(p)
        return {"type": "op", "version": ver, "operator": typ, "literals": literals, "len": pos - origpos}

def process(content):
    stream = [int(content[i: i+2], 16) for i in range(0, len(content), 2)]
    parse(stream, 0)
    return sumver
    
def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()[0].strip()))

if __name__ == '__main__':
    main()
