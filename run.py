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
SHEET = GSPREAD_CLIENT.open('mini_tax_calculator_sheet')

info = SHEET.worksheet('payee-data')

data = info.get_all_values()

print(data)

def welcome_message():
    """
    Dispay greetings, information about the application
    and instruction for the user.
    """
    print("Welcome to Mini Tax Calculator.\n")
    print("This application will help You qickly calculate your taxes\n")
    print("The application needs to ask you for few informations that are necessary for calculate your taxes\n")
    print("All sensivite data are to be used for the calculations puposes only, and will never be shared")
    print("or used for any other purpose.")
    print(f"Welcome {validate_name(get_user_name())} Thank You for using our application")
    

def get_user_name():
    """
    Display asking for the users name.
    Returns that name.
    """
    return input("Please enter your name or nick here: ")

def validate_name(name):
    if name.replace(" ", "").isalpha():
        print ("Name is valid")
        return name
    else:
        print ("Name is invalid! Use letters from A to Z or a to z.")
        return validate_name(input("Please enter your name again "))

welcome_message()