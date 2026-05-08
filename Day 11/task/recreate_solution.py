import art
import random

def deal_card():
    """A function to deal one card and return 1 card, an integer"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculate the total score aof all the card in hand. Also handle if the user have ace and blackjack"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == 'n':
        print("Lets play later. bye!")
        return
    elif play_game == 'y':
        pass

    print(art.logo)
    user_card = []
    computer_card = []
    is_game_over = False

    while is_game_over is not True:
        for _ in range (2):
            user_card.append(deal_card())
            computer_card.append(deal_card())



        print(f"{user_card}, score : {calculate_score(user_card)}")
        print(f"{computer_card}, score : {calculate_score(computer_card)}")
        result = compare(calculate_score(user_card), calculate_score(computer_card))
        print(result)

play_game()