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

def get_valid_number(prompt):
    while True:
        number = input(prompt)
        try:
            valid_number = float(number)
            break
        except ValueError:
            print("That is not a valid number. Please try again.")
    return valid_number

def calculator():
    print(art.logo)
    continue_calculation = True

    initial_number = get_valid_number("Please input your first number? ")


    while continue_calculation:

        allowed_operations = ['+', '-', '*', '/']
        check_operations = True
        while check_operations:
            chosen_operation = input("+\n-\n*\n/\nPick an operation:  ")
            if chosen_operation in allowed_operations:
                check_operations = False
            else:
                print("Invalid choice. Please pick valid operations.")

        second_number = get_valid_number("What's the next number?:  ")
        while chosen_operation == "/" and second_number == 0.0:
            print("Number cannot be divided by 0.")
            second_number = get_valid_number("What's the next number?:  ")


        result = operations[chosen_operation](initial_number, second_number)
        print(f"{initial_number} {chosen_operation} {second_number} = {result}")

        should_continue = input(f"Type y to continue calculating with {result}, type 'n' to start a new calculation or type 'exit' to exit:  ").lower()

        if should_continue == "y":
            initial_number = result
        elif should_continue == "n":
            print("\n" * 20)
            initial_number = get_valid_number("Please input your first number? ")
        elif should_continue == "exit":
            continue_calculation = False
        else:
            print("Please input either 'y', 'n' or exit:  ")

calculator()