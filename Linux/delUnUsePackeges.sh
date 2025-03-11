#!/bin/bash
#Нужно полностью удалить неиспользуемые версии пакетов
set -eu
LANG=en_US.UTF-8 snap list --all | awk '/disabled/{print $1, $3}' |
while read snapname revision; do
    snap remove "$snapname" --revision="$revision"