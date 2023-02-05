# Expense Tracker

#### **Video Demo:**  <https://youtu.be/kl50_L8Zs_Q>

#### **Description:**
A command line application to track expenses. The application takes input from the user and stores it in a `.csv` file with the user's name. The user can then perform actions such as adding a new expense, deleting an expense, or viewing a full list of expenses.

#### **Dependencies:**
- `Python 3`
- `sys`
- `csv`
- `uuid`
- `tabulate`

#### **Usage:**
To run the application, open a terminal and navigate to the directory where the script is located. Run the following command:

```
python3 project.py
```

The script will prompt you to enter your username (without any spaces). A CSV file with the name `{username}.csv` will be created if it doesn't already exist.

You will then be presented with a menu of options:

- Type `1` to add a new expense
- Type `2` to delete an expense
- Type `3` to view a full expense report
- Type `4` to close the application

Follow the prompts to add, delete, or view expenses. The expense report will be printed in a table format.

#### **Functions:**

`add_expense(name, expense_date, expense_amount, spent_at)`

This function takes four arguments:

- `name:` the name of the user
- `expense_date:` the date of the expense in the format 'day/month/year' (e.g. '16/07/1998')
- `expense_amount:` the amount of the expense in USD
- `spent_at:` a description of where the expense was spent

The function generates a unique ID for the expense using the uuid module, and appends the expense data to the user's `.csv` file.

`delete_expense(name, uid)`

This function takes two arguments:

- `name:` the name of the user
- `uid:` the unique ID of the expense to be deleted

The function reads the user's `.csv` file, and removes the expense with the matching ID. The updated list of expenses is then written back to the `.csv` file.

`view_expense_report(name)`

This function takes one argument:

- `name:` the name of the user

The function reads the user's `.csv` file and returns the full list of expenses in a formatted table using the `tabulate` module.

#### **CSV File Format:**
The CSV file has the following structure:


| ID           | Date         | Expense amount  | Spent at      |
|:-------------|:-------------|:---------------:|--------------:|
| {uuid}       | {date}       | {amount}        | {location}    |
| {uuid}       | {date}       | {amount}        | {location}    |
| ...          | ...          | ...             | ...           |

The `ID` column contains a unique identifier for each expense. The `Date` column contains the date of the expenditure in the format `day/month/year`. The `Expense amount` column contains the amount spent in USD. The `Spent at` column contains the location where the expense was incurred.