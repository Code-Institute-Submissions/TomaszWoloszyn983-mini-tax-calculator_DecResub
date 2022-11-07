# Code validation. 
* The application were passed through the  [Pep8 validator:](http://pep8online.com/) with result of no errors detected.

![Code_validation](documentation/testing/code_validation_testing.jpg)


# Functionality Testing

## 1. get_name function testing:

* The entered value is passed to the validation function. 
    - If the validation succeeds the user is expected to be move to the next step.
    - If the validation doesn't succeeds the the user is redirected back.

![flowchart_name](documentation/testing/tax_calc_flowchart_name.jpg)

* Example of valid value:

![Name_validation](documentation/testing/name_1.jpg)

![Name_validation](documentation/testing/name_4_valid.jpg)

* Examples of invalid values:

Invalid input is refused by validator and the application repeats the request as many times as the validation succeeds.


Inputs that are too short, integers, empty inputs or any symbols other than lower and uppercase letter are refused.

![Name_validation](documentation/testing/name_3_errors.jpg)



## request_salary function testing:

Strings, empty string or input containing string or letters are refused by the validator. 
Also zero or negative numbers are refused.

![Income_validation](documentation/testing/salary_2_errors.jpg)

Float and integer input are allowed: number such as 123 or 123.45.

![Income_validation](documentation/testing/salary_3_valid.jpg)

Also Float numbers as 123.456789 are accepted by the validator.
The validation function rounds such a numbers to the correct format: 123.45

![Income_validation](documentation/testing/salary_4_valid.jpg)

#### calculate_salary function testing
After selection option "C" the user can calculate the salary by entering his hourly rate and number of working hours.
The function is secured from inputing any negative values.

![Income_validation](documentation/testing/salary_6_errors.jpg)

Only positive numbers are allowed.

![Income_validation](documentation/testing/salary_8_valid_calculation.jpg)

## get_age function testing

This function is secured from inputing any string or empty string values.

![Age_validation](documentation/testing/age_2_errors.jpg)

Also only numbers in range from 16 to 120 are allowed.

![Age_validation](documentation/testing/age_2_valid.jpg)


## is_married function testing

Function is_married takes agruments yes or no.
It refuses any string that are not "Y", "y" or "N", "n" empty strings, integers, or any other values.

![Marriage_validation](documentation/testing/marriage_2_errors.jpg)

![Marriage_validation](documentation/testing/marriage_3_n_answeer.jpg)

![Marriage_validation](documentation/testing/marriage_4_y_answer.jpg)

However the validation accepts also any string that start at letter n or letter y and interpretes then as "no" or "yes"

![Marriage_validation](documentation/testing/marriage_5_yes_answer.jpg)


## quit function testing

After selection option Q for quit the user is asked for submiting his choice.
He can only enter lower or uppercase "y" or "n". 


![Quit_validation](documentation/testing/quit_1.jpg)

Any other values are not allowed and they cause the question will be repeated.

![Quit_validation](documentation/testing/quit_2_errors.jpg)

If the user enters "Y" to submit he will be moved to the first question wich is question for the name:
If the user enters "N" for no he will be returned to the previous question.

![Quit_validation](documentation/testing/quit_2_errors_n_answer.jpg)


## submit function testing

Submit function accepts only "Y" or "N" input in upper and lowercase.

![Quit_validation](documentation/testing/submit_2_errors.jpg)

Submiting data causes that tax calculating function are lauched and the data are sent ot the google sheet.

![Quit_validation](documentation/testing/submit_2.jpg)


## update_sheet function testing

Function successfully sends calculated data to google sheet.

![Update_validation](documentation/testing/send_data_3.jpg)

![Update_validation](documentation/testing/send_data_3_sheet.jpg)

# Bugs and Error
### The following bugs and error were encountered during or after the development process.

* There was an unhandled edge case in the calculate_salary function that led to incorrect assigning the value of the salary variable. 

![Salary_error](documentation/testing/salary_none_bug.jpg)

In the result that caused stopping the application and displaying the error message. 

![Salary_error](documentation/testing/salary_none_error.jpg)

The reason of occuring the error was the line 165, where returning value of the calculate_salary() function wasn't assigned to any variable. 

![Salary_error](documentation/testing/salary_bug_code.jpg)

After assigning the functions value to the variable salary, the salary variable was correctly returned in the return statement of the function.
