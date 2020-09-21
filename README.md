## General Info

<br>

This project allows the user to check their information from the "CS135 course" in a more convenient way. It is runned by *Selenium*, which does the login to interpret the page. Hence, it is not necessary for the student to be logged in. **Note:** this program is only intended for students who are enrolled in the *University of Waterloo's CS135 course for Fall 2020*

<br>

## Technologies

* Python: version 3.8.5
* Selenium: version 3.141.0
* Chrome Webdriver: version 85

<br>

## Setup

<br>

Before you start running the program, you need have a *Chrome Webdriver* - which allows Selenium to automate Chrome. Go to https://chromedriver.chromium.org/downloads to download to the correct version of the chrome browser you are using. To check your browser's version, go to https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have (I use version 85 for this project). **Make sure you know your path variable to the chromedriver inclusive**; it should be in the form...

<br>

```
C:\\path\to\your\chromedriver
```

<br>

You also need to install *Selenium* (assuming you have python installed) and to do so, you can enter the following code in command prompt:

<br>

```
pip install selenium
```

<br>

After you have set this up, clone my project and click on the ```login.txt``` file. Replace the placeholders with your waterloo username and password respectively. Then, you can run ```main.py``` on your IDE.

<br>

## Features

<br>

The program calculates the percent of self-check exercises answered correctly on first try.