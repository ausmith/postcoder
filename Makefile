SHELL ?= /bin/bash
export VERSION ?= $(shell cat version)
export IMAGE_NAME ?= localhost/ausmith/postcoder

.PHONY: test build

test:
	docker build -f Dockerfile_test -t "${IMAGE_NAME}_test:latest" .
	docker run -it --rm "${IMAGE_NAME}_test:latest"

build:
	docker build -f Dockerfile -t "${IMAGE_NAME}:${VERSION}" .
