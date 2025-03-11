#/bin/bash
#Создайте файл со списком пользователей. С помощью for выведите на экран текст: «Creating new ur: uradd имя_пользователя».
cut -d':' -f1 /etc/passwd >> testfile4
for line in $(cat testfile4)
do echo "Creating new ur: uradd $line"
done