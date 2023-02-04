#!/bin/bash

# this script stops the container

set -x
container_id=$(docker ps | rg my_image | awk '{print $1}')
docker stop $container_id
