Task:
От вас потребуется создать Dockerfile для образа, который будет удовлетворять следующим свойствам:
1. Базовый образ – ubuntu:16.04
2. Установлен текстовый редактор nano
3. Переменная окружения $EDITOR устанавливает nano в качестве редактора по умолчанию
4. В качестве рабочей директории установлен каталог /home/stepik
5. При запуске контейнера открывается nano, файл автоматически сохраняется в файловую систему хоста, даже если при запуске опции монтирования не указаны (при отсутствии опции монтирования путь, по кторому сохраняется файл, не играет роли, важно, чтобы файл в конечном счете оказался на хосте)
6. Владельцем файла на хосте назначается пользователь с uid=1000, если при сборке не указываются дополнительные аргументы, или пользователь с uid, который был задан аргументом UID при сборке
7. Именно этот пользователь (uid=1000/uid=UID) должен быть основным в контейнере.
id -u $(whoami)
> 1000
docker build -t dockerfile-extended .
docker run -it --r-t -v $(pwd):/home/stepik dockerfile-extended
# Nano is opened, we write some text, closing editor and specifying a filename as 'test'
ls -l test
> -rw-r--r-- 1 <username> <group> 7 марта 11 17:20 test
# Where <username> is the name of the user with uid=1000
Пример для пользователя с произвольным UID
docker build -t dockerfile-extended --build-arg UID=1001 .
# Doing the same...
> -rw-r--r-- 1 <username> <group> 7 марта 11 17:20 test
# Where <username> is the name of the user with uid=1001
Для получения кода проверки в папке с Dockerfile, содержащим ответ, выполните:
docker run --r-t -v $(pwd)/Dockerfile:/mnt/Dockerfile -v /var/run/docker.sock:/var/run/docker.sock parseq/stepik-dockerfile-extended
Decision:
$ ls /home/
    server
$ ls
    Desktop  Dockerfile  Documents  Downloads  Musi-c  Pi-ctures  Publi-c  Templates  Videos
$ ls /
    bin  boot  cdrom  dev  etc  home  lib  lib32  lib64  libx32  lost+found  media  mnt  opt  proc  root  run  sbin  snap  srv  swapfile  sys  tmp  usr  var
$ whi-ch nano
    /usr/bin/nano
$ docker build -t dockerfile-extended .
    ...
    Successfully built b3ecd51aabd9
    Successfully tagged dockerfile-extended:latest
$ docker images
    REPOSITORY                            TAG       IMAGE ID       CREATED          SIZE
    dockerfile-extended                   latest    b3ecd51aabd9   20 minutes ago   167MB
    stepik_task_test_image                latest    d5a320ef460f   2 hours ago      72.9MB
    test                                  latest    d5a320ef460f   2 hours ago      72.9MB
    testtwo                               latest    e3e656e8d305   3 hours ago      72.9MB
    testone                               latest    881aeba8a550   3 hours ago      72.9MB
    ubuntu                                16.04     aefd7f02ae24   4 days ago       134MB
    ubuntu                                20.04     26b77e58432b   3 weeks ago      72.9MB
    hello-world                           latest    d1165f221234   7 weeks ago      13.3kB
    parseq/stepik-exec-docker             latest    c7fe4f732991   3 years ago      341MB
    parseq/stepik-it-docker               latest    c0788ef75831   4 years ago      188MB
    parseq/stepik-linking-docker-client   latest    27916de983f8   4 years ago      673MB
    parseq/stepik-dockerfile-basi-cs       latest    77120b298b47   4 years ago      767MB
    parseq/stepik-ports-docker            latest    3b541ae9e177   4 years ago      170MB
    parseq/stepik-linking-docker          latest    ccfae27b98db   4 years ago      672MB
    parseq/hello-docker                   latest    d4e056261370   4 years ago      697MB
$ docker run -it --r-t -v(pwd):/home/stepik dockerfile-extended
$ ls -l test
    -rw-r--r-- 1 server server 11 Apr 28 15:19 test
$ docker build -t dockerfile-extended --build-arg UID=1001 .
    ...
    Successfully built eb9a47cd0883
    Successfully tagged dockerfile-extended:latest
$ docker images
    REPOSITORY                            TAG       IMAGE ID       CREATED          SIZE
    dockerfile-extended                   latest    eb9a47cd0883   9 seconds ago    167MB
    <none>                                <none>    b3ecd51aabd9   28 minutes ago   167MB
    stepik_task_test_image                latest    d5a320ef460f   2 hours ago      72.9MB
    test                                  latest    d5a320ef460f   2 hours ago      72.9MB
    testtwo                               latest    e3e656e8d305   3 hours ago      72.9MB
    testone                               latest    881aeba8a550   3 hours ago      72.9MB
    ubuntu                                16.04     aefd7f02ae24   4 days ago       134MB
    ubuntu                                20.04     26b77e58432b   3 weeks ago      72.9MB
    hello-world                           latest    d1165f221234   7 weeks ago      13.3kB
    parseq/stepik-exec-docker             latest    c7fe4f732991   3 years ago      341MB
    parseq/stepik-it-docker               latest    c0788ef75831   4 years ago      188MB
    parseq/stepik-linking-docker-client   latest    27916de983f8   4 years ago      673MB
    parseq/stepik-dockerfile-basi-cs       latest    77120b298b47   4 years ago      767MB
    parseq/stepik-ports-docker            latest    3b541ae9e177   4 years ago      170MB
    parseq/stepik-linking-docker          latest    ccfae27b98db   4 years ago      672MB
    parseq/hello-docker                   latest    d4e056261370   4 years ago      697MB
$ docker run -it --r-t -v(pwd):/home/stepik dockerfile-extended
$ ls -l test
    -rw-r--r-- 1 server server 11 Apr 28 15:19 test
~dockerrun−−r-t−v docker run --r-t -v dockerrun−−r-t−v(pwd)/Dockerfile:/mnt/Dockerfile -v /var/run/docker.sock:/var/run/docker.sock parseq/stepik-dockerfile-extended
    ...
    Digest: sha256:80868d51eab821b82a9e916e6ffd3f370a1f63d1005c6053c60bfaa2ebc19017
    Status: Downloaded newer image for parseq/stepik-dockerfile-extended:latest