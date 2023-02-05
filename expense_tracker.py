import sys, csv, uuid
from tabulate import tabulate

def main():
    name = input("Type your username(without space)?: ").strip().replace(" ", "").lower()
    try:
        with open(f"{name}.csv", "r") as file:
            pass
    except FileNotFoundError:
        with open(f"{name}.csv", "w") as file:
            file.write("ID,Date,Expense amount(USD),Spent at\n")
    while True:
        action = input("===================================================\nType '1' to add new expense \nType '2' to delete an expense \nType '3' to view full expense list \nType '4' to close the application \n===================================================\nType a number: ").strip()
        if action == "1":
            expense_date = input("Date of expenditure in 'day/month/year' format (E.g. '16/07/1998') : ")
            expense_amount = input("Expenditure amount in USD: ")
            spent_at = input("Spent at: ")
            add_expense(name, expense_date, expense_amount, spent_at)

        elif action == "2":
            uid = input("Type the ID of the expense that you want to delete: ").strip()
            delete_expense(name, uid)
        elif action == "3":
            print(view_expense_report(name))
        elif action == "4":
            sys.exit("See you soon, Bye!")
        else:
            print("Wrong action, type again")



def add_expense(name, expense_date, expense_amount, spent_at):
    uid = uuid.uuid4()
    with open(f"{name}.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Date", "Expense amount(USD)", "Spent at"])
        writer.writerow({"ID": uid, "Date": expense_date, "Expense amount(USD)": expense_amount, "Spent at": spent_at})



def delete_expense(name, uid):
    expenses=[]
    with open(f"{name}.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["ID"] != uid:
                expenses.append(row)

    with open(f"{name}.csv", "w") as file:
        file.write("ID,Date,Expense amount(USD),Spent at\n")
        writer = csv.DictWriter(file, fieldnames=["ID", "Date", "Expense amount(USD)", "Spent at"])
        for expense in expenses:
            writer.writerow(expense)



def view_expense_report(name):
    with open(f"{name}.csv", "r") as file:
        rows = list(csv.reader(file))
        headers = rows[0]
        table = rows[1:]
        return(tabulate(table, headers,  tablefmt="fancy_grid"))


if __name__ == "__main__":
    main()