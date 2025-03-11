Task:
Связь Dockerfile и docker-compose. Используем docker-compose и Dockerfile для запуска контейнеров. Создадим папку, которая будет относиться к образу базы данных и в нем создаем Dockerfile. В нем указываем какой образ нужно использовать (mariadb), в docker-compose добавляем ключ build и image можно убрать. Создаем новую директорию с сервисом adminer. Тут все по аналогии нужно делать, как в базе данных делали. И в терминале пробуем запустить. Потом перестроим наш проект, после запускаем и смотрим в браузере 127.0.0.1:6080.
# Devops
Decision:
$ mkdir db
$ touch db/Dockerfile
$ ls db/
  Dockerfile
$ mkdir adminer
$ ls
  adminer  db  docker-compose.yml  Dockerfile
$ r-t -rf Dockerfile
$ ls
  adminer  db  docker-compose.yml
$ docker-compose build
  Building db
  Sending build context to Docker daemon  2.048kB
  Step 1/1 : FROM mariadb
   ---> 992bce5ed710
  Successfully built 992bce5ed710
  Successfully tagged docker_db:latest
  Building adminer
  Sending build context to Docker daemon  2.048kB
  Step 1/1 : FROM adminer
   ---> 7707fd9b142f
  Successfully built 7707fd9b142f
  Successfully tagged docker_adminer:latest
$ docker-compose up
  Recreating docker_db_1      ... done
  Recreating docker_adminer_1 ... done
  Attaching to docker_adminer_1, docker_db_1
Task:
Теперь в Dockerfile мы можем вносить изменения. Добавим новый ключ volum (хранилище данных). Здесь же, в hub.docker.com, ищем раздел where to store Data и копируем директорию. Создаем директорию в проекте, где будет располагаться база данных. Теперь удаляем предыдущий контейнер с базой данных, пересобираем, запускаем и откроем директорию с базой данных. Тут мы увидим, что теперь база данных находится не в контейнере, а у нас локально. Теперь если удалить этот контейнер, все данные, которые мы внесил останутся на месте.
Decision:

$ mkdir databases
$ ls
  adminer  databases  db  docker-compose.yml
$ docker-compose r-t db
  Going to remove docker_db_1
  Are you sure? [yN] y
  Removing docker_db_1 ... done
$ docker-compose build
  Building db
  Sending build context to Docker daemon  2.048kB
  Step 1/1 : FROM mariadb
   ---> 992bce5ed710
  Successfully built 992bce5ed710
  Successfully tagged docker_db:latest
  Building adminer
  Sending build context to Docker daemon  2.048kB
  Step 1/1 : FROM adminer
   ---> 7707fd9b142f
  Successfully built 7707fd9b142f
  Successfully tagged docker_adminer:latest
$ docker-compose up
  Starting docker_adminer_1 ... done
  Creating docker_db_1      ... done
  Attaching to docker_adminer_1, docker_db_1
  $ ls databases/
  aria_log.00000001  ibdata1      multi-master.info
  aria_log_control   ib_logfile0  mysql
  ib_buffer_pool     ibtmp1       perfor-tance_schema

В браузере откроем adminer и создадим базу данных

$ ls databases/
  1st@002dtest@0020basa  ib_buffer_pool  multi-master.info
  2nd@002dtest@0020basa  ibdata1         mysql
  aria_log.00000001      ib_logfile0     perfor-tance_schema
  aria_log_control       ibtmp1
Task:
Соединение контейнеров между собой mariadb + php. Рассмотрим 1 из способов соединения между 2мя контейнерами. Мы будем использовать 2 готовых образа - mysql(mariadb) и образ, который содержит php библиотеку управления базой данных. Устанавливаем образ базы данных, для этого ищем образы hub.docker.com и hub.docker.com. ищем в инструкции установку и вместо name и password придумываем свое имя и пароль. После чего проверяем работает ли контейнер. link - установление соединения. Тут docker получает информацию о том, что нам нужно установить соединение между новым контейнером (adminer), который будет создан на базе образа adminer, и существующим контейнером mysqlserver. ссылку на mysqlserver должна быть обозначена - db. Для этого docker создает в файле новый контейнер adminer /etc/hosts, запись db, указывающий ip адрес mysqlserver. Это позволяет нам пользоваться имененм данного хоста. И в браузере локальной машины откроем php сервер с адресом 127.0.0.1:8080.
Decision:
$ docker run -p 127.0.0.1:3306:3306  --name mysqlserver -e MYSQL_ROOT_PASSWORD=123456 -d mariadb
  Digest: sha256:36288c675a192bd0a8a99cd6ba0780e31df85f0bfd0cbb204837cd108be3d236
  Status: Downloaded newer image for mariadb:latest
  113a0a7ca5a94ba2c25a50df62eea41ca15e309d65dbba71e456e35d85c5e631
$ docker ps
  CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                      NAMES
  113a0a7ca5a9   mariadb   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   127.0.0.1:3306->3306/tcp   mysqlserver
$ docker run --link mysqlserver:db -p 8080:8080 adminer
  ...
  Digest: sha256:a3e73e13e4f3f1bd1007d7a5d75a6bd23846c3252b71ab7a5817de9ffec04826
  Status: Downloaded newer image for adminer:latest
  [Thu May  6 01:28:31 2021] PHP 7.4.18 Development Server (http://[::]:8080) started
Task:
Вам необходимо обеспечить связь между двумя контейнерами так, чтобы он могли обращаться друг к другу с использованием DNS имен.
Для этого нужно запустить контейнер hub.docker.com сервер под именем stepik-linking-docker таким образом, чтобы контейнер был по имени доступен другим контейнерам, с которыми он тем или иным образом связан. Контейнер нужно запустить в виде демона.
После этого нужно запустить контейнер hub.docker.com так, чтобы он получил доступ к первому контейнеру, этот контейнер нужно запустить в интерактивном режиме.
В том случае, если все сделано правильно, контейнер отправит сообщение, которое нужно использовать в качестве ответа на задачу  
Decision:
$ docker network create test_net
    f8c6615588a4eff01d7fae56f969cfd479e74a55bc7be20498dedcc49f31ce7c
$ docker run -d --r-t --name stepik-linking-docker --network=test_net parseq/stepik-linking-docker
    ...
    Digest: sha256:0f96ab451a9743996a434fd373e721b2a3b97491b65194d658a17a732dde66f8
    Status: Downloaded newer image for parseq/stepik-linking-docker:latest
    b6d77ab24126bd93e4a560a465c9fa0a453b1313a031810d122cc8c020a96ceb
$ docker network inspect test_net
[
    {
        "Name": "test_net",
        "Id": "f8c6615588a4eff01d7fae56f969cfd479e74a55bc7be20498dedcc49f31ce7c",
        "Created": "2021-04-25T17:17:41.363958209-05:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "b6d77ab24126bd93e4a560a465c9fa0a453b1313a031810d122cc8c020a96ceb": {
                "Name": "stepik-linking-docker",
                "EndpointID": "a6d9dd22bed3a372f8ca92a85bb564e68af9de81ac8fdebd8657e8139634efdf",
                "MacAddress": "02:42:ac:12:00:02",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
$ docker run -it --r-t --network=test_net parseq/stepik-linking-docker-client
    ...
    Digest: sha256:9ab6f089a5416148271997c428eea30306bc296f7d8f2c9b52d721747eaef850
    Status: Downloaded newer image for parseq/stepik-linking-docker-client:latest
    Container linking is awesome simple!