FROM python:3
# template to be modified
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV EPIC_EMAIL=default
ENV EPIC_PASSWORD=default
ENV EPIC_TFA_TOKEN=default

COPY . .

CMD [ "python", "./Free_Games.py" ]
