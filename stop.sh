#!/bin/bash

# this script stops the container

# set -x
container_id=$(docker ps | rg django_tutorial | awk '{print $1}')
if [ -z "$container_id" ]; then
    echo "countainer not found"
    exit 1
fi
docker stop -t 0 $container_id
