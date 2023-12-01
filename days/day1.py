import re

digits = ['one', 'two', 'three', 'four', 'five', 'six',
          'seven', 'eight', 'nine']
num_pattern = re.compile(r'(?=(\d|' + '|'.join(digits) + '))')

def part1(inp):
    cal_nums = [[int(n) for n in re.findall(r'\d', line)]
                for line in inp.splitlines()]

    cal_vals = [num[0]*10 + num[-1] for num in cal_nums]
    return sum(cal_vals)


def parse_digit(d):
    if d.isnumeric():
        return int(d)
    else:
        return digits.index(d) + 1


def part2(inp):
    # Input is a little bit tricky here. The numbers actually do overlap
    # sometimes. E.g. eightwo => [8,2]. This is why the regex has a zero
    # length lockahead assertion at the beginning. Hacky, but it works.
    cal_nums = [[parse_digit(n) for n in num_pattern.findall(line)]
                for line in inp.splitlines()]

    cal_vals = [num[0]*10 + num[-1] for num in cal_nums]
    return sum(cal_vals)
