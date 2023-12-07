import collections
import itertools

def parse(inp):
    hands = []
    for line in inp.splitlines():
        hand, bid = line.split()
        hands.append((hand, int(bid)))
    return hands

card_scores1 = '23456789TJQKA'
card_scores2 = 'J23456789TQKA'

hand_types = {
    (5,): 6,        # Five of a kind
    (4,1): 5,       # Four of a kind
    (3,2): 4,       # Full house
    (3,1,1): 3,     # Three of a kind
    (2,2,1): 2,     # Two pair
    (2,1,1,1): 1,   # One pair
    (1,1,1,1,1): 0  # High card
}

def winnings(hands, score_fn):
    hands = sorted(hands, key=lambda e: score_fn(e[0]))
    vals = [bid*rank for ((_,bid), rank)
        in zip(hands, itertools.count(1))]
    return sum(vals)


def base_score(hand, card_scores):
    base = len(card_scores)
    score = 0
    for card in hand:
        score *= base
        score += card_scores.index(card)
    return score


def hand_type(hand):
    counter = collections.Counter(hand)
    return hand_types[tuple(c[1] for c in counter.most_common())]


def score_hand(hand):
    return hand_type(hand), base_score(hand, card_scores1)

def part1(hands):
    return winnings(hands, score_hand)


def score_hand2(hand):
    if 'J' in hand:
        best_type = 0
        for repl in card_scores2:
            best_type = max(best_type, hand_type(hand.replace('J', repl)))
    else:
        best_type = hand_type(hand)

    return best_type, base_score(hand, card_scores2)


def part2(hands):
    return winnings(hands, score_hand2)
