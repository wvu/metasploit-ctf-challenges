#!/bin/sh -ex

DOCKER_FLAGS="$DOCKER_FLAGS --rm"
RUN_CMD="docker run -dp 23:23 --name 5_of_hearts $DOCKER_FLAGS 5_of_hearts"

docker build -t 5_of_hearts "${BUILD_DIR:-..}/5_of_hearts"

if [ -n "$STARTUP_FILE" ]; then
  echo "$RUN_CMD" >> "$STARTUP_FILE"
  exit
fi

$RUN_CMD
