from collections import Counter
from itertools import combinations

import random


CARD_RANKS = '--23456789TJQKA'

COUNT_RANKINGS = {
    (5,): 10,
    (4,1): 7,
    (3,2): 6,
    (3,1,1): 3,
    (2,2,1): 2,
    (2,1,1,1): 1,
    (1,1,1,1,1): 0
}


def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand, hand,...]"
    # max_rank = hand_rank(max(hands, key=hand_rank))
    # return [hand for hand in hands if hand_rank(hand) == max_rank]
    return allmax(hands, key=hand_rank)

def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    "Shuffle the deck and deal out numhands n=card hands"
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # max_val = key(max(iterable, key=key))
    # return [el for el in iterable if key(el) == max_val]
    max_results, cur_max = [], None
    key = key or (lambda el: el)

    for val in iterable:
        cur_val = key(val)
        if not max_results or cur_val > cur_max:
            max_results, cur_max = [val], cur_val
        elif cur_val == cur_max:
            max_results.append(val)

    return max_results


def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    groups = group([CARD_RANKS.index(r) for r,s in hand])
    counts, ranks = unzip(groups)

    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1

    return max(COUNT_RANKINGS[counts], 4*straight + 5*flush), ranks


def best_hand(hand):
    return max(combinations(hand, 5), key=hand_rank)


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [CARD_RANKS.index(r) for r, s in cards]
    ranks.sort(reverse=True)

    if ranks == [14, 5, 4, 3, 2]:
        return [5, 4, 3, 2, 1]
    return ranks

def group(items):
    """Return a list of [(count, x)...], highest count first, then highest x
    first."""
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)


def unzip(pairs):
    return zip(*pairs)
