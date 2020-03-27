# Free_Games.py Description
Literally just a script that is automatically ran via Windows Task Scheduler or Cron that logs into the Epic Games Store website and grabs the two free games for the week. I've tested it on Windows, but there isn't any reason it wouldn't work on Linux as well. Just change the top line from "#! python3" to "#!/usr/bin/python3" and it should be fine. 

Quick shout-out to Andriesmenze for fixing this to work in the EU due to certain pop-ups that I wasn't seeing. Their work is very appreciated!

Another shout-out to ergoithz and their amazing function that finds the xpath for a given BeautifulSoup object. These updates wouldn't be possible without it! Check out thier super-helpful function here: https://gist.github.com/ergoithz/6cf043e3fdedd1b94fcf

Another *huge* shout-out to SonOfDiablo for creating and providing their awesome PowerShell script for installing geckodriver on Windows! Now you don't have to follow all the steps mentioned before. Just install the PowerShell script, and run it. This will: download and install the latest geckodriver for the correct architecture, install it, and add it to your path if it isn't already there: automagically! Find the script here: https://gist.github.com/SonOfDiablo/81f3d610295c69c777b512e4da90393d

Hope you enjoy!
  - Mason Stooksbury <><


# Updates II! (03/26/2020)
  - [1] Worked for 3 games. Tested today.
  - [2] SonOfDiablo created and provided an amazing PowerShell script to download and install geckodriver for Windows users! Find it here: https://gist.github.com/SonOfDiablo/81f3d610295c69c777b512e4da90393d

# Updates! (03/21/2020)
  - [1] The script can now handle more than two games! With the code I've got now, it should handle any amount of free games that show up.
  - [2] The script has been totally overhauled to work with BeautifulSoup. I had forgotten how amazing it was since first starting Python and a buddy turned me back on to it. This reworking will hopefully make the script far more robust to changes.


# Setup
The Python script needs a few things to run:
  - lxml (for parsing the HTML from the webpage) This can be installed by running "pip3 install lxml" in a command prompt/terminal
  - selenium (for roboting the website) This can be installed by running "pip3 install selenium" in a command prompt/terminal
  - BeautifulSoup (for better/more robust finding of objects and things) This can be installed by running "pip3 install beautifulsoup4". This addition will hopefully mean that it will break less often!
  - GeckoDriver (selenium needs this) Linux people can use this script to do everything for you after installing "jq" which is a JSON processor: https://gist.github.com/cgoldberg/4097efbfeb40adf698a7d05e75e0ff51.  Windows people can use this script provided by SonOfDiablo: https://gist.github.com/SonOfDiablo/81f3d610295c69c777b512e4da90393d.
  - Firefox (the browser) You can technically do all of this with Chrome, but it involves some more setup with selenium and particular drivers and I'm just too lazy. This works perfectly fine.
  - Replace the "usernameOrEmail" and "password" variables in the code to match your Epic Games Store account. Be sure to leave the single quotes where they are.
  - Finally, you'll also want to jump in and replace the user-agent. There are instructions inside the script on how to do this.
  
  
  # Setting up Windows Task Scheduler
  These steps should help you get Windows Task Scheduler setup in such a way that it will wake your computer from sleep and grab your free games then go back to sleep. It will also be setup to run again if something goes wrong as well as kill itself if it goes haywire. I realize the first picture shows it being setup for Vista and Windows Server 2008, but this was the only way it would work on Windows 10 without doing some wonky BIOS setup that only worked for some people.
  - Fill out General:
    - ![General](https://github.com/MasonStooksbury/Free-Games/blob/master/WTS_Setup/General.png)
  
  - Fill out Triggers:
    - ![Triggers](https://github.com/MasonStooksbury/Free-Games/blob/master/WTS_Setup/Triggers.png)
  
  - Fill out Actions:
    - ![Actions](https://github.com/MasonStooksbury/Free-Games/blob/master/WTS_Setup/Actions.png)
  
  - Fill out Conditions:
    - ![Conditions](https://github.com/MasonStooksbury/Free-Games/blob/master/WTS_Setup/Conditions.png)
  
  - Fill out Settings:
    - ![Settings](https://github.com/MasonStooksbury/Free-Games/blob/master/WTS_Setup/Settings.png)
