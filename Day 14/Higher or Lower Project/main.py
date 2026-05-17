import art
from random import randint
from game_data import data as DATA


def pick_random_data():
    return DATA[randint(0,len(DATA) - 1)]

def compare_ab(a,b):
    a_follower = a["follower_count"]
    b_follower = b['follower_count']
    if a_follower > b_follower:
        return "a"
    else:
        return "b"

def play_game():
    score = 0

    print(art.logo)
    continue_guessing = True

    a = pick_random_data()
    b = pick_random_data()

    while continue_guessing:

        if score > 0:
            print("\n" * 20)
            print(art.logo)
            print(f"You're right! Current score: {score}")
            a = b
            b = pick_random_data()
            while a == b:
                b = pick_random_data()

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(art.vs)
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        while guess != "a" and guess != "b":
            guess = input("Wrong input. Please answer either 'a' or 'b'.Who has more followers? Type 'A' or 'B': ").lower()
        answer = compare_ab(a,b)
        if guess == answer:
            score += 1
        else:
            continue_guessing = False
            print("\n"*20)
            print(art.logo)
            print(f"Sorry, that's wrong. Final score = {score}")

play_game()