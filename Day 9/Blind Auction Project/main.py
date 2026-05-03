# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


from art import logo

print(logo)

bidder = {}

other_bidder = True

while other_bidder:
    name = input("What is your name?:   ")
    bid = int(input("What is your bid?:   $"))
    anymore = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    bidder[name] = bid
    if anymore == "no":
        other_bidder = False
    elif anymore == "yes":
        print("\n" * 20)

winner = ""
winner_value = 0
for key,value in bidder.items():
    if value > winner_value:
        winner = key
        winner_value = value

print(f"The winner is {winner} with a bid of ${winner_value}")