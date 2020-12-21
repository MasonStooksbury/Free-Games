FROM python:3-buster
# Template to be modified
WORKDIR /usr/src/app

# prerequisites before pip install 
RUN apt-get install jq firefox
# Please change this wget location to a more suitable location
RUN wget -o geckodriver-install.sh https://gist.githubusercontent.com/cgoldberg/4097efbfeb40adf698a7d05e75e0ff51/raw/9332fe152f108293834f95d43949f9ff677eecd8/geckodriver-install.sh
RUN ./geckodriver-install.sh

# Installs all the requirements for the python project 
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

# This replaces the .env file
ENV EPIC_EMAIL=changeme
ENV EPIC_PASSWORD=changeme
ENV EPIC_TFA_TOKEN=changeme
ENV USER_AGENT=changeme

COPY ./Free_Games.py .

CMD [ "python", "./Free_Games.py" ]
