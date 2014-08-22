# Zookeeper
#
# VERSION   0.0.1

FROM        samuelchen/base
MAINTAINER  Samuel Chen <samuel.net@gmail.com>


# install zookeeper
RUN apt-get install -y zookeeper

# expose port 2181
EXPOSE      2181

# display info
RUN echo "Port 2181 is exposed"
RUN hostname -i

# add supervisord conf
ADD ./zookeeper-supervisord.conf /etc/supervisor/conf.d/zookeeper.conf
