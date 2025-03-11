#!/bin/bash
echo -e "Дата и Время:;$(date '+%F %T')\nПользователи:;$(eval $(awk '/^UID/{print $1"="$2}' /etc/login.defs) && awk -v min=$UID_MIN -v max=$UID_MAX -F: '$3>=min && $3<=max {print $1}' /etc/passwd)\nВремя работы (начало):;$(uptime -s)\nВремя работы (прошло):;$(uptime -p)" | column -t -s ";" | systemd-cat --identifier="задача3"
