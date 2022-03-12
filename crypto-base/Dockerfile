FROM python:3.9.10-buster

COPY requirements.txt /opt/requirements.txt

RUN pip3 install --upgrade pip \
 && pip3 install -r /opt/requirements.txt
