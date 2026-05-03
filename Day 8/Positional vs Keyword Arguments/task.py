# # Functions with input
#
# def greet_with_name(greeting, name):
#     print(f"{greeting} {name}")
#     print(f"{greeting} {name}?")
#
#
# greet_with_name("Hello", "Jack Bauer")
#

def calculate_love_score(name1, name2):
    combined = name1.lower() + name2.lower()
    true_count = 0
    love_count = 0
    for letters in combined:
        for letter in "love":
            if letters == letter:
                love_count += 1
        for letter in "true":
            if letters == letter:
                true_count += 1
    print(f"True Count = {true_count}, Love Count = {love_count}")
    result = str(true_count) + str(love_count)
    print(f"Love Score is {result}")

calculate_love_score("Kanye West", "Kim Kardashian")