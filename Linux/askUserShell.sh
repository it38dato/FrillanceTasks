 #!/bin/bash
# Сделайте скрипт, который будет спрашивать имя пользователя и выводить оболочку этого пользователя.
#!/bin/bash
read -p "Print urname: " user
cat /etc/passwd | grep "/home/$user:" >> testfile2
cut -d ':' -f 7 testfile2