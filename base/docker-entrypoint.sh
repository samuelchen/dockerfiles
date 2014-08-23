#!/bin/sh

# -n (nodaemon) will pass by CMD command in dockerfile
/usr/bin/supervisord $1
