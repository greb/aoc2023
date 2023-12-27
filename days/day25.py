import collections

from pprint import pprint

def parse(inp):
    graph = collections.defaultdict(set)
    for line in inp.splitlines():
        a, bs = line.split(': ')
        for b in bs.split(' '):
            graph[a].add(b)
            graph[b].add(a)
    return graph


def part1(graph):
    split = set(graph)
    count = lambda v: len(graph[v]-split)

    while sum(map(count, split)) != 3:
        split.remove(max(split, key=count))

    return len(split) * len(set(graph) - split)
