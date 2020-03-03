#! python3

# Free_Games.py - A script that Windows Task Scheduler can run to go and get me them sweet sweet free games I'll probably never play

from selenium import webdriver
import time
import lxml.html

##################### EDIT THESE ###############################

# Replace these with your info
usernameOrEmail = 'flumpdoople@gmail.com'
password = 's3cur3p@ssw0rd!!'

# You will want to replace the user-agent below for yours. Just Google 'what is my user agent' and copy that between the single quotes below
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'

##################### EDIT THESE ###############################

# Main store page for Epic Games Store
web_path = '''https://www.epicgames.com/store/en-US'''

profile = webdriver.FirefoxProfile()

# We will use the user-agent to trick the website into thinking we are a real person. This usually subverts most basic security
profile.set_preference("general.useragent.override", user_agent)

# Setup the browser object to use our modified profile
browser = webdriver.Firefox(profile)
browser.get(web_path + '/login')

# Give the page enough time to load before we enter anything
time.sleep(5)

# Let's login and get that out of the way
fill_out_user = browser.find_element_by_id('usernameOrEmail')
fill_out_user.send_keys(usernameOrEmail)
fill_out_pass = browser.find_element_by_id('password')
fill_out_pass.send_keys(password)
fill_out_pass.submit()
time.sleep(6)

# Go back to the store page
browser.get(web_path)
# Give the page enough time to load before grabbing the source text
# If you get any weird errors related to 'root' or anything, start here and adjust the time
time.sleep(2)

# Grab the source text of the html so we can grab stuff from it easier with xpath
root = lxml.html.fromstring(browser.page_source)

# Let's put allll the stuff for the two game links in a dictionary
games = []

# check for and close cookies banner
try:
    browser.find_element_by_xpath('''/html/body/div/div/div[4]/header/div/button/span''')
except:
    print()
else:
    cookies = browser.find_element_by_xpath('''/html/body/div/div/div[4]/header/div/button/span''')
    cookies.click()
    time.sleep(2)

# Imma keep these for archival purposes because the current solution didn't work the first time I tried it. So if it breaks, I'll look into using this again
#game_1_xpath = '''//body[@class='en_US']/div[@id='dieselReactWrapper']/div[@class='App-webApp_63c5411a App-app_108cbe3f']/div[@class='WebApp-webApp_e9fb876f contentGridPosition']/div[@class='Discover-pageWrapper_b7216868 containerSpacingPaddingBottom contentGridPosition storeSpacingTop Discover-customTheme_cc609da3']/span/div[@class='Discover-section_121fb922 gridContentWrapper Discover-fullbleedSection_9aa7215d SectionWrapper-fullBleedOnMobile_81fa72c2 SectionWrapper-horizontalInset_78f5fd4b']/div[@class='SectionWrapper-content_d9895861']/div[@class='CardGroup-root_29b20b59 CardGroup-rootFullBleedOnMobile_82c0bdab']/section[@class='CardGrid-groupWrapper_e669488f']/div[@class='CardGrid-group_c5363b6a']/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]/span[1]'''
#game_2_xpath = '''//body[@class='en_US']/div[@id='dieselReactWrapper']/div[@class='App-webApp_63c5411a App-app_108cbe3f']/div[@class='WebApp-webApp_e9fb876f contentGridPosition']/div[@class='Discover-pageWrapper_b7216868 containerSpacingPaddingBottom contentGridPosition storeSpacingTop Discover-customTheme_cc609da3']/span/div[@class='Discover-section_121fb922 gridContentWrapper Discover-fullbleedSection_9aa7215d SectionWrapper-fullBleedOnMobile_81fa72c2 SectionWrapper-horizontalInset_78f5fd4b']/div[@class='SectionWrapper-content_d9895861']/div[@class='CardGroup-root_29b20b59 CardGroup-rootFullBleedOnMobile_82c0bdab']/section[@class='CardGrid-groupWrapper_e669488f']/div[@class='CardGrid-group_c5363b6a']/div[2]/div[1]/a[1]/div[1]/div[1]/div[1]/span[1]'''
game_1_xpath = '''/html/body/div/div/div[4]/div[1]/span[3]/div/div/div/section/div/div[1]/div/a/div/div/div[1]/span'''
game_2_xpath = '''/html/body/div/div/div[4]/div[1]/span[3]/div/div/div/section/div/div[2]/div/a/div/div/div[1]/span'''

is_game_1_free = True if root.xpath(game_1_xpath + '/text()')[0] == 'Free Now' else False
is_game_2_free = True if root.xpath(game_1_xpath + '/text()')[0] == 'Free Now' else False

game_1_element = browser.find_element_by_xpath(game_1_xpath)
game_2_element = browser.find_element_by_xpath(game_2_xpath)

games.append({'xpath': game_1_xpath,
              'element': game_1_element,
                'freeOrNah': is_game_1_free})

games.append({'xpath': game_2_xpath,
              'element': game_2_element,
                'freeOrNah': is_game_2_free})

# Make a function to actually get the game that we can call later
def getGame(game):
    time.sleep(5)
    try:
        # We won't use this, but if it explodes, then there is no button to click
        root.xpath('''//span[contains(text(),'Continue')]''')
        geez_dad_im_not_a_kid_anymore = browser.find_element_by_xpath('''//span[contains(text(),'Continue')]''')
        geez_dad_im_not_a_kid_anymore.click()
        time.sleep(4)
    except:
        print()

    for elem in browser.find_elements_by_xpath('/html/body/div/div/div[4]/div[3]/div/div[2]/div[2]/div[3]/div/div/div[3]/div/button'):
        if elem.text == 'OWNED':
            break
        if elem.text == 'GET':
            elem.click()
            time.sleep(4)
            purchase = browser.find_element_by_xpath('''/html/body/div[3]/div/div/div[4]/div/div[4]/div[1]/div[2]/div[5]/div/div/button/span''')
            purchase.click()
            time.sleep(2)
            try:
                browser.find_element_by_xpath('''//span[contains(text(),'I Agree')]''')
            except:
                print()
            else:
                EU_Refund_and_Right_of_Withdrawal_Information = browser.find_element_by_xpath('''//span[contains(text(),'I Agree')]''')
                EU_Refund_and_Right_of_Withdrawal_Information.click()
                time.sleep(2)
            # We only want the first one (usually the game), so leave
            break

##### MAIN #####
        
for game in games:
    if game['freeOrNah']:
        game['element'].click()
        getGame(game)
        # Go back to the store page to get the other game
        browser.get(web_path)
        # Give the page enough time to load before grabbing the source text
        time.sleep(4)
        # Selenium complains this object no longer exists, so we need to re-get it so it doesn't explode
        games[1]['element'] = browser.find_element_by_xpath(game_2_xpath)
         
# Close everything
browser.quit()
