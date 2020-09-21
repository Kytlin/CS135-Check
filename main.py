import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.student.cs.uwaterloo.ca/~cs135/assess/viewselfcheck/"

# Path Name 
path = str(input("Please enter the full path of your chromedriver: "))

# Receiving Inputs from text
with open('login.txt', 'r') as f:
    your_username = f.readline()
    your_password = f.readline()


# Initializing Selenium
driver = webdriver.Chrome(path)
driver.get(url)

# Access the inputs for username and password and fill them out
username = driver.find_element_by_id("username")
username.send_keys(your_username)
password = driver.find_element_by_id("password")
password.send_keys(your_password)

password.send_keys(Keys.ENTER)

# Check the "First Try Correct?" column of the table
check_col_2 = driver.find_elements_by_css_selector("td:nth-of-type(2)")

ans, t, f, count = 0, 0, 0, 0
for i in check_col_2:
    if (len(i.text) > 0):
        count += 1
        if (i.text == "True"):
            t += 1
        if (i.text == "False"):
            f += 1   

# Calculating Results
ans = round((t / (t + f)) * 100)
print(f'You got {ans}% of the {count} self-check exercises right.')