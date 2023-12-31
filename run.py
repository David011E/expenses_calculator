import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from dateutil.relativedelta import relativedelta

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('expenses_calculator')

def get_fName():
    """
    Get's users First name .
    """
    while True:
        print("Please Enter your First Name")
        data_str = input("Enter your First name here:\n")
        data_str = data_str.strip()  # Remove leading and trailing spaces

        if data_str.isalpha(): # checks if contains only alphabetic characters (letters).
            return data_str
        else:
            print("Cannot insert numbers or leave this empty. Please try again.\n")

def get_lName():
    """
    Get's users Last name .
    """
    while True:
        print("\nPlease Enter your Last Name")
        data_str = input("Enter your Last name here:\n")
        data_str = data_str.strip()  # Remove leading and trailing spaces

        if data_str.isalpha(): # checks if contains only alphabetic characters (letters).
            return data_str
        else:
            print("Cannot insert numbers or leave this empty. Please try again.\n")

def greet_user():
    """"
    Greets the user
    """
    first_name = get_fName()
    last_name = get_lName()

    print(f"\n Hello, {first_name} {last_name}! Welcome!")
    return first_name, last_name

def get_job_position():

    """"
    Asks user to select the job position and to confirm it
    """

    job_positions = {
        "a": {"name": "Management", "rate": 960},
        "b": {"name": "Marketing", "rate": 1600},
        "c": {"name": "Accountant", "rate": 800},
        "d": {"name": "Project manager", "rate": 1150},
        "e": {"name": "Business Analyst", "rate": 1300},
    }

    while True:
        print("\nSelect your job position")
        
        for key, position in job_positions.items():
            print(f"{key}: {position['name']}")

        options = input("\nSelect one of the above options (a-e): ").lower()

        if options in job_positions:
            while True:
                confirm = input(
                    f"You chose {job_positions[options]['name']}. "
                    "Is this correct? Enter (y/n) only: ").lower()
                if confirm == "y":
                    selected_job = job_positions[options]
                    print(f"You make ฿{selected_job['rate']} per day as a {selected_job['name']}.")
                    return selected_job
                elif confirm == "n":
                    break  # User doesn't want to confirm, break the inner loop
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
            # If 'n' was entered, continue to the outer loop for job selection
        else:
            print("Invalid job option. Please choose a valid job position.\n")

def user_selected_job(selected_job, first_name):
    """"
    Calculates how much the user has made by from the selected job * how many days are in this month
    """
    rate = selected_job["rate"]
     # Get the current date
    current_date = datetime.now()

    # Calculate the first day of the current month
    first_day_of_month = current_date.replace(day=1)

    # Calculate the last day of the current month
    last_day_of_month = (first_day_of_month + relativedelta(months=1)) - relativedelta(days=1)

    # Calculate the number of days in the current month
    days_in_current_month = (last_day_of_month - first_day_of_month).days + 1

    made_per_month = rate * days_in_current_month

    print(f"\n{first_name} You made ฿{made_per_month} per month!")
    return made_per_month

def expenses_this_month(first_name):
    """"
    Ask user how much in expenses do they have this month and ask to confirm
    """
    while True:
        expenses_str = input("How much in expenses do you have this month?\n")
        expenses_str = expenses_str.strip()

        if expenses_str.isdigit():
            expenses = int(expenses_str)
            confirm = input(
                f"{first_name}, You have ฿{expenses} in expenses this month. Is this correct? Enter (y/n) only: ").lower()
            if confirm == "y":
                print(f"You have confirmed ฿{expenses} in expenses for this month.")
                return expenses
            elif confirm == "n":
                continue  # User doesn't want to confirm, continue the loop
            else:
                print("Invalid input. Please enter 'y' or 'n.'")
        else:
            print("Invalid input. Please enter a valid number for expenses.")
        


def after_all_expenses(made_per_month, expenses, first_name):
    """"
    Calculates how much the user is left after all expenses
    """
    remaining = made_per_month - expenses

    print(f"{first_name} after all expenses, you have ฿{remaining} remaining. ")

    return remaining

def update_google_sheets(first_name, last_name, selected_job, made_per_month, expenses, remaining):
    """"
    Updates all data recived to google sheets
    """
    print("Updating worksheet...\n")
    expenses_calculator_worksheet = SHEET.worksheet("expenses_calculator")
    
    # Create a list containing all the values you want to append
    row_data = [first_name, last_name, selected_job['name'], made_per_month, expenses, remaining]
    
    # Append the row data to the worksheet
    expenses_calculator_worksheet.append_row(row_data)
    
    print("Worksheet updated successfully.\n")

def restart_program():
    """
    Asks the user if they want to restart the program again after thier finished
    """
    while True:
        user_input = input("Do you want to run the program again? (yes/no): ")
        if user_input.lower() == "no":
            print("Goodbye")
            break
        elif user_input.lower() == "yes":
            main()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    """"
    Run all program functions
    """
    first_name, last_name = greet_user()
    selected_job = get_job_position()
    made_per_month = user_selected_job(selected_job, first_name)
    expenses = expenses_this_month(first_name)
    remaining = after_all_expenses(made_per_month, expenses, first_name)
    update_google_sheets(first_name, last_name, selected_job, made_per_month, expenses, remaining)

print("Welcome to the Expenses Calculator for our bussines\n")

if __name__ == "__main__":
    main()
    restart_program()