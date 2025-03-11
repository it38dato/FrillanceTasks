Task:
# Разработка Обработка логов.
Decision:
tuser@kvmubuntu:~$ mkdir Py-Logging
tuser@kvmubuntu:~$ cd Py-Logging
tuser@kvmubuntu:~$ python3 -m venv Py-Env
tuser@kvmubuntu:~$ source Py-Env/bin/activate
tuser@kvmubuntu:~$ python Py-Logging.py
tuser@kvmubuntu:~$ ls
mylog.log  Py-Env  Py-Logging.py
tuser@kvmubuntu:~$ cat mylog.log
12:35:11 - Py-Logging - INFO - <module>: 8 - Hello
tuser@kvmubuntu:~$ deactivate