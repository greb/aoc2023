import unittest
import collections

N = 256

class Test(unittest.TestCase):
    def test_ascii_hash(self):
        self.assertEqual(ascii_hash('HASH'), 52)


def ascii_hash(chars):
    h = 0
    for ch in chars:
        h = (h + ord(ch))*17 % N
    return h


def parse(inp):
    vals = inp.strip().split(',')
    return vals


def part1(vals):
    return sum(ascii_hash(v) for v in vals)


def part2(vals):
    boxes = [collections.OrderedDict() for _ in range(N)]

    for val in vals:
        op = None
        if val[-1] == '-':
            label = val[:-1]
        else:
            label = val[:-2]
            op = int(val[-1])

        h = ascii_hash(label)
        if op:
            boxes[h][label] = op
        elif label in boxes[h]:
            del boxes[h][label]

    score = 0
    for i, box in enumerate(boxes, start=1):
        for slot, focal in enumerate(box.values(),start=1):
            score += i * slot * focal
    return score


