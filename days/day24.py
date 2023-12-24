import collections
import math
import itertools

Obj = collections.namedtuple('Obj', ('x', 'y', 'z', 'vx', 'vy', 'vz'))

def parse(inp):
    objs = []
    parse_vec = lambda v: tuple(int(a) for a in v.split(', '))
    for line in inp.splitlines():
        p, v = line.split(' @ ')
        obj = Obj(*parse_vec(p), *parse_vec(v))
        objs.append(obj)
    return objs

def det(a, b, c, d):
    return a*d - b*c

def intersect(a, b):
    div = det(-a.vx, -a.vy, -b.vx, -b.vy)
    if div == 0:
        return None

    da = det(a.x, a.y, a.x+a.vx, a.y+a.vy)
    db = det(b.x, b.y, b.x+b.vx, b.y+b.vy)

    x = det(da, -a.vx, db, -b.vx) / div
    y = det(da, -a.vy, db, -b.vy) / div

    # check if it's in the future
    if (x > a.x) == (a.vx > 0) and (x > b.x) == (b.vx > 0):
        return x, y


def part1(objs):
    start = 200000000000000
    end = 400000000000000

    cnt = 0
    for a, b in itertools.combinations(objs, 2):
        if p := intersect(a, b):
            if start <= p[0] <= end and start <= p[1] <= end:
                cnt += 1

    return cnt

