# Password Locker


## Description
Password Locker is a terminal run python application that allows users to save and generate passwords for their various accounts in different sites.


## Versioning

Password Locker.

## Author


* [**Brian Major**](https://github.com/bryomajor)

## Features


As a user of the terminal application you will be able to:

1. Create an account
2. Log into your account
3. Add credentials for different accounts.
4. Store and generate passwords
5. See a list of all your saved credentials
6. Copy credentials to the clipboard

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./run.py** | Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, fc - Find Credential, cp - Copy Credential, del - Delete Credential, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Find a credential | **Enter: fc** | Prints the searched credential |
| Display prompt for which credential to copy | **Enter: cp** | Enter the site name of the credential you wish to copy. |
| Deletes a saved credential | **Enter: del** | Prints success |
| Exit application | **Enter: ex** | Exit the current navigation stage |



## Getting started
### Prerequisites
* python3.6
* pip
* pyperclip
* xclip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/bryomajor/password-locker/
        $ cd password-locker

## Running the Application
* To run the application, in your terminal:

        $ chmod +x run.py
        $ ./run.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 user_credentials_test.py
        
## Technologies Used
* Python3.6

This application is developed using [Python3.6](https://www.python.org/doc/). You can find more about this technology by clicking [here](https://www.python.org/doc/).


## Support and Team
Brian Major


[Slack Me!](https://slack.com/intl/en-ke/)  @bryomajor


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)