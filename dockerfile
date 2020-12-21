FROM python:3-alpine

# Template to be modified
WORKDIR /usr/src/app

# Prerequisites before pip install 
RUN apk add --no-cache bash curl libxml2-dev libxml2 libxslt g++ gcc libxslt-dev jq firefox xauth 

# Script used to install GeckoDriver
COPY docker-geckodriver-install.sh ./
RUN chmod +x ./docker-geckodriver-install.sh && ./docker-geckodriver-install.sh

# Installs all the requirements for the python project 
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

# variables needed for docker specific selineum
ENV DISPLAY=:99
ENV IS_DOCKER=True

# This replaces the .env file
ENV EPIC_EMAIL=changeMe
ENV EPIC_PASSWORD=changeMe
ENV EPIC_TFA_TOKEN=changeMe
ENV USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"



COPY Free_Games.py .

CMD [ "python", "./Free_Games.py" ]
