#!/bin/sh

CWD=~/dockerfiles
NUM=$1

if [ $NUM 

touch $CWD/hosts
hostname -I|sed "s/\ /\n/g"|sed "\$d"|sed "s/^/docker-host\t/g" >> hosts

echo "You are staring $NUM zookeeper nodes..."
#docker run -c 1 -m 128m -d --name="zk1" -p 10022:22 -p 19001:9001 -p 12181:2181 -v $CWD/log:/var/log -v $CWD/data:/data  samuelchen/zookeeper
docker run -c 1 -m 128m -d --name="zk1" -p 10022:22 -p 19001:9001 -p 12181:2181 samuelchen/zookeeper

