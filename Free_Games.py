#! python3

# Free_Games.py - A script that Windows Task Scheduler can run to go and get me them sweet sweet free games I'll probably never play

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import lxml.html
import time
import sys


##################### EDIT THESE ###############################
# Replace these with your info
email = ''
password = ''
two_fa_key = None # Leave as none if you are not using 2FA

# You will want to replace the user-agent below for yours. Just Google 'what is my user agent' and copy that between the single quotes below
user_agent = ''
##################### EDIT THESE ###############################








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
    time.sleep(7)
    # Re-get the source so that we can look for any "Continue" buttons
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
                break
        time.sleep(7)
    except:
        print()

    # Get the source again, just incase we came from clicking the potential "Continue" button
    html = BeautifulSoup(browser.page_source, 'lxml')

    # Get all the button tags so we can see whether we need to grab the game or leave
    buttons = html.find_all('button')

    for button in buttons:
        if button.get_text().upper() == 'OWNED':
            break
        if button.get_text().upper() == 'GET':
            # Get the xpath of this button
            xpath = xpath_soup(button)
            # Use the xpath to grab the browser element (so we can click it)
            browser_element = browser.find_element_by_xpath(xpath)
            browser_element.click()
            time.sleep(4)

            # Re-get the source (again)
            html = BeautifulSoup(browser.page_source, 'lxml')
            # Get all the spans so we can get the "Place Order" button
            spans = html.find_all('span')

            for span in spans:
                if span.get_text().upper() == 'PLACE ORDER':
                    # Get the xpath
                    xpath = xpath_soup(span)
                    # Use the xpath to grab the browser element (so we can click it)
                    purchase_button_element = browser.find_element_by_xpath(xpath)
                    # Create object and add it to the list
                    purchase_button_element.click()
                    break
            # If the EULA prompt shows up, click it
            try:
                browser.find_element_by_xpath('''//span[contains(text(),'I Agree')]''')
            except:
                print()
            else:
                EU_Refund_and_Right_of_Withdrawal_Information = browser.find_element_by_xpath('''//span[contains(text(),'I Agree')]''')
                EU_Refund_and_Right_of_Withdrawal_Information.click()
                time.sleep(2)
            # We only want the first one (usually the game), so leave

            # Wait until redirected to "THANK YOU" page
            wait_redirect_count = 0
            has_warned_captcha = False
            order_confirmed = False
            print("Waiting for order confirmation")
            while True:
                try:
                    if (wait_redirect_count >= 5) & (has_warned_captcha == False):
                        print("Still waiting - Possible captcha requiring completion")
                        has_warned_captcha = True
                    html = BeautifulSoup(browser.page_source, 'lxml')
                    spans = html.find_all('span')
                    for span in spans:
                        if span.get_text().upper() == 'THANK YOU FOR BUYING':
                            order_confirmed = True
                            break
                except:
                    time.sleep(1)
                    wait_redirect_count += 1

                if order_confirmed == True:
                    break
            print("Order confirmed")
            break

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
    try:
        wait_until_clickable_then_click("//*[@id='onetrust-accept-btn-handler']")
        print("Successfully accepted cookies")
    except:
        print("Failed to accept cookies - Could be that they were already accepted previously")

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
    from selenium import webdriver

    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", user_agent) # We will use the user-agent to trick the website into thinking we are a real person. This usually subverts most basic security

    browser = webdriver.Firefox(profile) # Setup the browser object to use our modified profile
    browser.maximize_window()
    return browser

def log_into_account(email, password, two_fa_key=None):
    import pyotp
    from selenium.webdriver.common.keys import Keys

    # Loading login page and waiting until ready
    print("Logging into account " + email)
    browser.get(epic_store_url + "/login")
    if not wait_until_clickable_then_click("//*[@id='login-with-epic']"): # Click 'Sign in with Epic Games'
        raise TypeError("Unable to find login account type button")
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

    # Waiting until redirected to home - captcha detection workaround
    wait_redirect_count = 0
    has_warned_captcha = False
    print("Waiting to be automatically redirected to home page")
    while browser.current_url != epic_home_url:
        if (wait_redirect_count >= 5) & (has_warned_captcha == False):
            print("Still waiting - Possible captcha requiring completion")
            has_warned_captcha = True
        time.sleep(1)
        wait_redirect_count += 1
    print("Successfully logged in " + email)

def get_free_games_list():
    if (browser.current_url != epic_store_url):
        browser.get(epic_store_url)
        wait_until_clickable("//*[@id='sitenav-link-0']") # Page should be loaded now
        time.sleep(5) # Wait 5 more seconds to be safe
        
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
    
    for index, game in enumerate(games): # Go thru each game we found and get it!
        if not try_click_game(game): # Try to click on the current game
            try:
                game['element'].click() # Try to click on the game one last time
            except:
                print("Skipped a game because I couldn't click on it") # If it didn't work, skip to the next game
                continue
        getGame()
        browser.get(epic_store_url) # Go back to the store page to get the other game
        time.sleep(5) # Give the page enough time to load before grabbing the source text
        try: # Selenium complains this object no longer exists, so we need to re-get it so it doesn't explode
            games[index + 1]['element'] = browser.find_element_by_xpath(games[index + 1]['xpath'])
        except:
            break

def wait_until_element_located(xstr, wait_duration=10):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException

    try:
        WebDriverWait(browser, wait_duration).until(EC.presence_of_element_located((By.XPATH, xstr)))
        return True
    except TimeoutException:
        return False

def wait_until_clickable_then_click(xstr, wait_duration=10):
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException

    try:
        wait_until_element_located(xstr, wait_duration)
        WebDriverWait(browser, wait_duration).until(EC.element_to_be_clickable((By.XPATH, xstr)))
        time.sleep(0.5) # Small wait to avoid potential issues
        browser.find_element_by_xpath(xstr).click()
        return True
    except TimeoutException:
        return False
    
def wait_until_clickable(xstr, wait_duration=10):
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException

    try:
        wait_until_element_located(xstr, wait_duration)
        WebDriverWait(browser, wait_duration).until(EC.element_to_be_clickable((By.XPATH, xstr)))
        return True
    except TimeoutException:
        return False

def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    import sys
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)
    browser.quit()

##### MAIN #####
sys.excepthook = show_exception_and_exit

epic_home_url = "https://www.epicgames.com/site/en-US/home"
epic_store_url = "https://www.epicgames.com/store/en-US"

browser = start_firefox_browser(user_agent)
log_into_account(email, password)
claim_free_games()
log_into_account(email, password, two_fa_key)
accept_cookies()
browser.quit()
