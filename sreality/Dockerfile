FROM python:3.11.6
RUN apt-get update && apt-get upgrade
RUN python -m venv venv
RUN . "./venv/bin/activate" 
RUN python -m pip install --upgrade pip
COPY ./requierements.txt .
RUN pip install --no-cache-dir -r requierements.txt
RUN playwright install --with-deps chromium
COPY . .
CMD [ "scrapy","crawl", "reality" ]