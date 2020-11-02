import pytest

from poker import best_hand, best_wild_hand


def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split())) == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split())) == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split())) == ['7C', '7D', '7H', '7S', 'JD'])


def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())) == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("6H 7H 8H 9H TH 5H ?R".split())) == ['7H', '8H', '9H', 'JH', 'TH'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split())) == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split())) == ['7C', '7D', '7H', '7S', 'JD'])
