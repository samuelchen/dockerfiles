#!/bin/sh

CWD=~/dockerfiles

docker run -c 1 -m 128m -d --name="base" -p 10022:22 -p 19001:9001 -v $CWD/log:/var/log -v $CWD/data:/data  samuelchen/base 
