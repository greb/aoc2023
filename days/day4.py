def parse(inp):
    cards = []
    for line in inp.splitlines():
        _, nums = line.split(':')
        winning, have = nums.split('|')
        winning = set(int(n.strip()) for n in winning.split())
        have = set(int(n.strip()) for n in have.split())
        cards.append(len(winning & have))
    return cards


def part1(cards):
    score = 0
    for n in cards:
        if n > 0:
            score += 2 ** (n-1)
    return score


def part2(cards):
    card_cnt = [1] * len(cards)

    for idx, n in enumerate(cards):
        for i in range(n):
            card_cnt[idx + i + 1] += card_cnt[idx]

    return sum(card_cnt)

