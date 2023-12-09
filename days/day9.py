def parse(inp):
    return [[int(n) for n in line.split()] for line in inp.splitlines()]


def predict1(seq):
    diff_seqs = []

    while any(n != 0 for n in seq):
        diff_seqs.append(seq)
        seq = [b-a for a,b in zip(seq, seq[1:])]
    return sum(s[-1] for s in diff_seqs)

def part1(seqs):
    return sum(predict1(s) for s in seqs)


def predict2(seq):
    diff_seqs = []
    while any(n != 0 for n in seq):
        diff_seqs.append(seq)
        seq = [b-a for a,b in zip(seq, seq[1:])]

    val = 0
    for s in reversed(diff_seqs):
        val = s[0] - val
    return val


def part2(seqs):
    return sum(predict2(s) for s in seqs)
