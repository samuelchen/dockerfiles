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

# set "docker-host" for the host in hosts
#RUN hostname -I|sed "s/\ /\n/g"|sed "\$d"|sed "s/^/docker-host\t/g" >> /etc/hosts

# set root password
RUN echo "root:123456" | chpasswd

# set volumns
VOLUMN ["/docker-data", "/docker-log"]

# config services
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor
ADD base-supervisord.conf /etc/supervisor/conf.d/base.conf

# config sshd
RUN sed "s/^PermitRootLogin/\#PermitRootLogin/g" /etc/ssh/sshd_config > /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
#COPY sshd_config /etc/ssh/sshd_config

# expose ports (ssh, supervisord http)
EXPOSE  22 9001	

# entrypoint script
ADD ./docker-entrypoint.sh /usr/bin/docker-entrypoint.sh
RUN chmod +x /usr/bin/docker-entrypoint.sh


CMD ["-n"]
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]
