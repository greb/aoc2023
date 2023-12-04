def parse(inp):
    cards = dict()
    for line in inp.splitlines():
        card_num, nums = line.split(':')
        card_num = int(card_num.split()[1])
        winning, have = nums.split('|')
        winning = set(int(n.strip()) for n in winning.split())
        have = set(int(n.strip()) for n in have.split())
        cards[card_num] = len(winning & have)
    return cards


def part1(cards):
    score = 0
    for match in cards.values():
        if match > 0:
            score += 2 ** (match-1)
    return score


def part2(cards):
    unchecked = list(cards.keys())
    total = len(cards)

    while unchecked:
        card_num = unchecked.pop()
        match = cards[card_num]
        total += match
        for n in range(match):
            next_card_num = card_num + n + 1
            unchecked.append(next_card_num)

    return total

