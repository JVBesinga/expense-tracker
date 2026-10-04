# Expense Tracker - Installment 2
# Author: John Vincent Y. Besinga
# Asks for a name and two expenses, then prints a summary.

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

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2 if total > 0 else 0

print()
print("-" * 50)
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 50)
print("Made by: John Vincent Y. Besinga | Installment 2")