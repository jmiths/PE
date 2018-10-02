#!/usr/bin/python3

import enum

class card:
    def __init__(self,card):
        self.suit = card[1]
        if card[0] == "A":
            self.value = 14
        elif card[0] == "K":
            self.value = 13
        elif card[0] == "Q":
            self.value = 12
        elif card[0] == "J":
            self.value = 11
        elif card[0] == "T":
            self.value = 10
        else:
            self.value = int(card[0])
    def __repr__(self):
        return(str(self.value)+self.suit)
    def __eq__(self,other):
        if self.value == other.value:
            return True
    def __gt__(self,other):
        if self.value > other.value:
            return True
        else:
            return False
    def __lt__(self,other):
        if self.value < other.value:
            return True
        else:
            return False

def straight(hand):
    if hand[0].value + 1 == hand[1].value:
        if hand[1].value + 1 == hand[2].value:
            if hand[2].value + 1 == hand[3].value:
                if hand[3].value + 1 == hand[4].value:
                    return(5,hand[4],hand[3],hand[2],hand[1],hand[0])
    return False

def royal(hand):
    if hand[4].value == 14:
        if hand[3].value == 13:
            if hand[2].value == 12:
                if hand[1].value == 11:
                    if hand[0].value == 10:
                        return True
    return False

def flush(hand):
    if hand[0].suit == hand[1].suit:
        if hand[1].suit == hand[2].suit:
            if hand[2].suit == hand[3].suit:
                if hand[3].suit == hand[4].suit:
                    return (6,hand[4],hand[3],hand[2],hand[1],hand[0])
    return False

def fourkind(hand):
    if hand[1] == hand[2] and hand[2] == hand[3]:
        if hand[0] == hand[1]:
            return(8,hand[0].value,hand[4].value)
        elif hand[3] == hand[4]:
            return(8,hand[1].value,hand[0].value)
    return False

def threekind_or_full(hand):
    if hand[0] == hand[1] and hand[1] == hand[2]:
        if hand[3] == hand[4]:
            return(7,hand[1].value,hand[3].value)
        else:
            return(4,hand[2].value,hand[4].value,hand[3].value)
    if hand[1] == hand[2] and hand[2] == hand[3]:
        return(4,hand[3].value,hand[4].value,hand[0].value)
    if hand[2] == hand[3] and hand[3] == hand[4]:
        if hand[0] == hand[1]:
            return(7,hand[3].value,hand[0].value)
    return False

def twopair(hand):
    if hand[0] == hand[1]:
        if hand[2] == hand[3]:
            return(3,hand[2].value,hand[0].value,hand[4].value)
        if hand[3] == hand[4]:
            return(3,hand[3].value,hand[0].value,hand[2].value)
    if hand[1] == hand[2]:
        if hand[3] == hand[4]:
            return(3,hand[3].value,hand[1].value,hand[0].value)
    return False

def onepair(hand):
    if hand[0] == hand[1]:
        return(2,hand[0].value,hand[4],hand[3],hand[2].value)
    if hand[1] == hand[2]:
        return(2,hand[1].value,hand[4],hand[3],hand[0].value)
    if hand[2] == hand[3]:
        return(2,hand[2].value,hand[4],hand[1],hand[0].value)
    if hand[3] == hand[4]:
        return(2,hand[3].value,hand[2],hand[1],hand[0].value)
    return False

def hand_decider(hand):
# Return code, tie breaker
#HC 1
#OP 2
#TP 3
#TK 4
#S  5
#F  6
#FH 7
#FK 8
#SF 9
#RF 10
    max_hand = 0
    payload = 0
    ret = 0
    ret = flush(hand) # What about a full house flush
    if ret:
        max_hand = 6
        payload = ret
        ret = royal(hand)
        if ret:
            max_hand = 10
            payload = ret
        ret = straight(hand)
        if ret and max_hand != 10:
            max_hand = 9
            payload = ret
        else:
            max_hand = 6
    ret = threekind_or_full(hand)
    if ret:
        if ret[0] > max_hand:
            payload = ret
            max_hand = ret[0]
    ret = fourkind(hand)
    if ret:
        if ret[0] > max_hand:
            max_hand = 8
            payload = ret
    if max_hand >= 6:
        return payload

    ret = twopair(hand)
    if ret:
        if ret[0] > max_hand:
            payload = ret
            max_hand = ret[0]
    ret = onepair(hand)
    if ret:
        if ret[0] > max_hand:
            payload = ret
            max_hand = ret[0]
    else: # High card
        return(1,hand[4],hand[3],hand[2],hand[1],hand[0]) 
    return payload


P1Wins = 0
with open('poker.txt') as f:
    for line in f:
        deck = (line.replace('\n','')).split(" ")
        H1 = [card(x) for x in deck[:5]]
        H2 = [card(x) for x in deck[5:]]
        H1 = sorted(H1,key=lambda card: card.value)
        H2 = sorted(H2,key=lambda card: card.value)
        H1 = hand_decider(H1)
        H2 = hand_decider(H2)
#        print(H1)
#        print(H2)
        for i in range(len(H1)):
            if H1[i] > H2[i]:
                P1Wins = P1Wins + 1
                break
            elif H1[i] < H2[i]:
                break
print(P1Wins)
