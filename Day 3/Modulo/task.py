number = int(input("Please enter a number:"))

oddOrEven = number % 2

if oddOrEven == 0:
    print(f'Entered number ({number}) is an even number')
else:
    print(f'Entered number ({number}) is an odd number')