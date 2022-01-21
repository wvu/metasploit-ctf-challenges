#!/bin/sh -ex

# XXX: Cap CPU at 30% due to high idle
DOCKER_FLAGS="$DOCKER_FLAGS --rm --cpus 0.3"
RUN_CMD="docker run -dp 7770:7770 --name king_of_spades $DOCKER_FLAGS king_of_spades"

docker build -t king_of_spades "${BUILD_DIR:-..}/king_of_spades"

if [ -n "$STARTUP_FILE" ]; then
  echo "$RUN_CMD" >> "$STARTUP_FILE"
  exit
fi

$RUN_CMD
