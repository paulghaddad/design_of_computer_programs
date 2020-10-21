import pytest

from poker import poker, card_ranks, straight, flush, kind

sf = "6C 7C 8C 9C TC".split() # => ['6C', '7C', '8C', '9C', 'TC']
fk = "9D 9H 9S 9C 7D".split()
fh = "TD TC TH 7C 7D".split()
tp = "5S 5D 9H 9C 6S".split()

@pytest.mark.skip()
def test_poker():
    "Test cases for the functions in poker program"
    assert poker([sf, fk, fh]) == sf

    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh

    assert poker([fh]) == fh
    assert poker(100 * [fh]) == fh


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
