Task:
Уменьшить размер образа - файловая система UnionFS и слои. Посмотрим список образов, которые у нас есть локально и команду историю образа. Создадим образ и проверим его историю. Тут каждая команда в отдельном слое
# Devops.
Decision:
$ docker images
  REPOSITORY        TAG       IMAGE ID       CREATED       SIZE
  dato138it/myapp   latest    52bf88faf371   2 days ago    147MB
  dato138it/myapp   <none>    c26a6cad11ba   2 days ago    147MB
  bitnami/apache    latest    6edfa339f61e   3 days ago    176MB
  adminer           latest    7707fd9b142f   4 days ago    89.8MB
  docker_adminer    latest    7707fd9b142f   4 days ago    89.8MB
  docker_db         latest    992bce5ed710   12 days ago   401MB
  mariadb           latest    992bce5ed710   12 days ago   401MB
  ubuntu            latest    7e0aa2d69a15   12 days ago   72.7MB
$ docker history adminer
  IMAGE          CREATED       CREATED BY                                      SIZE      COMMENT
  7707fd9b142f   4 days ago    /bin/sh -c #(nop)  EXPOSE 8080                  0B        
  <missing>      4 days ago    /bin/sh -c #(nop)  CMD ["php" "-S" "[::]:808…   0B        
  <missing>      4 days ago    /bin/sh -c #(nop)  USER adminer                 0B        
  <missing>      4 days ago    /bin/sh -c #(nop)  ENTRYPOINT ["entrypoint.s…   0B        
  <missing>      4 days ago    /bin/sh -c #(nop) COPY file:5ff0be587f5dd916…   482B      
  <missing>      4 days ago    /bin/sh -c set -x && curl -fsSL https://gith…   1.15MB    
  <missing>      4 days ago    /bin/sh -c #(nop)  ENV ADMINER_SRC_DOWNLOAD_…   0B        
  <missing>      4 days ago    /bin/sh -c #(nop)  ENV ADMINER_DOWNLOAD_SHA2…   0B        
  <missing>      4 days ago    /bin/sh -c #(nop)  ENV ADMINER_VERSION=4.8.0    0B        
  <missing>      4 days ago    /bin/sh -c #(nop) COPY multi:3020a2cf8da93de…   3.12kB    
  <missing>      4 days ago    /bin/sh -c set -x && apk add --no-cache --vi…   6.35MB    
  <missing>      4 days ago    /bin/sh -c #(nop) WORKDIR /var/www/html         0B        
  <missing>      4 days ago    /bin/sh -c addgroup -S adminer && adduser -S…   5.05kB    
  <missing>      4 days ago    /bin/sh -c #(nop)  STOPSIGNAL SIGINT            0B        
  <missing>      4 days ago    /bin/sh -c echo "upload_max_filesize = 128M"…   113B      
  <missing>      4 days ago    /bin/sh -c #(nop)  CMD ["php" "-a"]             0B        
  <missing>      4 days ago    /bin/sh -c #(nop)  ENTRYPOINT ["docker-php-e…   0B        
  <missing>      4 days ago    /bin/sh -c docker-php-ext-enable sodium         48.2kB    
  <missing>      4 days ago    /bin/sh -c #(nop) COPY multi:efd917b98407edb…   6.74kB    
  <missing>      4 days ago    /bin/sh -c set -eux;  apk add --no-cache --v…   62.7MB    
  <missing>      4 days ago    /bin/sh -c #(nop) COPY file:ce57c04b70896f77…   587B      
  <missing>      4 days ago    /bin/sh -c set -eux;   apk add --no-cache --…   10.4MB    
  <missing>      4 days ago    /bin/sh -c #(nop)  ENV PHP_SHA256=ab97f22b12…   0B        
  <missing>      4 days ago    /bin/sh -c #(nop)  ENV PHP_URL=https://www.p…   0B        
  <missing>      4 days ago    /bin/sh -c #(nop)  ENV PHP_VERSION=7.4.18       0B        
  <missing>      3 weeks ago   /bin/sh -c #(nop)  ENV GPG_KEYS=42670A7FE4D0…   0B        
  <missing>      3 weeks ago   /bin/sh -c #(nop)  ENV PHP_LDFLAGS=-Wl,-O1 -…   0B        
  <missing>      3 weeks ago   /bin/sh -c #(nop)  ENV PHP_CPPFLAGS=-fstack-…   0B        
  <missing>      3 weeks ago   /bin/sh -c #(nop)  ENV PHP_CFLAGS=-fstack-pr…   0B        
  <missing>      3 weeks ago   /bin/sh -c set -eux;  mkdir -p "$PHP_INI_DIR…   0B        
  <missing>      3 weeks ago   /bin/sh -c #(nop)  ENV PHP_INI_DIR=/usr/loca…   0B        
  <missing>      3 weeks ago   /bin/sh -c set -eux;  addgroup -g 82 -S www-…   4.68kB    
  <missing>      3 weeks ago   /bin/sh -c apk add --no-cache   ca-certifi-ca…   3.54MB    
  <missing>      3 weeks ago   /bin/sh -c #(nop)  ENV PHPIZE_DEPS=autoconf …   0B        
  <missing>      3 weeks ago   /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B        
  <missing>      3 weeks ago   /bin/sh -c #(nop) ADD file:8ec69d882e7f29f06…   5.61MB    
