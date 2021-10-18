#!/bin/sh -ex

docker build -t 2_of_diamonds .

# XXX: Cap CPU at 30% due to high idle
docker run -dp 25:25 -p 79:79 --rm --name 2_of_diamonds --cpus 0.3 2_of_diamonds
