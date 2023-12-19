import re
import operator
import math

def parse(inp):
    flows_lines, parts_lines = inp.split('\n\n')
    flow_re = re.compile(r'(.+)\{(.+)}')
    cond_re = re.compile(r'(.+)(\>|\<)(\d+):(.+)')
    part_re = re.compile(r'(.)=(\d+)')

    flows = dict()
    for line in flows_lines.splitlines():
        name, rs = flow_re.match(line).groups()
        rules = []
        for r in rs.split(','):
            if rule := cond_re.match(r):
                field, op, val, dst = rule.groups()
                rules.append((field, op, int(val), dst))
            else:
                rules.append(r)
        flows[name] = rules

    parts = []
    for line in parts_lines.splitlines():
        part = {var: int(val) for var, val in part_re.findall(line)}
        parts.append(part)

    return flows, parts


def apply(rules, part):
    for rule in rules:
        if isinstance(rule, tuple):
            field, op, val, dst = rule
            if op == '<' and part[field] < val:
                return dst
            elif op == '>' and part[field] > val:
                return dst
        else:
            return rule


def part1(system):
    flows, parts = system
    total = 0

    for part in parts:
        flow = 'in'
        while flow in flows:
            flow = apply(flows[flow], part)

        if flow == 'A':
            total += sum(part.values())

    return total


def split(rules, parts):
    for rule in rules:
        if isinstance(rule, tuple):
            nxt = parts.copy()
            field, op, val, dst = rule
            a, b = parts[field]

            # Check not really necessary, input behaves nicely
            if a <= val <= b:
                if op == '<':
                    parts[field] = (val, b)
                    nxt[field]   = (a, val-1)
                else:
                    parts[field] = (a, val)
                    nxt[field]   = (val+1, b)
                yield dst, nxt
        else:
            yield rule, parts


def count_parts(flow, parts, flows):
    if flow == 'R':
        return 0

    if flow == 'A':
        return math.prod(b-a+1 for a,b in parts.values())

    total = 0
    for dst, parts in split(flows[flow], parts):
        total += count_parts(dst, parts, flows)
    return total


def part2(system):
    flows, _ = system
    parts = {n: (1, 4000) for n in 'xmas'}
    return count_parts('in', parts, flows)
