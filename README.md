# FARM OVERFLOW/  FARMERS APP

## Description
This is a web application that allows users/mostly farmers to sign up, log in add problems,see problems or posts which other users can ccomment on, and delete. They can choose to update  their bio which includes their profile photo and posts they have posted they can also delete to write a pitch in and can view and comment.You also get your own page once you log in.

### By: FARMERS APP GROUP MEMBERS

## Prerequisites
1. python3.6
2. pip
3. Virtual environment(virtualenv)

## Cloning and running
Clone the application using git clone(this copies the app onto your device). In your terminal:

    $ git clone https://github.com/Omtatah/FarmOverflow.git
    $ cd FarmOverflow
    
Creating the virtual environment

    $ python3.6 -m venv --without-pip virtual
    $ source virtual/bin/env
    $ curl https://bootstrap.pypa.io/get-pip.py | python
    
Installing Flask and other Modules

    $ python3.6 -m pip install Flask
    $ python3.6 -m pip install Flask-Bootstrap
    $ python3.6 -m pip install Flask-Script
    
Run the application:

    $ chmod a+x start.sh
    $ ./start.sh
    
Testing the Application
To run the tests for the class files:

    $ python3.6 manage.py test
    
## Technologies Used
1. Python 3.6
2. Flask

## BDD
|Behaviour	             | Input	                         | Output                                                |
|------------------------|---------------------------------|-------------------------------------------------------|
|View landing page	       | Click on see more               | A  short description about the companies vission      |
|Add a new post       | click on post in farmers space                | Authentification page is displayed and user can add post delete and have his profile |
|Add a comment           | Click on comment                | Comment form is displayed and user can comment        |                                 |
|Delete         | Click on delete              | comment is deleted                              |

## Contact Information
For any questions, troubleshooting or contributions, find me on:
Email: farmersmembers@gmail.com

## License
[MIT](./License)
 Copyright (c) 2019 **FarmOverflow**
