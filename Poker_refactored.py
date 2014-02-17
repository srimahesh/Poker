# ??? -> Problem (understand) -> Spec (SPecify) -> Code (Actual Design)
# Hands Cards  Rank Suit
# Poker(hands) -> hand

# Hand Rank  =  hand -> 2 pair
# n-kind  (2, 3, 4) ,  Straight (suits don't matter) , flush  (same suit, rank don't matter)

# Representing Hands = ['JS', 'JD', '2Q'], or  [(11, 'Q'), (9, 'D')]   sets are good if we have a single deck, but when we have multiple deck, we can't have duplicates with sets

# Our implementation for a Hand [(11, 'Q'), (9, 'D')]    List of tuples containing Rank, Suit

# Hands is a list

import random # this will be a useful library for shuffling

def poker(hands):
    "Return the best hand: poker([hand,...]) => [hand,..]"
    return allmax(hands, key=hand_rank)
    
def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable"
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if (not result) or (xval > maxval):
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result

def hand_rank(hand):
    """ Returns the rank of the particular hand.  Tuple consists of (major-rank, tie-breaker)
    >>> hand_rank(['J5'])
    5
    >> hand_rank('2Q')
    2

    # count is the count of each rank; ranks lists corresponding ranks
    # E.g. '7 T 7 9 7' => count = (3, 1, 1); ranks = (7, 10, 9)
    """
    groups = group(['--23456789TJQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return (9 if (5,) == counts else
            8 if straight and flush else
            7 if (4, 1) == counts else
            6 if (3, 2) == counts else
            5 if flush else
            4 if straight else
            3 if (3, 1, 1) == counts else
            2 if (2, 2, 1) == counts else
            1 if (2, 1, 1, 1) == counts else
            0), ranks


def group(items):
    "Return a list of [(count, x)...], highest count first, then highest x first."
    groups = [(items.count(x), x) for x in set(items)]    #  [((3,2), (1, 2)) ...]
    return sorted(groups, reverse=True)

def unzip(pairs): return zip(*pairs)  # (3, 1, 1), (7, 10, 9) ...

def card_ranks(cards):
    """Return a list of the ranks, sorted with higher first."""
    ranks = ["--23456789TJQKA".index(r) for r,s in cards]  # Each card contains a rank and a suit,  hand/cards == [(11, 'Q'), (9, 'D')] 
    # Using a "Rank Strings Array" (i.e using an array to represent the rank strings)  to index it for the ranks
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 3, 2, 1]) else ranks
    
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight"
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    "Return Ture if all the cards have the same suit"
    suits = [s for r,s in hand]
    return len(set(suits)) == 1
    
def kind(n, ranks):
    """ REturn the first rank that this hand has exaclty n of.
    Return None if there is no n-of-a-kind in the hand"""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None
    
def two_pair(ranks):
    """If there are two pair, return the two ranks as a 
    tuple: (highest, lowerst); otherwise return None."""
    pair = kind(2, ranks)  # Ranks are ordered, so this return the highest pair(if present)
    lowpair = kind(2, list(reversed(ranks)))  # ranks.reverse()  also works
    if pair and (lowpair != pair):
        return (pair, lowpair)
    else:
        return None
    
    
def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    st = "JS TS 9S 8S 7S".split() # Straight
    fl = "TD 8D 5D 3D 2D".split() # Flush 
    tk = "7C 7S 7H 5C 2D".split() # Three of a Kind
    tp = "5S 5D 9H 9C 6S".split() # Two of a kind
    p  = "2S 2D JC KH QS".split() # A Pair
    n  = "7C 5S 8H 9S 4C".split() # Nothing, or Highest card
    
    s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
    s2 = "2C 3C 4C 5S 6S".split() # 2-6 Straight
    ah = "AS 2S 3S 4S 6C".split() # A high
    sh = "s@ 3S 4S 6C 7D".split() # 7 high

    assert poker([s1, s2, ah, sh]) == s2
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5)
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
    assert hand_rank(tp) == (2, 9, 5, [9, 9, 6, 5, 5]) # King is the highest to sort the list high -> low                                                                                                                                        
    assert hand_rank(p) == (1, 2, [13, 12, 11, 2, 2])
    assert hand_rank(n) == (0, 9, 8, 7, 5, 4)
    
    return 'tests pass'
    
# print test()

# print max([3, 4, 5, 0]), max([3, 4, -5, 0], key=abs)


# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

# def deal(numhands, n=5, deck=mydeck):

# Providing a default deck. 
# Making the function as generic as possible for passing in other kinds of cards too.
def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    """Shuffle the deck and deal out numhands n-card hands."""
    # deals numhands hands with n cards each.
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

# print deal(2)
# print deal(2, 7, mydeck)

def hand_percentage(n=700*1000):
    "Sample n random hands and print a table of percentages for each type of hand"
    count = [0] * 9
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            count[ranking] += 1
    for i in reversed(range(9)):
        print "%14s: %6.3f %%" % (hand_names[i], 100.*count[i]/n)
 
 hand_percentage()