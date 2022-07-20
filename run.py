import gspread
from google.oauth2.service_account import Credentials
import time
from pprint import pprint
import os
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

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
# prints data from the google sheets
# pprint(data)


def update_sheet(person):
    """
    Creates a list of data to be sent to the google sheet.
    The order of the elements is important. It is : Name, Age, Salary, Tax
    """
    users_data = [person.name, person.age,
                  person.married, person.salary, person.taxes]
    print(f"Send {person.name}'s data to the sheet")
    info.append_row(users_data)
    print("Data sent!")


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_message():
    """
    Dispays greetings, information about the application
    and instruction for the user.
    """
    clear()
    print("\n\n\tWelcome to Mini Tax Calculator!\n")
    # time.sleep(0.5)

    print("This application will help you qickly calculate your taxes")
    print("The application will ask you for some information that are")
    print("necessary for making calculations")
    print("This project will serve educational purposes only.")
    print("No users data are to be stored, shared")
    print("or used for any other purpose.\n")
    # time.sleep(2)
    input("Press Enter to continue...")
    clear()


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
    Check if the name doesn't contain other than letters.
    Accepted are only upper and lowercase letters.
    Also the name should contain at least three letter.
    """
    if name.replace(" ", "").isalpha() and len(name) >= 3:
        print ("Name is valid!")
        return name

    else:
        print ('Name is invalid! The name should contain at '
               'least three letters from A to Z or a to z.')
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
        confirm = input(f'Press "{Back.LIGHTYELLOW_EX}{Fore.BLACK} Y '
                        f'{Style.RESET_ALL}" to quit or "'
                        f'{Back.LIGHTYELLOW_EX}{Fore.BLACK} N '
                        f'{Style.RESET_ALL}" to return\n')
        if confirm.upper() == "Y":
            print("Process interrupted by the user\n\n")
            clear()
            return False
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
    while True:
        print(f'Please enter your weekly {Back.LIGHTYELLOW_EX}{Fore.BLACK}'
              f'salary{Style.RESET_ALL} in the following format: 99.99')
        print(f'or select option "{Back.LIGHTYELLOW_EX}{Fore.BLACK} C '
              f'{Style.RESET_ALL}" to calculate it.')
        user_input = input('If you want to quit You can select option '
                           f'"{Back.LIGHTYELLOW_EX}{Fore.BLACK} Q '
                           f'{Style.RESET_ALL}".\n')
        if user_input.upper() == "Q":
            if quit_all() is False:
                return False
        elif user_input.upper() == "C":
            result = calculate_salary()
            if validate_salary(result):
                return "{:.2f}".format(float(result))
            break
        elif validate_salary(user_input):
            return "{:.2f}".format(float(user_input))
            break


def calculate_salary():
    """
    Calculate salary based on ratio of weekly working hours and
    hourly rate.
    Hourly rate can be validated using validate_salary.
    Working hours must be validated especially dedicated function..
    """
    salary = 0
    try:
        hourly_rate = float(input("Enter your rate per hour\n"))
        working_hours = float(input("Enter your weekly working hours\n"))
        salary = "{:.2f}".format(hourly_rate * working_hours)
        if (hourly_rate < 0) or (working_hours < 0):
            print('Negative value!')
            raise ValueError
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        calculate_salary()
    return "{:.2f}".format(float(salary))


def validate_salary(salary):
    """
    Checks input salary data is the right type (integer ot float)
    and correct format,
    The function returns validated salary value.

    The function rounds the value to the demanded format instead of
    checking its correctness.
    """
    try:
        temp = float(salary)
        if temp <= 0:
            print("This value must be higher that 0.")
            raise ValueError
        # assert temp < 0
    # except AssertionError:
    #     print("This value must be higher that 0.")
    #     return False
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    print(f"Your income {salary} was successfully validated ")
    return True


def get_age():
    """
    Get age data from the user.
    Validate the data if it is the int type data.
    """
    age = 0
    try:
        age = input('Enter your '
                    f'{Back.LIGHTYELLOW_EX}{Fore.BLACK}age{Style.RESET_ALL} '
                    f'or select "{Back.LIGHTYELLOW_EX}{Fore.BLACK} Q '
                    f'{Style.RESET_ALL}" '
                    'to quit\n')
        if age.upper() == "Q":
            if quit_all() is False:
                return False
        elif int(age) < 16 or int(age) > 120:
            print("The age must be in the range between 16 and 120 years old.")
            raise ValueError
        else:
            age = int(age)
            print(f'You are {age} years old')
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        age = get_age()
    return age


def is_married():
    """
    Get information about formal married from the user.
    Any input that is a string that starts with the first character "n" or "N"
    will be recognized as Yes.
    Also any input that starts with "N" or "n" will be recognized as No.
    "Q" or "q" input will launch quit_all function that interrupts the process.
    The second elif should not return false. It must return a different value.
    """
    print("Are you living in a formal marriage?")
    while True:
        married = input('Press "'
                        f'{Back.LIGHTYELLOW_EX}{Fore.BLACK} Y '
                        f'{Style.RESET_ALL}" '
                        'for Yes or '
                        f'"{Back.LIGHTYELLOW_EX}{Fore.BLACK} N '
                        f'{Style.RESET_ALL}" '
                        'if you are not or select '
                        f'"{Back.LIGHTYELLOW_EX}{Fore.BLACK} Q '
                        f'{Style.RESET_ALL}" '
                        'to quit.\n')
        if len(married) == 0:
            print("Invalid value. Please try again!")
        elif married[0] == "Y" or married[0] == "y":
            print("You are married")
            return True
        elif married[0] == "N" or married[0] == "n":
            print("You are not married")
            return False
        elif married.upper() == "Q":
            if quit_all() is False:
                return 'quit'
        else:
            print("Invalid value. Please try again!")


class Person:
    """
    Store users data; such as name, age, information about formal relations and
    users salary.
    These data are base to further calculations
    """
    taxes = 0

    def __init__(self, name, age, married, salary):
        # This constructor doesn't have taxes parameter because it is used only
        # for taking data from the user for calculating taxes in the next step.
        self.name = name
        self.age = age
        self.married = married
        self.salary = salary
        self.taxes


def create_person():
    """
    An unfixed bug. Quit option inside each of data request
    functions interrupt only the functions they are in,
    but they don't interrupt create_person function.
    After the function is quit create_person function is resumed.

    I'm propably going to have to modify this function
    and close every nested functionsin a loop.
    Each function has to call the next one in the queue.
    Quit option has to call the first function in the queue.
    Go up function will call the previous function in the queue.
    """
    flag = True
    print("\nThe application needs some information about you.")
    while(flag is True):
        clear()
        name = get_user_name()
        time.sleep(1)
        clear()
        salary = request_salary()
        if salary is False:
            continue
        time.sleep(1)
        clear()
        age = get_age()
        if age is False:
            continue
        time.sleep(1)
        clear()
        married = is_married()
        if married == 'quit':
            continue
        time.sleep(3)
        clear()
        flag = False
    person = Person(name, age, married, salary)
    print('All data requests completed!')
    return person


def calculate_final_tax(salary, partnership):
    """
    Calculates the final tax value based on input users data and
    calculation made by other functions such as calculate_tax_credit,
    calculate_prsi, calculate_usc.
    Returns the value of tax or if the value is negative it returns 0
    (no tax)
    """
    sal = float(salary)
    base_tax = "{:.2f}".format(float(sal * 0.2))
    tax_credit = float(calculate_tax_credit(bool(partnership)))
    usc = float(calculate_usc(sal))
    prsi = float(calculate_prsi(sal))
    final_tax = (float(base_tax) - tax_credit) + prsi + usc
    rounded_tax = "{:.2f}".format(float(final_tax))
    if final_tax < 0:
        rounded_tax = 0
    print(f'Base tax: {base_tax} Tax Credit: {tax_credit} '
          f'USC: {usc} PRSI: {prsi} Final Tax: {rounded_tax}')
    return rounded_tax


def calculate_tax_credit(partnership):
    """
    Tax credits are used to reduce the amount of tax you pay.
    The Personal Tax Credit you get depends on whether you are:
    single, married or in a civil partnership, widowed or a
    surviving civil partner,separated, divorced or a former
    civil partner.
    Base tax credit for any person is 1700,
    for a single person it is increase by 1700,
    for a married it is increased by 3400.
    The result has to be divided by the number of weeks in a year.
    """
    result = 1700
    if(partnership):
        result += 3400
    else:
        result += 1700
    weekly_credit = result/52
    return "{:.2f}".format(float(weekly_credit))


def calculate_prsi(income):
    """
    Calculate one-sixth of your earnings over €352.01.
    €377- €352.01 = €24.99. Divided by 6 = €4.17.
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
    return "{:.2f}".format(float(prsi))


