# Mini Tax Calculator.

![Title image](documentation/images/am_i_responsive.jpg)

## Welcome to my Project! 


The subject of the project is a Tax Calculator. The purpose of the project is to create 
a simple and easy calculator for calculating income taxes based on the Irish Revenue system.



## Features

The application calculates the weekly tax. Which means that all input data should also base on the weekly period.

After the application starts it asks the user for some details that are required for the tax to be calculated.
- **Name:** The first question is about the users name. This information is only needed for identification the user.

![Get Name](documentation/images/get_name.jpg)

- **Salary:** Salary is the main factor tax calculation is based on.

  * **Enter Salary:** The salary can be entered directly by writting its numeric, float value in the terminal, or 
    in a case that the user doesn't know it, it can be calculated.

    ![Enter salary](documentation/images/get_salary.jpg)

  * **Calculate Salary:** To calculate salary the option "C" has to be chosen. Then a set of two question will be asked:
    A question about the hourly rate and the number of hours worked. The salary is calculated by multiplication the hourly rate and the number of hours.

    ![Calculate income](documentation/images/calc_salary.jpg)

  * **Validation:** The next step is validation that follows after the salary is either entered or calculated. The validation check if the salary doesn't contain invalid symbol or negative numbers.
- **Age:** Although there is no minimum age at which you are liable to pay taxes, only people 16 uears old or older can be employed for full time work. That is why the application asks for this information. Validation function refuses any input that is lower than 16 and higher than 120 years old.

    ![Get Age](documentation/images/get_age.jpg)

- **Marriage/Partnership:** The main factor for calculating Tax Credit. Returns boolean value.

  ![Marriage](documentation/images/is_married.jpg)

- **Submitting Data**

  The last step is to decide if you want to submit your data or to discard them and repeat all the requests again.

  Submitted data will be processed by calculator, passed into Person class and sent to the Google Sheet.

  ![Submit data](documentation/images/submit_data.jpg)

  After the application it completed the user can choose to restart the application or to close it.

- **Tax Calculation:** The main functionality of this application. Calculates the Taxes value based on Irish Revenue system, it uses following factors:
  * **Tax Credit:** Tax relief. Dependend on marital status.
  * **USC:** Universal Social Charge.
  * **PRSI:** Pay Related Social Insurance.
  * **Final Tax:** Calculates the sum of all taxes.
- **Update Google Sheet:** The last functionality, that allows the user to send and archive his result.

- **Quit function**

  Quit function interrupts the current request and moves the user to first question. 

  ![Quit function](documentation/images/quit_all.jpg)

- **Class Person**

  Stores all the users data collected by the application. Also the results of calculations are passed to this class.

  `
  
      class Person:
      """
      Store users data such as name, age, information about formal relations and
      users salary.
      These data are base to further calculations.
      """
      taxes = 0

      def __init__(self, name, age, married, salary):
          self.name = name
          self.age = age
          self.married = married
          self.salary = salary
          self.taxes
  `



## Flowchart ##

  ![Flowchart image](documentation/images/tax_calc_flowchart.jpg)
 
## Future Features
  - Searching and displaying users data from google sheet.
    Creating authorisation function to protect data from being loaded by authorised user.
  - Calculating other type of taxes such as Capital Gains Tax.
  - Improve calculation of the Tax Credit to make it more accurate. At the moment it is based on rounded number of weeks.

## Technologies used:
  
 - **Python** - an interpreted, object-oriented, high-level programming language.
 - **Google Drive API** - allows you to create apps that leverage Google Drive cloud storage.
 - **Google Sheets** - A web-based application that enables users to create, update and modify spreadsheets and share the data online in real time.
 - **Colorama** - The Colorama is one of the built-in Python modules to display the text in different colors. It is used to make the code more readable.


## Testing
  The applications code was tested using Pep8 code validator: http://pep8online.com/.
  More details about tesings are available in the separate testing section here or in the dedicated file testing.md [here](testing.md).



## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser. This is to improve the accessibility of the project to others.

The live deployed application can be found at [Mini Tax Calculator](https://mini-tax-calculator.herokuapp.com/).

### Local Deployment

*Gitpod* IDE was used to write the code for this project.

To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/TomaszWoloszyn983/mini-tax-calculator.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/TomaszWoloszyn983/mini-tax-calculator)

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select *Add Buildpack*.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: node index.js > Procfile`

------------------ !!!!!!!!!!!!!!!!!!! ------------------- !!!!!!!!!!!!!!!!!!!!!!!!! ---------------------
IMPORTANT SECTION YOU MUST UPDATE !!!!!!!!!!!!!!!!
If you are using an API like Google Sheets, then you must also include the instructions on how someone can obtain their own API/Credentials.
Advise how they can get their own, steps necessary to get one, and then creating the creds.json file or env.py file and pasting in their keys.
Also on Heroku config vars, which variable key/value is also needed to get it working on Heroku
END OF IMPORTANT EXTRA SECTION !!!!!!!!!!!!!!!!!!!

To create users own Google Sheet following steps must be taken.
 - Create an account on Google Cloud Platform.
 - Open new project.
 - Choose APIs and Services option and click Library.
 - Enable two APIs: 
    * Google Drive Api that provides credentials for security access.
      
      Instruction how to create and setup google sheet with the program. 
      > Select Create Credential option and create credentials for the application data. 
      > Create Service account, name it, mark as Editor (or owner) and select the JSon option. Click continue to download the credential file to your computer. Add the file the   Mini_Tax_Talculator workspace.

    * Google Sheet allows to create you own sheet where your data can stored and analized.
      
      Instruction how to create and setup google sheet with the program. 
      > To achive this create a new sheet. Copy client_email from credential file in your workspace. Select "Share" option in your sheet and paste the client_email in the diagram.
      > Update your requirements.txt file with gspread==your version of gspread.

    * Heroku. For the application to be deployed properly Heroku Account has to be updated.
      
      Instruction how to update Heroku config vars:
      > Find your application in your Heroku account. Enter to the settings. Select Config Vars. 
      > Add new variable with key = CREDS and into value section paste the whole content of the CREDS.json file from the application.
      > Add another new variable enter Key = PORT, value = 8000. 

------------------ !!!!!!!!!!!!!!!!!!! ------------------- !!!!!!!!!!!!!!!!!!!!!!!!! ---------------------

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

Alternatively, you can enable Automatic Deployments from within the Heroku app, by connecting it to your GitHub repository.

The frontend terminal should now be connected and deployed to Heroku.



## References and Credits:


## Credits:
<!-- I would like to especially thank to Tim Nelson from Code Institute for his great support. -->