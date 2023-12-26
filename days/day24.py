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


def search_v_rock(objs, dim):
    # Iteratively constrain velocity on a particular axis. Possible set starts
    # with a range of maximal velovity of hail in a particular dimension in
    # either direction. A rock moving faster won't intercept any hail.
    r_min = min(obj[dim+3] for obj in objs)
    r_max = max(obj[dim+3] for obj in objs)
    v_rock = set(range(r_min, r_max+1))
    for a, b in itertools.combinations(objs, 2):
        if a[dim+3] == b[dim+3]:
            # If two hail stones have the same speed in a dimension, their
            # seperation will always be the same in that dimension. Assuming
            # the time of hit is an integer (it is lol), the seperation must
            # be an integer multiply of their relative velocity to the rock.
            # We can use this to constrain the speed of the rock.
            new_v_rock = set()
            diff = b[dim] - a[dim]
            for v in v_rock:
                rel_v = v-a[dim+3]
                if rel_v != 0 and diff % rel_v == 0:
                    new_v_rock.add(v)
            v_rock = new_v_rock
            if len(v_rock) == 1:
                break
    # Won't work on example
    assert len(v_rock) == 1
    return v_rock.pop()


def part2(objs):
    vr = vx, vy, vz = [search_v_rock(objs, dim) for dim in range(3)]

    # Find two hailstones with the same x velocity
    for a, b in itertools.combinations(objs, 2):
        if a.vx == b.vx:
            break

    # Determine time between rock hits a and rock hits b
    dt = (a.x - b.x) // (a.vx - vx)

    # The distance the rock travels in this time in y is the same as the y
    # seperation of the hailstones between the hit events. This allows us to
    # find out time of first hit.
    # dt*vy = (b.y + (t+td)*b.vy) - (a.y + t*a.vx) => solve for t
    t = (a.y - b.y + dt*vy - dt*b.vy) // (b.vy - a.vy)

    # Knowing t we can find out position of first hit event and from there we
    # can backtrack to the rock's origin.
    pa = [a[i] + t*a[i+3] for i in range(3)]
    pr = [p - t*v for p,v in zip(pa, vr)]
    return sum(pr)
