# ??? -> Problem (understand) -> Spec (SPecify) -> Code (Actual Design)
# Hands Cards  Rank Suit
# Poker(hands) -> hand

# Hand Rank  =  hand -> 2 pair
# n-kind  (2, 3, 4) ,  Straight (suits don't matter) , flush  (same suit, rank don't matter)

# Representing Hands = ['JS', 'JD', '2Q'], or  [(11, 'Q'), (9, 'D')]   sets are good if we have a single deck, but when we have multiple deck, we can't have duplicates with sets

# Hands is a list

import random # this will be a useful library for shuffling

def poker(hands):
    "Return the best hand: poker([hand,...]) => [hand,..]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # Your code here.
    list = []
    # return [list.append(a) if iterable.next == max(iterable) for a in iterable.next]
    a = 1
    while a: 
        a = iterable.next()
        if a == max(iterable):
            list.append(a)
    return a    
    
def hand_rank(hand):
    """ Returns the rank of the particular hand.
    >>> hand_rank(['J5'])
    5
    >> hand_rank('2Q')
    2
    """
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif straight(ranks):                          # straight
        return (5, max(ranks))
    elif flush(hand):                              # flush
        return (4, ranks.sort())   #  (4, ranks)
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks.sort())
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks.sort())
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks.sort)
    else:                                          # high card
        ranks.sort()
        return (0, ranks[0], ranks[1], ranks[2], ranks[3], ranks[4])


        
def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [map(r) for r,s in cards]
    ranks.sort(reverse=True)
    return ranks

def map(r):
    if r == 'T':
        return '10'
    elif r == 'J':
        return '11'
    elif r == 'Q':
        return '12'
    elif r == 'K':
        return '13'
    elif r == 'A':
        return '14'
    else:
        return r
        
        
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight"
    for i in range(0, 4):
        if ranks[i] - 1 != ranks[i + 1]:
            return False
    return True
    
def flush(hand):
    "REturn True if all the cards have the same suit"
    suits = [s for r,s in hand]
    for i in range(0, 4):
        if suits[i] != suits[i + 1]:
            return False
    return True
          
### Should use the built-in funcitons more effectively
def kind(n, ranks):
    """ REturn the first rank that this hand has exaclty n of.
    Return None if there is no n-of-a-kind in the hand"""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None
    
def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    two_pair = []
    set_ranks = set(ranks)
    for r in set_ranks:
        if ranks.count(r) == 2: two_pair.append(r)
    
    if len(two_pair) == 2: 
        two_pair.sort(reverse=True)
        return (two_pair[0], two_pair[1])
    return None
    
def sort_ranks(ranks):
    """ Returns a sorted_list of the ranks
    >>> sort_ranks([10, 15, 2, 4, 5])
    [15, 10, 5, 4, 2]
    """
    sorted_list = ranks
    return sorted_list.sort()
     
     
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
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
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


# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    """deals numhands hands with n cards each."""
    # Deck consists of  ['2S', ..]     with random methods get one card randomly  2C  
    # numhands == # of players      hand == n random cards
    random.shuffle(mydeck)
    hands = [random.sample(mydeck, 1)  for _ in numhands for _ in n]
    return hands


