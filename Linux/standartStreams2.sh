#!/bin/bash
# Напишите скрипт на bash, который принимает на вход один аргумент (целое число от 0 до бесконечности), который будет обозначать число студентов в аудитории. В зависимости от значения числа нужно вывести разные сообщения.
# Соответствие входа и выхода должно быть таким:
#  0 -->  No students
#  1 -->  1 student
#  2 -->  2 students
#  3 -->  3 students
#  4 -->  4 students
#  5 и больше --> A lot of students
number=student
case $1 in
0) result="No ${number}s";;
1) result="$1 ${number}";;
[2-4]) result="$1 ${number}s";;
*) result="A lot of ${number}s";;
esac
echo "$result"