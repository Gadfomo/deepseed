import datetime


budget_data = {}  



def validate_month(month_str):
    try:
        datetime.datetime.strptime(month_str, "%Y-%m")
        return True
    except ValueError:
        return False

def add_income(month):
    category = input("Enter income category (e.g., salary): ").strip()
    amount = float(input(f"Enter amount for {category}: $"))
    budget_data.setdefault(month, {}).setdefault("income", {})
    budget_data[month]["income"][category] = budget_data[month]["income"].get(category, 0) + amount
    print("Income added successfully.\n")

def add_expense(month):
    category = input("Enter expense category (e.g., food): ").strip()
    amount = float(input(f"Enter amount for {category}: $"))
    budget_data.setdefault(month, {}).setdefault("expenses", {})
    budget_data[month]["expenses"][category] = budget_data[month]["expenses"].get(category, 0) + amount
    print("Expense added successfully.\n")

def set_budget(month):
    category = input("Set budget for which expense category? ").strip()
    limit = float(input(f"Enter budget limit for {category}: $"))
    budget_data.setdefault(month, {}).setdefault("budgets", {})
    budget_data[month]["budgets"][category] = limit
    print("Budget limit set.\n")

def calculate_summary(month):
    data = budget_data.get(month, {})
    incomes = data.get("income", {})
    expenses = data.get("expenses", {})
    budgets = data.get("budgets", {})

    total_income = sum(incomes.values())
    total_expense = sum(expenses.values())
    net_savings = total_income - total_expense
    savings_percent = (net_savings / total_income * 100) if total_income > 0 else 0

    print("\n=== PERSONAL BUDGET TRACKER ===")
    print(f"Month: {datetime.datetime.strptime(month, '%Y-%m').strftime('%B %Y')}\n")

    print("FINANCIAL SUMMARY")
    print(f"Total Income: ${total_income:,.2f}")
    print(f"Total Expenses: ${total_expense:,.2f}")
    print(f"Net Savings: ${net_savings:,.2f} ({savings_percent:.1f}%)\n")

    print("EXPENSE BREAKDOWN")
    for cat, amt in expenses.items():
        percent = (amt / total_expense * 100) if total_expense > 0 else 0
        bar = "█" * int(percent / 3) + "░" * (30 - int(percent / 3))
        print(f"{cat.ljust(12)} {bar} ${amt:.0f} ({percent:.1f}%)")
    print()

    alerts = []
    for cat, limit in budgets.items():
        spent = expenses.get(cat, 0)
        if spent > limit:
            alerts.append(f"{cat}: ${spent - limit:.0f} over budget ({(spent / limit * 100):.0f}% of limit)")

    if alerts:
        print("BUDGET ALERTS:")
        for alert in alerts:
            print(alert)
        print()

def export_summary(month):
    filename = f"budget_summary_{month}.txt"
    with open(filename, "w") as f:
        data = budget_data.get(month, {})
        incomes = data.get("income", {})
        expenses = data.get("expenses", {})
        budgets = data.get("budgets", {})

        total_income = sum(incomes.values())
        total_expense = sum(expenses.values())
        net_savings = total_income - total_expense
        savings_percent = (net_savings / total_income * 100) if total_income > 0 else 0

        f.write(f"=== PERSONAL BUDGET TRACKER ===\nMonth: {month}\n\n")
        f.write("FINANCIAL SUMMARY\n")
        f.write(f"Total Income: ${total_income:.2f}\n")
        f.write(f"Total Expenses: ${total_expense:.2f}\n")
        f.write(f"Net Savings: ${net_savings:.2f} ({savings_percent:.1f}%)\n\n")

        f.write("EXPENSE BREAKDOWN\n")
        for cat, amt in expenses.items():
            percent = (amt / total_expense * 100) if total_expense > 0 else 0
            f.write(f"{cat}: ${amt:.2f} ({percent:.1f}%)\n")

        f.write("\nBUDGET ALERTS:\n")
        for cat, limit in budgets.items():
            spent = expenses.get(cat, 0)
            if spent > limit:
                f.write(f"{cat}: ${spent - limit:.2f} over budget ({(spent / limit * 100):.0f}% of limit)\n")
    print(f"Summary exported to {filename}.\n")

# === MAIN EXECUTION ===

while True:
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Set Monthly Budget")
    print("4. View Summary")
    print("5. Export Summary")
    print("6. Exit")

    choice = input("Choose an option: ").strip()

    if choice in {"1", "2", "3", "4", "5"}:
        month = input("Enter month (YYYY-MM): ").strip()
        if not validate_month(month):
            print("Invalid date format. Use YYYY-MM.\n")
            continue

    if choice == "1":
        add_income(month)
    elif choice == "2":
        add_expense(month)
    elif choice == "3":
        set_budget(month)
    elif choice == "4":
        calculate_summary(month)
    elif choice == "5":
        export_summary(month)
    elif choice == "6":
        print("Exiting Budget Tracker.")
        break
    else:
        print("Invalid choice.\n")
