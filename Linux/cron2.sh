#!/bin/bash
#Создайте пользователя backup и настройте для него cron, чтобы тот раз в день находил файлы старее 5 дней в директории /data и добавлял эти файлы в архив /backup/archive.tar, после чего удалял из исходной директории.
if find /data/ -type f -mtime +5; then
    cd /data
    tar -cvf /backup/archive.tar testfile*
    rm -rf /data/testfile*
else
    echo "No files"
fi