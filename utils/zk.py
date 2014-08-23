#!/usr/bin/env python
# coding=utf-8

import os, sys
import commands
import logging

log = logging.getLogger('root')

# temp logging
log.info = lambda x: sys.stdout.write(x + '\n')
log.error = lambda x: sys.stderr.write(x+'\n')

_cwd = os.getcwd()
_mem = 128
_cpu = 1
_name = 'node'
_ports = [22, 9001, 2181]
_repository = 'samuelchen/zookeeper'

# nodes count
count = 3
if len(sys.argv) > 1:
	try:
		count = int(sys.argv[1])
	except:
		count = 3


log.info('You are staring %d zookeeper nodes' % count)

nodenames = map(lambda x: '%s%d' % (_name, x), range(count))
nodeports = {}
temp_ports = map(lambda x: x+10000, _ports)
for host in nodenames:
	nodeports[host] = temp_ports

	script = 'docker run -c %d -m %dm --name="%s" ' % (_cpu, _mem, host)
	for i in range(count):
		script = script + ' -p %d:%d ' % (nodeports[host][i], _ports[i])
		log.info('exposing container port %d to host port %d' % (nodeports[host][i], _ports[i]))
	script = script + _repository

	temp_ports = map(lambda x: x+1, temp_ports)
	log.info(script)
	#status, out = commands.getstatusoutput(script)
	#log.error(status)
	#log.error(out)

