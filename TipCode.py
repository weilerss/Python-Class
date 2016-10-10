print("Welcome to tipCalc 0.1!")
bill = float(raw_input("How much was the bill? "))
tip = round(bill * .15, 2)
print("Your tip amount is: ${}".format(tip))
total = bill + tip
print("Your total amount is: ${}".format(total))
raw_input("Press any key to exit!")
