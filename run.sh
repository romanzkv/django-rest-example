#!/bin/bash

docker build -t my_image . && \
docker run -v $(pwd)/src:/app my_image
