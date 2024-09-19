print("welcome to tip calculator!\n")

bill = float(input("Enter your total bill ₹"))
tip_percentage = float(input("What percentage of tip would you like to give?\n"))
people = int(input("How many people are going to split the bill? "))

tip_amount = (tip_percentage / 100) * bill

total_amount = bill + tip_amount

bill_divided_into_people = total_amount / people

print(f"Tip amount: ₹{tip_amount: .2f}")
print(f"Total amount to be paid ₹{total_amount: .2f}")
print(f"Every individul needs to pay ₹{bill_divided_into_people: .2f}")
