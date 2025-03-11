#!/bin/bash
name1=$(whoami)
#echo $name1
cmd1=$(cat /etc/allowedurs | grep $name1)
#echo $cmd1
#for line1 in $(cat /etc/allowedurs)
#do
#    echo 'line1' $line1
  #if [[ $name1 == $line1 ]];
  #then
  #    echo '+'
  #else
  #    echo '-'
  #fi    
#done
if cat /etc/allowedurs | grep $name1
then
  echo '+'
else
  echo 'This incident will be reported'
  logger -p local2.err "ur $name1 tried to run this script!"
fi
ls /data
read -p "specify the file name: " rename
read -p "specify the modification date and time for the shift: " date