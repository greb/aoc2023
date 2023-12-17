import heapq

def parse(inp):
    grid = {(x,y): int(ch)
            for y,line in enumerate(inp.splitlines())
            for x,ch in enumerate(line)}
    return grid


DIRS = [(1,0), (0,1), (-1, 0), (0,-1)]


def shortest_path(grid, least, most):
    start = (0,0)
    end = max(grid)
    queue = [(0, start, (0,0))]
    seen = set()

    while queue:
        heat, pos, in_dir = heapq.heappop(queue)
        if pos == end:
            return heat

        if (pos, in_dir) in seen:
            continue
        seen.add((pos, in_dir))

        ix, iy = in_dir
        for dx, dy in DIRS:
            # Prevent going forward or backwards
            if (dx == ix and dy == iy) or (dx == -ix and dy == -iy):
                continue

            (x, y), h = pos, heat
            for i in range(1, most+1):
                x, y = x+dx, y+dy
                if (x,y) not in grid:
                    break
                h += grid[(x,y)]

                if i >= least:
                    heapq.heappush(queue, (h, (x,y), (dx,dy)))


def part1(grid):
    return shortest_path(grid, 1, 3)


def part2(grid):
    return shortest_path(grid, 4, 10)
