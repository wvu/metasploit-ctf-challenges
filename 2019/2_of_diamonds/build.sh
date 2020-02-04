#!/bin/sh -ex

# XXX: Cap CPU at 30% due to high idle
DOCKER_FLAGS="$DOCKER_FLAGS --rm --cpus 0.3"
RUN_CMD="docker run -dp 25:25 -p 79:79 --name 2_of_diamonds $DOCKER_FLAGS 2_of_diamonds"

docker build -t 2_of_diamonds "${BUILD_DIR:-..}/2_of_diamonds"

if [ -n "$STARTUP_FILE" ]; then
  echo "$RUN_CMD" >> "$STARTUP_FILE"
  exit
fi

$RUN_CMD
