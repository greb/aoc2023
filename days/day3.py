import re
import math

steps = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]


def parse(inp):
    symbols = dict() # x,y of symbol: symbol
    numbers = dict() # x,y of first digit: end, value
    lines = inp.splitlines()
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if not ch.isnumeric() and ch != '.':
                symbols[(x,y)] = ch

    for y, line in enumerate(lines):
        ns = re.finditer(r'\d+', line)
        for n in ns:
            x = n.start()
            numbers[(x,y)] = (n.end(), int(n[0]))

    return symbols, numbers


def neighbors(x,y):
    for dx, dy in steps:
        yield x+dx, y+dy


def part1(inp):
    symbols, numbers = inp
    total = 0

    for (nx, ny), (num_end, num_val) in numbers.items():
        check = [any(neigh in symbols for neigh in neighbors(x, ny))
                for x in range(nx, num_end)]
        if any(check):
            total += num_val

    return total


def part2(inp):
    symbols, numbers = inp
    total = 0

    gears = [pos for pos, sym in symbols.items() if sym == '*']
    for gear in gears:
        gear_nums = []
        for (nx, ny), (num_end, num_val) in numbers.items():
            check = [any(gear == neigh for neigh in neighbors(x, ny))
                    for x in range(nx, num_end)]
            if any(check):
                gear_nums.append(num_val)

        if len(gear_nums) > 1:
            total += math.prod(gear_nums)

    return total
