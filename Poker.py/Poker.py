#  File: Poker.py

#  Description: Simulating Poker game

#  Student's Name: William Kwon

#  Student's UT EID: uk669

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:9/25/18

#  Date Last Modified:9/28/18
import random


class Card(object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__(self, rank=12, suit='S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__(self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit

    # equality tests
    def __eq__(self, other):
        return (self.rank == other.rank)

    def __ne__(self, other):
        return (self.rank != other.rank)

    def __lt__(self, other):
        return (self.rank < other.rank)

    def __le__(self, other):
        return (self.rank <= other.rank)

    def __gt__(self, other):
        return (self.rank > other.rank)

    def __ge__(self, other):
        return (self.rank >= other.rank)

 # constructor
class Deck(object):
    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(rank, suit)
                self.deck.append(card)

    # shuffle the deck

    def shuffle(self):
        random.shuffle(self.deck)

    # deal a card
    def deal(self):
        if (len(self.deck) == 0):
            return None
        else:

            return self.deck.pop(0)


class Poker(object):
    # all functions under classes are methods
    # methods = functions defined under a class
    # self is a tag that allows you to have access to the class' methods
    def __init__(self, num_players):
        self.deck = Deck()  # create a deck
        self.deck.shuffle()
        self.players = []
        numcards_in_hand = 5
        # deal all the hands
        for i in range(num_players):
            # start dealing out hands
            hand = []
            for j in range(numcards_in_hand):
                hand.append(self.deck.deal())
            self.players.append(hand)

    # simulates the play of the game
    def play(self):
        for i in range(len(self.players)):
            sortedHand = sorted(self.players[i], reverse=True)
            self.players[i] = sortedHand
            hand = ''
            for card in sortedHand:
                hand = hand + str(card) + ' '
            print('Player ' + str(i + 1) + " : " + hand)

            # determine the each type of hand and print
        points_hand = []  # create list to store points for each hand

    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_royal(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if (not rank_order):
            return 0

        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points

    # determine if a hand is straight flush
    def is_straight_flush(self, hand):
        # check if first card starts with A

        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[1 + i].suit)
        if (not same_suit):
            return 0
        return True

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == hand[i + 1].rank + 1)
        if (not rank_order):
            return 0

        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return  points

        # If there are two straight flushes, then which ever hand has the highest card value wins. In the above example, Hand 2 wins.

    def is_four_kind(self, hand):
        points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        same_rank = 1  # number count of cards with same rank
        for i in range(len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                same_rank = same_rank + 1
        if (same_rank == 4):
            return points
        else:
            return 0

    # In the event of a tie the hand that has highest ranking four of a kind cards wins. In the above example, Hand 2 wins.

    def is_full_house(self, hand):
        full = False  # is full house
        r1_count = 0  # number count of first group of same ranked cards
        r2 = 0  # unset second numerical rank
        r2_count = 0  # number count of second group of same ranked cards
        # finds count of first group
        for i in range(len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                r1_count = r1_count + 1
            else:
                r2 = hand[i].rank  # sets second rank
        # finds count of second group
        for i in range(len(hand)):
            if (hand[i].rank == r2):
                r2_count = r2_count + 1

        # checks full house condition
        if (r1_count == 3 or r1_count == 2):
            if (r2_count == (len(hand) - r1_count)):
                points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
                points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
                points = points + (hand[4].rank)
                return points
        return 0
    # If there are two full houses, then the hand that has the higher ranking cards for the three of a kind wins. In the above example, Hand 2 wins.

    def is_flush(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[1 + i].suit)
        if (not same_suit):
            return 0
        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return points

        # In the event of two flushes, the one with the highest ranking card wins. In the above example, Hand 1 wins

    def is_straight(self, hand):
        # check if 5 cards in numerical order
        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == hand[i + 1].rank + 1)
        if (not rank_order):
            return 0
        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return points


        # When there are two straight hands, then the one with the highest ranking card wins. In the above example, Hand 2 wins.

    def is_three_kind(self, hand):

        if (hand[0].rank == hand[1].rank == hand[2].rank):
             points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
             points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
             points = points + (hand[4].rank)
             return points
        elif (hand[1].rank == hand[2].rank == hand[3].rank):
             points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
             points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
             points = points + (hand[4].rank)
             return points
        elif (hand[2].rank == hand[3].rank == hand[4].rank):
             points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
             points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
             points = points + (hand[4].rank)
             return points
        return 0

    def is_two_pair(self, hand):
        if (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank):
            if (hand[0].rank != hand[4].rank) and (hand[2].rank != hand[4].rank):
                points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
                points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
                points = points + (hand[4].rank)
                return points
            else:
                return 0
        else:
            return 0


    # determine if a hand is one pair
    def is_one_pair(self, hand):
        one_pair = False
        for i in range(len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                one_pair = True
                break
        if (not one_pair):
            return 0

        points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points

    def is_high_card(self, hand):
        # return hand with highest rank, or very first card
        points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)
        return points


def main():
    # prompt user to enter the number of players
    num_players = int(input('Enter number of players: '))
    while ((num_players < 2) or (num_players > 6)):
        num_players = int(input('Enter number of players: '))

    # create the Poker object
    game = Poker(num_players)

    # play the game (poker)
    game.play()
    # add up total points
    types = []
    points_hand = []
    for i in range(num_players):
        # create a new list to hold all of the players' total points
        # current player's current hand
        players_hand = game.players[i]
        if (game.is_royal(players_hand)):
            points_hand.append(10)
            types.append('Royal Flush')
        elif (game.is_straight_flush(players_hand)):
            points_hand.append(9)
            types.append('Straight Flush')
        elif (game.is_four_kind(players_hand)):
            points_hand.append(8)
            types.append('Four of a Kind')
        elif (game.is_full_house(players_hand)):
            points_hand.append(7)
            types.append('Full House')
        elif (game.is_flush(players_hand)):
            points_hand.append(6)
            types.append('Flush')
        elif (game.is_straight(players_hand)):
            points_hand.append(5)
            types.append('Straight')
        elif (game.is_three_kind(players_hand)):
            points_hand.append(4)
            types.append('Three of a Kind')
        elif (game.is_two_pair(players_hand)):
            points_hand.append(3)
            types.append('Two Pair')
        elif (game.is_one_pair(players_hand)):
            points_hand.append(2)
            types.append('One Pair')
        elif (game.is_high_card(players_hand)):
            points_hand.append(1)
            types.append('High Card')

    print()

    for i in range(num_players):
        print("Player %d : %s" % (i + 1, types[i]))

    finalpts = []
    for i in range(num_players):
        # for each card in player's hand
        c1 = game.players[i][0].rank
        c2 = game.players[i][1].rank
        c3 = game.players[i][2].rank
        c4 = game.players[i][3].rank
        c5 = game.players[i][4].rank

        h = points_hand[i]

        total_points = h * 15 ** 5 + c1 * 15 ** 4 + c2 * 15 ** 3 + c3 * 15 ** 2 + c4 * 15 + c5

        finalpts.append(total_points)

    tie = []
    player_number = 1
    win = finalpts[0]
    for i in range(num_players):
        if (finalpts[i] > win):
            tie = []
            win = finalpts[i]
            player_number = i + 1
        elif (finalpts[i] == win):
            tie.append(i + 1)

    if (len(tie) > 1):
        for i in range(len(tie)):
            print("Player %d ties." % (tie_list[i]), '\n')

    print()

    print("Player %d wins." % (player_number))


main()