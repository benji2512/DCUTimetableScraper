import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

from_address = #"Your sending email here"
to_address = #"Your receiving email here"
password = #"Your sending email password"

def chrome_init():
    opts = webdriver.ChromeOptions()
    opts.add_argument("headless")
    opts.add_argument("window-size=1920,1080")
    opts.add_argument("no-sandbox")
    opts.add_argument("disable-setuid-sandbox")
    opts.add_argument("disable-dev-shm-usage")
    browser = webdriver.Chrome(options=opts)
    print("Chrome Initilised")
    return browser

def send_email():  
    fromaddr = from_address
    toaddr = to_address
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    # storing the senders email address   
    msg['From'] = fromaddr 
    # storing the receivers email address  
    msg['To'] = toaddr 
    # storing the subject  
    msg['Subject'] = "Timetable Request"
    # string to store the body of the mail 
    body = "Your requested timetable edit from DCU"
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    # open the file to be sent  
    filename = "timeTable.png"
    attachment = open("/home/ben/code/python/year3Timetable/projectFiles/timeTable.png", "rb") 
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    # encode into base64 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    # start TLS for security 
    s.starttls() 
    # Authentication 
    s.login(fromaddr, password) 
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    # terminating the session 
    s.quit()

def main():
    one = "Programme of Study"
    two = "Location"
    three = "Module"
    browser = chrome_init()
    browser.get('https://opentimetable.dcu.ie')
    browser.implicitly_wait(30)
    dropdown_input = input("Enter one = Programme of Study, two = Location or three = Module \n")
    if dropdown_input == "one":
        dropdown_input = "Programmes of Study"
    elif dropdown_input == "two":
        dropdown_input = "Location"
    elif dropdown_input == "three":
        dropdown_input = "Module"
    search_type_dropdown = Select(browser.find_element_by_xpath("//select[@class='js-pg-changemange-search-type']"))
    search_type_dropdown.select_by_visible_text(dropdown_input)
    print("Input in dropdown complete")
    if dropdown_input == "Programmes of Study":
        textSearch_input = input("What programme? \n")
    elif dropdown_input == "Location":
        textSearch_input = "GLA."
        textSearch_input += input("What room? \n")
    elif dropdown_input == "Module":
        textSearch_input = input("What Module? \n")
    programme_input = browser.find_element_by_id('textSearch')
    programme_input.send_keys(textSearch_input)
    print("Sent information to webpage")
    time.sleep(3)
    tick_checkbox = browser.find_element_by_xpath("//input[@type='checkbox']")
    tick_checkbox.click()
    time.sleep(4)
    print("Clicked checkbox")
    close_sidebar = browser.find_element_by_xpath("//i[@class='i-core i-core--double-arrow-left']")
    close_sidebar.click()
    time.sleep(4)
    print("Closed sidebar")
    expand_table = browser.find_element_by_xpath("//span[@class='slider round']")
    expand_table.click()
    time.sleep(2)
    print("Table expanded")
    browser.get_screenshot_as_file("timeTable.png")
    print('Screenshot taken')
    browser.quit()
    print("Closed browser")
    send_email()
    print("Email sent")

if __name__ == "__main__":
    main()
