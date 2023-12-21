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


def in_bounds(pos, bounds):
    return all(0 < p <= b for p,b in zip(pos, bounds))


def step(positions, rocks, bounds):
    new_positions = set()
    for pos in positions:
        for move in moves(pos):
            if move in rocks:
                continue
            if not in_bounds(move, bounds):
                continue
            new_positions.add(move)
    return new_positions


def part1(garden):
    positions, rocks, bounds = garden
    for _ in range(64):
        positions = step(positions, rocks, bounds)
    return len(positions)
