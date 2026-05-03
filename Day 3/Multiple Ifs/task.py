print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    want_photos = input("Do you want photos? Y/N")
    if age <= 12:
        if want_photos == "Y":
            print("Child ticket are $8.")
        else:
            print("Child ticket are $5.")
    elif age <= 18:
        if want_photos == "Y":
            print("Youth ticket are $10.")
        else:
            print("Youth ticket are $7.")
    else:
        if want_photos == "Y":
            print("Adult ticket are $15.")
        else:
            print("Adult ticket are $12.")




else:
    print("Sorry you have to grow taller before you can ride.")
