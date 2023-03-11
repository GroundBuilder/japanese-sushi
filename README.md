# Sushi bar surplus!

![PNG of App](docs/readme_images/herokuapp_sushi.png)

## Table of fontents

* [Introduction](#Introduction)
    * [Site goals](#Site-goals)
    * [Target business](#Target-business)
    * [User stories](#User-stories)
    * [Features planned](#Features-planned)
* [Structure](#Structure)
    * [Features](#Features)
* [Flowchart](#Flowchart)
* [Technologies](#Technologies)
* [Testing](#Testing)
    * [Functional Testing](#Functional-Testing)
    * [Pep8 Validation](#Pep8-Validation)
    * [Bugs and Fixes](#Bugs-and-Fixes)
* [Deployment](#Deployment)
    * [Version Control](#Version-Control)
    * [Heroku Deployment](#Heroku-Deployment)
    * [Clone Locally](Clone-Locally)
* [Credits](#Credits)
  * [Content](#Content)


## Introduction

This project was created to get the small sushi bar input in how much they need to premanufacturing till the next day. So the customers doesn't need to wait to get their lunch.

### Site goals

* Simpel program for the user to send input for how much they have sold and get input how much to premanufactur next day. Just to optimize their business.

### Target business

* Let small business get benefits of technologi to optimize their business with a low cost.

### User stories

* As a user, I want a easy way to put in my data and recieve new data for next days.
* As a user, I want to get back if I enter worng sales data to the program.
* As a user, I want to see what I enterd, so I can correct the values that was handled in to the program.
* As a user, I want to like follow how the program is working while I wait for the input to premanufacturing.
* As a user, I want to exit the program in the beginning, if I forgot to take in every data.

### Features planned

* Return profit for todays sale.
* Return wast cost of sushi that din't get sold under lunch time.

## Structure

The input for the user is folowing the structure of the flowcart. The flowcart is created my using the Balsamico program. 


### Features

User story
- As a user, I want a easy way to put in my data and recieve new data for next days.
![PNG of App](docs/readme_images/herokuapp_sushi.png)

- As a user, I want to get back if I enter worng sales data to the program.
![PNG of wrong input](docs/readme_images/herokuapp_wron_input.png)

- As a user, I want to see what I enterd, so I can correct the values that was handled in to the program.
![PNG of valid/visual input](docs/readme_images/herokuapp_valid_input.png)

- As a user, I want to like follow how the program is working while I wait for the input to premanufacturing.
![PNG of progress](docs/readme_images/herokuapp_progress.png)

- As a user, I want to exit the program in the beginning, if I forgot to take in every data.
![PNG of progress](docs/readme_images/herokuapp_correct_and_delete.png)


## Flowchart

The Flowchart for my program was created using Balasamiq and it visually represents how the flow system works.

![Flow](docs/readme_images/WireframeSushiBar.png)

## Technologies

* Python - The main language used to build this application
    * Python package:
        * Gspread - To access and creat and delete rows in the google spreadsheet.

## Testing

## VALIDATORS TESTING  
### PEP8 CI Python Linter - Validator
I tested my Python code and there are no errors. There were E501, cause it's comments on the code in the same line.
https://pep8ci.herokuapp.com/
![PEP8](docs/test_images/Pep8_ok.png)

### HTML Validator
Not done, cause there is no web-page. The one is through Heroku.

### CSS Validator
The whole website was tested and its free from errors in CSS.
<img src="assets/images/css_valid.JPG" width="70%">


## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!