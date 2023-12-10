import collections


N = lambda x,y: (x,y-1)
E = lambda x,y: (x+1,y)
S = lambda x,y: (x,y+1)
W = lambda x,y: (x-1,y)


def detect_loop(start, pipes):
    loop_nodes = [start]

    for neigh in pipes[start]:
        if neigh in pipes and any(start == n for n in pipes[neigh]):
            node = neigh
            break

    prev = start
    while node != start:
        loop_nodes.append(node)
        next_a, next_b = pipes[node]

        if next_a == prev:
            prev = node
            node = next_b
        else:
            prev = node
            node = next_a
    return loop_nodes


def parse(inp):
    pipes = dict()
    start = None
    for y, line in enumerate(inp.splitlines()):
        for x, ch in enumerate(line):
            match ch:
                case 'S':
                    start = (x,y)
                    pipes[(x,y)] = [N(x,y), E(x,y), S(x,y), W(x,y)]
                case '|':
                    pipes[(x,y)] = [N(x,y), S(x,y)]
                case '-':
                    pipes[(x,y)] = [E(x,y), W(x,y)]
                case 'L':
                    pipes[(x,y)] = [N(x,y), E(x,y)]
                case 'J':
                    pipes[(x,y)] = [N(x,y), W(x,y)]
                case '7':
                    pipes[(x,y)] = [S(x,y), W(x,y)]
                case 'F':
                    pipes[(x,y)] = [S(x,y), E(x,y)]

    return detect_loop(start, pipes)


def part1(loop):
    return len(loop) // 2


def part2(loop):
    # Calculate area inside loop using the shoelace method
    area = 0
    loop = loop + [loop[0]]
    for (a,b), (c,d) in zip(loop, loop[1:]):
        area += a*d - b*c
    area //= 2

    # Pick's theorem
    return area - (len(loop) // 2 - 1)
