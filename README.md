# Free_Games.py Description
Literally just a script that is automatically ran via Windows Task Scheduler or Cron that logs into Epic Store Games' website and grabs the two free games for the week. I've tested it on Windows, but there isn't any reason it wouldn't work on Linux as well. Just change the top line from "#! python3" to "#!/usr/bin/python3" and it should be fine.


# Setup
The Python script needs a few things to run:
  - lxml (for parsing the HTML from the webpage) This can be installed by running "pip3 install lxml" in a command prompt/terminal
  - selenium (for roboting the website) This can be installed by running "pip3 install selenium" in a command prompt/terminal
  - GeckoDriver (selenium needs this. Linux people can use this script to do everything for you after installing "jq" which is a JSON processor: https://gist.github.com/cgoldberg/4097efbfeb40adf698a7d05e75e0ff51.  Windows people will need to download it here: https://github.com/mozilla/geckodriver/releases.  You will need to add the location of GeckoDriver to your PATH so that Windows and Python know where to look for it.
  
  
  # Setting up Windows Task Scheduler
  These steps should help you get Windows Task Scheduler setup in such a way that it will wake your computer from sleep and grab your free games then go back to sleep. It will also be setup to run again if something goes wrong as well as kill itself if it goes haywire. I realize the first picture shows it being setup for Vista and Windows Server 2008, but this was the only way it would work on Windows 10 without doing some wonky BIOS setup that only worked for some people.
  - Fill out ![General](https://github.com/MasonStooksbury/Free-Games/General.png)
  
  - Fill out ![Triggers](https://github.com/MasonStooksbury/Free-Games/Triggers.png)
  
  - Fill out ![Actions](https://github.com/MasonStooksbury/Free-Games/Actions.png)
  
  - Fill out ![Conditions](https://github.com/MasonStooksbury/Free-Games/Conditions.png)
  
  - Fill out ![Settings](https://github.com/MasonStooksbury/Free-Games/Settings.png)
