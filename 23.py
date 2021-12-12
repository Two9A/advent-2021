#!/usr/bin/env python3
# Advent of Code 2021, but I'm learning Python
# Star 23
import sys

def process(content):
    graph = {}
    for path in [x.strip() for x in content]:
        one, two = path.split('-')
        # Ooh, dict.setdefault is a useful thing
        graph.setdefault(one, []).append(two)
        graph.setdefault(two, []).append(one)

    paths = []
    # I freely admit to lifting this DFS from somewhere
    def walk(node, visited):
        nonlocal graph, paths
        visited.append(node)
        for neighbour in graph[node]:
            # And str.isupper/islower are things too
            if neighbour.isupper() or neighbour not in visited:
                walk(neighbour, visited.copy())
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
