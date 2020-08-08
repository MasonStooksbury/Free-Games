#! python3
# Free_Games.py - A script that Windows Task Scheduler can run to go and get me them sweet sweet free games I'll probably never play

##################### EDIT THESE ###############################
# Replace these with your info
credentials = []
credentials.append(["myemail@domain.com", "password", "5MBJBQUZRU9K1XULAIL8FKH0UPDX6LDESZEHOFMCIBCYSZ2UEYTQ"]) # Example for account with 2FA
credentials.append(["myemail@domain.com", "password"]) # Example for account without 2FA

# You will want to replace the user-agent below for yours. Just Google 'what is my user agent' and copy that between the single quotes below
user_agent = ''
##################### EDIT THESE ###############################




from bs4 import BeautifulSoup
import lxml.html
import pyotp
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import traceback
from urllib.parse import quote as uriencode

# Find the xpath of a given soup object.
# Full credit goes to ergoithz over at:               https://gist.github.com/ergoithz
# Here is the link to the function on their GitHub:   https://gist.github.com/ergoithz/6cf043e3fdedd1b94fcf
def xpath_soup(element):
    # type: (typing.Union[bs4.element.Tag, bs4.element.NavigableString]) -> str
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:  # type: bs4.element.Tag
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name if 1 == len(siblings) else '%s[%d]' % (
                child.name,
                next(i for i, s in enumerate(siblings, 1) if s is child)
                )
            )
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)

# Make a function to actually get the game that we can call later
def getGame():
    language = None
    while not isinstance(language, str):
        try: 
            language = re.search(r"/store/(\D+?)/", browser.current_url).group(1)
        except Exception:
            pass
    if language != "en-US":
        print("Product page loaded in language other than english, reloading as english")
        browser.get( re.sub(language, "en-US", browser.current_url) )
    else:
        browser.get(browser.current_url)
           
    # Get the source so that we can look for any "Continue" buttons
    html = BeautifulSoup(browser.page_source, 'lxml')
    try:
        spans = html.find_all('span')
        # Check for a "Continue" button for the 18+ games. If we find it, click it
        for span in spans:
            if span.get_text().upper() == 'CONTINUE':
                # Get the xpath
                xpath = xpath_soup(span)
                # Use the xpath to grab the browser element (so we can click it)
                geez_dad_im_not_a_kid_anymore = browser.find_element_by_xpath(xpath)
                geez_dad_im_not_a_kid_anymore.click()
                time.sleep(1)
                html = BeautifulSoup(browser.page_source, 'lxml')
                break
    except Exception:
        pass
        
    try:
        game_title = browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/main/div/nav[1]/div/nav/div/div[1]/ul/li[2]/a/h2/span').text
    except:
        game_title = browser.title
    print("Claiming game " + game_title)    

    if wait_until_element_located("//*[text() = 'Owned']", 1):
        print("Already owned")
        return
    
    wait_until_clickable_then_click("//*[text() = 'Get']")
    wait_until_clickable_then_click("//*[text() = 'Place Order']")    
    
    # Wait until redirected to "THANK YOU" page
    wait_redirect_count = 0
    has_warned_captcha = False
    print("Waiting for order confirmation")
    while True:
        try:
            if wait_until_element_located("//*[text() = 'I Agree']", 0.1): # EULA prompt
                time.sleep(1)
                wait_until_clickable_then_click("//*[text() = 'I Agree']")
                print("EULA accepted")
            if (wait_redirect_count >= 5) & (has_warned_captcha == False):
                print("Still waiting - Possible captcha requiring completion")
                has_warned_captcha = True
                
            if wait_until_element_located("//*[contains(text(), 'Thank you for buying')]"):
                break
            
            time.sleep(1)
            wait_redirect_count += 1
        except Exception:
            pass
    print("Order confirmed")

# Try clicking on a game
def try_click_game(game):
    next_button = try_get_carousel_button()
    for _ in range(60):
        try:
            # Wait 1 second for the game to become clickable, throw an exception if it doesn't
            # If the script gets stuck cycling through the carousel, means that the object it wants to click on
            # is unclickable for some other reason I haven't encountered before
            WebDriverWait(browser, 1).until(
                EC.element_to_be_clickable((By.XPATH, game['xpath']))
            ).click()
        except:
            # Click the next button, cycling through the carousel if it can
            if next_button is not None:
                next_button.click()
        else:
            # Exit the loop once the game was clicked
            return True
    return False

# Check for, and close, the cookies banner
def accept_cookies():
    print("Accepting cookies")
    if wait_until_clickable_then_click("//*[@id='onetrust-accept-btn-handler']"):
        print("Successfully accepted cookies")
    else:
        print("Failed to accept cookies")

# Get carousel next button
def try_get_carousel_button():
    html = BeautifulSoup(browser.page_source, 'lxml') # Grab the source text, and make a beautiful soup object
    next_button_tag = html.find("button", { 'aria-label' : 'Next item' })
    if next_button_tag is not None:
        next_xpath = xpath_soup(next_button_tag)
        return browser.find_element_by_xpath(next_xpath)
    else:
        print('next button not found')
        return None

def start_firefox_browser(user_agent):
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", user_agent) # We will use the user-agent to trick the website into thinking we are a real person. This usually subverts most basic security

    browser = webdriver.Firefox(profile) # Setup the browser object to use our modified profile
    browser.maximize_window()
    return browser

