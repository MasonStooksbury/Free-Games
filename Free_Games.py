#! python3
# Free_Games.py - A script that Windows Task Scheduler can run to go and get me them sweet sweet free games I'll probably never play

from os import getenv
from dotenv import load_dotenv
load_dotenv()

credentials = [getenv("EPIC_EMAIL"), getenv("EPIC_PASSWORD"), getenv("EPIC_TFA_TOKEN") if len(getenv("EPIC_TFA_TOKEN")) > 0 else None]
print(credentials)

# You may desire to replace the user-agent below. You can leave it as is or google 'what is my user agent' and copy that between the single quotes below
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"

import lxml.html, pyotp, re, sys, time, traceback
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    wait_until_xpath_visible("//*[@id='siteNav']")
    time.sleep(1)
               
    game_title = browser.title
    print("Claiming game " + game_title)    
    
    wait_until_xpath_clickable_then_click("//*[text() = 'Continue']", 1) # Continue +18 button

    if wait_until_xpath_visible("//*[text() = 'Owned']", 1):
        print("Already owned")
        return
    
    try:
        if not wait_until_xpath_clickable_then_click("//*[text() = 'Get']"):
            raise TypeError("Unable to find 'Get' button")
    except:
        print("Failed to click on 'Get' button. Using parent element workaround... ", end='')
        if not wait_until_xpath_clickable_then_click("//*[text() = 'Get']/.."):
            raise TypeError("Workaround failed")
        else:
            print("Worked")
    if not wait_until_xpath_clickable_then_click("//*[text() = 'Place Order']"):
        raise TypeError("Unable to find 'Place Order' button")
        
    # Wait until redirected to "THANK YOU" page
    wait_redirect_count = 0
    has_warned_captcha = False
    eula_accepted = False
    print("Waiting for order confirmation")
    while True:
        try:
            if (eula_accepted == False):
                if wait_until_xpath_visible("//*[text() = 'I Agree']", 1): # EULA prompt
                    time.sleep(1)
                    wait_until_xpath_clickable_then_click("//*[text() = 'I Agree']")
                    print("EULA accepted")
                    eula_accepted = True
                    
            if (wait_redirect_count >= 5) & (has_warned_captcha == False):
                print("Still waiting - Possible captcha requiring completion")
                has_warned_captcha = True
                
            if wait_until_xpath_visible("//*[contains(text(), 'Thank you for buying') or contains(text(), 'Got Epic Games')]", 1):
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
        if wait_until_xpath_clickable_then_click(game["xpath"], 1):
            # Wait 1 second for the game to become clickable, throw an exception if it doesn't
            # If the script gets stuck cycling through the carousel, means that the object it wants to click on
            # is unclickable for some other reason I haven't encountered before           
            # Exit the loop once the game was clicked
            return True
        else:
            # Click the next button, cycling through the carousel if it can
            if next_button is not None:
                print("Cycling through carousel")
                next_button.click()           
    return False

# Check for, and close, the cookies banner
def accept_cookies():
    print("Accepting cookies")
    is_displayed_count = 0
    has_warned_cookies = False
    cookies_button = wait_until_xpath_clickable_then_click("//*[@id='onetrust-accept-btn-handler']")
    if cookies_button:
        while cookies_button.is_displayed(): # Wait until cookie banner disappears
            if (is_displayed_count >= 5) & (has_warned_cookies == False):
                print("Waiting - Cookies banner is still visible and obscuring games elements")
            is_displayed_count += 1
            time.sleep(1)
        print("Successfully accepted cookies")
    else:
        print("Cookies banner not found, probably accepted already")

