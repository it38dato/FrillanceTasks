Task:
Создадим новый проект. Для этого создаем файл docker-compose.yml. В ссылке https://hub.docker.com/_/mariadb есть инструкция для compose - копируем и вставлем по этой инструкции. после в директории, где расположен этот файл запустим ее. Потом надо будет в браузере локальной машины запустить 127.0.0.1:6080
# Devops
Decision:
$ ls
  docker-compose.yml  Dockerfile
$ docker -v
  Docker version 20.10.6, build 370c289
$ docker-compose -v
  docker-compose version 1.29.1, build c34c88b2
$ docker-compose up
  Starting docker_db_1        ... done
  Recreating docker_adminer_1 ... done
  Attaching to docker_db_1, docker_adminer_1
$ docker-compose up -d
  Starting docker_db_1      ... done
  Starting docker_adminer_1 ... done
  $ docker-compose ps
        Name                Command          State           Ports        
  ------------------------------------------------------------------------
  docker_adminer_1   entrypoint.sh docker-   Up      0.0.0.0:6080->8080/tc
                     php-e ...                       p,:::6080->8080/tcp  
  docker_db_1        docker-entrypoint.sh    Up      3306/tcp             
                     mysqld

В винде тот же самый файл и те же команды запуска. Единственное, чтоб узнать ip адрес машины, для запуска в браузере напишем команду - docker-machine ip default. и в браузере уже по этому адресу запускаем проект