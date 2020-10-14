import pytest

from poker import poker


def test_poker():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf

    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh

    assert poker([fh]) == fh
    assert poker(100 * [fh]) == fh

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    assert card_ranks(sf)  == [10, 9, 8, 7, 6]
    assert card_ranks(fk)  == [9, 9, 9, 9, 7]
    assert card_ranks(fh)  == [10, 10, 10, 7, 7]
