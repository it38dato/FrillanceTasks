#!/bin/bash
#Сделайте скрипт, который спросит имя пользователя и скажет, является ли пользователь администратором?
  read -p "Print urname: " user1
  user2=$(cat /etc/group | grep wheel | cut -d ':' -f 4)
  if [ "$user1" = "$user2" ]
  then
    echo "He is Admin"
  else
    echo "He is not Admin"
  fi