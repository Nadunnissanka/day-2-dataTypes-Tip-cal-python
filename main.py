#Tip calculator
print("Welcome to the Tip Calculator")
print("-----------------------------\n")
bill_amount = float(input("What was the total bill: $"))
percentage = int(input("What percentage tip would you like to give (10, 12 or 15):  "))
people = int(input("How many people to split the bill? "))

tip_of_each_person = ((bill_amount * percentage) / 100) / people
bill_of_each_person = bill_amount / people

total_bill_per_person = tip_of_each_person + bill_of_each_person
final_amount = "{:.2f}".format(total_bill_per_person)

print(f"Each person should pay: ${final_amount}")