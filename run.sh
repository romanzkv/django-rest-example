#!/bin/bash

docker build -t django_tutorial . && \
docker run -v $(pwd)/src:/app --rm django_tutorial
