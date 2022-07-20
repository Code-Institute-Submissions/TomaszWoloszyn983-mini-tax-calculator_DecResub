# Validator Tests. 
* No errors were detected when passing through the [Pep8 validator:](http://pep8online.com/)

![Code_validation](documentation/testing/code_validation_testing.jpg)



# get_name function testing:

Invalid input is refused by validator and the application repeats the request until the validation succeeds.

![Name_validation](documentation/testing/name_1.jpg)

Inputs that are too short, integers, empty inputs or any symbols other than lower and uppercase letter are refused.

![Name_validation](documentation/testing/name_3_errors.jpg)

![Name_validation](documentation/testing/name_4_valid.jpg)


# request_salary function testing:

Strings, empty string or input containing string or letters are refused by the validator. 
Also zero or negative numbers are refused.

![Income_validation](documentation/testing/salary_2_errors.jpg)

Float and integer input are allowed: number such as 123 or 123.45.

![Income_validation](documentation/testing/salary_3_valid.jpg)

Also Float numbers as 123.456789 are accepted by the validator.
The validation function rounds such a numbers to the correct format: 123.45

![Income_validation](documentation/testing/salary_4_valid.jpg)

### calculate_salary function testing
After selection option "C" the user can calculate the salary by entering his hourly rate and number of working hours.
The function is secured from inputing any negative values.

![Income_validation](documentation/testing/salary_6_errors.jpg)

Only positive numbers are allowed.

![Income_validation](documentation/testing/salary_8_valid_calculation.jpg)

# get_age function testing

This function is secured from inputing any string or empty string values.

![Age_validation](documentation/testing/age_2_errors.jpg)

Also only numbers in range from 16 to 120 are allowed.

![Age_validation](documentation/testing/age_2_valid.jpg)


# is_married function testing

Function is_married takes agruments yes or no.
It refuses any string that are not "Y", "y" or "N", "n" empty strings, integers, or any other values.

![Marriage_validation](documentation/testing/marriage_2_errors.jpg)

![Marriage_validation](documentation/testing/marriage_3_n_answeer.jpg)

![Marriage_validation](documentation/testing/marriage_4_y_answer.jpg)

However the validation accepts also any string that start at letter n or letter y and interpretes then as "no" or "yes"

![Marriage_validation](documentation/testing/marriage_5_yes_answer.jpg)


# quit function testing

After selection option Q for quit the user is asked for submiting his choice.
He can only enter lower or uppercase "y" or "n". 


![Quit_validation](documentation/testing/quit_1.jpg)

Any other values are not allowed and they cause the question will be repeated.

![Quit_validation](documentation/testing/quit_2_errors.jpg)

If the user enters "Y" to submit he will be moved to the first question wich is question for the name:
If the user enters "N" for no he will be returned to the previous question.

![Quit_validation](documentation/testing/quit_2_errors_n_answer.jpg)


# submit function testing

Submit function accepts only "Y" or "N" input in upper and lowercase.

![Quit_validation](documentation/testing/submit_2_errors.jpg)

Submiting data causes that tax calculating function are lauched and the data are sent ot the google sheet.

![Quit_validation](documentation/testing/submit_2.jpg)


<<<<<<< HEAD:testing.md

=======
>>>>>>> cfb7176 (Rename and update testing file. Minor improvements in the code):TESTING.md
# update_sheet function testing

Function successfully sends calculated data to google sheet.

![Update_validation](documentation/testing/send_data_3.jpg)

<<<<<<< HEAD:testing.md
![Update_validation](documentation/testing/send_data_3_sheet.jpg)
=======
![Update_validation](documentation/testing/send_data_3_sheet.jpg)
>>>>>>> cfb7176 (Rename and update testing file. Minor improvements in the code):TESTING.md
