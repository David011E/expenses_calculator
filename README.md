# Expenses Calculator Business Program
![Expenses Calculator header](/assets/images/for-intro.png)

This is a Businesses Expenses Calculator program for all the people in contracts to use to see and calculate how much they have made this month. And it will also ask for their expenses so it can calculate after expenses for them aswell. After it has calculated after all expenses it will update the data to google sheets so they can keep track.

The live link can be found [HERE](https://expenses--calculator-4db02840ab2a.herokuapp.com/) - After clicked will open in a new window

## Contents

- [Introduction](#introduction)
- [Project](#project)
    - [User goals:](#user-goals)

- [Pre development](#pre-development)

- [Development](#development)

- [Features](#features)
    - [Name and Greet the user](#name-and-last-name-input)
    - [Job Position](#name-and-last-name-input)
    - [Expenses](#Expenses)

- [Google Sheets](#google-sheets)
    - [Google Sheets preview](#confirm-information)
    - [What information is included](#What-information-is-included)

- [Technologies Used](#technologies-used)
- [Resources](#resources)
    - [Libraries](#libraries)

- [Testing](#testing)

- [Validation](#validation)
- [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Branching the GitHub Repository using GitHub and Visual Studio Code](#branching-the-github-repository-using-github-and-visual-studio-code)

- [Credits](#credits)

---

## Introduction

This portal asks users to input their name, job position and expenses this month. Then the expenses calculater will calcutle how much the user will be left with after all expenses. Then the data will be forwarded to google sheets so the user can keep track of this month's expenses.

## Project 

The aim of this project is to:
 - Encourage users to enter the information to calculate thier expenses.
 - Provide clear, visible instructions with each visit.
 - To keep track of the users expenses via google sheets.

 ![storyboard](assets/images/Project-storyboard.png)

 ### User goals:

 Get clear instructions on how to use the system in front of them that they can refer to if needed.
The ability to input their details including name, job position and expenses this month. And they will be able to keep track by google sheets.

### Site owner goals

Provide a program that is easy to use and maintain.
Present a program that gives clear instructions each time a users visits.
Get access to the information inputted by google sheets.

### Pre development

I wrote out notes and created a flow chart. All I had to do then is follow my notes and code one area at a time before moving on to the next. I set up projects in GitHub to write out work that needed to be done. The aim is to provide early and continuous delivery of the project. Through out the project I did make some changes that are not in the notes.

![Expenses Calculator flow chart](/assets/images/users-goals.png)

My actual notes that created the flow chart

![Expenses Calculator notes](/assets/images/page-1-of-flow-chart.jpeg)

![Expenses Calculator notes](/assets/images/page-2-of-flow-chart.jpeg)

![Expenses Calculator notes](/assets/images/page-3-of-flow-chart.jpeg)

---

### Development

Code was written for each part of the program starting with the header and input for users to add their name. Once each section was working the development of the following section took place. Once all sections had been created testing took place which highlighted the need for additional features.

i.e. In the "input name" section the user could hit enter and a blank space would be inputted so the first and last names were made required fields. Instructions were written to ensure each user understood the importance of entering their name only. After testing with required fields, the inability to add symbols and numbers was also added.

![Expenses Calculator name error](/assets/images/invalid-name.png)

## Features

### Name and Greet the user
This feature gives the program the information it needs to greet the user.

![Expenses Calculator name](/assets/images/greet-user.png)

### Job Position

Next. The user is asked to select their job position. An error message is displayed if an invalid letter is added:

![Expenses Calculator invalid](/assets/images/job-position-if-invalid.png)

This is if the user selects and then presses n the program will loop and ask job position again. 

![Expenses Calculator n](/assets/images/job-position-if-n.png)

This is if the user select y it will then calculate how much they have made this month then ask the next question.

![Expenses Calculator y](/assets/images/job-position-if-y.png)

### Expenses

Then the user will now be ask to enter thier expenses for this month. If the user enters any alphabetical words in the input it will loop and then ask the question again.

![Expenses Calculator alphabetical words](/assets/images/expenses-if-enter-alphabet-with-numbers.png)

If the user has entered the amount then they will be asked to confirm

![Expenses Calculator confirm](/assets/images/expenses-confirm.png)

If the user has entered the amount the presses n then the question will be asked again.

![Expenses Calculator n](/assets/images/expenses-loop-if-no.png)

After that if the user enters the amount then presses yes all the data will be updated to google sheets

![Expenses Calculator y](/assets/images/updated-to-sheets.png)

---