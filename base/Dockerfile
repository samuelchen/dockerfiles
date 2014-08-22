# Base image 
#
# VERSION   0.2.0

FROM        ubuntu
MAINTAINER  Samuel Chen <samuel.net@gmail.com>


# make sure the package repository is up to date
#RUN echo "deb http://cn.archive.ubuntu.com/ubuntu precise main universe" >> /etc/apt/sources.list

# timezone
RUN cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN ntpdate cn.pool.ntp.org

# update
RUN apt-get update
RUN apt-get -y --fix-missing upgrade 

# install  base softwares
RUN apt-get install -y  openssh-server supervisor python-setuptools vim

# start services
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
ADD ./base-supervisord.conf /etc/supervisor/conf.d/base.conf
ADD ./docker-entrypoint.sh /usr/bin/docker-entrypoint.sh
RUN chmod +x /usr/bin/docker-entrypoint.sh

# set root password
RUN echo 'root:123456' | chpasswd

# expose ports
EXPOSE      22 9001

# display info
RUN echo "Port 22 (ssh) 9001 (supervisord) are exposed."
RUN hostname -i

#WORKDIR /root
#ADD ./auto-start.sh /root/auto-start.sh
#chmod +x /root/auto-start.sh

ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]
