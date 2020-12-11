FROM python:3.9.1-buster

COPY requirements.txt /opt/requirements.txt

RUN pip3 install --upgrade pip \
 && pip3 install -r /opt/requirements.txt
