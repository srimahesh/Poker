# ??? -> Problem (understand) -> Spec (SPecify) -> Code (Actual Design)
# Hands Cards  Rank Suit
# Poker(hands) -> hand

# Hand Rank  =  hand -> 2 pair
# n-kind  (2, 3, 4) ,  Straight (suits don't matter) , flush  (same suit, rank don't matter)

# Representing Hands = ['JS', 'JD', '2Q'], or  [(11, 'Q'), (9, 'D')]   sets are good if we have a single deck, but when we have multiple deck, we can't have duplicates with sets

# Hands is a list
def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)
    
    
def hand_rank(hand):
    """ Returns the rank of the particular hand.
    >>> hand_rank(['J5'])
    5
    >> hand_rank('2Q')
    2
    """
    ranks = card_ranks(hand)
    if straight(hand) and flush(hand):
        return (8, max(ranks)) # 2 3 4 5 6  (8, 6)  6 7 8 9 T  (8, 10)
    elif kind(4, ranks):  # Here kind(4, ranks)  is used to return a bolean value
        # kind(4, ranks)  returns the int when true, returns false if not true (used as boolean)
        return (7, kind(4, ranks), kind(1, ranks)) # 9 9 9 9 3  (7, 9, 3)   9 9 9 9 5 (7, 9, 5)
    elif kind(3, ranks) and kind(2, ranks):        # full house
           return # your code here
    elif flush(hand):                              # flush
       return # your code here
    elif straight(ranks):                          # straight
       return # your code here
    elif kind(3, ranks):                           # 3 of a kind
       return # your code here
    elif two_pair(ranks):                          # 2 pair
       return # your code here
    elif kind(2, ranks):                           # kind
       return # your code here
    else:                                          # high card
           return # your code here
    
def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    st = "JS TS 9S 8S 7S".split() # Straight
    fl = "TD 8D 5D 3D 2D".split() # Flush 
    tk = "7C 7S 7H 5C 2D".split() # Three of a Kind
    tp = "JS JD 3D 3H KH".split() # Two of a kind
    p  = "2S 2D JC KH QS".split() # A Pair
    n  = "7C 5S 8H 9S 4C".split() # Nothing, or Highest card
    
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert hand_rank(st) == (5, 11)
    assert hand_rank(fl) == (4, [10, 8, 5, 3, 2])
    assert hand_rank(tk) == (3, 7, [7, 7, 7, 5, 2])
    assert hand_rank(tp) == (2, 11, 3, [13, 11, 11, 3, 3]) # King is the highest to sort the list high -> low                                                                                                                                        
    assert hand_rank(p) == (1, 2, [13, 12, 11, 2, 2])
    assert hand_rank(n) == (0, 9, 8, 7, 5, 4)
    
    return 'tests pass'
    
print test()

    

# print max([3, 4, 5, 0]), max([3, 4, -5, 0], key=abs)