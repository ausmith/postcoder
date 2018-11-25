FROM alpine:3.8

MAINTAINER Aaron Goldsmith "<goldsmithaaron@gmail.com>"

RUN apk add --no-cache python py-pip

COPY requirements.txt /opt/postcoder/requirements.txt

WORKDIR /opt/postcoder/

RUN pip install -r requirements.txt

COPY . /opt/postcoder/

RUN python setup.py develop

ENTRYPOINT ["postcoder"]
