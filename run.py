import gspread
from google.oauth2.service_account import Credentials
import time

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
# prints data from the google sheets

def welcome_message():
    """
    Dispays greetings, information about the application
    and instruction for the user.
    """
    print("\n\n\tWelcome to Mini Tax Calculator!\n")
    time.sleep(0.5)
    print("This application will help you qickly calculate your taxes")
    print("This project will serve educational purposes only. No users data are not going to be stored or shared")
    print("or used for any other purpose.\n")
    time.sleep(2)
    input("Press Enter to continue...")


def get_user_name():
    """
    Display asking for the users name.
    Returns that name.
    """
    name = validate_name(input("Please enter your name here: \n"))
    print(f"Welcome {name} Thank You for using our application")
    return name

def validate_name(name):
    """
    Validate input data.
    Check if the name doesn't contain other than.
    letters. Accepted are only upper and lowercase letters.
    """
    if name.replace(" ", "").isalpha():
        print ("Name is valid!")
        return name
    else:
        print ("Name is invalid! Use letters from A to Z or a to z.")
        return validate_name(input("Please enter your name again \n"))


def quit_all():
    """
    This function is called when Q-key is pressed on the keyboard 
    it interrupts the whole process and 
    moves the user to the welcome_message function where he can 
    start the application from the beginning.
    """
    print("Are you sure you want to quit the process?")
    while True:
        confirm = input('Press "Y" to quit or "N" to return\n')
        if confirm.upper() == "Y":
            print("Process interrupted by the user\n\n")
            create_person()
            break
        elif confirm.upper() == "N":
            print("Return to the process\n")
            break
        else:
            print('Tap "Y" to submit or "N" to return to the previous process')


def request_salary():
    """
    Request salary from the user. 
    The entered value has to be validated for being integer and 
    having the right format.
    If the user doesn't know the value of his salary it can be 
    calculated after typing C-key on keyboard.
    """
    print("\nWe need your weekly salary to calculate your taxes.")
    print('Please enter your salary in following format: 99.99 ')
    while True:
        print('Please enter your weekly salary or type "C" to calculate it.')
        user_input = input('If you want to quit You can press "Q". \n')
        if user_input.upper() == "Q":  
            quit_all()
        elif user_input.upper() == "C":
# Validate_salary returns boolean this is causing a bug.
            if validate_salary(calculate_salary()):
                return calculate_salary()
            break
        elif validate_salary(user_input):
            print(f"Your salary is {user_input}")
            return user_input
            break

def calculate_salary():
    """
    Calculate salary based on multiplication of weekly working hours and
    hourly rate.
    Hourly rate can be validated using validate_salary.
    Working hours must be validated especially dedicated function..
    """
    salary = 0
    try:
        hourly_rate = float(input("Enter your rate per hour\n"))
        working_hours = float(input("Enter your weekly working hours\n"))
        salary = "{:.2f}".format(hourly_rate * working_hours)
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        calculate_salary()
    return salary


def validate_salary(salary):
    """
    Checks input salary data is the right type (integer ot float) and correct format,
    The function returns validated salary value.

    The function rounds the value to the demanded format instead of checking its
    correctness.
    """
    try:
        # Line below doesn't make a sense. The function returns Boolean.
        "{:.2f}".format(float(salary))
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    print(f"Your salary {salary} was successfully validated ")
    return True
        

def get_age():
    """
    Get age data from the user.
    Validate the data if it is the int type data.
    """
    age = 0
    try:
        age = input("Enter your age or choose Q to quit\n")
        if age == "Q" or age == "q":
            quit_all()
        else:
            age = int(age)
            print(f'You are {age} years old')
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        age = get_age()
    return age

def is_in_relation():
    """
    Get information about formal married from the user.
    Any input that is a string that starts with the first character "n" or "N"
    will be recognized as Yes.
    Also any input that starts with "N" or "n" will be recognized as No.
    "Q" or "q" input will launch quit_all function that interrupts the process.
    """
    print("Are you living in a formal marriage?")
    while True:
        married = input('Press "Y" for Yes or "N" if you are not or choose Q to quit.\n')
        if married[0] == "Y" or married[0] == "y":
            print("You are in married")
            return True
        elif married[0] == "N" or married[0] == "n":
            print("You are not in a married")
            return False
        elif married == "Q" or married == "q":
            quit_all()
        else:
            print("Invalid value. Please try again")
            is_in_relation()

