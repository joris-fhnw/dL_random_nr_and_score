#!/usr/bin/env bash

EXERCISE_ID=d4da5c33-7e6d-49e8-926c-0b31900b6f77

docker build --no-cache --label=pytm.exercise="$EXERCISE_ID" -t $EXERCISE_ID .
docker stop $EXERCISE_ID && docker rm $EXERCISE_ID
docker run -p 8000:8080 -d --name $EXERCISE_ID $EXERCISE_ID:latest
