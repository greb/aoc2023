import itertools

N = (0, -1)
E = (1, 0)
S = (0, 1)
W = (-1, 0)

def parse(inp):
    lines = inp.splitlines()
    w, h = len(lines[0]), len(lines)
    movers = set()
    fixers = set()

    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            rock = x, y
            match ch:
                case 'O':
                    movers.add(rock)
                case '#':
                    fixers.add(rock)
    return w, h, movers, fixers


def tilt(w, h, movers, fixers, d):
    dx, dy = d
    stopped = fixers.copy()

    while movers:
        new_movers = set()
        for x, y in movers:
            nxt = nx, ny = x+dx, y+dy
            in_bounds = 0 <= nx < w and 0 <= ny < h
            if not in_bounds or nxt in stopped:
                stopped.add((x,y))
            elif nxt in movers:
                new_movers.add((x,y))
            else:
                new_movers.add(nxt)
        movers = new_movers
    return stopped - fixers


def load(w, h, movers):
    score = 0
    for y in range(h):
        rocks = sum((x,y) in movers for x in range(w))
        score += rocks * (h-y)
    return score


def cycle(w, h, movers, fixers):
    for d in [N, W, S, E]:
        movers = tilt(w, h, movers, fixers, d)
    return frozenset(movers)


def display_dish(w, h, movers, fixers):
    for y in range(h):
        line = []
        for x in range(w):
            if (x,y) in movers:
                line.append('O')
            elif (x,y) in fixers:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))
    print()


def part1(dish):
    w, h, movers, fixers = dish
    movers = tilt(w, h, movers, fixers, N)
    return load(w, h, movers)


def part2(dish):
    w, h, movers, fixers = dish

    N = 1000000000
    hist_lut = dict()
    hist = []

    for i in itertools.count(1):
        movers = cycle(w, h, movers, fixers)
        if movers in hist_lut:
            start = hist_lut[movers]
            length = i - start
            break
        else:
            hist_lut[movers] = i
            hist.append(movers)

    offset = (N-start) % length
    return load(w, h, hist[start+offset-1])
