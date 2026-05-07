import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack = [11, 10]

def deal_card(card_on_hand, number):
    while number != 0:
        card_on_hand.append(random.choice(cards))
        number -= 1

def calculate_score(player_cards):
    score = sum(player_cards)
    aces = player_cards.count(11)
    while aces != 0 and score > 21:
        score -= 10
        aces -= 1
    return score

def decide_winner(user_cards, comp_cards):
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)
    print(f"     Your final hand: {user_cards}, final score: {user_score}\n"
          f"     Computer's final hand: {comp_cards}, final score: {comp_score}")
    if set(user_cards) == blackjack and len(user_cards) == 2:
        print("Marvelous. You got black jack. you win")
    elif user_score > 21:
        print("You went over. You lose")
    elif comp_score > 21 or user_score > comp_score:
        print("You win")
    elif user_score < comp_score:
        print("You lose")
    elif user_score == comp_score:
        print("Draw")

def show_score(user, comp):
    print(f"     Your cards: {user}, current score: {calculate_score(user)}\n"
          f"     Computer's card: {comp}")

def blackjack():
    continue_game = True
    while continue_game:
        play_blackjack = input("Do you want to play a game of Blackjack? type 'y' or 'n':  ")
        if play_blackjack == "y":
            pass
        elif play_blackjack == "n":
            print("Bye. Lets play later")
            return

        print(art.logo)
        user_hand = []
        dealer_hand = []

        deal_card(user_hand, 2)
        deal_card(dealer_hand, 1)

        show_score(user_hand, dealer_hand)
        give_card = True
        while give_card: # Player deal card
            get_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_card == 'n':
                give_card = False
            elif get_card == 'y':
                deal_card(user_hand, 1)
                if calculate_score(user_hand) == 21:
                    decide_winner(user_hand, dealer_hand)
                    give_card = False
                elif calculate_score(user_hand) > 21:
                    decide_winner(user_hand, dealer_hand)
                    give_card = False
                else:
                    show_score(user_hand, dealer_hand)
        while calculate_score(dealer_hand) < 17:
            deal_card(dealer_hand, 1)
        if calculate_score(user_hand) < 21:
            decide_winner(user_hand, dealer_hand)


blackjack()