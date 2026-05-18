from source import MENU as MENU

ready = True

# 1. Ask user what would they like?
resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

while not ready:
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    # action = input("What would you like? (espresso/latte/cappucino): ")
    # if action in MENU:
    #     print(MENU[action])
    print(MENU["espresso"]["ingredients"]["milk"])
    ready = False

# 2. When user answer, check the resources, if it is enough to make the drink

def check_resources(drink):
    ingredients = MENU[drink]['ingredients']
    for ingredient, amount_needed in ingredients.items():
        if amount_needed > resources[ingredient]:
            print(f"Sorry. Not enough {ingredient}.")
            return False
    return True

# 3. If sufficient resources, prompt the user to insert coins. quarters (0.25), dimes (0.10), nickles (0.05), pennies (0.01) and return value

def process_coins():
    quarters = int(input('How many quarters? : ')) * 0.25
    dimes = int(input('How many dimes? : ')) * 0.1
    nickles = int(input('How many nickels? : ')) * 0.05
    pennies = int(input('How many pennies? : ')) * 0.01
    return quarters + dimes + nickles + pennies

paid = process_coins()
print(paid)

# 4.  store in money , return the balance if needed

def process_transactions(price):
    pass


# 5. Make the coffee. Deduct the resources that is used, return the coffee and print Here is your {drink}. Enjoy!

def make_coffee(drink):
    pass

# 6. Apart from the drink, make option to print report and switch off at the input

def show_report():
    pass

def run_coffee_machine():
    pass