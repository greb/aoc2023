import collections
import itertools
import math


def parse(inp):
    mods = dict()
    cables = dict()

    for line in inp.splitlines():
        mod, outs = line.split(' -> ')
        if mod[0] in '%&':
            op, mod = mod[0], mod[1:]
            mods[mod] = op
        cables[mod] = outs.split(', ')
    return mods, cables


def init_mem(mods, cables):
    mem = dict()
    for mod, op in mods.items():
        match op:
            case '%':
                mem[mod] = False
            case '&':
                mem[mod] = dict()

    for mod, outs in cables.items():
        for out in outs:
            if mods.get(out) == '&':
                mem[out][mod] = False

    return mem


def press_button(mods, cables, mem, cnt):
    # Initial low pulse
    cnt[0] += 1

    queue = collections.deque()
    src = 'broadcaster'
    for out in cables[src]:
        queue.append((src, out, False))

    while queue:
        src, dst, pulse = queue.popleft()
        cnt[pulse] += 1

        match mods.get(dst):
            case '%':
                if not pulse:
                    mem[dst] = not mem[dst]
                    for out in cables[dst]:
                        queue.append((dst, out, mem[dst]))

            case '&':
                mem[dst][src] = pulse
                pulse = not all(mem[dst].values())
                for out in cables[dst]:
                    queue.append((dst, out, pulse))


def part1(machine):
    mods, cables = machine
    mem = init_mem(mods, cables)

    cnt = [0, 0]
    for _ in range(1000):
        press_button(mods, cables, mem, cnt)
    return math.prod(cnt)
