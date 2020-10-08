def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)

def hand_rank(hand):
    # will be implemented later on, for now assume it provides a rank given a hand
    pass
