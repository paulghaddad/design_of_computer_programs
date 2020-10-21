from collections import Counter


def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(ranks):            # Straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                            # Four of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):         # Full House
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(ranks):                              # Flush
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