class Person:
    """
    Store users data; such as name, age, information about formal relations and 
    users salary.
    These data are base to further calculations 
    """
    def __init__(self, name, age, married, salary):
        self.name = name
        self.age = age
        self.married = married
        self.salary = salary
    

def create_person():
    """
    An unfixed bug. Quit option inside each of data request functions interrupt only
    the functions they are in, but they don't interrupt create_person function.
    After the function is quit create_person function is resumed.

    I'm propably going to have to modify this function and close every nested functions
    in a loop. Each function has to call the next one in the queue. 
    Quit option has to call the first function in the queue. 
    Go up function will call the previous function in the queue.
    """
    print("\nThe application needs some information about you.")
    name = get_user_name()
    salary = request_salary()
    age = get_age()
    married = is_in_relation()
    person = Person(name, age, married, salary)
    print(f'{person.name} - {person.age} years old. Married: {person.married}, Salary - {person.salary}')
    return person


def calculate_final_tax(salary, partnership):
    base_tax = salary * 0.2
    print(f"The base tax is: {base_tax}")
    tax_credit = calculate_tax_credit(partnership)
    usc = calculate_usc(salary)
    prsi = calculate_prsi(salary)
    final_tax = (base_tax - tax_credit) + prsi + usc
    if final_tax > 0:
        print(f"The final tax is: {final_tax}")
        return final_tax
    else:
        print(f"The final tax is: {final_tax} which means it's 0")
        return 0


def calculate_tax_credit(partnership):
    """
    Tax credits are used to reduce the amount of tax you pay.
    The Personal Tax Credit you get depends on whether you are:
    single, married or in a civil partnership, widowed or a surviving civil partner,
    separated, divorced or a former civil partner.
    Base tax credit for any person is 1700, for a single person it is increase by 1700, 
    for a married it is increased by 3400.
    The result has to be divided by the number of weeks in a year
    """
    result = 1700
    if(partnership):
        result += 3400
    else:
        result += 1700
    weekly_credit = result/52
    print(f"Tax Credit is: {weekly_credit}")
    return (weekly_credit * 100.0)/100.0

def calculate_prsi(income):
    """
    Calculate one-sixth of your earnings over €352.01. €377- €352.01 = €24.99. Divided by 6 = €4.17.
    Subtract this from the maximum credit of €12, giving you a credit of €7.83.
    The basic PRSI charge is 4% of €377 = €15.08.
    You will pay €7.25 PRSI weekly (€15.08 minus your €7.83 PRSI credit).
    prsi_rate is an equivalent of percentage value of 4% in this case.
    If the income is lower than 352 prsi is 0.
    """
    prsi = 0
    if income > 352:
        prsi_rate = 0.04
        credit = (income - 352)/6
        if(credit > 12):
            credit = 12
        else:
            credit = 12-credit
        charge = income * prsi_rate
        prsi = charge - credit
    print(f"Prsi is: {prsi}")
    return (prsi * 100.0)/100.0

def calculate_usc(income):
    """
    Calculates Universal Social Charge (USC)
    It is set on the basis of the annual income. That's why the weekly income
    is multiplied by the average number of weeks in a year (number of weeks per year somethimes 
    can be different). 
    Everythime users income is in the range that meets the if condition the the result value is
    increased and the and the income value is decresed.
    The last condition has to be nested in the previous one.
    """
    result = 0
    annual_income = income * 52
    if annual_income > 12012:
        result += 12012*0.005
        annual_income -= 12012
    if annual_income > 9283:
        result += 9283*0.02
        annual_income -= 9283
    if annual_income > 49357:
        result += 49357*0.045
        annual_income -= 49357
        if annual_income > 0:
            result += annual_income*0.08
    print(f"USC = {result/52}")
    # Return value below propably is going to have to be rounded
    return (result/52 * 100.0)/100.0


def main():
    welcome_message()
    create_person()
    print("Thank you for filling in the form. Now we are going to process your data")
    calculate_final_tax(359, False)

main()

""""
To name validation add first letter condition, and lenght condition

To age validation add between 16 to 120 condition
"""