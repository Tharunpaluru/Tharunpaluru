from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace with your Instagram username and password
username = "your_username"
password = "your_password"

# Start a new instance of the Chrome browser
driver = webdriver.Chrome()

# Navigate to the Instagram login page
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)

# Find the username and password input fields, and enter your login credentials
username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")
username_field.send_keys(username)
password_field.send_keys(password)

# Press Enter to submit the login form
password_field.send_keys(Keys.RETURN)
time.sleep(5)

# Perform automation actions on Instagram
# Replace with your desired actions

# Close the browser
driver.quit()
