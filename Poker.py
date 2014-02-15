# ??? -> Problem (understand) -> Spec (SPecify) -> Code (Actual Design)
# Hands Cards  Rank Suit
# Poker(hands) -> hand

# Hand Rank  =  hand -> 2 pair
# n-kind  (2, 3, 4) ,  Straight (suits don't matter) , flush  (same suit, rank don't matter)

# Representing Hands = ['JS', 'JD', '2Q'], or  [(11, 'Q'), (9, 'D')]   sets are good if we have a single deck, but when we have multiple deck, we can't have duplicates with sets

# Our implementation for a Hand [(11, 'Q'), (9, 'D')]    List of tuples containing Rank, Suit

# Hands is a list
def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)
    
    
def hand_rank(hand):
    """ Returns the rank of the particular hand.  Tuple consists of (major-rank, tie-breaker)
    >>> hand_rank(['J5'])
    5
    >> hand_rank('2Q')
    2
    """
    ranks = card_ranks(hand)  # ranks is a list of all the ranks. A sorted list of ranks is returned
    if straight(hand) and flush(hand):      # Straight flush
        return (8, max(ranks)) # 2 3 4 5 6  (8, 6)  6 7 8 9 T  (8, 10)
    elif kind(4, ranks):  # Here kind(4, ranks)  is used to return a bolean value
        # kind(4, ranks)  returns the int when true, returns false if not true (used as boolean)
        return (7, kind(4, ranks), kind(1, ranks)) # 9 9 9 9 3  (7, 9, 3)   9 9 9 9 5 (7, 9, 5)
    elif kind(3, ranks) and kind(2, ranks):        # full house
           return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
       return (5, ranks)
    elif straight(ranks):                          # straight
       return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
       return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
       return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
       return (1, kind(2, ranks), ranks)
    else:                                          # high card
           return (0, ranks)
    
def card_ranks(cards):
    """Return a list of the ranks, sorted with higher first."""
    ranks = ["--23456789TJQKA".index(r) for r,s in cards]  # Each card contains a rank and a suit,  hand/cards == [(11, 'Q'), (9, 'D')] 
    # Using a "Rank Strings Array" (i.e using an array to represent the rank strings)  to index it for the ranks
    ranks.sort(reverse=True)
    return ranks
    
    
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
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
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