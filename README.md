dockerfiles
===========

My docker files

1. Auto-build on docker hub

1. `config_latest_docker.sh` is the script used to set docker repository source and get latest version in ubuntu.

1. `./base/` folder contains the  base dockerfile. Use it to build my base images.
 * It bases on ubuntu latesed image.
 * It contains `supervisord` service.
 * supervisord will start sshd by using `/etc/supervisor/conf.d/base.conf`
 * Copy your own `foo.conf` to `/etc/supervisor/conf.d/` to start it automatically by supervisor.
 * Use `> docker build -t samuelchen/base .` in base/ folder to create this image
 * The password of root is '123456'. Change it in Dockerfile.
 * Port 22 is exposed for sshd. Use `docker run -d -p 10022:22 samuelchen/base` to start. Then you could connect via `ssh -p 10022 localhost` to login to this container.
 * Port 9001 is exposed for supervisord. Use `docker -d -p 10022:22 -p 19001:9001 samuelchen/base` to start it. Then you could also visit http://localhost:19001 to access supervisor web console.
