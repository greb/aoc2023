import re
import itertools
import math

def parse(inp):
    lines = inp.splitlines()
    moves = lines[0]
    nodes = dict()
    for node in lines[2:]:
        start, left, right = re.match(r'(.+) = \((.+), (.+)\)', node).groups()
        nodes[start] = left, right
    return moves, nodes


def part1(nav):
    moves, nodes = nav

    node = 'AAA'
    for cnt, move in enumerate(itertools.cycle(moves)):
        if node == 'ZZZ':
            return cnt
        node = nodes[node][move == 'R']


def detect(node, moves, nodes):
    # Observation: Input is designed so that amount of steps from start to end
    # is the same amount as end returns to end. So we don't even need a
    # separate cycle detection. Very convinient.
    for cnt, move in enumerate(itertools.cycle(moves)):
        if node[2] == 'Z':
            return cnt
        node = nodes[node][move == 'R']


def part2(nav):
    moves, nodes = nav

    start_nodes = [n for n in nodes.keys() if n[2] == 'A']
    lengths = [detect(n, moves, nodes) for n in start_nodes]
    return math.lcm(*lengths)
