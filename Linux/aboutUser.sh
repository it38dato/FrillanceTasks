#/bin/bash
aboutuser() {
  read -p "About user: " line
  cat /etc/passwd | grep -w $line
}
adduser(){
  read -p "Add user: " name
  #cut -d':' -f1 /etc/passwd | grep -w $name
}
deleteuser(){
  read -p "Delete user: " name
  #cut -d':' -f1 /etc/passwd | grep -w $name
}
user() {
  select option in "About user" "Add user" "Delete user" "Exit"
  do
  case $option in
      "About user") aboutuser ;;
      "Add user") adduser ;;
      "Delete user") deleteuser ;;
      "Exit") break ;;
      *) echo Wrong option ;;
  esac
  done
}
user