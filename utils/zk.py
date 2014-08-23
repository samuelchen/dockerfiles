#!/usr/bin/env python
# coding=utf-8

import os, sys
import commands
import logging

log = logging.getLogger('root')

# temp logging
log.info = lambda x: sys.stdout.write(x + '\n')
log.error = lambda x: sys.stderr.write(x+'\n')

_cwd = '~/dockerfiles' #os.getcwd()
_mem = 128
_cpu = 1
_name = 'node'
_ports = [22, 9001, 2181]
_repository = 'samuelchen/zookeeper'
_data = _cwd + '/data'
_log = _cwd + '/log'
_myid = '/etc/zookeeper/conf/myid'

# nodes count
count = 1
if len(sys.argv) > 1:
	try:
		count = int(sys.argv[1])
	except:
		count = 3


log.info('You are staring %d zookeeper nodes' % count)

nodenames = map(lambda x: '%s%d' % (_name, x), xrange(count))
nodeports = {}
temp_ports = map(lambda x: x+10000, _ports)
for host in nodenames:
	nodeports[host] = temp_ports

	script = 'docker run -c %d -m %dm --name="%s" ' % (_cpu, _mem, host)
	for i in range(len(_ports)):
		script = script + ' -p %d:%d ' % (nodeports[host][i], _ports[i])
		#log.info('exposing container port %d to host port %d' % (nodeports[host][i], _ports[i]))
	vol_data = _data + '/' + host
	vol_log = _log + '/' + host

	script += ' -v %s:/docker-data -v %s:/docker-log ' % (vol_data, vol_log)
	script +=  _repository


	log.info(script)
	sys.command('docker rm %s' % hostname)
	status, out = commands.getstatusoutput(script)
	log.error('status: %d' % status)
	log.error(out)

	temp_ports = map(lambda x: x+1, temp_ports)

