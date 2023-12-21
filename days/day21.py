import collections

def parse(inp):
    positions = set()
    rocks = set()

    lines = inp.splitlines()
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == 'S':
                positions.add((x,y))
            if ch == '#':
                rocks.add((x,y))

    bounds = len(lines[0]), len(lines)
    return positions, rocks, bounds


DIRS = [(1,0), (0,1), (-1,0), (0,-1)]
def moves(pos):
    for dir in DIRS:
        yield tuple(p+d for p,d in zip(pos, dir))


def wrap(pos, bounds):
    return tuple(p%b for p,b in zip(pos, bounds))


def find_positions(positions, rocks, bounds, steps):
    queue = collections.deque()
    for pos in positions:
        queue.append((pos, steps))

    new_positions = set()
    visited = positions.copy()

    while queue:
        pos, steps = queue.popleft()
        if steps % 2 == 0:
            new_positions.add(pos)
        if steps == 0:
            continue

        for move in moves(pos):
            if move in visited:
                continue
            if wrap(move, bounds) in rocks:
                continue
            visited.add(move)
            queue.append((move, steps-1))

    return new_positions


def part1(garden):
    positions, rocks, bounds = garden
    return len(find_positions(positions, rocks, bounds, 64))


def part2(garden):
    positions, rocks, bounds = garden
    size = bounds[0]
    goal = 26501365

    ys = []
    for steps in [size//2, size, size]:
        positions = find_positions(positions, rocks, bounds, steps)
        ys.append(len(positions))

    # use data points for quadratic interpolation
    x = goal // size
    a, b, c = ys
    return a + (b-a)*x + ((c-b)-(b-a))*(x*(x-1)//2)
