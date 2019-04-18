#!/bin/sh -ex

# XXX: Cap CPU at 10% due to SIMH bug
DOCKER_FLAGS="$DOCKER_FLAGS --cpus .1"

docker build -t 2_of_diamonds "${BUILD_DIR:-..}/2_of_diamonds"
docker run -dp 25:25 -p 79:79 --name 2_of_diamonds $DOCKER_FLAGS 2_of_diamonds
