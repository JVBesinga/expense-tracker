# Expense Tracker - Installment 3
# Author: John Vincent Y. Besinga
# Asks for expenses, tax rate and budget, then prints a summary.

print("=" * 50)
print("\t\tEXPENSE TRACKER")
print("\t  Know where your money goes.")
print("=" * 50)
print()
print("MAIN MENU")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)")
print()

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

average = subtotal / 2
tax = subtotal * tax_percent / 100
total = subtotal + tax
over_budget = total > budget
left = budget - total

print()
print("-" * 50)
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 50)
print("Made by: John Vincent Y. Besinga | Installment 3")