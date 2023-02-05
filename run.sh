#!/bin/bash

docker build -t django_tutorial . && \

# use this run just to run the container
#docker run -v $(pwd)/src:/app --rm --init django_tutorial

# use this run to run the container and open an interactive bash session into it
docker run \
	-it \
	-v $(pwd)/src:/app \
	-p 8000:8000 \
	--rm \
	--init \
	django_tutorial \
	bash
