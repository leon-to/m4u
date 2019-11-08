#!/bin/bash

docker image build -t m4u .
docker container run --publish 8000:8000 --detach --name m4u m4u