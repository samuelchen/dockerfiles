# Zookeeper
#
# VERSION   0.0.1

FROM        samuelchen/base
MAINTAINER  Samuel Chen <samuel.net@gmail.com>


# install zookeeper
RUN apt-get install -y zookeeper

# expose port 2181
EXPOSE      2181

# add supervisord conf
ADD zookeeper-supervisord.conf /etc/supervisor/conf.d/zookeeper.conf
COPY zoo.cfg /etc/zookeeper/conf/zoo.cfg

