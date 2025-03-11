Task:
Calling sleep() via time.sleep()
# Разработка Режим засыпания.
Decision:
tuser@kvmubuntu:~$ python3 -m venv Py-Env
tuser@kvmubuntu:~$ source Py-Env/bin/activate
tuser@kvmubuntu:~$ ls
Py-Env
tuser@kvmubuntu:~$ python3 Py-SLeep.py
tuser@kvmubuntu:~$ python3 -m timeit -n 3 "import time; time.sleep(3)"
3 loops, best of 5: 3 sec per loop
Task:
Системному администратору всегда нужно быть в курсе, если какой-то из сайтов упал. 
Вы бы хотели иметь возможность проверить код состояния сайта регулярно, но запрашивать веб сервер постоянно нельзя, ведь это сильно повлияет на производительность. В Python одним из простых способов совершить такую проверку является использование системного вызова sleep()
# Разработка Режим засыпания.
Decision:
tuser@kvmubuntu:~$ pip install requests
tuser@kvmubuntu:~$ python3 Py-SLeep1.py
HTTPError: 404 для http://www.google.com/py
tuser@kvmubuntu:~$ python3 Py-SLeep1.py
http://www.google.com поднят
Task:
Вызов sleep() с декораторами
# Разработка Режим засыпания.
Decision:
tuser@kvmubuntu:~$ python3 Py-SLeep2.py
HTTPError: 404 для http://www.google.com/py
Сон на 3 секунд
HTTPError: 404 для http://www.google.com/py
Сон на 3 секунд
HTTPError: 404 для http://www.google.com/py
Сон на 3 секунд
Task:
Использование time.sleep() в threading
# Разработка Режим засыпания.
Decision:
tuser@kvmubuntu:~$ python3 Py-SLeep3.py
     2 Thread-1 (worker) рабочий поток вносится
     3 Thread-2 (worker) рабочий поток вносится
     3 MainThread Добавление из главного потока
   754 MainThread Добавление из главного потока
  1004 Thread-1 (worker) рабочий поток вносится
  1004 Thread-2 (worker) рабочий поток вносится
  1505 MainThread Добавление из главного потока
  2005 Thread-1 (worker) рабочий поток вносится
  2006 Thread-2 (worker) рабочий поток вносится
  2256 MainThread Добавление из главного потока
  3007 Thread-1 (worker) рабочий поток вносится
  3007 MainThread Добавление из главного потока
  3007 Thread-2 (worker) рабочий поток вносится
  3759 MainThread Добавление из главного потока
  4009 Thread-1 (worker) рабочий поток вносится
  4009 Thread-2 (worker) рабочий поток вносится
  4510 MainThread Добавление из главного потока
  5010 Thread-1 (worker) рабочий поток вносится
  5010 Thread-2 (worker) рабочий поток вносится
  5261 MainThread Добавление из главного потока
^C  5880 MainThread Остановка
Task:
Вызов sleep() с Async IO
# Разработка Режим засыпания.
Decision:
tuser@kvmubuntu:~$ python3 Py-SLeep4.py
Hello ...
... World!
tuser@kvmubuntu:~$ python3 Py-SLeep5.py
Started: 11:41:57
First
Second
Third
Ended: 11:42:03
tuser@kvmubuntu:~$ python3 Py-SLeep6.py
Started: 11:43:16
First counter: 1 seconds
Second counter: 2 seconds
Third counter: 3 seconds
Second counter: 1 seconds
Third counter: 2 seconds
Third counter: 1 seconds
Ended: 11:43:19
Task:
Для должного погружения tkinter в сон потребуется использовать after()
# Разработка Режим засыпания.
Decision:
tuser@kvmubuntu:~$ python3 Py-SLeep8.py
Я задержался