import pytest

from poker import poker, card_ranks, straight, flush, kind, two_pair

sf = "6C 7C 8C 9C TC".split() # => ['6C', '7C', '8C', '9C', 'TC']
fk = "9D 9H 9S 9C 7D".split()
fh = "TD TC TH 7C 7D".split()
tp = "5S 5D 9H 9C 6S".split()
al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight

@pytest.mark.skip()
def test_poker():
    "Test cases for the functions in poker program"
    assert poker([sf, fk, fh]) == sf

    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh

    assert poker([fh]) == fh
    assert poker(100 * [fh]) == fh

def test_poker_with_ties():
    sf1 = "6C 7C 8C 9C TC".split()
    sf2 = "6D 7D 8D 9D TD".split()
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]


@pytest.mark.skip()
def test_hand_rank():
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

def test_card_rank():
    assert card_ranks(sf)  == [10, 9, 8, 7, 6]
    assert card_ranks(fk)  == [9, 9, 9, 9, 7]
    assert card_ranks(fh)  == [10, 10, 10, 7, 7]


def test_straight():
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert straight(card_ranks(al)) == True


def test_flush():
    assert flush(sf) == True
    assert flush(fk) == False

def test_kind():
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7


def test_two_pair():
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert two_pair(tpranks) == (9, 5)
    assert two_pair(fkranks) == None
