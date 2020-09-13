# Free_Games.py Description

Literally just a script that is automatically ran via Windows Task Scheduler or Cron that logs into the Epic Games Store website and grabs the free games for the week. I've tested it on Windows, but there isn't any reason it wouldn't work on Linux as well. Just change the top line from `#! python3` to `#!/usr/bin/python3` and it should be fine. 

Big shout-out to [@ergoithz](https://github.com/ergoithz) and their amazing function that finds the xpath for a given BeautifulSoup object. These updates wouldn't be possible without it! Check out their super-helpful function here: https://gist.github.com/ergoithz/6cf043e3fdedd1b94fcf

Another *huge* shout-out to [@SonOfDiablo](https://github.com/SonOfDiablo) for creating and providing their awesome PowerShell script for installing geckodriver on Windows! Now you don't have to follow all the steps mentioned before. Just install the PowerShell script, and run it. This will: download and install the latest geckodriver for the correct architecture, install it, and add it to your path if it isn't already there: automagically! Find the script here: https://gist.github.com/SonOfDiablo/81f3d610295c69c777b512e4da90393d

Finally, a warm thank you to:
  - [@Andriesmenze](https://github.com/Andriesmenze) for fixing the script to work in the EU due to certain pop-ups that I wasn't seeing. Their work is very appreciated!
  - [@Steve-Tech](https://github.com/Steve-Tech) for adding some code to click the "Sign in with Epic Games" that apparently shows up now.
  - [@Spifffff](https://github.com/Spifffff) for modifying the Xpath for the cookies banner, for noticing that EGS requires email-only for logging in now, and for modifying the script to work with the games carousel that shows up sometimes
  - [@lemasato](https://github.com/lemasato) for adding 2FA support, adding some more reliability and readability changes as well as adding functionality for multiple accounts to be used.
  - [@Medallyon](https://github.com/Medallyon) for cleaning up my README file and adding "requirements.txt" functionality. This will help cut down on install time/complexity significantly.

Hope you enjoy!
  - Mason Stooksbury <><

### Updates! (09/13/2020)
  -You can now install all the necessary dependencies using the "requirements.txt" created by [@Medallyon](https://github.com/Medallyon). Also, please enjoy the newly manicured README, also courtesy of [@Medallyon](https://github.com/Medallyon)!

# Setup

## Requirements

1. Run `pip install -r requirements.txt` to automatically install dependencies

***OR***

Install them manually:
  + `pip install lxml` (for parsing the HTML from the webpage)
  + `pip install selenium` (for "roboting" the website
  + `pip install beautifulsoup4` (for better/more robust finding of objects and things)
  + `pip install pyotp` (for Two-factor authentication)

### Additionally

+ `GeckoDriver` (selenium needs this) Linux users can use this script to do everything for you after installing "jq" which is a JSON processor: https://gist.github.com/cgoldberg/4097efbfeb40adf698a7d05e75e0ff51. Windows users can use this script provided by [@SonOfDiablo:](https://github.com/SonOfDiablo:) https://gist.github.com/SonOfDiablo/81f3d610295c69c777b512e4da90393d.
+ [Firefox](https://www.mozilla.org/firefox/new/) - You can technically do all of this with Chrome, but it involves some more setup with selenium and particular drivers and I'm just too lazy. This works perfectly fine.
+ Replace the `email` and `password` variables in the code to match your Epic Games Store account. Be sure to leave the single quotes where they are.
+ Finally, you'll also want to jump in and replace the `user_agent` variable. There are instructions inside the script on how to do this.

# Two-factor authentication

If you already have 2FA enabled on your account, you will be required to disabled it temporarily. This is required to retrieve the key we need.

1. Go to [your Epic account settings](https://www.epicgames.com/account/password) and enable "**Authenticator App**".
1. Keep a copy of the "**Manual Entry Key**". This will be used later in the python script. Do not close the page yet.
1. On your phone, download [Google Authentificator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en) or another similar application.
1. Using the application, scan the QR code visible on browser. Enter the code obtained from the application on the browser and click "**Activate**".
1. Keep a copy of the "**Rescue Codes**". This will come in handy to retrieve your account if you ever lose access to your Authentificator application (losing phone, etc.)
1. In the python script, input the "**Manual Entry Key**" retrieved earlier in the corresponding field, again leaving the single quotes as is.
1. Done!
  
# Setting up Windows Task Scheduler

These steps should help you get Windows Task Scheduler setup in such a way that it will wake your computer from sleep and grab your free games then go back to sleep. It will also be setup to run again if something goes wrong as well as kill itself if it goes haywire. I realize the first picture shows it being setup for Vista and Windows Server 2008, but this was the only way it would work on Windows 10 without doing some wonky BIOS setup that only worked for some people.

1. Fill out General:
    1. ![General](https://github.com/MasonStooksbury/Free-Games/blob/master/WTS_Setup/General.png)
2. Fill out Triggers:
    1. ![Triggers](https://github.com/MasonStooksbury/Free-Games/blob/master/WTS_Setup/Triggers.png)
3. Fill out Actions:
    1. ![Actions](https://github.com/MasonStooksbury/Free-Games/blob/master/WTS_Setup/Actions.png)
4. Fill out Conditions:
    1. ![Conditions](https://github.com/MasonStooksbury/Free-Games/blob/master/WTS_Setup/Conditions.png)
5. Fill out Settings:
    1. ![Settings](https://github.com/MasonStooksbury/Free-Games/blob/master/WTS_Setup/Settings.png)
