import gspread
from google.oauth2.service_account import Credentials

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
    first_name = get_fName()
    last_name = get_lName()

    print(f"\n Hello, {first_name} {last_name}! Welcome!")
    return first_name, last_name

first_name, last_name = greet_user()

def get_job_position():

    job_positions = {
        "a": {"name": "Management", "rate": 250},
        "b": {"name": "Marketing", "rate": 320},
        "c": {"name": "Accountant", "rate": 230},
        "d": {"name": "Project manager", "rate": 300},
        "e": {"name": "Business Analyst", "rate": 350},
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

selected_job = get_job_position()

def user_selected_job(selected_job, first_name):
    rate = selected_job["rate"]
    made_per_month = rate * 30

    print(f"\n{first_name} You made ฿{made_per_month} per month!")

made_per_month = user_selected_job(selected_job, first_name)

def expenses_this_month(first_name):
    while True:
        expenses_str = input("How much in expenses do you have this month?\n")
        expenses_str = expenses_str.strip()  

        if expenses_str.isdigit(): 
            expenses = int(expenses_str)
            print(f"\n{first_name} You have ฿{expenses_str} in expenses this month")
            return expenses
        else:
            print("Cannot leave this empty or enter any words. Please try again.\n")

expenses = expenses_this_month(first_name)