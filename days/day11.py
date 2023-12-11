import itertools

def parse(inp):
    gals = set()

    lines = inp.splitlines()
    w, h = len(lines[0]), len(lines)

    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '#':
                gals.add((x,y))
    return gals, w, h


def expand(gals, w, h, n=2):
    n -= 1
    y_gals = set()
    y_offset = 0
    for y in range(h):
        xs = [gx for gx, gy in gals if gy==y]
        for x in xs:
            y_gals.add((x, y+y_offset))
        if not xs:
            y_offset += n

    x_gals = set()
    x_offset = 0
    for x in range(w):
        ys = [gy for gx,gy in y_gals if gx==x]
        for y in ys:
            x_gals.add((x+x_offset, y))
        if not ys:
            x_offset += n

    return x_gals


def dist(g0, g1):
    return sum(abs(b-a) for a,b in zip(g0,g1))


def part1(image):
    gals = expand(*image)
    combs = itertools.combinations(gals, 2)
    return sum(dist(g0, g1) for g0,g1 in combs)


def part2(image):
    gals = expand(*image, n=1_000_000)
    combs = itertools.combinations(gals, 2)
    return sum(dist(g0, g1) for g0,g1 in combs)

