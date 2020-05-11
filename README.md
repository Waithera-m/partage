# Partage
#### The web application allows users to view, add, and comment on blog posts, May 11, 2020 
#### By **Waithera-m**
## Description
Partage is a simple flask application that allows users to view and comment on posts. Users can also use provided links to add new posts, update and delete existing posts.

## Setup/Installation Requirements
To use the application, users need internet access and web browsers, preferably  Chrome, Safari, and Firefox. Users also need an authenticated account to access comment and add post features.
## Set-Up a Local Project
### Prerequisites
* Python version 3.6 or later
* pip
* flask
* flask-uploads
* flask-login
* flask-wtf
* flask-mail
* flask-sqlalchemy
* postgresql account and database

To set up a local project:
* Fork the repository
* Clone the repository using the git clone command
* Activate a virtual environment
* Install all prerequisites
## Known Bugs
* None at the moment.
## Behavior Driven Development (BDD)
### Landing Page
![image](https://user-images.githubusercontent.com/60571734/81597402-59f50f80-93ce-11ea-8a6b-d0b45f276b2a.png)

### Blog View
![image](https://user-images.githubusercontent.com/60571734/81597543-932d7f80-93ce-11ea-876d-d94eb04cc529.png)


### Post View
![image](https://user-images.githubusercontent.com/60571734/81597736-da1b7500-93ce-11ea-89da-2219773a236f.png)

### Profile View
![image](https://user-images.githubusercontent.com/60571734/81597801-f7504380-93ce-11ea-8d51-22dc3abd546d.png)

|Behavior                |Input                            |Output                             |
|------------------------|----------------------------------|----------------------------------|
|The landing page loads |Users scroll | Users see about section and button that redirects users to posts template|
|The landing page loads|Users click on view posts button|Users see all submitted posts|
|The landing page loads|Users click on sign in button|Users are directed to sign in/ register view, users sign in if they have an account or click on the sign up link to create an account|
|The landing page loads|Users click on profile navbar link|Users see they profiles and options to edit or upload profile image|
|The landing page loads|Users click on blog navbar link|Users see their profile image, username and list of all their blog|
|The post page loads|Users click on read and comment link|Users see full post and options to edit, delete, or comment on post|
|The landing page loads|Users click on sign out link in the navbar|Users are logged out|
## Technologies Used
* HTML - HTML dictates the structure of webpages.
* CSS & Bootstrap - CSS determines the appearance of webpages. The styling language was used to add background images and colors and style the site's content.
* Python 3.8.2 - The language was used to create classes, testcases, and functions to retrieve data 
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) -  Flask is a Python microframework.The framework's templates were used to refactor code and promote code maintenance. Inbuilt filters,classes, and methods were used to initialize the application and extensions and loop through and display pitches and navigate to different views. 
## Support and contact details
You are free to suggest and improve the code. To make your changes:
* Fork the repo
* Create a new branch
* Create, add, commit, and push your changes to the branch
* Create a pull request
* You can also contact the creator via this email address: njihiamary11@gmail.com
## Demo
You can view changes made to the website by visiting this working live demo: https://partage-flask.herokuapp.com/
### License
*MIT*
MIT License Copyright (c) 2020 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
Copyright (c) 2020 **Waithera-m**