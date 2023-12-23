import collections

def parse(inp):
    lines = inp.splitlines()
    tiles = dict()
    for y, row in enumerate(lines):
        for x, ch in enumerate(row):
            if ch != '#':
                tiles[(x, y)] = ch

    w, h = len(lines[0]), len(lines)
    return w, h, tiles


slopes = {'^': (0,-1), '>': (1,0), '<': (-1,0), 'v': (0,1)}

def move(pos, delta):
    return tuple(p+d for p,d in zip(pos, delta))


def find_neighbors(tiles, part2):
    neighbors = dict()
    for pos in tiles:
        if part2 or tiles[pos] == '.':
            ns = []
            for delta in slopes.values():
                n_pos = move(pos, delta)
                if n_pos in tiles:
                    ns.append(n_pos)
            neighbors[pos] = set(ns)
        elif delta := slopes.get(tiles[pos]):
            neighbors[pos] = set([move(pos, delta)])
    return neighbors


def solve(grid, part2=False):
    w, h, tiles = grid
    neighbors = find_neighbors(tiles, part2)
    start = (1,0)
    end = (w-2, h-1)

    # Longest path problems are really expensive to calculate (apparently
    # it's NP-complete). So, we have to reduce the size of the search space as
    # much as possible. Luckily the maze can be split into segments between
    # path junctions.
    segments = collections.defaultdict(list)
    stack = [(start, None)]
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        pos, seg = node
        prev, dist = seg, 0 if pos == start else 1
        ns = [n for n in neighbors[pos] if n != prev]
        while len(ns) == 1:
            pos, prev = ns[0], pos
            dist += 1
            ns = [n for n in neighbors[pos] if n != prev]

        if ns or pos == end:
            segments[seg].append((pos, dist))
            for n in ns:
                stack.append((n, pos))

    stack = [(None, frozenset(), 0)]
    longest = []
    while stack:
        seg, visited, dist = stack.pop()
        if seg == end:
            longest.append(dist)
            continue

        visited |= set([seg])
        for nxt, nxt_dist in segments[seg]:
            if nxt not in visited:
                stack.append((nxt, visited, dist+nxt_dist))
    return max(longest)


def part1(grid):
    return solve(grid)


def part2(grid):
    return solve(grid, True)
