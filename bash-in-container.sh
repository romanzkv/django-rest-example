#!/bin/bash

# this script runs interactive bash sessios insithe the continer

set -x
container_id=$(docker ps | rg django_tutorial | awk '{print $1}')
docker exec -it $container_id bash
