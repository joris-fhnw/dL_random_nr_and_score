#!/usr/bin/env bash

EXERCISE_ID=f6a7f9e3-9a54-447b-b9e1-986c7fc4c57d

docker build --no-cache --label=pytm.exercise="$EXERCISE_ID" -t $EXERCISE_ID .
docker stop $EXERCISE_ID && docker rm $EXERCISE_ID
docker run -p 8000:8080 -d --name $EXERCISE_ID $EXERCISE_ID:latest
