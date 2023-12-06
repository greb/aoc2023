import re
import math

def part1(inp):
    times, dists = inp.splitlines()
    times = [int(n) for n in re.findall('\d+', times)]
    dists = [int(n) for n in re.findall('\d+', dists)]

    win_counts = []
    for time, old_dist in zip(times, dists):
        cnt = 0
        for hold in range(time+1):
            dist = hold * (time-hold)
            if dist > old_dist:
                cnt += 1
        win_counts.append(cnt)
    return math.prod(win_counts)


def part2(inp):
    time, dist = inp.splitlines()
    time = int(''.join(re.findall('\d', time)))
    old_dist = int(''.join(re.findall('\d', dist)))

    cnt = 0
    for hold in range(time+1):
        dist = hold * (time-hold)
        if dist > old_dist:
            cnt += 1
    return cnt
