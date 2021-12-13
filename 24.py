#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 24
import sys
from collections import Counter

def process(content):
    nodenames = []
    nodeids = {}
    nodeid = 0
    for path in [x.strip() for x in content]:
        one, two = path.split('-')
        if one not in nodeids:
            nodeids[one] = nodeid
            nodeid += 1
            nodenames.append(one)
        if two not in nodeids:
            nodeids[two] = nodeid
            nodeid += 1
            nodenames.append(two)

    graph = {}
    for path in [x.strip() for x in content]:
        one, two = path.split('-')
        graph.setdefault(nodeids[one], []).append(nodeids[two])
        graph.setdefault(nodeids[two], []).append(nodeids[one])

    paths = []
    def walk(node, visited, singlev, doublev):
        nonlocal graph, paths
        visited.append(node)
        if node == nodeids['end']:
            paths.append(visited)
            return
        if nodenames[node].islower():
            singlev ^= (1 << node)
            if (singlev & (1 << node)) == 0:
                doublev |= (1 << node)
        for n in graph[node]:
            if nodenames[n].isupper() or (len(nodenames[n]) < 3 and doublev == 0) or ((singlev & (1 << n)) == 0 and (doublev & (1 << n)) == 0):
                walk(n, visited.copy(), singlev, doublev)
        paths.append(visited)
    walk(nodeids['start'], [], 0, 0)
    return len([p for p in paths if p[-1] == nodeids['end']])

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
