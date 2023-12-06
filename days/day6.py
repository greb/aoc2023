import re
import math


def count_wins(time, dist):
    det = (time*time/4.0) - dist
    lower = time/2.0 - math.sqrt(det)
    upper = time/2.0 + math.sqrt(det)
    return math.ceil(upper) - math.floor(lower) - 1


def part1(inp):
    times, dists = inp.splitlines()
    times = [int(n) for n in re.findall('\d+', times)]
    dists = [int(n) for n in re.findall('\d+', dists)]
    return math.prod(count_wins(*elem) for elem in zip(times, dists))


def part2(inp):
    time, dist = inp.splitlines()
    time = int(''.join(re.findall('\d', time)))
    dist = int(''.join(re.findall('\d', dist)))
    return count_wins(time, dist)
