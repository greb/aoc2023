import functools

def parse(inp):
    rows = []
    for line in inp.splitlines():
        springs, groups = line.split()
        groups = [int(n) for n in groups.split(',')]
        rows.append((springs, groups))
    return rows


def gen_arrangements(groups, n):
    if not groups:
        yield '.'*n
        return

    offset = 0
    head, *tail = groups
    while offset+head <= n:
        chunk = '.'*offset + '#'*head
        if tail:
            chunk += '.'
            next_n = n - (offset+head+1)
        else:
            next_n = n - (offset+head)
        for next_chunk in gen_arrangements(tail, next_n):
            yield chunk + next_chunk
        offset += 1

def min_group_len(groups):
    if not groups:
        return 0
    return sum(groups) + len(groups) - 1


@functools.lru_cache
def count(springs, groups):
    if not groups:
        return '#' not in springs

    if len(springs) < min_group_len(groups):
        return 0

    cnt = 0
    offset = 0
    head, *tail = groups

    while head+offset+min_group_len(tail) <= len(springs):
        arr = '.'*offset + '#'*head
        if tail:
            arr += '.'
        head_spr, tail_spr = springs[:len(arr)], springs[len(arr):]

        if all(s=='?' or s==a for s,a in zip(head_spr, arr)):
            cnt += count(tail_spr, tuple(tail))

        offset += 1

    return cnt


def part1(rows):
    total = 0
    for springs, groups in rows:
        total += count(springs, tuple(groups))
    return total


def part2(rows):
    total = 0
    for springs, groups in rows:
        springs = '?'.join([springs]*5)
        groups = groups*5
        total += count(springs, tuple(groups))
    return total
