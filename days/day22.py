import collections


def parse(inp):
    bricks = []
    for line in inp.splitlines():
        a, b = line.split('~')
        a = [int(n) for n in a.split(',')]
        b = [int(n) for n in b.split(',')]
        bricks.append((a, b))
    return bricks


def drop_bricks(bricks):
    heights = dict()
    sup_by = collections.defaultdict(set)
    sup_from = collections.defaultdict(set)

    bricks = sorted(bricks, key=lambda b: b[0][2])
    for b, brick in enumerate(bricks):
        (x0,y0,z0), (x1,y1,z1) = brick
        # Input bricks behave nicely
        assert x0 <= x1 and y0 <= y1 and z0 <= z1

        proj = [(x,y) for x in range(x0,x1+1) for y in range(y0,y1+1)]
        sup = [heights[p] for p in proj if p in heights]
        if not sup:
            z_offset = z0 - 1
        else:
            z_max = max(sup)[0]
            z_offset = z0 - z_max - 1
            for z, s in sup:
                if z == z_max:
                    sup_by[s].add(b)
                    sup_from[b].add(s)
        for p in proj:
            heights[p] = (z1 - z_offset, b)
    return sup_by, sup_from


def part1(bricks):
    _, sup_from = drop_bricks(bricks)

    unsafe = set()
    for bs in sup_from.values():
        if len(bs) == 1:
            unsafe.add(list(bs)[0])
    return len(bricks) - len(unsafe)


def part2(bricks):
    sup_by, sup_from = drop_bricks(bricks)

    unsafe = set()
    for bs in sup_from.values():
        if len(bs) == 1:
            unsafe.add(list(bs)[0])

    total = 0
    for start in unsafe:
        removed = set()
        queue = collections.deque([start])
        while queue:
            s = queue.popleft()
            if s in removed:
                continue
            removed.add(s)
            for b in sup_by[s]:
                # Make sure all supporting bricks are removed before continue
                # the search.
                if not sup_from[b] - removed:
                    queue.append(b)
        total += len(removed) - 1
    return total
