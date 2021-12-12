#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 24
import sys
from collections import Counter

def process(content):
    graph = {}
    for path in [x.strip() for x in content]:
        one, two = path.split('-')
        graph.setdefault(one, []).append(two)
        graph.setdefault(two, []).append(one)

    paths = []
    def walk(node, visited):
        nonlocal graph, paths
        visited.append(node)
        # Dictionary comprehensions, I should use those more
        overcounts = {n: c for n, c in Counter(visited).items() if n.islower() and len(n) < 3 and c >= 2}
        for n in graph[node]:
            if n.isupper() or (len(n) < 3 and len(overcounts.keys()) == 0) or n not in visited:
                walk(n, visited.copy())
        paths.append(visited)
    walk('start', [])
    return len([p for p in paths if p[-1] == 'end'])

def main():
    assert len(sys.argv) == 2, 'Filename not provided'
    filename = sys.argv[1]
    
    with open(filename) as fp:
        print(process(fp.readlines()))

if __name__ == '__main__':
    main()