def calculate_usc(income):
    """
    Calculates Universal Social Charge (USC)
    It is set on the basis of the annual income.
    That's why the weekly income
    is multiplied by the average number of weeks in a year
    (number of weeks per year somethimes can be different).
    Everythime users income is in the range that meets
    the if condition the the result value is
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
    return "{:.2f}".format(float(result/52))


def submit_data(person):
    """
    Dispalys users data and ask for submition the data
    and to pass them for the further precessing
    or to not to submit and start the getting information again.
    """
    print(f'User: {person.name}:')
    print(f'\t{person.age} years old,')
    print(f'\tMarried: {person.married},')
    print(f'\tSalary: {person.salary}.')
    submit = input(f'Enter "{Back.LIGHTYELLOW_EX}{Fore.BLACK} Y '
                    f'{Style.RESET_ALL}" '
                    'to submit your data or select '
                    f'"{Back.LIGHTYELLOW_EX}{Fore.BLACK} N {Style.RESET_ALL}" '
                    'to discard data.\n')
    while True:
        if submit.upper() == "Y":
            # Returning false runs a new iteration in the function_manager loop
            print("Thank you for filling in the form. ")
            print("Now we are going to process your data.")
            return False
        elif submit.upper() == "N":
            # Returning true breaks the loop in function_manager
            print("Process interrupted by the user\n\n")
            return True
        else:
            submit = input('Enter " Y " to submit or "N" to enter new data.\n')


def functions_manager():
    flag = True
    welcome_message()
    while(flag):
        person = create_person()
        if person is False:
            continue
        flag = submit_data(person)
    person.taxes = calculate_final_tax(person.salary, person.married)
    update_sheet(person)
    print('Application complete!!!')
    renew = input('\nWould You like to make a new calculation? '
                  f'{Back.LIGHTYELLOW_EX}{Fore.BLACK}Y/N{Style.RESET_ALL}\n')
    while True:
        if renew.upper() == "Y":
            functions_manager()
            break
        elif renew.upper() == "N":
            clear()
            print("\n\tThank You. Have a nice day!\n")
            break
        else:
            renew = input(f'Enter "{Back.LIGHTYELLOW_EX}{Fore.BLACK}'
                          f' Y {Style.RESET_ALL}" '
                          'to start a new Calculation '
                          f'or "{Back.LIGHTYELLOW_EX}{Fore.BLACK} N '
                          f'{Style.RESET_ALL}"'
                          ' to quit.\n')


def main():
    functions_manager()

main()
