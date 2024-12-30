import csv
import os

# File where expenses will be saved
EXPENSES_FILE = 'expenses.csv'

# Function to check if file exists, if not create it with headers
def initialize_expenses_file():
    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Description', 'Amount'])

# Function to add a new expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, Bills): ")
    description = input("Enter a description: ")
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount entered. Please enter a number.")
        return

    with open(EXPENSES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully.")

# Function to view all expenses
def view_expenses():
    try:
        with open(EXPENSES_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            total = 0
            print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':<10}")
            print("-" * 65)
            for row in reader:
                print(f"{row[0]:<15}{row[1]:<15}{row[2]:<25}{row[3]:<10}")
                total += float(row[3])
            print("-" * 65)
            print(f"Total expenses: {total}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Function to show menu options
def menu():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    initialize_expenses_file()
    menu()
