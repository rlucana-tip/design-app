#!/bin/bash

docker build -t designapp .
docker run -t -d -p 8080:8080 --name designapprun designapp
docker ps -a