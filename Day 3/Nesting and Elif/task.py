print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age >= 18:
        print("Fare is $27")
    elif 12 < age < 18:
        print("Fare is $20")
    else:
        print("Fare is $15")
else:
    print("Sorry you have to grow taller before you can ride.")
