#!/bin/sh

NUM=$1

echo "You are staring $NUM zookeeper nodes..."
docker run -c 1 -m 128m -d --name="zk1" -p 10022:22 -p 19001:9001 -p 12181:2181 -v ../log:/var/log -v ../data:/data  samuelchen/base

