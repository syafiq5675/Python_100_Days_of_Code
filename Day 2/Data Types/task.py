print("Welcome to the tip calculator")
Total_Bill = input("How much is the total bill?\n")
print(f"${Total_Bill}")
Tips = input("How much tip you want to give? 10, 12, 15\n")
People = input("How many people you want to split the bill?\n")

Tip = int(Total_Bill) * (int(Tips) + 1) / int(People)
print(f"Each person should pay : ${round(Tip, 2)}")