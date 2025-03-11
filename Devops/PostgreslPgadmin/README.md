Task:
Docker-compose.yml For PgAdmin And PostgreSQL
Here I am using Docker Compose to create a PostgreSQL container and access it using pgAdmin 4, the PostgreSQL admin web interface. You also need to access the PostgreSQL database server running in a Docker container from the Datagrid IDE.
# Devops
Decision:
$ mkdir PostgreslPgadmin
$ cd PostgreslPgadmin/
$ docker-compose up -d
$ sudo netstat -tlpn
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:5442            0.0.0.0:*               LISTEN      732/docker-proxy
tcp        0      0 0.0.0.0:8889            0.0.0.0:*               LISTEN      752/docker-proxy
tcp6       0      0 :::5442                 :::*                    LISTEN      739/docker-proxy
tcp6       0      0 :::8889                 :::*                    LISTEN      759/docker-proxy
$ docker images
REPOSITORY              TAG            IMAGE ID       CREATED         SIZE
lamp_web-server         latest         dc8b9808febc   12 hours ago    414MB
php                     latest         dc8b9808febc   12 hours ago    414MB
dd/nginxphpfpm       v2             c67942c7509d   18 hours ago    317MB
dd/apachephpfpm      v2             29ef4135471f   19 hours ago    297MB
<none>                  <none>         89d11a0d9919   19 hours ago    297MB
<none>                  <none>         bfa2b51fd878   20 hours ago    297MB
<none>                  <none>         9358fff8e06c   20 hours ago    297MB
<none>                  <none>         090debabce8f   20 hours ago    297MB
dpage/pgadmin4          latest         d13c9d7d0193   4 days ago      382MB
postgres                12             ffc079081fed   2 weeks ago     373MB
ubuntu                  20.04          20fffa419e3a   7 weeks ago     72.8MB
phpmyadmin/phpmyadmin   5.0.2          125749bd47bf   22 months ago   469MB
mysql                   8.0.19         0c27e8e5fcfa   2 years ago     546MB
php                     7.4.3-apache   d753d5b380a1   2 years ago     414MB
$ docker container ls
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                                            NAMES
08df4a338c5c   dpage/pgadmin4   "/entrypoint.sh"         3 minutes ago   Up 3 minutes   443/tcp, 0.0.0.0:8889->80/tcp, :::8889->80/tcp   postgreslpgadmin_demo-pgadmin4_1
4509fb2998d9   postgres:12      "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes   0.0.0.0:5442->5432/tcp, :::5442->5432/tcp        postgreslpgadmin_demo-container-db_1
$ docker inspect 08df4a338c5c
...
                    "NetworkID": "c10c99985b170aff19e1a1cd821eaf9d5b5388befeaa3dd41201ab7ef208a531",
                    "EndpointID": "5ab5778a6b85124aff3c9a0c5f1a470bca6cede16b7ea8c1665f0f96a45a8c85",
                    "Gateway": "172.18.0.1",
                    "IPAddress": "172.18.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:12:00:03",
                    "DriverOpts": null
                }
            }
        }
    }
]
- Web browser - http://localhost:8889 - Mail logins - Servers - register - server - name - TestServer - port - 5432 - username - TestUser - password - TestP@ssword - save password - hostname - 172.18.0.3 - save
$ docker-compose down
$ docker ps -a
CONTAINER ID   IMAGE                    COMMAND                  CREATED             STATUS                           PORTS     NAMES
d45bbc7ec699   dt/apache:v1     "/bin/sh -c 'apache2…"   About an hour ago   Exited (137) About an hour ago             ecstati-c_tesla
$ docker images -a
REPOSITORY              TAG            IMAGE ID       CREATED             SIZE
lamp_web-server         latest         428133d10311   55 minutes ago      414MB
dt/apache       v1             4da2a350261a   About an hour ago   223MB
dt/webapps      apache         4da2a350261a   About an hour ago   223MB
<none>                  <none>         18438e1744ee   About an hour ago   223MB
<none>                  <none>         904adff67a91   About an hour ago   223MB
<none>                  <none>         0a70b2fcdcd0   About an hour ago   223MB
<none>                  <none>         fdc143eff63f   About an hour ago   110MB
<none>                  <none>         78ba4bb3d58c   About an hour ago   72.8MB
<none>                  <none>         936a09b19415   About an hour ago   72.8MB
<none>                  <none>         3a96f3a7af82   About an hour ago   72.8MB
<none>                  <none>         f4a9c029f523   About an hour ago   72.8MB
<none>                  <none>         7a15a11bf5d6   About an hour ago   72.8MB
dpage/pgadmin4          latest         d13c9d7d0193   4 days ago          382MB
postgres                12             ffc079081fed   2 weeks ago         373MB
ubuntu                  20.04          20fffa419e3a   7 weeks ago         72.8MB
phpmyadmin/phpmyadmin   5.0.2          125749bd47bf   22 months ago       469MB
mysql                   8.0.19         0c27e8e5fcfa   2 years ago         546MB
php                     7.4.3-apache   d753d5b380a1   2 years ago         414MB
$ cd ..
Source:
# https://linuxhint.com/postgresql_docker/
# https://www.youtube.com/playlist?list=PL7-fzhJ95xrPJUSzziEsymILf0bKusiLZ
# PavelZloiAkaEvilFreelancer