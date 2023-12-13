import functools
import operator

def parse(inp):
    chunks = inp.split('\n\n')
    patterns = []
    for chunk in chunks:
        lines = chunk.splitlines()
        cols = [0]*len(lines[0])
        rows = []
        for line in lines:
            row = 0
            for col, ch in enumerate(line):
                d = ch == '#'
                row = row*2 + d
                cols[col] = cols[col]*2 + d
            rows.append(row)
        patterns.append((cols, rows))
    return patterns


def find_reflection(vals):
    for split in range(1, len(vals)):
        left, right = reversed(vals[:split]), vals[split:]
        if all(l==r for l,r in zip(left, right)):
               return split
    return None


def part1(patterns):
    sum_cols = 0
    sum_rows = 0
    for cols, rows in patterns:
        if col := find_reflection(cols):
            sum_cols += col
        if row := find_reflection(rows):
            sum_rows += row
    return sum_cols + sum_rows*100


def find_smudged(vals):
    for split in range(1, len(vals)):
        left, right = reversed(vals[:split]), vals[split:]
        diffs = (l^r for l,r in zip(left, right))
        diff = functools.reduce(operator.or_, diffs)
        # check if exact power of two
        if diff > 0 and diff & (diff-1) == 0:
            return split


def part2(patterns):
    sum_cols = 0
    sum_rows = 0
    for cols, rows in patterns:
        if col := find_smudged(cols):
            sum_cols += col
        if row := find_smudged(rows):
            sum_rows += row
    return sum_cols + sum_rows*100
