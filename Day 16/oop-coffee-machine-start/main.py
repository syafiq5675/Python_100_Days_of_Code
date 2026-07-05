from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_machine = CoffeeMaker()
cashier = MoneyMachine()

menu_list = menu.get_items().strip("/").split("/")
menu_list.append("off")
menu_list.append("report")

def run_coffee_machine():
    ready = True

    while ready:
        take_order = input(f"What would you like? {menu.get_items()} : ").lower()

        if take_order not in menu_list:
            print("Please state your order from our menu only.")
            continue
        elif take_order == "off":
            print("Thank you. Please come again!")
            ready = False
        elif take_order == "report":
            print("Here is the current resources")
            coffee_machine.report()
            cashier.report()        
        else:
            order = menu.find_drink(take_order)
            is_sufficient_resources = coffee_machine.is_resource_sufficient(order)
            if not is_sufficient_resources:
                continue
        
            print(f"The price of {take_order} is {order.cost}. How would you like to pay?")
            
            is_payment_sufficient = cashier.make_payment(order.cost)

            if is_payment_sufficient:
                coffee_machine.make_coffee(order)
     

run_coffee_machine()