Task:
Building your own Apache image
# Devops
Decision:
$ mkdir Apache
$ cd Apache/
$ vim Dockerfile
$ cat Dockerfile
FROM ubuntu:20.04

MAINTAINER TestUser <test@gmail.com>

ENV TZ=Asia/Irkutsk

RUN apt-get -y update
RUN apt-get install -y apache2 && apt-get clean

COPY ./test.html /var/www/html

EXPOSE 80
CMD apache2ctl -D FOREGROUND
$ docker build -t dd/apache:v1 .
...
Configuring tzdata
------------------

Please select the geographi-c area in whi-ch you live. Subsequent configuration
questions will narrow this down by presenting a list of cities, representing
the time zones in whi-ch they are located.
  1. Afri-ca      4. Australia  7. Atlanti-c  10. Pacifi-c  13. Etc
  2. Ameri-ca     5. Arcti-c     8. Europe    11. SystemV
  3. Antarcti-ca  6. Asia       9. Indian    12. US
Geographi-c area:
$ vim Dockerfile
$ cat Dockerfile
FROM ubuntu:20.04

MAINTAINER TestUser <test@gmail.com>

ENV TZ=Asia/Irkutsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -y update
RUN apt-get install -y apache2 && apt-get clean

COPY ./test.html /var/www/html

EXPOSE 80
CMD apache2ctl -D FOREGROUND
$ docker build -t dd/apache:v1 .
...
Step 7/9 : COPY ./test.html /var/www/html
COPY failed: file not found in build context or excluded by .dockerignore: stat test.html: file does not exist
$ vim Dockerfile
$ cat Dockerfile
FROM ubuntu:20.04

MAINTAINER TestUser <test@gmail.com>

ENV TZ=Asia/Irkutsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -y update
RUN apt-get install -y apache2 && apt-get clean

#COPY ./test.html /var/www/html
RUN echo 'Hey! This apache v1.' > /var/www/html/index.html

EXPOSE 80
CMD apache2ctl -D FOREGROUND
$ docker build -t dt/apache:v1 .
...
Successfully built 4da2a350261a
Successfully tagged dt/apache:v1
$ docker images
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
dt/apache   v1        4da2a350261a   56 seconds ago   223MB
<none>              <none>    f4a9c029f523   7 minutes ago    72.8MB
ubuntu              20.04     20fffa419e3a   7 weeks ago      72.8MB
$ docker run -d -p 8080:80 dt/apache:v1
d45bbc7ec6996cdee5962fd52ca4be262696c9d1567e4c677cd409e77b39bcb4

Web - http://localhost:8080 - https://hub.docker.com - Registration - Add new Repository - webservers

$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED              STATUS              PORTS                                   NAMES
d45bbc7ec699   dt/apache:v1   "/bin/sh -c 'apache2…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp, :::8080->80/tcp   ecstati-c_tesla
$ docker stop d45bbc7ec699
d45bbc7ec699
$ docker login --username dt
$ docker ps -a
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS                            PORTS     NAMES
d45bbc7ec699   dt/apache:v1   "/bin/sh -c 'apache2…"   3 minutes ago   Exited (137) About a minute ago             ecstati-c_tesla
$ docker tag dt/apache:v1 dt/webapps:apache
$ docker push dt/webapps:apache
$ docker ps -a
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                        PORTS     NAMES
d45bbc7ec699   dt/apache:v1   "/bin/sh -c 'apache2…"   12 minutes ago   Exited (137) 10 minutes ago             ecstati-c_tesla
$ docker images -a
REPOSITORY           TAG       IMAGE ID       CREATED          SIZE
dt/webapps   apache    4da2a350261a   15 minutes ago   223MB
dt/apache    v1        4da2a350261a   15 minutes ago   223MB
<none>               <none>    18438e1744ee   15 minutes ago   223MB
<none>               <none>    904adff67a91   15 minutes ago   223MB
<none>               <none>    0a70b2fcdcd0   16 minutes ago   223MB
<none>               <none>    fdc143eff63f   19 minutes ago   110MB
<none>               <none>    78ba4bb3d58c   20 minutes ago   72.8MB
<none>               <none>    936a09b19415   20 minutes ago   72.8MB
<none>               <none>    3a96f3a7af82   20 minutes ago   72.8MB
<none>               <none>    f4a9c029f523   22 minutes ago   72.8MB
<none>               <none>    7a15a11bf5d6   22 minutes ago   72.8MB
ubuntu               20.04     20fffa419e3a   7 weeks ago      72.8MB
Task:
Set up a LAMP server in Docker
Here I am using Docker Compose to create a LAMP server for PHP web development.
# Devops.
Decision:
$ mkdir Lamp
$ cd Lamp/
$ mkdir html
$ docker-compose up -d
$ docker-compose down --remove-orphans
$ docker-compose up -d
$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS          PORTS                                   NAMES
71da65041f3c   phpmyadmin/phpmyadmin:5.0.2   "/docker-entrypoint.…"   19 seconds ago   Up 14 seconds   0.0.0.0:5000->80/tcp, :::5000->80/tcp   lamp_phpmyadmin_1
ec024f3a8241   mysql:8.0.19                  "docker-entrypoint.s…"   19 seconds ago   Up 14 seconds   3306/tcp, 33060/tcp                     lamp_thost_1
d7776265abb4   lamp_web-server               "docker-php-entrypoi…"   19 seconds ago   Up 15 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   lamp_web-server_1

Web - http://localhost:5000 - new - tdb - create - http://localhost:8080

$ docker-compose down
$ docker ps -a
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                        PORTS     NAMES
d45bbc7ec699   dt/apache:v1   "/bin/sh -c 'apache2…"   28 minutes ago   Exited (137) 26 minutes ago             ecstati-c_tesla
$ docker images -a
REPOSITORY              TAG            IMAGE ID       CREATED          SIZE
lamp_web-server         latest         428133d10311   8 minutes ago    414MB
dt/apache       v1             4da2a350261a   31 minutes ago   223MB
dt/webapps      apache         4da2a350261a   31 minutes ago   223MB
<none>                  <none>         18438e1744ee   31 minutes ago   223MB
<none>                  <none>         904adff67a91   31 minutes ago   223MB
<none>                  <none>         0a70b2fcdcd0   31 minutes ago   223MB
<none>                  <none>         fdc143eff63f   34 minutes ago   110MB
<none>                  <none>         78ba4bb3d58c   35 minutes ago   72.8MB
<none>                  <none>         936a09b19415   35 minutes ago   72.8MB
<none>                  <none>         3a96f3a7af82   35 minutes ago   72.8MB
<none>                  <none>         f4a9c029f523   37 minutes ago   72.8MB
<none>                  <none>         7a15a11bf5d6   37 minutes ago   72.8MB
ubuntu                  20.04          20fffa419e3a   7 weeks ago      72.8MB
phpmyadmin/phpmyadmin   5.0.2          125749bd47bf   22 months ago    469MB
mysql                   8.0.19         0c27e8e5fcfa   2 years ago      546MB
php                     7.4.3-apache   d753d5b380a1   2 years ago      414MB
Source:
# https://linuxhint.com/lamp_server_docker/
# https://www.youtube.com/playlist?list=PLTd7y0vdxhK643dY-Th-fQvyNP46eW7CU