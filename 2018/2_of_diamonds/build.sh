#!/bin/sh -ex

docker build -t 2_of_diamonds .

# XXX: Cap CPU at 10% due to SIMH bug
docker run -dp 25:25 -p 79:79 --name 2_of_diamonds --cpus .1 2_of_diamonds
