import art
import random

def compare_number(p_guess, answer):
    """Function to compare the guess and the answer and print hint either lower or higher"""
    if p_guess > answer:
        print("Too high.\n"
              "Guess again")
    elif p_guess < answer:
        print("Too low.\n"
              "Guess again")

def play_game():
    is_game_over = False
    random_number = random.choice(range(1, 101))
    while not is_game_over:
        print(art.logo)
        # print("The number is:" + str(random_number))
        print("Welcome to the Number Guessing Game!\n"
              "I'n thinking of a number between 1 and 100.")
        difficulty = (input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
        while difficulty not in ['easy', 'hard']:
            difficulty = input("Invalid choice. Type 'easy' or 'hard': ").lower()
        #Choose difficulty either easy or hard. If user didnt input easy or hard, ask again

        lives = 10 if difficulty == 'easy' else 5 if difficulty == 'hard' else 0
        # Assign lives either to 10 or 5 based on difficulty chosen
        guess = 0

        while guess != random_number and lives != 0:
            print(f"You have {lives} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            # let the user guess an number and shows how many attempt left
            # Checking to break the loop either lives reach 0 or user can guess
            if guess == random_number or lives == 0:
                is_game_over = True
            elif guess != random_number:
                lives -= 1
                if lives == 0:
                    is_game_over = True
            if lives != 0:
                compare_number(guess, random_number)  # compare the number using function and give hint



    if guess == random_number:
        print(f"You got it! The answer was {random_number}")
    else:
        print("You've run out of guesses. Refresh the page tu run again.")

play_game()