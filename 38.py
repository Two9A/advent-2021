#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 38
import sys, math
from collections import Counter

transforms = [
  lambda a: [ a[0],  a[1],  a[2]],
  lambda a: [ a[1],  a[2],  a[0]],
  lambda a: [ a[2],  a[0],  a[1]],
  lambda a: [-a[0],  a[2],  a[1]],
  lambda a: [ a[2],  a[1], -a[0]],
  lambda a: [ a[1], -a[0],  a[2]],
  lambda a: [ a[0],  a[2], -a[1]],
  lambda a: [ a[2], -a[1],  a[0]],
  lambda a: [-a[1],  a[0],  a[2]],
  lambda a: [ a[0], -a[2],  a[1]],
  lambda a: [-a[2],  a[1],  a[0]],
  lambda a: [ a[1],  a[0], -a[2]],
  lambda a: [-a[0], -a[1],  a[2]],
  lambda a: [-a[1],  a[2], -a[0]],
  lambda a: [ a[2], -a[0], -a[1]],
  lambda a: [-a[0],  a[1], -a[2]],
  lambda a: [ a[1], -a[2], -a[0]],
  lambda a: [-a[2], -a[0],  a[1]],
  lambda a: [ a[0], -a[1], -a[2]],
  lambda a: [-a[1], -a[2],  a[0]],
  lambda a: [-a[2],  a[0], -a[1]],
  lambda a: [-a[0], -a[2], -a[1]],
  lambda a: [-a[2], -a[1], -a[0]],
  lambda a: [-a[1], -a[0], -a[2]],
];

def vlen(a):
    return int(math.sqrt(sum([i * i for i in a])))

def dist(a, b):
    return vlen([abs(i - j) for i, j in zip(*[a, b])])

def pathdist(a, b):
    return str([i - j for i, j in zip(*[a, b])])

def manhattan(a, b):
    return str([abs(i - j) for i, j in zip(*[a, b])])

def distset(b):
    output = set()
    for i in b:
        for j in b:
            output.add(dist(i, j))
        output.remove(0)
    return output

def pathdistlist(a, b):
    output = list()
    for i in a:
        for j in b:
            output.append(pathdist(i, j))
    return output

def centroid(points):
    return [sum(p)//3 for p in list(zip(*points))]

def process(content):
    beacons = []
    manhattans = {}
    for scan in content:
        beacons.append([list(map(int, l.split(','))) for l in scan.splitlines()[1:]])
    transformed_beacons = {0: beacons[0].copy()}
    centroids = {0: [0, 0, 0]}

    while len(transformed_beacons) < len(beacons):
        print(transformed_beacons.keys())
        comparisons = transformed_beacons.copy().keys()
        for scan in range(1, len(beacons)):
            if scan in transformed_beacons.keys():
                continue
            eligible = False
            for compar in comparisons:
                fielddist = distset(transformed_beacons[compar])
                bdist = distset(beacons[scan])
                if len(bdist.intersection(fielddist)) >= 11:
                    # Line segments in common, so some points
                    tdistances = []
                    maxes = []
                    for tdx in range(0, len(transforms)):
                        tbeacons = [transforms[tdx](p) for p in beacons[scan]]
                        pd = Counter(pathdistlist(tbeacons, transformed_beacons[compar]))
                        maxes.append([tdx, max(pd.values())])
                    maxes.sort(key=(lambda a: a[1]))
                    if len(maxes) and len([m for m in maxes if m[1] >= 12]):
                        print(f"    {scan} vs {compar}: {[m for m in maxes if m[1] >= 12]}")
                        maxes = [m for m in maxes if m[1] == maxes[-1][1]]
                        # Enough points in common
                        tbeacons = [transforms[maxes[-1][0]](p) for p in beacons[scan]]
                        if not eligible:
                            transformed_beacons[scan] = tbeacons.copy()
                            eligible = True
                            pd = Counter(pathdistlist(tbeacons, transformed_beacons[compar]))
                            commondist = pd.most_common(1)[0][0]
                            centroids[scan] = [centroids[compar][i] + eval(commondist)[i] for i in range(3)]
                if eligible:
                    break

    for s in range(len(beacons)):
        for t in range(len(beacons)):
            manhattans[t * len(beacons) + s] = sum(eval(manhattan(centroids[s], centroids[t])))
    return max(manhattans.values())

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.read().split("\n\n")))

if __name__ == '__main__':
    main()
