import re



def parse(inp):
    chunks = inp.split('\n\n')
    seeds, *chunks = chunks
    seeds = [int(s) for s in seeds.split()[1:]]

    maps = dict()
    for chunk in chunks:
        lines = chunk.splitlines()
        header, *lines = lines

        src_cat, dst_cat = re.match(r'(.+)\-to\-(.+) map', header).groups()
        convs = []
        for line in lines:
            dst, src, n = [int(tok) for tok in line.split()]
            convs.append((src, dst, n))
        maps[src_cat] = dst_cat, sorted(convs)
    return seeds, maps


def convert_vals(vals, convs):
    for val in vals:
        for src, dst, n in convs:
            offset = val - src
            if 0 <= offset < n:
                yield dst+offset
                break
        else:
            yield val


def part1(almanac):
    seeds, maps = almanac

    src = 'seed'
    src_vals = seeds
    while src in maps:
        src, convs = maps[src]
        src_vals = list(convert_vals(src_vals, convs))
    return min(src_vals)


def chunk_iter(it, n):
    it = iter(it)
    iters = [it]*n
    return zip(*iters)


def intersect(a_start, a_len, b_start, b_len):
    start = max(a_start, b_start)
    end = min(a_start+a_len, b_start, b_len)
    return start, end


def convert_ranges(ranges, convs):
    for rng_start, rng_len in ranges:
        # Only works if convs is sorted by src; done in parse
        for src, dst, length in convs:
            int_start = max(rng_start, src)
            int_end = min(rng_start+rng_len, src+length)

            if int_start >= int_end:
                # No intersection
                continue

            # Left of intersection
            if rng_start < int_start:
                yield rng_start, int_start - rng_start

            # Intersection
            offset = int_start - src
            yield dst+offset, int_end - int_start


            # Right of intersection
            if rng_start + rng_len > int_end:
                rng_start = int_end
                rng_len -= int_end - int_start
            else:
                break
        else:
            yield rng_start, rng_len


def part2(almanac):
    seeds, maps = almanac

    src = 'seed'
    src_ranges = list(chunk_iter(seeds, 2))
    while src in maps:
        src, convs = maps[src]
        src_ranges = list(convert_ranges(src_ranges, convs))

    return min(src_ranges)[0]