# Get carousel next button
def try_get_carousel_button():
    next_button_tag = wait_until_xpath_visible("//*[@aria-label='Next item']")
    if next_button_tag:
        return next_button_tag
    else:
        print("Carousel 'Next item' button not found")
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
    if not wait_until_xpath_presence_located("//*[@id='email']"):
        raise TypeError("Unable to find email input field")

    # Logging in into the account
    browser.find_element_by_id('email').send_keys(email)
    browser.find_element_by_id('password').send_keys(password)
    if not wait_until_xpath_clickable_then_click("//*[@id='sign-in']"):
        raise TypeError("Unable to find sign-in button")
    # 2FA
    if (two_fa_key != None):
        wait_located_count = 0
        has_warned_captcha = False
        while not wait_until_xpath_presence_located("//*[@id='code']", 1):
            if (wait_located_count >= 3) & (has_warned_captcha == False):
                print("Waiting - Cannot find 2FA input field - Possible captcha requiring completion")
                has_warned_captcha = True
            wait_located_count += 1
        browser.find_element_by_id('code').send_keys(Keys.HOME) # Make sure to be at beginning of field
        browser.find_element_by_id('code').send_keys(pyotp.TOTP(two_fa_key).now()) # 2FA login code
        if not wait_until_xpath_clickable_then_click("//*[@id='continue']"):
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
    wait_until_xpath_visible("//*[@id='siteNav']")
    time.sleep(1)
    
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
        wait_until_xpath_visible("//*[@id='siteNav']")
        time.sleep(1)
    
    free_now_xpath_str = "//*[translate(text(),'FREE NOW','free now') = 'free now']"
    get_it_free_xpath_str = "//*[translate(text(),'GET IT FREE','get it free') = 'get it free']"           
                
    free_now_elements = browser.find_elements_by_xpath(free_now_xpath_str)
    get_it_free_element = browser.find_elements_by_xpath(get_it_free_xpath_str)
    if len(free_now_elements) == 0 & len(get_it_free_element) == 0:
        raise TypeError("Free games list is empty")
    
    free_games = []
    for index, element in enumerate(free_now_elements):
        num = "[" + str(index+1) + "]"
        free_games.append({"xpath": "(" + free_now_xpath_str + ")" + num, "element": element}) # Literally "(//*[translate(text(),'FREE NOW','free now') = 'free now'])[1]"
    for index, element in enumerate(get_it_free_element):
        num = "[" + str(index+1) + "]"
        free_games.append({"xpath": "(" + get_it_free_xpath_str + ")" + num, "element": element}) # Literally "(//*[translate(text(),'GET IT FREE','get it free') = 'get it free'])[1]"
    
    return free_games

def claim_free_games():
    games = get_free_games_list()
    games_count = len(games)
    print("Found " + str(games_count) + " free games")
    for index, game in enumerate(games): # Go thru each game we found and get it!
        if not try_click_game(game): # Try to click on the current game
            try:
                game.click() # Try to click on the game one last time
            except:
                game_claim_errors_count += 1
                print("Game at index " + str(index) + " was skipped due to being unable to click on it") # If it didn't work, skip to the next game
                continue
        getGame()
        if (index+1 < games_count):
            browser.get(epic_store_url) # Go back to the store page to get the other game
            wait_until_xpath_visible("//*[@id='siteNav']")
            time.sleep(1)
            games[index+1]["element"] = browser.find_element_by_xpath(game["xpath"]) # Selenium complains this object no longer exists, so we need to re-get it so it doesn't explode
            

def wait_until_xpath_presence_located(xstr, wait_duration=10):
    try:
        element = WebDriverWait(browser, wait_duration).until(EC.presence_of_element_located((By.XPATH, xstr)))
        return element
    except TimeoutException:
        return False

def wait_until_xpath_clickable_then_click(xstr, wait_duration=10):
    try:
        element = WebDriverWait(browser, wait_duration).until(EC.element_to_be_clickable((By.XPATH, xstr)))
        time.sleep(0.5) # Small wait to avoid potential issues
        browser.find_element_by_xpath(xstr).click()
        return element
    except TimeoutException:
        return False
    
def wait_until_xpath_clickable(xstr, wait_duration=10):
    try:
        element = WebDriverWait(browser, wait_duration).until(EC.element_to_be_clickable((By.XPATH, xstr)))
        return element
    except TimeoutException:
        return False
    
def wait_until_xpath_visible(xstr, wait_duration=10):
    start_time = time.time()
    while True:
        try:
            element = WebDriverWait(browser, wait_duration).until(EC.presence_of_element_located((By.XPATH, xstr)))
            if element.is_displayed():
                return element
            if ( (time.time() - start_time) > wait_duration ):
                return False
            time.sleep(1)
            
        except TimeoutException:
            return False
    
def show_exception_and_exit(exc_type, exc_value, tb):
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    browser.quit()
    sys.exit(-1)
   
##### MAIN #####
sys.excepthook = show_exception_and_exit
game_claim_errors_count = 0

epic_home_url = "https://www.epicgames.com/site/en-US/home"
epic_store_url = "https://www.epicgames.com/store/en-US"
epic_login_url = "https://www.epicgames.com/id/login/epic"
epic_logout_url = "https://www.epicgames.com/id/logout"

browser = start_firefox_browser(user_agent)
log_into_account(*credentials)
accept_cookies()
claim_free_games()

log_out()
browser.quit()

if game_claim_errors_count > 0:
    print("/!\\ Some games failed to be claimed /!\\")
    input("Press any key to exit.")
