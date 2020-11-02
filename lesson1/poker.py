from collections import Counter
from itertools import combinations, product

import random


CARD_RANKS = '--23456789TJQKA'
BLACK_SUITS = 'SC'
RED_SUITS = 'HD'
RED_WILDS = [r+s for r in CARD_RANKS[2:] for s in RED_SUITS]
BLACK_WILDS = [r+s for r in CARD_RANKS[2:] for s in BLACK_SUITS]

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
    "From a 7-card hand, return the best 5 card hand."
    return max(combinations(hand, 5), key=hand_rank)


def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    max_hand, max_hand_score = None, None
    black_joker, red_joker = False, False

    if '?B' in hand:
        hand.remove('?B')
        black_joker = True

    if '?R' in hand:
        hand.remove('?R')
        red_joker = True

    if black_joker and red_joker:
        blacK_red_combinations = product(RED_WILDS, BLACK_WILDS)
        max_hand, max_hand_score = _best_hand_for_wild(hand, blacK_red_combinations)
    elif red_joker:
        max_hand, max_hand_score = _best_hand_for_wild(hand, RED_WILDS)
    elif black_joker:
        max_hand, max_hand_score = _best_hand_for_wild(hand, BLACK_WILDS)
    else:
        max_hand = max(combinations(hand, 5), key=hand_rank)

    return sorted(max_hand)


def _best_hand_for_wild(hand, wilds):
    max_hand, max_hand_score = None, None

    for combination in wilds:
        if isinstance(combination, str):
            cur_high_hand = max(combinations(hand + [combination], 5), key=hand_rank)
        else:
            cur_high_hand = max(combinations(hand + list(combination), 5), key=hand_rank)

        cur_hand_score = hand_rank(cur_high_hand)
        if max_hand_score is None or cur_hand_score > max_hand_score:
            max_hand_score = cur_hand_score
            max_hand = cur_high_hand

    return max_hand, max_hand_score


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
