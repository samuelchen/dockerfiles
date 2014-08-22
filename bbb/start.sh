#!/bin/sh

docker run -c 1 -m 128m -d --name="base" -p 10022:22 -p 19001:9001 -v ../log:/var/log -v ../data:/data  samuelchen/base 
