FROM alpine:3.8

MAINTAINER Aaron Goldsmith "<goldsmithaaron@gmail.com>"

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip setuptools

COPY requirements.txt /opt/postcoder/requirements.txt

WORKDIR /opt/postcoder/

RUN pip install -r requirements.txt

COPY . /opt/postcoder/

RUN python3 setup.py develop

ENTRYPOINT ["postcoder"]
