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

get_fName()

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

get_lName()