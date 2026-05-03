import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

answer_list = list(placeholder)
display = ""
already_matched = []
lives = 6

while "_" in answer_list:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if guess == letter:
                answer_list[i] = guess
            else:
                pass
    else:
        lives -= 1
        print("Try again")
    answer = "".join(answer_list)
    print(answer)

    print(stages[lives])

print("Congratulations, you finished the word")