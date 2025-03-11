#!/bin/bash
  ##############
  #RESULT=$(echo 'hello')
  #echo $RESULT
  ##############
  #echo -n "Enter a number: "
  #read VAR
  #if [[ $VAR -gt 10 ]]
  #then
  # echo "The variable is greater than 10."
  #fi
  ##############
string='Моя длинная строка'
if [[ $string == *"Моя длинная"* ]]; then
echo "Подстрока найдена!"
fi