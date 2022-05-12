FROM ubuntu:latest
RUN apt update -y
RUN apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools git wget nano mongodb -y
RUN pip install uwsgi flask pymongo requests
# RUN prometheus-flask-exporter



ARG BRANCH
RUN mkdir app 
RUN git clone -b $BRANCH https://github.com/abelovn/github_epam_diploma_task.git
WORKDIR github_epam_diploma_task
ENV db_name='epam'
ENV artist_name='The Beatles'
ENV collection='beatles-collection' 
ENV connection_str='main'

ENTRYPOINT uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app --enable-threads