$ vim Dockerfile
$ docker build -t dkatest .
  ...
  Successfully built 52bf88faf371
  Successfully tagged dkatest:latest
$ docker images
  REPOSITORY        TAG       IMAGE ID       CREATED       SIZE
  dato138it/myapp   latest    52bf88faf371   2 days ago    147MB
  dkatest           latest    52bf88faf371   2 days ago    147MB
  dato138it/myapp   <none>    c26a6cad11ba   2 days ago    147MB
  bitnami/apache    latest    6edfa339f61e   3 days ago    176MB
  adminer           latest    7707fd9b142f   4 days ago    89.8MB
  docker_adminer    latest    7707fd9b142f   4 days ago    89.8MB
  mariadb           latest    992bce5ed710   12 days ago   401MB
  docker_db         latest    992bce5ed710   12 days ago   401MB
  ubuntu            latest    7e0aa2d69a15   12 days ago   72.7MB
$ docker history dkatest
  IMAGE          CREATED       CREATED BY                                      SIZE      COMMENT
  52bf88faf371   2 days ago    /bin/sh -c #(nop)  ENTRYPOINT ["cowsay"]        0B        
  c43d3a9413c9   2 days ago    /bin/sh -c apt-get update && apt-get install…   73.9MB    
  7e0aa2d69a15   12 days ago   /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B        
  <missing>      12 days ago   /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B        
  <missing>      12 days ago   /bin/sh -c [ -z "$(apt-get indextargets)" ]     0B        
  <missing>      12 days ago   /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   811B      
  <missing>      12 days ago   /bin/sh -c #(nop) ADD file:5c44a80f547b7d68b…   72.7MB
Task:
Давайте изменим Dockerfile, чтобы каждая команда начиналась на новых уровнях и в конце добавим удаление всех файлов, которая насоздавала команда. Переформируем навый образ и посмотрим на размер. Вернем в этом файле команды и добавим удаление. Также создаем образ и просмотрим размер.
Decision:
$ vim "Dockerfile copy"
$ docker build -t dkamanyrun .
  ...
  Successfully built 944e60e98ca0
  Successfully tagged dkamanyrun:latest
$ docker images
  REPOSITORY        TAG       IMAGE ID       CREATED         SIZE
  dkamanyrun        latest    944e60e98ca0   9 seconds ago   147MB
  dato138it/myapp   latest    52bf88faf371   2 days ago      147MB
  dkatest           latest    52bf88faf371   2 days ago      147MB
  dato138it/myapp   <none>    c26a6cad11ba   2 days ago      147MB
  bitnami/apache    latest    6edfa339f61e   3 days ago      176MB
  adminer           latest    7707fd9b142f   4 days ago      89.8MB
  docker_adminer    latest    7707fd9b142f   4 days ago      89.8MB
  mariadb           latest    992bce5ed710   12 days ago     401MB
  docker_db         latest    992bce5ed710   12 days ago     401MB
  ubuntu            latest    7e0aa2d69a15   12 days ago     72.7MB
$ vim Dockerfile
$ docker build -t dkaonerun .
  ...
  Successfully built af8ceb4756cc
  Successfully tagged dkaonerun:latest
$ docker images
  REPOSITORY        TAG       IMAGE ID       CREATED          SIZE
  dkaonerun         latest    af8ceb4756cc   14 seconds ago   119MB
  dkamanyrun        latest    944e60e98ca0   4 minutes ago    147MB
  dato138it/myapp   latest    52bf88faf371   2 days ago       147MB
  dkatest           latest    52bf88faf371   2 days ago       147MB
  dato138it/myapp   <none>    c26a6cad11ba   2 days ago       147MB
  bitnami/apache    latest    6edfa339f61e   3 days ago       176MB
  adminer           latest    7707fd9b142f   4 days ago       89.8MB
  docker_adminer    latest    7707fd9b142f   4 days ago       89.8MB
  mariadb           latest    992bce5ed710   12 days ago      401MB
  docker_db         latest    992bce5ed710   12 days ago      401MB
  ubuntu            latest    7e0aa2d69a15   12 days ago      72.7MB