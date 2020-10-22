from collections import Counter
import random


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
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # Straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                            # Four of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):         # Full House
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # Flush
        return (6, kind(3, ranks), kind(2, ranks))
    elif straight(ranks):                           # Straight
        return (4, max(ranks))
    elif kind(3, ranks):                            # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                           # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                            # kind
        return (1, kind(2, ranks), ranks)
    else:                                           # high card
        return (0, ranks)

CARD_RANKS = '--23456789TJQKA'

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [CARD_RANKS.index(r) for r, s in cards]
    ranks.sort(reverse=True)

    if ranks == [14, 5, 4, 3, 2]:
        return [5, 4, 3, 2, 1]
    return ranks

def straight(ranks):
    high = max(ranks)
    low = min(ranks)

    return ranks == [rank for rank in range(high, low-1, -1)]

def flush(hand):
    return len({suit for rank,suit in hand}) == 1

def kind(n, ranks):
    """
    Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand.
    """
    for rank, count in Counter(ranks).items():
        if count == n:
            return rank

    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
       tuple: (highest, lowest); otherwise return None."""
    counts = Counter(ranks)
    pairs = []

    for rank, count in counts.items():
        if count == 2:
            pairs.append(rank)

    if len(pairs) == 2:
        return tuple(sorted(pairs, reverse=True))

    return None
