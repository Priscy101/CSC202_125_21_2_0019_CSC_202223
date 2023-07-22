# Day_11
#Blackjack

import random

def deal_cards():
    cards = [11, 2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) ==21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)

def compare(u_cards, d_cards):
    if u_cards == d_cards:
        return "Draw "
    elif u_cards == 0:
        return "Blackjack, you win"
    elif d_cards == 0:
        return "Dealer has Blackjack, you lose "
    elif u_cards > 21:
        return "your cards are greater than 21, you lose"
    elif d_cards > 21:
        return "Dealer cards are greater than 21, you win"
    else:
        return "Dealers cards are higher, you lose"

    def playgame():
        user_cards = []
        dealer_cards = []
        is_playing = []

        for i in range(2):
            user_cards.append(deal_cards())
            dealer_cards.append(deal_cards())

        while is_playing:

            sum_user_cards = calculate_score(user_cards)
            sum_dealer_cards = calculate_score(dealer_cards)
        print(f"users cards: {user_cards}")
    print(f"dealer cards: {dealer_cards[0]}")
    if sum_user_cards == 0 or sum_user_cards > 21 or sum_dealer_cards == 0:
        is_playing = False

    else:
        another_card = input("press 'y' to deal an extra cards or 'n' to show results").lower()

        if another_card == "y":
            user_cards.append(deal_cards())
            print((user_cards))
            print(dealer_cards)
        else:
            is_playing = False

    while dealer_cards < 17:
        deal_cards.append(deal_cards())
        sum_dealer_cards = calculate_score(dealer_cards)

    print(f"your first score is{sum_user_cards}, {user_cards}")
    print(f"dealer final score is {sum_dealer_cards}, {deal_cards}")
    compare(sum_user_cards, sum_dealer_cards)

    while input("do you want to play a game of Blackjack, Y/N: ")== "Y":
        playgame()




