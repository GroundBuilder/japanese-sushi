# Sushi bar surplus!

![PNG of App](docs/readme_images/herokuapp_sushi.png)

## Table of fontents

* [Introduction](#Introduction)
    * [Site goals](#Site-goals)
    * [Target business](#Target-business)
    * [User stories](#User-stories)
    * [Features planned](#Features-Planned)
* [Structure](#Structure)
    * [Features](#Features)
    * [Features left to Implement](#Features-Left-to-Implement)
* [Logical Flow](#Logical-Flow)
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

## Wireframe

![Flow](docs/readme_images/WireframeSushiBar.png)

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