def log_into_account(email, password, two_fa_key=None):
    # Loading login page and waiting until ready
    print("Logging into account " + email)
    browser.get(epic_login_url + "?redirectUrl=" + uriencode(epic_store_url))
    if not wait_until_element_located("//*[@id='email']"):
        raise TypeError("Unable to find email input field")

    # Logging in into the account
    browser.find_element_by_id('email').send_keys(email)
    browser.find_element_by_id('password').send_keys(password)
    if not wait_until_clickable_then_click("//*[@id='login']"):
        raise TypeError("Unable to find login button")
    # 2FA
    if (two_fa_key != None):
        wait_located_count = 0
        has_warned_captcha = False
        while not wait_until_element_located("//*[@id='code']", 1):
            if (wait_located_count >= 3) & (has_warned_captcha == False):
                print("Waiting - Cannot find 2FA input field - Possible captcha requiring completion")
                has_warned_captcha = True
            wait_located_count += 1
        browser.find_element_by_id('code').send_keys(Keys.HOME) # Make sure to be at beginning of field
        browser.find_element_by_id('code').send_keys(pyotp.TOTP(two_fa_key).now()) # 2FA login code
        if not wait_until_clickable_then_click("//*[@id='continue']"):
            raise TypeError("Unable to find 2FA continue button")

    # Waiting until redirected to store - captcha detection workaround
    wait_redirect_count = 0
    has_warned_captcha = False
    print("Waiting to be automatically redirected to store page")
    while not re.search(epic_store_url, browser.current_url):
        if (wait_redirect_count >= 5) & (has_warned_captcha == False):
            print("Still waiting - Possible captcha requiring completion")
            has_warned_captcha = True
        time.sleep(1)
        wait_redirect_count += 1
    print("Successfully logged in " + email)
    browser.get(epic_store_url) # So it automatically waits until page is loaded
    
def log_out():    
    
    browser.get(epic_logout_url + "?redirectUrl=" + uriencode(epic_store_url))
    wait_redirect_count = 0
    has_warned_logout = False
    while not re.search(epic_store_url, browser.current_url):
        if (wait_redirect_count >= 5) & (has_warned_logout == False):
            print("Still waiting to be redirected to store page after logout")
            has_warned_logout = True
        time.sleep(1)
        wait_redirect_count += 1
    print("Successfully logged out\n")

def get_free_games_list():   
    if not re.search(epic_store_url, browser.current_url):
        browser.get(epic_store_url)
        
    html = BeautifulSoup(browser.page_source, 'lxml') # Grab the source text, and make a beautiful soup object
    spans = html.find_all('span') # Get all the span tags to make sure we get every available game
    # Create a list for all the free game dictionaries
    free_games = []
    for span in spans:
        if span.get_text().upper() == 'FREE NOW':
            xpath = xpath_soup(span) # Get the xpath
            browser_element = browser.find_element_by_xpath(xpath) # Use the xpath to grab the browser element (so we can click it)
            free_games.append({'xpath': xpath, 'element': browser_element}) # Create object and add it to the list
            
    if len(free_games) == 0:
        raise TypeError("Free games list is empty")
    
    return free_games

def claim_free_games():
    games = get_free_games_list()
    games_count = len(games)
    for index, game in enumerate(games): # Go thru each game we found and get it!
        if not try_click_game(game): # Try to click on the current game
            try:
                game['element'].click() # Try to click on the game one last time
            except:
                print("Skipped a game because I couldn't click on it") # If it didn't work, skip to the next game
                continue
        getGame()
        if (index < games_count):
            browser.get(epic_store_url) # Go back to the store page to get the other game
        try: # Selenium complains this object no longer exists, so we need to re-get it so it doesn't explode
            games[index + 1]['element'] = browser.find_element_by_xpath(games[index + 1]['xpath'])
        except:
            break

def wait_until_element_located(xstr, wait_duration=10):
    try:
        WebDriverWait(browser, wait_duration).until(EC.presence_of_element_located((By.XPATH, xstr)))
        return True
    except TimeoutException:
        return False

def wait_until_clickable_then_click(xstr, wait_duration=10):
    try:
        wait_until_element_located(xstr, wait_duration)
        WebDriverWait(browser, wait_duration).until(EC.element_to_be_clickable((By.XPATH, xstr)))
        time.sleep(0.5) # Small wait to avoid potential issues
        browser.find_element_by_xpath(xstr).click()
        return True
    except TimeoutException:
        return False
    
def wait_until_clickable(xstr, wait_duration=10):
    try:
        wait_until_element_located(xstr, wait_duration)
        WebDriverWait(browser, wait_duration).until(EC.element_to_be_clickable((By.XPATH, xstr)))
        return True
    except TimeoutException:
        return False

def show_exception_and_exit(exc_type, exc_value, tb):
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)
    browser.quit()

##### MAIN #####
sys.excepthook = show_exception_and_exit

epic_home_url = "https://www.epicgames.com/site/en-US/home"
epic_store_url = "https://www.epicgames.com/store/en-US"
epic_login_url = "https://www.epicgames.com/id/login/epic"
epic_logout_url = "https://www.epicgames.com/id/logout"

browser = start_firefox_browser(user_agent)
for index, account in enumerate(credentials):
    if len(account) == 3:
        log_into_account(account[0], account[1], account[2])
    else:
        log_into_account(account[0], account[1])
    if index == 0:
        accept_cookies()
    claim_free_games()
    log_out()
browser.quit()
