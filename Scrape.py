./
./                                              _______________
./                                             |  ___________  |
./                                             | | Free Porn | |
./                                             | | Free Porn | |
./                                             | | Free Porn | |
./                                             | |___ ___ ___| |
./----Made by SleepTheGod ClumsyLulz           |_____o___o_____|
./                                               _|__|/ \|_|_
./                                              / ********** \
./                                             / ************ \
./                                           --------------------
./                                          We could be homiesexual
./
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from bs4 import BeautifulSoup


mobile_emulation = {"deviceName": "Nexus 5"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)


# log in
driver.get("https://www.onlyfans.com")

time.sleep(2)

# find the login button
log_in = driver.find_element(By.XPATH, '//button[text()="Log In"]')

log_in.click()


time.sleep(1)


# enter your username and password
username = "username"
password = "password"

# username
user_element = driver.find_element(By.NAME, "username")
user_element.send_keys(username)

# password
pass_element = driver.find_element(By.NAME, "password")
pass_element.send_keys(password)

# log in
pass_element.send_keys(Keys.ENTER)

time.sleep(3)


# Instagram will ask you to save your login information
login_info = driver.find_element(By.XPATH, '//button[text() = "Not Now"]')
login_info.click()


# Let's see if we can start scrolling
SCROLL_PAUSE_TIME = round(random.uniform(1, 3), 2)


check_flag = 1


    
if check_flag == 1:
     # scroll down twice
    scroll(driver, number_of_times=2)

    # check if there's a presentation
    check_for_presentation(driver)

    # scroll again twice
    scroll(driver, number_of_times=2)

    check_for_presentation(driver)

    check_flag = 0



# download for lonleyhands
explore = driver.find_element(By.XPATH, '//a[@href="/explore/"]')
explore.click()

time.sleep(2)

# search for the target
username = driver.find_element(By.CLASS_NAME, "j_2Hd")
username.send_keys("username")

time.sleep(1)

# click the first option that comes up UwU
first_username = driver.find_element(By.CLASS_NAME, "-qQT3")
first_username.click()

# scroll through targets's feed
scroll(driver)

# get image feed and sht
likes, comments = test_grab_photo(driver)

# go back to users nudes
go_back(driver)



# =====================
# Help for retards kek
# =====================

def check_for_presentation(driver):
    import time
    
    # Notifications
    try:
        add_to_home_screen = driver.find_element(By.CLASS_NAME, 'HoLwm')
        add_to_home_screen.click()
        
            
    except Exception as e:
        print("You fucked up somewhere skid")
        print(e)
        
    time.sleep(1)
    
    try:
        notifications = driver.find_element(By.CLASS_NAME, 'HoLwm')
        notifications.click()

    except Exception as e:
        print("You fucked up somewhere skid")
        print(e)

    finally:
        print("All checks completed")




def scroll(driver, number_of_times=1):
    for i in range(number_of_times):
        SCROLL_PAUSE_TIME = round(random.uniform(2, 4), 2)
        driver.execute_script("window.scrollTo({top:document.body.scrollHeight, behaviour: 'smooth'})")

        # wait for the content to finish loading
        time.sleep(SCROLL_PAUSE_TIME)        


def go_back(driver):
    PAUSE_TIME = round(random.uniform(1, 5), 2)
    time.sleep(PAUSE_TIME)
    driver.get("https://www.onlyfans.com/target/")
    time.sleep(PAUSE_TIME)


def test_grab_photo(driver):
    LOWER_LIMIT_SCROLLS, UPPER_LIMIT_SCROLLS = 1, 3
    LOWER_LIMIT_ROW_NUMBER = 1
    
    chosen_numbers = {}
    
    number_of_scrolls = random.randint(LOWER_LIMIT_SCROLLS, UPPER_LIMIT_SCROLLS)
    
    while chosen_numbers.get(number_of_scrolls):
        number_of_scrolls = random.randint(LOWER_LIMIT_SCROLLS, UPPER_LIMIT_SCROLLS)
            
    
    chosen_numbers[number_of_scrolls] = number_of_scrolls
    
    scroll(driver, number_of_times=number_of_scrolls)
    
    # scroll a number of times
    photo_rows = driver.find_elements(By.CLASS_NAME, "Nnq7C")
    
    # pick a random row
    print("Number of rows: {}".format(len(photo_rows)))
    random_row = random.randint(LOWER_LIMIT_ROW_NUMBER, len(photo_rows)-1)
    
    time.sleep(3)
    
    # get likes and comments data
    likes, comments = test_grab_data(driver, photo_rows[random_row])    
    
    return likes, comments


def test_grab_data(driver, photo_row):
    photos = photo_row.find_elements(By.TAG_NAME, "div")
    driver.execute_script("arguments[0].click();", photos[2])
    
    time.sleep(3)
    
    # get nudes from the article element
    try:
        article = driver.execute_script("return document.querySelector('div.eo2As').innerHTML;")
        print("Printing the contents...")
        likes, comments = extract_likes_and_comments(article)
        
        
    except Exception as e:
        print('Unable to find element')
        print(e)
        likes, comments = "", ""
        
    time.sleep(2)
    
    return likes, comments


def extract_images_and_videos(html):
    soup = BeautifulSoup(html, 'lxml')
    likes = soup.find("span", class_="vcOH2").span.text
    
    if(likes == None):
        likes = soup.find("a", class_="zV_Nj").span.text
        
    comments = soup.find("a", class_="r8ZrO").span.text
    
    return likes, comments
