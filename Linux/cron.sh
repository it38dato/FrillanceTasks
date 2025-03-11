#!/bin/bash
# у пользователя root создайте cron, чтобы он каждую пятницу в 23:30 записывал содержимое директории /data и содержимое архива /backup/archive.tar в файл /var/log/reports/текущаядата.
mkdir /var/log/reports
ls -l /data > /var/log/reports/$(date +"%d.%m.%Y")
tar -tf /backup/archive.tar >> /var/log/reports/$(date +"%d.%m.%Y")