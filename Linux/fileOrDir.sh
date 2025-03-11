#!/bin/bash
#Определить файл или директория ваши данные.
dir=/home/ik/* # your data
for file in $dir
do
if [ -d "$file" ]
then
echo "$file - директория"
elif [ -f "$file" ]
then
echo "$file - файл"
else
echo "Неизвестный файл"
fi
done