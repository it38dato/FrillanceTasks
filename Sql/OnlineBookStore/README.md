Task:
База данных Книжный интернет-магазин.
В интернет-магазине продаются книги. Каждая книга имеет название, написана одним автором, относится к одному жанру, имеет определенную цену. В магазине доступно по нескольку экземпляров каждой книги.
Покупатель регистрируется на сайте интернет-магазина, указывает свои имя и фамилию, адрес электронной почты и город проживания. Он может сформировать один или несколько заказов, написать несколько пожеланий к каждому заказу. Каждый заказ включает в себя одну или несколько книг, каждую книгу можно заказать в нескольких экземплярах. Затем заказ проходит ряд последовательных этапов (операций): он оплачивается, упаковывается, передается курьеру или транспортной компании для транспортировки и, наконец, доставляется покупателю. Дата каждой операции фиксирована. Среднее время доставки книг известно для каждого города.
В то же время магазин ведет учет книг, их количество уменьшается при покупке, увеличивается при поступлении товара, когда количество исчерпано, размещен заказ и т.д. Разработать базу данных Книжный интернет-магазин
# Разработка баз данных.
Decision:
mysql> CREATE DATABASE OnlineBookStore;
Query OK, 1 row affected (0.32 sec)
mysql> show databases;
+--------------------+
| Database     |
+--------------------+
| OnlineBookStore  |
| information_schema |
| mysql       |
| performance_schema |
| sys        |
| testbdserver   |
+--------------------+
6 rows in set (0.01 sec)
mysql> USE OnlineBookStore;
Database changed
Task:
Установите связи между информационными объектами Жанр и Книга, Город и Клиент, Заказ и Этапы. Выберите верную концептуальную схему.
Наполнить таблицы информацией.
Структура и наполнение таблиц базы данных Интернет-магазин книг»
Таблица author (создание, заполнение):
author_id   name_author
1   Булгаков М.А.
2   Достоевский Ф.М.
3   Есенин С.А.
4   Пастернак Б.Л.
5   Лермонтов М.Ю.
Таблица genre (создание, заполнение, рассмотрено в качестве примеров):
genre_id   name_genre
1   Роман
2   Поэзия
3   Приключения
Таблица book (создание, заполнение):
book_id   title   author_id   genre_id   price   amount
1   Мастер и Маргарита   1   1   670.99   3
2   Белая гвардия   1   1   540.50   5
3   Идиот   2   1   460.00   10
4   Братья Карамазовы   2   1   799.01   2
5   Игрок   2   1   480.50   10
6   Стихотворения и поэмы   3   2   650.00   15
7   Черный человек   3   2   570.20   6
8   Лирика   4   2   518.99   2
Таблица city (в последнем столбце указано примерное количество дней, необходимое для доставки товара в каждый город):
city_id   name_city   days_delivery
INT PRIMARY KEY
AUTO_INCREMENT   VARCHAR(30)   INT
1   Москва   5
2   Санкт-Петербург   3
3   Владивосток   12
Таблица client:
client_id   name_client   city_id   email
INT PRIMARY KEY
AUTO_INCREMENT   VARCHAR(50)   INT   VARCHAR(30)
1   Баранов Павел   3   baranov@test
2   Абрамова Катя   1   abramova@test
3   Семенонов Иван   2   semenov@test
4   Яковлева Галина   1   yakovleva@test
Таблица buy (столбец buy_description предназначен для пожеланий покупателя, которые он хочет добавить в свой заказ, если пожеланий нет - поле остается пустым):
buy_id   buy_description   client_id
INT PRIMARY KEY
AUTO_INCREMENT   VARCHAR(100)   INT
1   Доставка только вечером   1
2     3
3   Упаковать каждую книгу по отдельности   2
4     1
Таблица buy_book:
buy_book_id   buy_id   book_id   amount
INT PRIMARY KEY
AUTO_INCREMENT   INT   INT   INT
1   1   1   1
2   1   7   2
3   1   3   1
4   2   8   2
5   3   3   2
6   3   2   1
7   3   1   1
8   4   5   1
Таблица step:
step_id   name_step
INT PRIMARY KEY
AUTO_INCREMENT   VARCHAR(30)
1   Оплата
2   Упаковка
3   Транспортировка
4   Доставка
Таблица buy_step ( если столбец date_step_end не заполнен (имеет значение Null), это означает что операция еще не выполнена, например для заказа с id 2, книги переданы для доставки 2020-03-02, но еще не доставлены):
buy_step_id   buy_id   step_id   date_step_beg   date_step_end
INT PRIMARY KEY
AUTO_INCREMENT   INT   INT   DATE   DATE
1   1   1   2020-02-20   2020-02-20
2   1   2   2020-02-20   2020-02-21
3   1   3   2020-02-22   2020-03-07
4   1   4   2020-03-08   2020-03-08
5   2   1   2020-02-28   2020-02-28
6   2   2   2020-02-29   2020-03-01
7   2   3   2020-03-02  
8   2   4    
9   3   1   2020-03-05   2020-03-05
10   3   2   2020-03-05   2020-03-06
11   3   3   2020-03-06   2020-03-10
12   3   4   2020-03-11  
13   4   1   2020-03-20  
14   4   2    
15   4   3    
16   4   4
# Разработка баз данных.
Decision:
mysql> CREATE TABLE author( author_id INT PRIMARY KEY AUTO_INCREMENT, name_author VARCHAR(30));
Query OK, 0 rows affected (0.14 sec)
mysql> INSERT INTO author (name_author) VALUES ('Булгаков М.А.'), ('Достоевский Ф.М.'), ('Есенин С.А.'), ('Пастернак Б.Л.'), ('Лермонтов М.Ю.');
Query OK, 5 rows affected (0.04 sec)
Records: 5 Duplicates: 0 Warnings: 0
mysql> SELECT * FROM author;
+-----------+-------------------------------+
| author_id | name_author         |
+-----------+-------------------------------+
|     1 | Булгаков М.А.         |
|     2 | Достоевский Ф.М.       |
|     3 | Есенин С.А.         |
|     4 | Пастернак Б.Л.        |
|     5 | Лермонтов М.Ю.        |
+-----------+-------------------------------+
5 rows in set (0.00 sec)
mysql> CREATE TABLE genre(genre_id INT PRIMARY KEY AUTO_INCREMENT, name_genre VARCHAR(30));
mysql> INSERT INTO genre(name_genre) VALUES ('Роман'), ('Поэзия'), ('Приключения');
Query OK, 3 rows affected (0.14 sec)
Records: 3 Duplicates: 0 Warnings: 0
mysql> SELECT * FROM genre;
+----------+------------------------+
| genre_id | name_genre       |
+----------+------------------------+
|    1 | Роман         |
|    2 | Поэзия         |
|    3 | Приключения      |
+----------+------------------------+
3 rows in set (0.00 sec)
mysql> CREATE TABLE book
(
book_id INT PRIMARY KEY AUTO_INCREMENT,
title VARCHAR(50),
author_id INT NOT NULL,
genre_id INT,
price DECIMAL(8, 2),
amount INT,
FOREIGN KEY (author_id)
  REFERENCES author (author_id)
  ON DELETE CASCADE,
FOREIGN KEY (genre_id)
  REFERENCES genre (genre_id)
  ON DELETE SET NULL
);
Query OK, 0 rows affected (0.24 sec)
mysql> INSERT INTO book (title, author_id, genre_id, price, amount)
VALUES
('Мастер и Маргарита', 1, 1, 670.99, 3),
('Белая гвардия ', 1, 1, 540.50, 5),
('Идиот', 2, 1, 460.00, 10),
('Братья Карамазовы', 2, 1, 799.01, 2),
('Игрок', 2, 1, 480.50, 10),
('Стихотворения и поэмы', 3, 2, 650.00, 15),
('Черный человек', 3, 2, 570.20, 6),
('Лирика', 4, 2, 518.99, 2);
Query OK, 8 rows affected (0.06 sec)
Records: 8 Duplicates: 0 Warnings: 0
mysql> SELECT * FROM book;
+---------+------------------------------------------+-----------+----------+--------+--------+
| book_id | title                  | author_id | genre_id | price | amount |
+---------+------------------------------------------+-----------+----------+--------+--------+
|   1 | Мастер и Маргарита           |     1 |    1 | 670.99 |   3 |
|   2 | Белая гвардия              |     1 |    1 | 540.50 |   5 |
|   3 | Идиот                  |     2 |    1 | 460.00 |   10 |
|   4 | Братья Карамазовы            |     2 |    1 | 799.01 |   2 |
|   5 | Игрок                  |     2 |    1 | 480.50 |   10 |
|   6 | Стихотворения и поэмы          |     3 |    2 | 650.00 |   15 |
|   7 | Черный человек             |     3 |    2 | 570.20 |   6 |
|   8 | Лирика                 |     4 |    2 | 518.99 |   2 |
+---------+------------------------------------------+-----------+----------+--------+--------+
8 rows in set (0.00 sec)
mysql> CREATE TABLE city(
city_id INT PRIMARY KEY AUTO_INCREMENT,
name_city VARCHAR(30),
days_delivery INT
);
Query OK, 0 rows affected (0.25 sec)
mysql> INSERT INTO city(name_city, days_delivery)
VALUES
('Москва', 5),
('Санкт-Петербург', 3),
('Владивосток', 12);
Query OK, 3 rows affected (0.06 sec)
Records: 3 Duplicates: 0 Warnings: 0
mysql> SELECT * FROM city;
+---------+-------------------------------+---------------+
| city_id | name_city           | days_delivery |
+---------+-------------------------------+---------------+
|   1 | Москва            |       5 |
|   2 | Санкт-Петербург       |       3 |
|   3 | Владивосток         |      12 |
+---------+-------------------------------+---------------+
3 rows in set (0.00 sec)
mysql> CREATE TABLE client (
client_id INT PRIMARY KEY AUTO_INCREMENT,
name_client VARCHAR(50),
city_id INT,
email VARCHAR(30),
FOREIGN KEY (city_id) REFERENCES city (city_id)
);
Query OK, 0 rows affected (0.24 sec)
mysql> INSERT INTO client(name_client, city_id, email)
VALUES
('Баранов Павел', 3, 'baranov@test'),
('Абрамова Катя', 1, 'abramova@test'),
('Семенонов Иван', 2, 'semenov@test'),
('Яковлева Галина', 1, 'yakovleva@test');
Query OK, 4 rows affected (0.12 sec)
Records: 4 Duplicates: 0 Warnings: 0
mysql> SELECT * FROM client;
+-----------+-------------------------------+---------+----------------+
| client_id | name_client         | city_id | email     |
+-----------+-------------------------------+---------+----------------+
|     1 | Баранов Павел         |   3 | baranov@test |
|     2 | Абрамова Катя         |   1 | abramova@test |
|     3 | Семенонов Иван        |   2 | semenov@test |
|     4 | Яковлева Галина       |   1 | yakovleva@test |
+-----------+-------------------------------+---------+----------------+
4 rows in set (0.01 sec)
mysql> CREATE TABLE buy(
buy_id INT PRIMARY KEY AUTO_INCREMENT,
buy_description VARCHAR(100),
client_id INT,
FOREIGN KEY (client_id) REFERENCES client (client_id)
);
Query OK, 0 rows affected (0.24 sec)
mysql> INSERT INTO buy (buy_description, client_id)
VALUES
('Доставка только вечером', 1),
(NULL, 3),
('Упаковать каждую книгу по отдельности', 2),
(NULL, 1);
Query OK, 4 rows affected (0.04 sec)
Records: 4 Duplicates: 0 Warnings: 0
mysql> SELECT * FROM buy;
+--------+------------------------------------------------------------------------+-----------+
| buy_id | buy_description                            | client_id |
+--------+------------------------------------------------------------------------+-----------+
|   1 | Доставка только вечером                        |     1 |
|   2 | NULL                                 |     3 |
|   3 | Упаковать каждую книгу по отдельности                 |     2 |
|   4 | NULL                                 |     1 |
+--------+------------------------------------------------------------------------+-----------+
4 rows in set (0.00 sec)
mysql> CREATE TABLE buy_book (
buy_book_id INT PRIMARY KEY AUTO_INCREMENT,
buy_id INT,
book_id INT,
amount INT,
FOREIGN KEY (buy_id) REFERENCES buy (buy_id),
FOREIGN KEY (book_id) REFERENCES book (book_id)
);
Query OK, 0 rows affected (0.24 sec)
mysql> INSERT INTO buy_book(buy_id, book_id, amount)
VALUES
(1, 1, 1),
(1, 7, 2),
(1, 3, 1),
(2, 8, 2),
(3, 3, 2),
(3, 2, 1),
(3, 1, 1),
(4, 5, 1);
Query OK, 8 rows affected (0.03 sec)
Records: 8 Duplicates: 0 Warnings: 0
mysql> SELECT * FROM buy_book;
+-------------+--------+---------+--------+
| buy_book_id | buy_id | book_id | amount |
+-------------+--------+---------+--------+
|     1 |   1 |   1 |   1 |
|     2 |   1 |   7 |   2 |
|     3 |   1 |   3 |   1 |
|     4 |   2 |   8 |   2 |
|     5 |   3 |   3 |   2 |
|     6 |   3 |   2 |   1 |
|     7 |   3 |   1 |   1 |
|     8 |   4 |   5 |   1 |
+-------------+--------+---------+--------+
8 rows in set (0.00 sec)
mysql> CREATE TABLE step (
step_id INT PRIMARY KEY AUTO_INCREMENT,
name_step VARCHAR(30)
);
Query OK, 0 rows affected (0.18 sec)
mysql> INSERT INTO step(name_step)
VALUES
('Оплата'),
('Упаковка'),
('Транспортировка'),
('Доставка');
Query OK, 4 rows affected (0.03 sec)
Records: 4 Duplicates: 0 Warnings: 0
mysql> SELECT * FROM step;
+---------+--------------------------------+
| step_id | name_step           |
+---------+--------------------------------+
|   1 | Оплата             |
|   2 | Упаковка           |
|   3 | Транспортировка        |
|   4 | Доставка           |
+---------+--------------------------------+
4 rows in set (0.00 sec)
mysql> CREATE TABLE buy_step (
buy_step_id INT PRIMARY KEY AUTO_INCREMENT,
buy_id INT,
step_id INT,
date_step_beg DATE,
date_step_end DATE,
FOREIGN KEY (buy_id) REFERENCES buy (buy_id),
FOREIGN KEY (step_id) REFERENCES step (step_id)
);
Query OK, 0 rows affected (0.26 sec)
mysql> INSERT INTO buy_step(buy_id, step_id, date_step_beg, date_step_end)
VALUES (1, 1, '2020-02-20', '2020-02-20'),
(1, 2, '2020-02-20', '2020-02-21'),
(1, 3, '2020-02-22', '2020-03-07'),
(1, 4, '2020-03-08', '2020-03-08'),
(2, 1, '2020-02-28', '2020-02-28'),
(2, 2, '2020-02-29', '2020-03-01'),
(2, 3, '2020-03-02', NULL),
(2, 4, NULL, NULL),
(3, 1, '2020-03-05', '2020-03-05'),
(3, 2, '2020-03-05', '2020-03-06'),
(3, 3, '2020-03-06', '2020-03-10'),
(3, 4, '2020-03-11', NULL),
(4, 1, '2020-03-20', NULL),
(4, 2, NULL, NULL),
(4, 3, NULL, NULL),
(4, 4, NULL, NULL);
Query OK, 16 rows affected (0.14 sec)
Records: 16 Duplicates: 0 Warnings: 0
mysql> SELECT * FROM buy_step;
+-------------+--------+---------+---------------+---------------+
| buy_step_id | buy_id | step_id | date_step_beg | date_step_end |
+-------------+--------+---------+---------------+---------------+
|     1 |   1 |   1 | 2020-02-20  | 2020-02-20  |
|     2 |   1 |   2 | 2020-02-20  | 2020-02-21  |
|     3 |   1 |   3 | 2020-02-22  | 2020-03-07  |
|     4 |   1 |   4 | 2020-03-08  | 2020-03-08  |
|     5 |   2 |   1 | 2020-02-28  | 2020-02-28  |
|     6 |   2 |   2 | 2020-02-29  | 2020-03-01  |
|     7 |   2 |   3 | 2020-03-02  | NULL     |
|     8 |   2 |   4 | NULL     | NULL     |
|     9 |   3 |   1 | 2020-03-05  | 2020-03-05  |
|     10 |   3 |   2 | 2020-03-05  | 2020-03-06  |
|     11 |   3 |   3 | 2020-03-06  | 2020-03-10  |
|     12 |   3 |   4 | 2020-03-11  | NULL     |
|     13 |   4 |   1 | 2020-03-20  | NULL     |
|     14 |   4 |   2 | NULL     | NULL     |
|     15 |   4 |   3 | NULL     | NULL     |
|     16 |   4 |   4 | NULL     | NULL     |
+-------------+--------+---------+---------------+---------------+
16 rows in set (0.00 sec)
Task:
Вывести все заказы Баранова Павла (id заказа, какие книги, по какой цене и в каком количестве он заказал) в отсортированном по номеру заказа и названиям книг виде.
Decision:
mysql> SELECT client_id, name_client FROM client;
+-----------+-------------------------------+
| client_id | name_client         |
+-----------+-------------------------------+
|     1 | Баранов Павел         |
|     2 | Абрамова Катя         |
|     3 | Семенонов Иван        |
|     4 | Яковлева Галина       |
+-----------+-------------------------------+
4 rows in set (0.01 sec)
mysql> SELECT buy_id, client_id FROM buy;
+--------+-----------+
| buy_id | client_id |
+--------+-----------+
|   1 |     1 |
|   4 |     1 |
|   3 |     2 |
|   2 |     3 |
+--------+-----------+
4 rows in set (0.00 sec)
mysql> SELECT buy_book_id, buy_id, book_id, amount FROM buy_book;
+-------------+--------+---------+--------+
| buy_book_id | buy_id | book_id | amount |
+-------------+--------+---------+--------+
|     1 |   1 |   1 |   1 |
|     2 |   1 |   7 |   2 |
|     3 |   1 |   3 |   1 |
|     4 |   2 |   8 |   2 |
|     5 |   3 |   3 |   2 |
|     6 |   3 |   2 |   1 |
|     7 |   3 |   1 |   1 |
|     8 |   4 |   5 |   1 |
+-------------+--------+---------+--------+
8 rows in set (0.00 sec)
mysql> SELECT book_id, title, price, amount FROM book;
+---------+------------------------------------------+--------+--------+
| book_id | title                  | price | amount |
+---------+------------------------------------------+--------+--------+
|   1 | Мастер и Маргарита           | 670.99 |   3 |
|   2 | Белая гвардия              | 540.50 |   5 |
|   3 | Идиот                  | 460.00 |   10 |
|   4 | Братья Карамазовы            | 799.01 |   2 |
|   5 | Игрок                  | 480.50 |   10 |
|   6 | Стихотворения и поэмы          | 650.00 |   15 |
|   7 | Черный человек             | 570.20 |   6 |
|   8 | Лирика                 | 518.99 |   2 |
+---------+------------------------------------------+--------+--------+
8 rows in set (0.00 sec)
mysql> SELECT buy_book.buy_id, book.title, book.price, buy_book.amount
FROM
client
INNER JOIN buy ON client.client_id=buy.client_id
INNER JOIN buy_book ON buy_book.buy_id = buy.buy_id
INNER JOIN book ON buy_book.book_id=book.book_id
WHERE name_client = 'Баранов Павел'
ORDER BY buy.buy_id, title;
+--------+------------------------------------+--------+--------+
| buy_id | title               | price | amount |
+--------+------------------------------------+--------+--------+
|   1 | Идиот               | 460.00 |   1 |
|   1 | Мастер и Маргарита         | 670.99 |   1 |
|   1 | Черный человек           | 570.20 |   2 |
|   4 | Игрок               | 480.50 |   1 |
+--------+------------------------------------+--------+--------+
4 rows in set (0.01 sec)
Task:
Посчитать, сколько раз была заказана каждая книга, для книги вывести ее автора (нужно посчитать, в каком количестве заказов фигурирует каждая книга). Вывести фамилию и инициалы автора, название книги, последний столбец назвать Количество. Результат отсортировать сначала по фамилиям авторов, а потом по названиям книг
# Написание Sql запросов.
Decision:
mysql> SELECT book_id, title, author_id FROM book;
+---------+------------------------------------------+-----------+
| book_id | title                  | author_id |
+---------+------------------------------------------+-----------+
|   1 | Мастер и Маргарита           |     1 |
|   2 | Белая гвардия              |     1 |
|   3 | Идиот                  |     2 |
|   4 | Братья Карамазовы            |     2 |
|   5 | Игрок                  |     2 |
|   6 | Стихотворения и поэмы          |     3 |
|   7 | Черный человек             |     3 |
|   8 | Лирика                 |     4 |
+---------+------------------------------------------+-----------+
8 rows in set (0.00 sec)
mysql> SELECT author_id, name_author FROM author;
+-----------+-------------------------------+
| author_id | name_author         |
+-----------+-------------------------------+
|     1 | Булгаков М.А.         |
|     2 | Достоевский Ф.М.       |
|     3 | Есенин С.А.         |
|     4 | Пастернак Б.Л.        |
|     5 | Лермонтов М.Ю.        |
+-----------+-------------------------------+
5 rows in set (0.00 sec)
mysql> SELECT book_id, amount FROM buy_book;
+---------+--------+
| book_id | amount |
+---------+--------+
|   1 |   1 |
|   7 |   2 |
|   3 |   1 |
|   8 |   2 |
|   3 |   2 |
|   2 |   1 |
|   1 |   1 |
|   5 |   1 |
+---------+--------+
8 rows in set (0.00 sec)
mysql> SELECT author.name_author,book.title,SUM(buy_book.amount) AS Количество
FROM
book
INNER JOIN buy_book ON book.book_id=buy_book.book_id
INNER JOIN author ON book.author_id=author.author_id
GROUP BY author.name_author, book.title
ORDER BY author.name_author, book.title;
+-------------------------------+------------------------------------+----------------------+
| name_author         | title               | Количество     |
+-------------------------------+------------------------------------+----------------------+
| Булгаков М.А.         | Белая гвардия           |          1 |
| Булгаков М.А.         | Мастер и Маргарита         |          2 |
| Достоевский Ф.М.       | Игрок               |          1 |
| Достоевский Ф.М.       | Идиот               |          3 |
| Есенин С.А.         | Черный человек           |          2 |
| Пастернак Б.Л.        | Лирика               |          2 |
+-------------------------------+------------------------------------+----------------------+
6 rows in set (0.01 sec)
mysql> SELECT author.name_author,book.title,SUM(buy_book.amount) AS Количество
FROM
book
LEFT JOIN buy_book ON book.book_id=buy_book.book_id
LEFT JOIN author ON book.author_id=author.author_id
GROUP BY author.name_author,book.title
ORDER BY author.name_author,book.title;
+-------------------------------+------------------------------------------+----------------------+
| name_author         | title                  | Количество     |
+-------------------------------+------------------------------------------+----------------------+
| Булгаков М.А.         | Белая гвардия              |          1 |
| Булгаков М.А.         | Мастер и Маргарита           |          2 |
| Достоевский Ф.М.       | Братья Карамазовы            |         NULL |
| Достоевский Ф.М.       | Игрок                  |          1 |
| Достоевский Ф.М.       | Идиот   &nbs