FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update -y
RUN apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools git wget nano vim -y
# RUN apt install  uwsgi-plugin-python3 -y

RUN pip install uwsgi 
RUN pip install flask 
RUN pip install pymongo 
RUN pip install requests 
RUN echo "deb http://security.ubuntu.com/ubuntu impish-security main" | tee /etc/apt/sources.list.d/impish-security.list
RUN apt update -y
RUN apt install libssl1.1 -y
RUN wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list
RUN apt update -y
RUN apt-get install -y mongodb-org=5.0.8 mongodb-org-database=5.0.8 mongodb-org-server=5.0.8 mongodb-org-shell=5.0.8 mongodb-org-mongos=5.0.8 mongodb-org-tools=5.0.8 

# RUN apt install mongodb-org -y
# RUN prometheus-flask-exporter#



ARG BRANCH
RUN mkdir app 
RUN git clone -b $BRANCH https://github.com/abelovn/github_epam_diploma_task.git
WORKDIR github_epam_diploma_task

RUN wget https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem


ENV db_name='epam'
ENV artist_name='The Beatles'
ENV collection='beatles-collection' 
ENV connection_str='mongodb://root1:password1@docdb-cluster-abelovn-0.chwzxdshuqus.us-east-2.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&retryWrites=false'

ENTRYPOINT uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app --enable-threads