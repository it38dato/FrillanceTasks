#/bin/bash
read -p "Print username: " user
#idd=$(id -u $user)
id1=$(cat /etc/passwd | grep $user | cut -d ':' -f 4)
home1=$(cat /etc/passwd | grep $user | cut -d ':' -f 6)
group1=$(cat /etc/group | grep $user | cut -d ':' -f 1)
echo "uid = $id1"
echo "home = $home1"
echo "group = $group1"
read -p "What should be changed? (uid/home/group): " change
#echo "$change"
if [ $change == "uid" ]
then
  read -p "Write youser own version: " id2
  if cut -d':' -f3 /etc/passwd | grep -w $id2
  then
  echo "there is such a user"
  else
  #echo "there is no such user"
  read -p "Re-Enter. Write youser own version: " id2
  if cut -d':' -f3 /etc/passwd | grep -w $id2
      then
              echo "there is such a user"
  fi
  fi
elif [ $change == "home" ]
then
  read -p "Write youser own version: " home2
  if cut -d':' -f6 /etc/passwd | grep -w $home2
  then
  echo "Such a directory already exists"
  else
  echo "This is a unique home directory"
  fi
elif [ $change == "group" ]
then
  read -p "Write youser own version: " group2
  if cut -d':' -f1 /etc/group | grep -w $group2
  then
  echo "+"
  else
  echo "-"
  fi
else
  echo "command not found"
fi