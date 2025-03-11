#!/bin/bash
# case-menu: программа вывода системной информации, управляемая с помощью меню.
clear
echo "
Please Select:
1. Display System Information
2. Display Disk Space
3. Display Home Space Utilization
0. Quit
"
read -p "Enter selection [0-3] > "
case $REPLY in
  q|Q)    echo "Program terminated."
      exit
      ;;
  a|A)    echo "Hostname: $HOSTNAME"
      uptime
      ;;
  b|B)    df -h
      ;;
  c|C)    if [[ $(id -u) -eq 0 ]]; then
          echo "Home Space Utilization (All Users)"
          du -sh /home/*
      else
          echo "Home Space Utilization ($USER)"
          du -sh $HOME
      fi
      ;;
  *)      echo "Invalid entry." >&2
      exit 1
      ;;
esac