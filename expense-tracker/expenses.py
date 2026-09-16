

expenses = []
categories = set()
default_categories = ("Food", "Travel", "Shopping", "Education", "Other")
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    categories.add(category)
    print("Expense added successfully!")
def display_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return
    for expense in expenses:
        print("Expense:", expense["name"])
        print("Amount:", expense["amount"])
        print("Category:", expense["category"])



def search_expense():

    name = input("Enter expense name to search: ")

    for expense in expenses:

        if expense["name"].lower() == name.lower():

            print("Expense Found")
            print("Name:", expense["name"])
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])

            return

    print("Expense not found.")



def update_expense():

    name = input("Enter expense name to update: ")

    for expense in expenses:

        if expense["name"].lower() == name.lower():

            new_name = input("Enter new expense name: ")
            new_amount = float(input("Enter new amount: "))
            new_category = input("Enter new category: ")

            expense["name"] = new_name
            expense["amount"] = new_amount
            expense["category"] = new_category

            categories.add(new_category)

            print("Expense updated successfully!")
            return

    print("Expense not found.")



def delete_expense():

    name = input("Enter expense name to delete: ")

    for expense in expenses:

        if expense["name"].lower() == name.lower():

            expenses.remove(expense)

            print("Expense deleted successfully!")
            return

    print("Expense not found.")



def calculate_total():

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense =", total)

    return total



def highest_expense():

    if len(expenses) == 0:
        print("No expenses found.")
        return

    highest = expenses[0]

    for expense in expenses:

        if expense["amount"] > highest["amount"]:
            highest = expense

    print("Highest Expense")
    print("Name:", highest["name"])
    print("Amount:", highest["amount"])
    print("Category:", highest["category"])



def lowest_expense():

    if len(expenses) == 0:
        print("No expenses found.")
        return

    lowest = expenses[0]

    for expense in expenses:

        if expense["amount"] < lowest["amount"]:
            lowest = expense

    print("Lowest Expense")
    print("Name:", lowest["name"])
    print("Amount:", lowest["amount"])
    print("Category:", lowest["category"])



def category_expense():

    category = input("Enter category: ")

    total = 0

    for expense in expenses:

        if expense["category"].lower() == category.lower():
            total = total + expense["amount"]

    print("Total spent on", category, "=", total)

    return total




# Main Program
while True:

    print("\n===== EXPENSE TRACKER =====")

    print("1. Add Expense")
    print("2. Display Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Calculate Total Expense")
    print("7. Highest Expense")
    print("8. Lowest Expense")
    print("9. Category-wise Expense")

    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expense()

    elif choice == 2:
        display_expenses()

    elif choice == 3:
        search_expense()

    elif choice == 4:
        update_expense()

    elif choice == 5:
        delete_expense()

    elif choice == 6:
        calculate_total()

    elif choice == 7:
        highest_expense()

    elif choice == 8:
        lowest_expense()

    elif choice == 9:
        category_expense()

  
    elif choice == 10:
        print("Expense tracker ended.")
        break

    else:
        print("Invalid choice!")