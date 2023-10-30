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

        if data_str:
            return data_str
        else:
            print("cannot leave this empty. Please try again.\n")

def get_lName():
    """
    Get's users Last name .
    """
    while True:
        print("\nPlease Enter your Last Name")
        data_str = input("Enter your Last name here:\n")
        data_str = data_str.strip()  # Remove leading and trailing spaces

        if data_str:
            return data_str
        else:
            print("cannot leave this empty. Please try again.\n")

def greet_user():
    first_name = get_fName()
    last_name = get_lName()

    print(f"Hello, {first_name} {last_name}! Welcome!")

greet_user()

def get_job_position():

    job_positions = {
        "a": {"name": "Management", "rate": 250},
        "b": {"name": "Marketing", "rate": 320},
        "c": {"name": "Accountant", "rate": 230},
        "d": {"name": "Project manager", "rate": 300},
        "e": {"name": "Business Analyst", "rate": 350},
    }

    while True:
        print("Select your job position")
        
        for key, position in job_positions.items():
            print(f"{key}: {position['name']}")

        options = input("\n Select one of the above options (a-e): ").lower()

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
                    break  # User doesn't want to confirm, break the loop
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        
        print("Please choose job position again.\n")

get_job_position()