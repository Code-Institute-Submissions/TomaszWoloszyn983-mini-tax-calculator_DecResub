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
    print("All sensivite data are to be used for the calculations purposes only, and will never be shared")
    print("or used for any other purpose.")
    print(f"Welcome {get_user_name()} Thank You for using our application")
    

def get_user_name():
    """
    Display asking for the users name.
    Returns that name.
    """
    return validate_name(input("Please enter your name or nick here: "))

def validate_name(name):
    """
    Validate input data
    Check if the name doesn't contain other than
    letters. Accepted are only upper and lowercase letters.
    """
    if name.replace(" ", "").isalpha():
        print ("Name is valid!")
        return name
    else:
        print ("Name is invalid! Use letters from A to Z or a to z.")
        return validate_name(input("Please enter your name again "))


def quit_all():
    """
    This function is called when Q-key is pressed on the keyboard 
    it interrupts the whole process and 
    moves the user to the welcome_message function where he can 
    start the application from the beginning.
    """
    print("Are you sure you want to quit the process and return to the beginning?")
    while True:
        confirm = input('Press "Y" or "N" to cancel\n')
        if confirm.upper() == "Y":
            print("Process interrupted by the user\n\n")
            welcome_message()
            break
        elif confirm.upper() == "N":
            print("Return to the process\n")
            break
        else:
            print('Tap "Y" to submit or "N" to return to the previous process')


def request_salary():
    """
    Request salary from the user. 
    If the entered value has to be validated for being integer and 
    having the right format.
    If the user doesn't know the value of his salary it can be 
    calculated after typing C-key on keyboard.
    """
    print("\nWe are going to need your weekly salary to calculate your taxes.")
    while True:
        print('Please enter your weekly salary or type "C" to calculate it.')
        print('If you want to quit You can press "Q". ')
        user_input = input()
        if user_input.upper() == "Q":
            quit_all()
        elif user_input.upper() == "C":
            print("Not defined yet")
        else:
            print("We are going to calculate taxes")

def main():
    welcome_message()
    request_salary()

main()