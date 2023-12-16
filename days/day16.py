import collections

dirs = [(1,0), (0,1), (-1,0), (0,-1)]

def parse(inp):
    lines = inp.splitlines()
    w, h = len(lines[0]), len(lines)

    devices = dict()
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch != '.':
                devices[(x,y)] = ch
    return w, h, devices


def next_pos(pos, dir_idx):
    return tuple(p+d for p,d in zip(pos, dirs[dir_idx]))


def simulate(cave, pos=(0,0), dir_idx=0):
    energized = collections.defaultdict(set)
    w, h, devices = cave
    beams = [(pos, dir_idx)]

    while beams:
        new_beams = []
        for pos, dir_idx in beams:
            if not (0 <= pos[0] < w and 0 <= pos[1] < h):
                continue
            if pos in energized and dir_idx in energized[pos]:
                continue

            energized[pos].add(dir_idx)
            device = devices.get(pos)

            if device == '/':
                dir_idx = dir_idx ^ 0b11
            elif device == '\\':
                dir_idx = dir_idx ^ 0b01
            elif device == '-' and dir_idx & 0b01:
                new_beams.append((next_pos(pos, 0), 0))
                new_beams.append((next_pos(pos, 2), 2))
                continue
            elif device == '|' and not (dir_idx & 0b01):
                new_beams.append((next_pos(pos, 1), 1))
                new_beams.append((next_pos(pos, 3), 3))
                continue

            new_beams.append((next_pos(pos, dir_idx), dir_idx))
        beams = new_beams

    return energized


def part1(cave):
    energized = simulate(cave)
    return len(energized)


def part2(cave):
    w, h, _ = cave
    beams = []

    for x in range(w):
        beams.append(((x, 0), 1))
        beams.append(((x, h-1), 3))
    for y in range(h):
        beams.append(((0, y), 0))
        beams.append(((w-1, y), 2))

    return max(len(simulate(cave, pos, dir_idx)) for pos, dir_idx in beams)
