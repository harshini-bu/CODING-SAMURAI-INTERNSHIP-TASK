import json
import locale

# Set the locale to Indian English (en_IN)
locale.setlocale(locale.LC_ALL, 'en_IN')

def format_inr(amount):
    return locale.currency(amount, grouping=True)

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_expense(expenses, date, amount, category, description):
    expenses.append({
        "date": date,
        "amount": float(amount),
        "category": category,
        "description": description
    })

def list_expenses(expenses):
    for expense in expenses:
        formatted_amount = format_inr(expense['amount'])
        print(f"Date: {expense['date']}, Amount: {formatted_amount}, Category: {expense['category']}, Description: {expense['description']}")

def calculate_total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)
    return total

def generate_monthly_report(expenses):
    report = {}
    for expense in expenses:
        date_parts = expense["date"].split("-")
        month = date_parts[1]
        if month not in report:
            report[month] = {}
        category = expense["category"]
        amount = expense["amount"]
        if category not in report[month]:
            report[month][category] = 0
        report[month][category] += amount
    return report

if __name__ == "__main__":
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses")
        print("4. Generate Monthly Report")
        print("5. Save Expenses")
        print("6. Load Expenses")
        print("7. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            amount = input("Enter the amount: ")
            category = input("Enter the category: ")
            description = input("Enter a description: ")
            add_expense(expenses, date, amount, category, description)
            print("Expense added successfully!")

        elif choice == "2":
            list_expenses(expenses)

        elif choice == "3":
            total = calculate_total_expenses(expenses)
            formatted_total = format_inr(total)
            print(f"Total expenses: {formatted_total}")

        elif choice == "4":
            report = generate_monthly_report(expenses)
            for month, data in report.items():
                print(f"\nMonthly Report for {month}:")
                for category, amount in data.items():
                    formatted_amount = format_inr(amount)
                    print(f"Category: {category}, Total Amount: {formatted_amount}")

        elif choice == "5":
            save_expenses(expenses)
            print("Expenses saved successfully!")

        elif choice == "6":
            expenses = load_expenses()
            print("Expenses loaded successfully!")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
