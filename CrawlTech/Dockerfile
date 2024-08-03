FROM python:alpine


RUN mkdir /scrapy
WORKDIR /scrapy

COPY requirements.txt /scrapy/
# نصب وابستگی‌های Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /scrapy/