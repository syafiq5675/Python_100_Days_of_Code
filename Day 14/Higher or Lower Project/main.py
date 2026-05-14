import art
from random import randint
from game_data import data

DATA = data

def pick_random_data():
    random_number = randint(0,49)
    random_data = DATA[random_number]
    return random_data

def compare_ab(a,b):
    a_follower = int(a["follower_count"])
    b_follower = int(b['follower_count'])
    if a_follower > b_follower:
        return "a"
    else:
        return "b"


game_over = False

while not game_over:
    score = 0

    a = pick_random_data()
    b = pick_random_data()
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(a['follower_count'])
    print(art.vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    print(b['follower_count'])
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    answer = compare_ab(a,b)
    if guess == answer:
        score + 1
    else:
        game_over = True
    print(f"your score = {score}")
    print(guess)
    print(answer)
    game_over = True