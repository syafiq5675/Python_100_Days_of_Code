import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(card_on_hand):
    card_on_hand.append(random.choice(cards))

def count_value(cards):
    total = 0
    for card in cards:
        total += card
    return total

def blackjack():
    play_blackjack = input("Do you want to play a game of Blackjack? type 'y' or 'n':  ")
    if play_blackjack == "y":
        pass
    elif play_blackjack == "n":
        print("Bye. Lets play later")
        return

    print(art.logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_hand = []
    dealer_hand = []

    deal_card(user_hand)
    deal_card(user_hand)
    deal_card(dealer_hand)

    print(f"     Your cards: {user_hand}, current score: {count_value(user_hand)}\n"
          f"     Computer's first card: {dealer_hand}")

