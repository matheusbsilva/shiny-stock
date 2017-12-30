FROM python:3.6

RUN mkdir /shinystock
WORKDIR /shinystock/

ADD requirements.txt /shinystock/
RUN pip install -r requirements.txt

ADD . /shinystock/
