#!/bin/bash

# this script stops the container

set -x
container_id=$(docker ps | rg django_tutorial | awk '{print $1}')
docker stop -t 0 $container_id
