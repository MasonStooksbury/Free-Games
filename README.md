# Free_Games.py Description
Literally just a script that is automatically ran via Windows Task Scheduler or Cron that logs into the Epic Games Store website and grabs the two free games for the week. I've tested it on Windows, but there isn't any reason it wouldn't work on Linux as well. Just change the top line from "#! python3" to "#!/usr/bin/python3" and it should be fine. Hope you enjoy!
  - Mason Stooksbury <><


# Setup
The Python script needs a few things to run:
  - lxml (for parsing the HTML from the webpage) This can be installed by running "pip3 install lxml" in a command prompt/terminal
  - selenium (for roboting the website) This can be installed by running "pip3 install selenium" in a command prompt/terminal
  - GeckoDriver (selenium needs this) Linux people can use this script to do everything for you after installing "jq" which is a JSON processor: https://gist.github.com/cgoldberg/4097efbfeb40adf698a7d05e75e0ff51.  Windows people will need to download it here: https://github.com/mozilla/geckodriver/releases.  You will need to add the location of GeckoDriver to your PATH so that Windows and Python know where to look for it.
  - Firefox (the browser) You can technically do all of this with Chrome, but it involves some more setup with selenium and particular drivers and I'm just too lazy. This works perfectly fine.
  - Replace the "usernameOrEmail" and "password" variables in the code to match your Epic Games Store account. Be sure to leave the single quotes where they are.
  
  
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
