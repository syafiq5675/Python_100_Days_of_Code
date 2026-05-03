import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

com_choice = [rock, paper, scissors]
com_input = random.choice(com_choice)

user_input = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))

if user_input >= 0 and user_input <= 2:
    print(com_choice[user_input])
else:
    print("Please input either 0/1/2 for your choice")

if 0<= user_input <=2:
    print("Computer Choose:\n" + com_input)

if user_input == 0: #Rock
    if com_input == rock:
        print("Draw.  choose again")
    elif com_input == paper:
        print("You lose")
    else:
        print("You win!")
elif user_input == 1: # paper
    if com_input == rock:
        print("You win!")
    elif com_input == paper:
        print("Draw.  choose again")
    else:
        print("You lose")
elif user_input == 2: #Scissors
    if com_input == rock:
        print("You lose")
    elif com_input == paper:
        print("You win!")
    else:
        print("Draw.  choose again")