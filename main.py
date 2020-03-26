import schedule
import time
import bs4
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import datetime
import random

users = {"sstryker.mobile@gmail.com":["Sam", "Scolari"], "joeylbarroso@gmail.com":["Joey", "Barroso"], "zentekgm@gmail.com":["Keeton", "Kowalski"]}

def RunTask():
    time.sleep(random.randint(1, 1800)) # Waits either 1 second or 30 minutes
    for user in users.keys(): 
        time.sleep(random.randint(900, 1800)) # Waits either 15 or 30 minutes
        FormSubmitter(user)
        

def FormSubmitter(user):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    print("Submitting form for {}.".format(users[user][0]))
    
    driver.get("https://fs24.formsite.com/shimba/rifgenynyv/index.html")

    time.sleep(2) # Wait for DOM to load

    # Name
    first_name = driver.find_element_by_name("RESULT_TextField-2").send_keys(users[user][0])
    last_name = driver.find_element_by_name("RESULT_TextField-3").send_keys(users[user][1])

    # Grade Level
    current_grade_box = driver.find_element_by_name("RESULT_RadioButton-4").click()
    current_grade_option = driver.find_elements_by_tag_name("option")[2].click()

    # Class
    enrolled_class = driver.find_element_by_xpath('//*[@id="q46"]/table/tbody/tr[10]/td/label').click()

    # School
    my_school = driver.find_element_by_xpath('//*[@id="q59"]/table/tbody/tr[5]/td/label').click()

    # Email
    email = driver.find_element_by_name("RESULT_TextField-7").send_keys(user)
    confirm_email = driver.find_element_by_name("CONFIRM_TextField-7").send_keys(user)

    # Date
    icon_calendar = driver.find_element_by_class_name("icon_calendar").click()
    current_day = driver.find_element_by_class_name("ui-state-highlight").click()

    # Submit
    submit = driver.find_element_by_name("Submit").click()

    print("Successfully submitted the form for {}.".format(user))

    time.sleep(15) # Wait for new page to load
    driver.close()

schedule.every().day.at("7:00").do(RunTask)

while True:
    schedule.run_pending()
    time.sleep(1)

