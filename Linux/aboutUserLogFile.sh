#!/bin/bash
echo "выводит число секунд прошедших с начала эпохи unix:"
date '+%s'
echo "выводит локальное время:"
date '+%F %T'
echo "список зарегистрировавшихся обычных пользователей, которые создаются с UID от UID_MIN до UID_MAX которые определены в файле /etc/login.defs:"
awk '/^UID/{print $1"="$2}' /etc/login.defs
echo "из файла /etc/passwd выбрать только тех пользователей у которых UID (третий столбик :) из этого диапазона:"
eval $(awk '/^UID/{print $1"="$2}' /etc/login.defs)
awk -v min=$UID_MIN -v max=$UID_MAX -F: '$3>=min && $3<=max {print $1}' /etc/passwd
echo "uptime системы:"
uptime -p