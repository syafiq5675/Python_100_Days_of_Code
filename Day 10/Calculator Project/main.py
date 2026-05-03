import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    continue_calculation = True
    initial_number = float(input("What's the first number?:  "))

    while continue_calculation == True:

        chosen_operation = input("+\n-\n*\n/\nPick an operation:  ")
        second_number = float(input("What's the next number?:  "))

        result = operations[chosen_operation](initial_number, second_number)
        print(f"{initial_number} {chosen_operation} {second_number} = {result}")

        should_continue = input(f"Type y to continue calculating with {result}, type 'n' to start a new calculation or type 'exit' to exit:  ").lower()

        if should_continue == "y":
            initial_number = result
        elif should_continue == "n":
            print("\n" * 20)
            calculator()
        elif should_continue == "exit":
            continue_calculation = False
        else:
            print("Please input either 'y', 'n' or exit:  ")

calculator()