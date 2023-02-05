

import csv, os
from project import add_expense, delete_expense, view_expense_report

lines = []

def main():
    test_add_expense()
    test_delete_expense()
    test_view_expense_report()

def test_add_expense():
    global lines

    with open("tester.csv", "w") as file:
        file.write("ID,Date,Expense amount(USD),Spent at\n")

    add_expense("tester", "12/12/1212", "1000", "Testing1")
    add_expense("tester", "12/12/2222", "10000", "Testing2")

    with open("tester.csv", "r") as file:
        reader = list(csv.reader(file))
        assert reader[1][1] == "12/12/1212"
        assert reader[1][2] == "1000"
        assert reader[1][3] == "Testing1"
        assert reader[2][1] == "12/12/2222"
        assert reader[2][2] == "10000"
        assert reader[2][3] == "Testing2"
        lines = reader

def test_delete_expense():
    global lines

    delete_expense("tester", lines[1][0])
    with open("tester.csv", "r") as file:
        reader = list(csv.reader(file))
        assert len(reader) == 2
        assert reader[1] == lines[2]

def test_view_expense_report():
    global lines

    print(view_expense_report("tester"))
    testing_table = f"╒══════════════════════════════════════╤════════════╤═══════════════════════╤════════════╕\n│ ID                                   │ Date       │   Expense amount(USD) │ Spent at   │\n╞══════════════════════════════════════╪════════════╪═══════════════════════╪════════════╡\n│ {lines[2][0]} │ {lines[2][1]} │                 {lines[2][2]} │ {lines[2][3]}   │\n╘══════════════════════════════════════╧════════════╧═══════════════════════╧════════════╛"

    assert view_expense_report("tester") == testing_table
    os.remove("tester.csv")