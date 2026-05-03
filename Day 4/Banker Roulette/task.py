import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# random_number = random.randint(0, 4)
# random_friend = friends[random_number]
#
# print(random_number)
# print(random_friend)

random_friend = random.choice(friends)

print(random_friend)