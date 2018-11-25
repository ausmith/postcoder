# postcoder
CLI for interacting with postal codes

Initially, just looking at UK postcodes (cause they are so different
from US postal codes) using postcodes.io.

## Prerequisite

It is assumed you have a recent version of Docker and are capable of
using GNU Make to build and run the code.

## Usage

To test the code:

```
make test
```

To get postcode output:

```
make build
...
docker run -it --rm localhost/ausmith/postcoder:0.1.0 "CB3 0FA"
```

This takes in the postcode "CB3 0FA" and outputs some of the info
about it. If a postcode is determined to be invalid according to
the input country, then it will just say the code is invalid.

Invalid example:

```bash
$ docker run -it --rm localhost/ausmith/postcoder:0.1.0 "XXX"
Postcode 'XXX' is invalid
404 Client Error: Not Found for url: https://api.postcodes.io/postcodes/XXX
```

## Without Docker

So you don't have docker or want to run this code outside of docker.
Ok, that can be done too.

Requirements:

* Python3
* pip3

Once those are installed:

```
cd postcoder
pip3 install -r requirements.txt
python3 setup.py develop
postcoder "CB3 0FA"
```
