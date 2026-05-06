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

def decide_winner(user, comp):
    user_value = count_value(user)
    comp_value = count_value(comp)
    print(f"     Your final hand: {user}, final score: {user_value}\n"
          f"     Computer's final hand: {comp}, final score: {comp_value}")
    if user_value > comp_value:
        print("You win")
    elif user_value == comp_value:
        print("Draw")
    elif comp_value > user_value:
        print("You lose")

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

    give_card = True
    get_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_card == 'n':
        decide_winner(user_hand, dealer_hand)
    elif get_card == 'y':
        deal_card(user_hand)
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")

blackjack()