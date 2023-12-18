import re

def parse(inp):
    re_line = re.compile(r'(.) (\d+) \(#(.*)\)')
    plan = []
    for line in inp.splitlines():
        d, n, c = re_line.match(line).groups()
        plan.append((d, int(n), c))
    return plan


DIRS = {'U': (0,-1), 'D': (0,1), 'L': (-1, 0), 'R': (1,0)}
DIR_LUT = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}


def solve(plan):
    # Similar to day 10. Using shoelace algorithm to calculate area and Pick's
    # theorem to calculate internal cubes.
    verts = [(0,0)]
    circum = 0
    x, y = 0, 0
    for d, n in plan:
        dx, dy = DIRS[d]
        circum += n
        x, y = x+n*dx, y+n*dy
        verts.append((x,y))

    area = 0
    for (a,b), (c,d) in zip(verts, verts[1:]):
        area += a*d - b*c
    area //= 2

    inside = area - (circum // 2 - 1)
    return inside + circum


def part1(plan):
    plan = [tuple(p[:2]) for p in plan]
    return solve(plan)


def part2(plan):
    new_plan = []
    for _, _, c in plan:
        d = DIR_LUT[c[-1]]
        n = int(c[:-1], 16)
        new_plan.append((d, n))
    return solve(new_plan)
