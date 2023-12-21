import collections

DIRS = [(1,0), (0,1), (-1,0), (0,-1)]
def moves(pos):
    for dir in DIRS:
        yield tuple(p+d for p,d in zip(pos, dir))


def parse(inp):
    start = None
    rocks = set()

    lines = inp.splitlines()
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == 'S':
                start = (x,y)
            if ch == '#':
                rocks.add((x,y))
    bounds = len(lines[0]), len(lines)

    visited = dict()
    queue = collections.deque()
    queue.append((0, start))
    while queue:
        steps, pos = queue.popleft()
        if pos in visited:
            continue
        visited[pos] = steps

        for move in moves(pos):
            if move in visited or move in rocks:
                continue
            if not all(0 <= p < b for p,b in zip(move, bounds)):
                continue
            queue.append((steps+1, move))
    return list(visited.values()), bounds[0]


def part1(garden):
    visited, _ = garden
    return sum(v%2==0 and v <= 64 for v in visited)


def part2(garden):
    visited, size = garden

    steps = 26501365
    n = steps // size
    h = size // 2

    even = n*n * sum(v%2==0 for v in visited)
    odd  = (n-1)*(n-1) * sum(v%2==1 for v in visited)
    even_corners = n * sum(v%2==0 and v > h for v in visited)
    odd_corners = (n+1) * sum(v%2==1 and v > h for v in visited)

    return even + odd + even_corners - odd_corners
