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


def step(positions, rocks, bounds):
    new_positions = set()
    for pos in positions:
        for move in moves(pos):
            if wrap(move, bounds) in rocks:
                continue
            new_positions.add(move)
    return new_positions


def display(positions, rocks, bounds):
    for y in range(bounds[0]):
        line = []
        for x in range(bounds[1]):
            if (x,y) in rocks:
                line.append('#')
            elif (x,y) in positions:
                line.append('O')
            else:
                line.append('.')
        print(''.join(line))


def part1(garden):
    positions, rocks, bounds = garden
    for _ in range(64):
        positions = step(positions, rocks, bounds)
    return len(positions)


def part2(garden):
    positions, rocks, bounds = garden
    assert bounds[0] == bounds[1]
    size = bounds[0]
    goal = 26501365

    steps = 0
    ys = []
    while True:
        positions = step(positions, rocks, bounds)
        steps += 1
        if steps % size == goal % size:
            ys.append(len(positions))
            if len(ys) == 3:
                break

    # use data points for quadratic interpolation
    x = goal // size
    a, b, c = ys
    return a + (b-a)*x + ((c-b)-(b-a))*(x*(x-1)//2)



