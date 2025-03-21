#!/bin/bash

CONTAINER="fastapi-example"
DOCKER_HUB_USERNAME="edgar"
DOCKER_REPO="$DOCKER_HUB_USERNAME/$CONTAINER"
VERSION="1.0.1"

MESSAGE="[edgar]"

docker build -t $DOCKER_REPO:$VERSION .
docker push $DOCKER_REPO:$VERSION

echo "[`date "+%Y-%m-%d %H:%M:%S"`] $DOCKER_REPO:$VERSION => {$MESSAGE}" >> logs/ImageInfo.txt
