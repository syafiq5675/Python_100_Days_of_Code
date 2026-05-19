from pickle import GLOBAL

from source import MENU as MENU

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

# 4.  store in money , return the balance if needed

def process_transactions(drink, payment, money):
    global moneys
    price = MENU[drink]['cost']
    print(type(price))
    print(type(money))
    moneys += price
    return round(payment - price, 2)

# 5. Make the coffee. Deduct the resources that is used, return the coffee and print Here is your {drink}. Enjoy!

def make_coffee(drink, balance):
    ingredients = MENU[drink]['ingredients']
    if balance > 0 or balance == 0:
        print(f"Here is ${balance} dollars in change")
        for ingredient, amount in ingredients.items():
            resources[ingredient] -= amount
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# 6. Apart from the drink, make option to print report and switch off at the input

def show_report():
    for resource, amount in resources.items():
        print(f"{resource.capitalize()} : {amount}")
    print(f"Money: ${moneys}")

resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        }
moneys = 0

def run_coffee_machine():
    # 1. Ask user what would they like?

    ready = True

    while not ready:
        action = input("What would you like? (espresso/latte/cappucino): ")
        if action in MENU:
            print(MENU[action])
        print(MENU["espresso"]["ingredients"]["milk"])
        ready = False