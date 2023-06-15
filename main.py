import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager
import time as time
from datetime import datetime,timedelta
import dateparser
import smtplib


chrome_options=Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
  


## function that sends an email about the status 
def send_conf_email(body):
    try:
        sender_email='rishabh040801@gmail.com'
        reciever_email='rgundavarapu@wisc.edu'
        server_ssl=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server_ssl.ehlo()
        subject = 'Sign in Successful'
        email_text = f"""\
        From: {sender_email}
        To: {reciever_email}
        Subject: {subject}
        \n
        {body}
        """
        gmail_pass = os.environ['gmail_password']
        server_ssl.login(sender_email, gmail_pass)
        server_ssl.sendmail(sender_email,reciever_email,email_text)
        server_ssl.close()
    except:
        print('error')



## make send_conf_email situational on messages

url='https://whentowork.com'
driver.get(url)

btn = driver.find_element(by='xpath',value='/html/body/nav/div/div[1]/div/ul/li[2]/button').click()
user_id='rishabh329' #hide
useridbox=driver.find_element(by='xpath',value='//*[@id="username"]').send_keys(user_id)
passwdbox=driver.find_element(by='xpath',value='//*[@id="password"]').send_keys(whenpass)
time.sleep(2)

signinbutton=driver.find_element(by='xpath',value='/html/body/div/div/div/div/div/form/div[2]/button').click()

mysched=driver.find_element(by='xpath',value='//*[@id="myschedule"]').click()
upcomingshed=driver.find_element(by='xpath',value='//*[@id="AutoNumber2"]/tbody/tr[2]/td[3]').click()
nextshift=driver.find_element(by='xpath',value='//*[@id="maincontent"]/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/nobr/b').text
timeperiod=driver.find_element(by='xpath',value='//*[@id="maincontent"]/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[1]').text

send_conf_email(timeperiod)
print('sent email')
#check if you have already signed in
# check if current status is 'in' and then check for time.total_seconds and then sign out

startshift=timeperiod.split('\n')[1].split('-')[0]
endshift=timeperiod.split('\n')[1].split('-')[1]
totalstart=dateparser.parse(nextshift)+timedelta(hours=dateparser.parse(startshift).hour)-datetime.now()
totalend=dateparser.parse(nextshift)+timedelta(hours=dateparser.parse(endshift).hour)-datetime.now()
if (False): #totalstart.total_seconds()<540
    ### myuw signin
    loginurl='https://my.wisc.edu/'
    driver.get(loginurl)
    netid='rgundavarapu'
    meow=driver.find_element(by='xpath',value='//*[@id="j_username"]').send_keys(netid)
    meow2=driver.find_element(by='xpath',value='//*[@id="j_password"]').send_keys(uwpass)
    signin2=driver.find_element(by='xpath',value='//*[@id="loginForm"]/div[3]/div/button').click()
    time.sleep(30)
    launch=driver.find_element(by='xpath',value='//*[@id="widget-id-leave-statement"]/md-card-content/widget-content/div/basic-widget/launch-button/a').click()
    time.sleep(2)
    webclock=driver.find_element(by='xpath',value='//*[@id="Pluto_89_ctf6_1044965_dl-time-absence"]/div[2]/div[3]/a').click()
    #get current window handle
    p = driver.current_window_handle

    #get list of window handles
    chwd = driver.window_handles

    for w in chwd:
        if(w!=p):
            driver.switch_to.window(w) #switch to child window
    orgbtton=driver.find_element(by='xpath',value='//*[@id="campus-select"]/option[5]').click()
    gobutton=driver.find_element(by='xpath',value='//*[@id="submit-go"]').click()
    ## actual signing in  -- do not run until actually working
    time.sleep(30)
    attempts=5
    for i in range(attempts):
        try:
            punchbutton=driver.find_element(by='xpath',value='//*[@id="TL_RPTD_TIME_PUNCH_TYPE$0"]/option[2]').click()
            time.sleep(5)
            timecode=driver.find_element(by='xpath',value='//*[@id="TL_RPTD_TIME_TRC$0"]/option[2]').click()
            send_conf_email('Hey, I have successfully punched in for work. Have a good shift! ')
            break
        except NoSuchElementException:
            time.sleep(5)
    #finalsubmit=driver.find_element(by='xpath',value='//*[@id="TL_WEB_CLOCK_WK_TL_SAVE_PB"]').click()
    #driver.close()
    #driver.switch_to.window(chwd[0])
    #driver.close()
elif(True): #totalend.total_seconds()<300
    loginurl='https://my.wisc.edu/'
    driver.get(loginurl)
    netid='rgundavarapu'
    print('in last cell')
    meow=driver.find_element(by='xpath',value='//*[@id="j_username"]').send_keys(netid)
    meow2=driver.find_element(by='xpath',value='//*[@id="j_password"]').send_keys(uwpass)
    signin2=driver.find_element(by='xpath',value='//*[@id="loginForm"]/div[3]/div/button').click()
    time.sleep(30)
    launch=driver.find_element(by='xpath',value='//*[@id="widget-id-leave-statement"]/md-card-content/widget-content/div/basic-widget/launch-button/a').click()
    time.sleep(2)
    webclock=driver.find_element(by='xpath',value='//*[@id="Pluto_89_ctf6_1044965_dl-time-absence"]/div[2]/div[3]/a').click()
    #get current window handle
    p = driver.current_window_handle

    #get list of window handles
    chwd = driver.window_handles

    for w in chwd:
        if(w!=p):
            driver.switch_to.window(w) #switch to child window
    orgbtton=driver.find_element(by='xpath',value='//*[@id="campus-select"]/option[5]').click()
    gobutton=driver.find_element(by='xpath',value='//*[@id="submit-go"]').click()
    ## actual signing in  -- do not run until actually working
    time.sleep(30)
    attempts=5
    for i in range(attempts):
        try:
            punchbutton=driver.find_element(by='xpath',value='//*[@id="TL_RPTD_TIME_PUNCH_TYPE$0"]/option[4]').click()
            time.sleep(5)
            timecode=driver.find_element(by='xpath',value='//*[@id="TL_RPTD_TIME_TRC$0"]/option[2]').click()
            send_conf_email('Hey, I have successfully punched out for work. Enjoy! ')
            break
        except NoSuchElementException:
            time.sleep(5)
    #finalsubmit=driver.find_element(by='xpath',value='//*[@id="TL_WEB_CLOCK_WK_TL_SAVE_PB"]').click()
    #driver.close()
    #driver.switch_to.window(chwd[0])
    #driver.close()
driver.close()
