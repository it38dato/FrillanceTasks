#!/bin/bash
# read-validate: проверка ввода.
invalid_input () {
  echo "Invalid input '$REPLY'" >&2
  exit 1
}
read -p "Enter a single item > "
# пустой ввод (недопустимо)
[[ -z $REPLY ]] && invalid_input
# ввод множества элементов (недопустимо)
(( $(echo $REPLY | wc -w) > 1 )) && invalid_input
# введено допустимое имя файла?
if [[ $REPLY =~ ^[-[:alnum:]\._]+$ ]]; then
  echo "'$REPLY' is a valid filename."
  if [[ -e $REPLY ]]; then
  echo "And file '$REPLY' exists."
  else
  echo "However, file '$REPLY' does not exist."
  fi
  # введено вещественное число?
  if [[ $REPLY =~ ^-?[[:digit:]]*\.[[:digit:]]+$ ]]; then
  echo "'$REPLY' is a floating point number."
  else
  echo "'$REPLY' is not a floating point number."
  fi
  # введено целое число?
  if [[ $REPLY =~ ^-?[[:digit:]]+$ ]]; then
  echo "'$REPLY' is an integer."
  else
  echo "'$REPLY' is not an integer."
  fi
else
  echo "The string '$REPLY' is not a valid filename."
fi