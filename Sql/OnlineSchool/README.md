Task:
База данных "Online School".
Вставить данные в таблицу
# Разработка Баз данных.
Decision:
testbd=> CREATE TABLE superheroes(  
id SERIAL PRIMARY KEY,
name VARCHAR(100),
align VARCHAR(30),
eye VARCHAR(30),
hair VARCHAR(30),
gender VARCHAR(30),
appearances INT,
year INT,
universe VARCHAR(10)
);
  CREATE TABLE
testbd=> SELECT * FROM superheroes;
   id | name | align | eye | hair | gender | appearances | year | universe
  ----+------+-------+-----+------+--------+-------------+------+----------
  (0 rows)
testbd=> INSERT INTO superheroes(name, appearances, universe)
testbd-> VALUES ('Spider-Man', 4043,'marvel');
  INSERT 0 1
testbd=> SELECT * FROM superheroes;
   id |  name  | align | eye | hair | gender | appearances | year | universe
  ----+------------+-------+-----+------+--------+-------------+------+----------
   1 | Spider-Man |   |   |   |    |    4043 |   | marvel
  (1 row)
testbd=> INSERT INTO superheroes(name, align, eye, hair,
testbd(> gender, appearances, year, universe)
testbd-> VALUES ('Spider-Man (Peter Parker)', 'Good
testbd'> Characters', 'Hazel Eyes', 'Brown Hair',
testbd(> 'Male Characters', 4043, 1962, 'marvel');
  INSERT 0 1
testbd=> SELECT * FROM superheroes;
   id |     name      | align  |  eye   |  hair  |   gender   | appearances | year | universe
  ----+---------------------------+------------+------------+------------+-----------------+-------------+------+----------
   1 | Spider-Man        |      |      |      |         |    4043 |   | marvel
   2 | Spider-Man (Peter Parker) | Good   +| Hazel Eyes | Brown Hair | Male Characters |    4043 | 1962 | marvel
    |             | Characters |      |      |         |       |   |
  (2 rows)
testbd=> INSERT INTO superheroes(id, name, align, eye, hair,
gender, appearances, year, universe)
VALUES (5, 'Spider-Man (Peter Parker)', 'Good
Characters', 'Hazel Eyes', 'Brown Hair',
'Male Characters', 4043, 1962, 'marvel');
  INSERT 0 1
testbd=> SELECT * FROM superheroes;
   id |     name      | align  |  eye   |  hair  |   gender   | appearances | year | universe
  ----+---------------------------+------------+------------+------------+-----------------+-------------+------+----------
   1 | Spider-Man        |      |      |      |         |    4043 |   | marvel
   2 | Spider-Man (Peter Parker) | Good   +| Hazel Eyes | Brown Hair | Male Characters |    4043 | 1962 | marvel
    |             | Characters |      |      |         |       |   |
   3 | Spider-Man (Peter Parker) | Good   +| Hazel Eyes | Brown Hair | Male Characters |    4043 | 1962 | marvel
    |             | Characters |      |      |         |       |   |
   5 | Spider-Man (Peter Parker) | Good   +| Hazel Eyes | Brown Hair | Male Characters |    4043 | 1962 | marvel
    |             | Characters |      |      |         |       |   |
  (4 rows)
Task:
Изменить данные в таблице
# Написание Sql запросов.
Decision:
testbd=> UPDATE superheroes
SET name='Batman',
universe='dc'
WHERE id=1;
UPDATE 1
testbd=> SELECT * FROM superheroes;
   id | name | align  |  eye   |  hair  |   gender   | appearances | year | universe
  ----+--------+------------+------------+------------+-----------------+-------------+------+----------
   1 | Batman | Good   +| Hazel Eyes | Brown Hair | Male Characters |    4043 | 1962 | dc
    |    | Characters |      |      |         |       |   |
  (1 row)
testbd=> UPDATE superheroes
SET gender='Man'
WHERE gender='Male Characters';
UPDATE 1
testbd=> SELECT * FROM superheroes;
   id | name | align  |  eye   |  hair  | gender | appearances | year | universe
  ----+--------+------------+------------+------------+--------+-------------+------+----------
   1 | Batman | Good   +| Hazel Eyes | Brown Hair | Man  |    4043 | 1962 | dc
    |    | Characters |      |      |    |       |   |
  (1 row)
Task:
Удалить данные из таблицы
# Написание Sql запросов.
Decision:
testbd=> INSERT INTO superheroes(id, name, align, eye, hair,
gender, appearances, year, universe)
VALUES (2, 'Spider-Man (Peter Parker)', 'Good
Characters', 'Hazel Eyes', 'Brown Hair',
'Male Characters', 4043, 1962, 'marvel');
INSERT 0 1
testbd=> SELECT * FROM superheroes;
   id |     name      | align  |  eye   |  hair  |   gender   | appearances | year | universe
  ----+---------------------------+------------+------------+------------+-----------------+-------------+------+----------
   1 | Batman          | Good   +| Hazel Eyes | Brown Hair | Man       |    4043 | 1962 | dc
    |             | Characters |      |      |         |       |   |
   2 | Spider-Man (Peter Parker) | Good   +| Hazel Eyes | Brown Hair | Male Characters |    4043 | 1962 | marvel
    |             | Characters |      |      |         |       |   |
  (2 rows)
testbd=> DELETE FROM superheroes
WHERE id=2;
DELETE 1
testbd=> SELECT * FROM superheroes;
   id | name | align  |  eye   |  hair  | gender | appearances | year | universe
  ----+--------+------------+------------+------------+--------+-------------+------+----------
   1 | Batman | Good   +| Hazel Eyes | Brown Hair | Man  |    4043 | 1962 | dc
    |    | Characters |      |      |    |       |   |
  (1 row)
testbd=> INSERT INTO superheroes(id, name, align, eye, hair,
gender, appearances, year, universe)
VALUES (2, 'Spider-Man (Peter Parker)', 'Good
Characters', 'Hazel Eyes', 'Brown Hair',
'Male Characters', 4043, 1962, 'marvel');
  INSERT 0 1
testbd=> DELETE FROM superheroes
WHERE gender='Male Characters';
DELETE 1
testbd=> SELECT * FROM superheroes;
   id | name | align  |  eye   |  hair  | gender | appearances | year | universe
  ----+--------+------------+------------+------------+--------+-------------+------+----------
   1 | Batman | Good   +| Hazel Eyes | Brown Hair | Man  |    4043 | 1962 | dc
    |    | Characters |      |      |    | &
Task:
Удалить все данные
# Написание Sql запросов.
Decision:
testbd=> DELETE FROM superheroes;
  DELETE 1
testbd=> SELECT * FROM superheroes;
   id | name | align | eye | hair | gender | appearances | year | universe
  ----+------+-------+-----+------+--------+-------------+------+----------
  (0 rows)
Task:
Удаление дубликатов email
# Написание Sql запросов.
Decision:
Table: Person
+-------------+---------+
| Column Name | Type  |
+-------------+---------+
| id     | int   |
| email   | varchar |
+-------------+---------+
Task:
Напишите SQL-запрос, чтобы удалить все дубликаты электронных писем, сохранив только одно уникальное электронное письмо с наименьшим идентификатором.
Верните таблицу результатов в любом порядке.
# Написание Sql запросов.
Decision:
postgres=# CREATE TABLE person(
postgres(#   id INT,
postgres(#   email VARCHAR
postgres(# );
INSERT INTO person(id, email) VALUES (1, 'john@example.com');
INSERT INTO person(id, email) VALUES (2, 'bob@example.com');
INSERT INTO person(id, email) VALUES (3, 'john@example.com');
  CREATE TABLE
postgres=# INSERT INTO person(id, email) VALUES (1, 'john@example.com');
postgres=# INSERT INTO person(id, email) VALUES (2, 'bob@example.com');
postgres=# INSERT INTO person(id, email) VALUES (3, 'john@example.com');
postgres=# INSERT INTO person(id, email) VALUES (1, 'john@example.com');
  INSERT 0 1
postgres=# INSERT INTO person(id, email) VALUES (2, 'bob@example.com');
  INSERT 0 1
postgres=# INSERT INTO person(id, email) VALUES (3, 'john@example.com');
  INSERT 0 1
postgres=# SELECT * FROM Person;
   id |   email
  ----+------------------
   1 | john@example.com
   2 | bob@example.com
   3 | john@example.com
  (3 строки)
postgres=# SELECT MIN(id), email FROM person GROUP BY email;
   min |   email
  -----+------------------
   2 | bob@example.com
   1 | john@example.com
  (2 строки)
postgres=# SELECT MIN(id) FROM person GROUP BY email;
  min
  -----
   2
   1
  (2 строки)
postgres=# DELETE FROM person WHERE id NOT IN (SELECT MIN(id) FROM person GROUP BY email);
  DELETE 1
Task:
Группировка
# Написание Sql запросов.
Decision:
testbd=> SELECT * FROM superheroes;
   id | name | align | eye | hair | gender | appearances | year | universe
  ----+------+-------+-----+------+--------+-------------+------+----------
  (0 rows)
testbd=> INSERT INTO superheroes(id, name, align, eye, hair,
gender, appearances, year, universe)
VALUES (2, 'Spider-Man (Peter Parker)', 'Good
Characters', 'Hazel Eyes', 'Brown Hair',
'Male Characters', 4043, 1962, 'marvel');
  INSERT 0 1
testbd=> SELECT gender, COUNT(*) FROM superheroes
testbd-> GROUP BY gender;
     gender   | count
  -----------------+-------
   Male Characters |   1
  (1 row)
testbd=> SELECT * FROM superheroes;
   id |     name      | align  |  eye   |  hair  |   gender   | appearances | year | universe
  ----+---------------------------+------------+------------+------------+-----------------+-------------+------+----------
   2 | Spider-Man (Peter Parker) | Good   +| Hazel Eyes | Brown Hair | Male Characters |    4043 | 1962 | marvel
    |             | Characters |      |      |         |       |   |
  (1 row)
testbd=> SELECT align, COUNT(*) FROM superheroes
testbd-> GROUP BY align;
   align  | count
  ------------+-------
   Good   +|   1
   Characters |
  (1 row)
Task:
Многоуровневая группировка данных
# Написание Sql запросов.
Decision:
estbd=> SELECT universe, align, COUNT(*) FROM superheroes
GROUP BY universe, align;
   universe | align  | count
  ----------+------------+-------
   marvel | Good   +|   1
       | Characters |
  (1 row)
Task:
Фильтрация, группировка, сортировка и лимит
# Написание Sql запросов.
Decision:
testbd=> SELECT hair, COUNT(*) FROM superheroes
WHERE gender='Male Characters'
GROUP BY hair;
    hair  | count
  ------------+-------
   Brown Hair |   1
  (1 row)
testbd=> SELECT hair, COUNT(*) FROM superheroes
WHERE gender='Male Characters'
GROUP BY hair
ORDER BY count(*) DESC;
    hair  | count
  ------------+-------
   Brown Hair |   1
  (1 row)
testbd=> SELECT hair, COUNT(*) FROM superheroes
WHERE gender='Male Characters'
GROUP BY hair
ORDER BY count(*) DESC
LIMIT 5;
    hair  | count
  ------------+-------
   Brown Hair |   1
  (1 row)
Task:
Использование агрегатных функций
# Написание Sql запросов.
Decision:
testbd=> SELECT * FROM superheroes;
   id |                 name                 |   align    |   eye   |     hair     |     gender     | appearances | year | universe
  ------+-----------------------------------------------------------------------+--------------------+-----------------+-----------------------+------------------------+-------------+------+----------
    1 | Spider-Man (Peter Parker)                       | Good Characters  | Hazel Eyes   | Brown Hair      | Male Characters    |    4043 | 1962 | marvel
    2 | Captain America (Steven Rogers)                   | Good Characters  | Blue Eyes   | White Hair      | Male Characters    |    3360 | 1941 | marvel
    3 | Wolverine (James \"Logan\" Howlett)                 | Neutral Characters | Blue Eyes   | Black Hair      | Male Characters    |    3061 | 1974 | marvel
    4 | Iron Man (Anthony \"Tony\" Stark)                   | Good Characters  | Blue Eyes   | Black Hair      | Male Characters    |    2961 | 1963 | marvel
    5 | Thor (Thor Odinson)                         | Good Characters  | Blue Eyes   | Blond Hair      | Male Characters    |    2258 | 1950 | marvel
    6 | Benjamin Grimm (Earth-616)                      | Good Characters  | Blue Eyes   | No Hair       | Male Characters    |    2255 | 1961 | marvel
    7 | Reed Richards (Earth-616)                       | Good Characters  | Brown Eyes   | Brown Hair      | Male Characters    |    2072 | 1961 | marvel
    8 | Hulk (Robert Bruce Banner)                      | Good Characters  | Brown Eyes   | Brown Hair      | Male Characters    |    2017 | 1962 | marvel
    9 | Scott Summers (Earth-616)                       | Neutral Characters | Brown Eyes   | Brown Hair      | Male Characters    |    1955 | 1963 | marvel
   10 | Jonathan Storm (Earth-616)                      | Good Characters  | Blue Eyes   | Blond Hair      | Male Characters    |    1934 | 1961 | marvel
   11 | Henry McCoy (Earth-616)                       | Good Characters  | Blue Eyes   | Blue Hair       | Male Characters    |    1825 | 1963 | marvel
   12 | Susan Storm (Earth-616)                       | Good Characters  | Blue Eyes   | Blond Hair      | Female Characters   |    1713 | 1961 | marvel
   13 | Ororo Munroe (Earth-616)                       | Good Characters  | Blue Eyes   | White Hair      | Female Characters   |    1512 | 1975 | marvel
   14 | Clinton Barton (Earth-616)                      | Good Characters  | Blue Eyes   | Blond Hair      | Male Characters    |    1394 | 1964 | marvel
   15 | Matthew Murdock (Earth-616)                     | Good Characters  | Blue Eyes   | Red Hair       | Male Characters    |    1338 | 1964 | marvel
testbd=> SELECT align, COUNT(*), SUM(appearances)
testbd-> FROM superheroes
testbd-> GROUP BY align;
     align    | count | sum
  --------------------+-------+--------
   Bad Characters   | 489 | 29478
   Good Characters  | 773 | 125961
   Neutral Characters | 249 | 30513
  (3 rows)
Task:
Выражения с агрегатными функциями
# Написание Sql запросов.
Decision:
testbd=> SELECT align, AVG(appearances),
testbd-> SUM(appearances)/COUNT(*) AS average
testbd-> FROM superheroes
testbd-> GROUP BY align;
     align    |     avg     | average
  --------------------+----------------------+---------
   Bad Characters   | 60.2822085889570552 |   60
   Good Characters  | 162.9508408796895213 |   162
   Neutral Characters | 122.5421686746987952 |   122
  (3 rows)
Task:
Использование агрегатных функций
# Написание Sql запросов.
Decision:
testbd=> SELECT year, MIN(appearances), MAX(appearances)
testbd-> FROM superheroes
testbd-> GROUP BY year;
   year | min | max
  ------+-----+------
   1964 | 20 | 1394
   1969 | 17 | 558
   2008 | 19 | 200
   1989 | 19 | 408
   1991 | 18 | 500
   1945 | 81 | 81
   1974 | 18 | 3061
   1943 | 34 | 140
   1971 | 17 | 368
   1977 | 17 | 471
   1956 | 25 | 114
   1940 | 17 | 373
   1983 | 18 | 245
   1984 | 18 | 348
   2009 | 18 | 98
   1958 | 25 | 25
   2005 | 18 | 325
   1973 | 17 | 323
   2013 | 18 | 53
   2003 | 18 | 238
   1993 | 18 | 147
   1990 | 18 | 636
   1953 | 37 | 141
   2002 | 20 | 171
   1979 | 18 | 525
   1997 | 18 | 97
   2004 | 18 | 265
   1980 | 19 | 886
   1986 | 18 | 612
   1970 | 20 | 787
   1975 | 17 | 1512
   1982 | 17 | 657
testbd=> SELECT year, MIN(appearances), MAX(appearances)
testbd-> FROM superheroes
testbd-> GROUP BY year
testbd-> ORDER BY year;
   year | min | max
  ------+-----+------
   1939 | 18 | 548
   1940 | 17 | 373
   1941 | 17 | 3360
   1942 | 19 | 28
   1943 | 34 | 140
   1944 | 30 | 550
   1945 | 81 | 81
   1946 | 99 | 99
   1947 | 139 | 139
   1948 | 17 | 106
   1949 | 26 | 532
   1950 | 70 | 2258
   1951 | 18 | 223
   1953 | 37 | 141
   1954 | 19 | 72
   1955 | 44 | 65
   1956 | 25 | 114
   1958 | 25 | 25
   1960 | 26 | 237
   1961 | 21 | 2255
   1962 | 21 | 4043
   1963 | 20 | 2961
   1964 | 20 | 1394
   1965 | 17 | 1304
   1966 | 17 | 696
   1967 | 17 | 752
   1968 | 17 | 1007
   1969 | 17 | 558
   1970 | 20 | 787
   1971 | 17 | 368
   1972 | 19 | 856
   1973 | 17 | 323
testbd=> SELECT year, MIN(appearances), MAX(appearances)
testbd-> FROM superheroes
testbd-> GROUP BY year
testbd-> ORDER BY MAX(appearances) DESC;
   year | min | max
  ------+-----+------
   1962 | 21 | 4043
   1941 | 17 | 3360
   1974 | 18 | 3061
   1963 | 20 | 2961
   1950 | 70 | 2258
testbd=> SELECT year, MIN(appearances),
testbd-> MAX(appearances) AS max_ap
testbd-> FROM superheroes
testbd-> GROUP BY year
testbd-> ORDER BY max_ap DESC;
   year | min | max_ap
  ------+-----+--------
   1962 | 21 | 4043
   1941 | 17 | 3360
   1974 | 18 | 3061
   1963 | 20 | 2961
   1950 | 70 | 2258
testbd=> SELECT year, MIN(appearances),
testbd-> MAX(appearances) AS max_ap
testbd-> FROM superheroes
testbd-> GROUP BY year
testbd-> ORDER BY max_ap DESC
testbd-> LIMIT 5;
   year | min | max_ap
  ------+-----+--------
   1962 | 21 | 4043
   1941 | 17 | 3360
   1974 | 18 | 3061
   1963 | 20 | 2961
   1950 | 70 | 2258
  (5 rows)
Task:
Агрегатные функции без группировки
# Написание Sql запросов.
Decision:
testbd=> SELECT COUNT(*),
testbd-> MIN(appearances),
testbd-> MAX(appearances),
testbd-> SUM(appearances),
testbd-> AVG(appearances)
testbd-> FROM superheroes;
   count | min | max | sum |     avg    
  -------+-----+------+--------+----------------------
   1511 | 17 | 4043 | 185952 | 123.0655195234943746
  (1 row)
Task:
Группировка данных
# Написание Sql запросов.
Decision:
testbd=> SELECT hair, COUNT(*) FROM superheroes
WHERE gender='Female Characters'
GROUP BY hair;
       hair     | count
  -----------------------+-------
   Strawberry Blond Hair |  11
   Bald         |   2
   Green Hair      |   9
   Silver Hair     |   5
   Red Hair       |  40
Task:
Фильтрация групповых результатов
# Написание Sql запросов.
Decision:
testbd=> SELECT hair, COUNT(*) FROM superheroes
testbd-> WHERE gender='Female Characters'
testbd-> AND COUNT(*) > 10
testbd-> GROUP BY hair;
  ERROR: aggregate functions are not allowed in WHERE
  LINE 3: AND COUNT(*) > 10
        ^
testbd=> SELECT hair, COUNT(*) FROM superheroes
testbd-> WHERE gender='Female Characters'
testbd-> GROUP BY hair
testbd-> HAVING COUNT(*) > 10;
       hair     | count
  -----------------------+-------
   Strawberry Blond Hair |  11
   Red Hair       |  40
   White Hair      |  15
   Black Hair      | 176
   Blond Hair      | 110
testbd=> SELECT hair, COUNT(*) FROM superheroes
WHERE gender='Female Characters'
GROUP BY hair
HAVING COUNT(*) BETWEEN 50 AND 300;
    hair  | count
  ------------+-------
   Black Hair | 176
   Blond Hair | 110
   Brown Hair |  63
  (3 rows)
Task:
Запрос данных из нескольких таблиц
# Написание Sql запросов.
Decision:
testbd=> SELECT * FROM products;
   id |               name               | type_id | price
  ----+---------------------------------------------------------------+---------+-------
   1 | Основы искусственного интеллекта               |   1 | 15000
   2 | Технологии обработки больших данных             |   1 | 50000
   3 | Программирование глубоких нейронных сетей           |   1 | 30000
   4 | Нейронные сети для анализа текстов              |   1 | 50000
   5 | Нейронные сети для анализа изображений            |   1 | 50000
   6 | Инженерия искусственного интеллекта             |   1 | 60000
   7 | Как стать DataScientist'ом                  |   2 |   0
   8 | Планирование карьеры в DataScience              |   2 | 2000
   9 | Области применения нейросетей: в какой развивать экспертность |   2 | 4000
   10 | Программирование глубоких нейронных сетей на Python     |   3 | 1000
   11 | Математика для DataScience                  |   3 | 2000
   12 | Основы визуализации данных                  |   3 | 500
   13 | Анализ временных рядов                    |     | 30000
  (13 rows)
testbd=> SELECT * FROM product_types;
   id | type_name
  ----+--------------
   1 | Онлайн-курс
   2 | Вебинар
   3 | Книга
   4 | Консультация
  (4 rows)
Task:
Объединение данных из нескольких таблиц в SELECT
# Написание Sql запросов.
Decision:
testbd=> SELECT products.name, product_types.type_name
testbd-> FROM products JOIN product_types
testbd-> ON products.type_id = product_types.id;
                 name               | type_name
  ---------------------------------------------------------------+-------------
   Основы искусственного интеллекта               | Онлайн-курс
   Технологии обработки больших данных             | Онлайн-курс
   Программирование глубоких нейронных сетей           | Онлайн-курс
   Нейронные сети для анализа текстов              | Онлайн-курс
   Нейронные сети для анализа изображений            | Онлайн-курс
   Инженерия искусственного интеллекта             | Онлайн-курс
   Как стать DataScientist'ом                  | Вебинар
   Планирование карьеры в DataScience              | Вебинар
   Области применения нейросетей: в какой развивать экспертность | Вебинар
   Программирование глубоких нейронных сетей на Python     | Книга
   Математика для DataScience                  | Книга
   Основы визуализации данных                  | Книга
  (12 rows)
Task:
Псевдонимы таблиц
# Написание Sql запросов.
Decision:
testbd=> SELECT p.name, t.type_name
testbd-> FROM products AS p JOIN product_types AS t
testbd-> ON p.type_id = t.id;
                 name               | type_name
  ---------------------------------------------------------------+-------------
   Основы искусственного интеллекта               | Онлайн-курс
   Технологии обработки больших данных             | Онлайн-курс
   Программирование глубоких нейронных сетей           | Онлайн-курс
   Нейронные сети для анализа текстов              | Онлайн-курс
   Нейронные сети для анализа изображений            | Онлайн-курс
   Инженерия искусственного интеллекта             | Онлайн-курс
   Как стать DataScientist'ом                  | Вебинар
   Планирование карьеры в DataScience              | Вебинар
   Области применения нейросетей: в какой развивать экспертность | Вебинар
   Программирование глубоких нейронных сетей на Python     | Книга
   Математика для DataScience                  | Книга
   Основы визуализации данных                  | Книга
  (12 rows)
Task:
Псевдонимы таблиц и столбцов
# Написание Sql запросов.
Decision:
testbd=> SELECT p.name AS product_name,
testbd-> t.type_name AS product_type,
testbd-> p.price AS product_price
testbd-> FROM products AS p JOIN product_types AS t
testbd-> ON p.type_id = t.id;
               product_name             | product_type | product_price
  ---------------------------------------------------------------+--------------+---------------
   Основы искусственного интеллекта               | Онлайн-курс |     15000
   Технологии обработки больших данных             | Онлайн-курс |     50000
   Программирование глубоких нейронных сетей           | Онлайн-курс |     30000
   Нейронные сети для анализа текстов              | Онлайн-курс |     50000
   Нейронные сети для анализа изображений            | Онлайн-курс |     50000
   Инженерия искусственного интеллекта             | Онлайн-курс |     60000
   Как стать DataScientist'ом                  | Вебинар   |       0
   Планирование карьеры в DataScience              | Вебинар   |     2000
   Области применения нейросетей: в какой развивать экспертность | Вебинар   |     4000
   Программирование глубоких нейронных сетей на Python     | Книга    |     1000
   Математика для DataScience                  | Книга    |     2000
   Основы визуализации данных                  | Книга    |     500
  (12 rows)
Task:
Фильтрация данных из нескольких таблиц
# Написание Sql запросов.
Decision:
testbd=> SELECT p.name AS product_name,
testbd-> t.type_name AS product_type,
testbd-> p.price AS product_price
testbd-> FROM products AS p JOIN product_types AS t
testbd-> ON p.type_id = t.id
testbd-> WHERE t.type_name='Онлайн-курс';
         product_name        | product_type | product_price
  -------------------------------------------+--------------+---------------
   Основы искусственного интеллекта     | Онлайн-курс |     15000
   Технологии обработки больших данных   | Онлайн-курс |     50000
   Программирование глубоких нейронных сетей | Онлайн-курс |     30000
   Нейронные сети для анализа текстов    | Онлайн-курс |     50000
   Нейронные сети для анализа изображений  | Онлайн-курс |     50000
   Инженерия искусственного интеллекта   | Онлайн-курс |     60000
  (6 rows)
testbd=> SELECT p.name AS product_name,
testbd-> t.type_name AS product_type,
testbd-> p.price AS product_price
testbd-> FROM products AS p JOIN product_types AS t
testbd-> ON p.type_id = t.id
testbd-> WHERE t.type_name = 'Вебинар'
testbd-> AND p.price = 0;
      product_name    | product_type | product_price
  ----------------------------+--------------+---------------
   Как стать DataScientist'ом | Вебинар   |       0
  (1 row)
Task:
Сортировка данных из нескольких таблиц
# Написание Sql запросов.
Decision:
testbd=> SELECT p.name AS product_name,
testbd-> t.type_name AS product_type,
testbd-> p.price AS product_price
testbd-> FROM products AS p JOIN product_types AS t
testbd-> ON p.type_id = t.id
testbd-> WHERE t.type_name='Онлайн-курс'
testbd-> ORDER BY p.price DESC;
         product_name        | product_type | product_price
  -------------------------------------------+--------------+---------------
   Инженерия искусственного интеллекта   | Онлайн-курс |     60000
   Технологии обработки больших данных   | Онлайн-курс |     50000
   Нейронные сети для анализа текстов    | Онлайн-курс |     50000
   Нейронные сети для анализа изображений  | Онлайн-курс |     50000
   Программирование глубоких нейронных сетей | Онлайн-курс |     30000
   Основы искусственного интеллекта     | Онлайн-курс |     15000
  (6 rows)
Task:
Типы JOIN
# Написание Sql запросов.
Decision:
testbd=> SELECT * FROM products;
   id |               name               | type_id | price
  ----+---------------------------------------------------------------+---------+-------
   1 | Основы искусственного интеллекта               |   1 | 15000
   2 | Технологии обработки больших данных             |   1 | 50000
   3 | Программирование глубоких нейронных сетей           |   1 | 30000
   4 | Нейронные сети для анализа текстов              |   1 | 50000
   5 | Нейронные сети для анализа изображений            |   1 | 50000
   6 | Инженерия искусственного интеллекта             |   1 | 60000
   7 | Как стать DataScientist'ом                  |   2 |   0
   8 | Планирование карьеры в DataScience              |   2 | 2000
   9 | Области применения нейросетей: в какой развивать экспертность |   2 | 4000
   10 | Программирование глубоких нейронных сетей на Python     |   3 | 1000
   11 | Математика для DataScience                  |   3 | 2000
   12 | Основы визуализации данных                  |   3 | 500
   13 | Анализ временных рядов                    |     | 30000
  (13 rows)
testbd=> SELECT * FROM product_types;
   id | type_name
  ----+--------------
   1 | Онлайн-курс
   2 | Вебинар
   3 | Книга
   4 | Консультация
  (4 rows)
Task:
Объединение таблиц в запросе
# Написание Sql запросов.
Decision:
testbd=> SELECT products.name, product_types.type_name
testbd-> FROM products JOIN product_types
testbd-> ON products.type_id = product_types.id;
                 name               | type_name
  ---------------------------------------------------------------+-------------
   Основы искусственного интеллекта               | Онлайн-курс
   Технологии обработки больших данных             | Онлайн-курс
   Программирование глубоких нейронных сетей           | Онлайн-курс
   Нейронные сети для анализа текстов              | Онлайн-курс
   Нейронные сети для анализа изображений            | Онлайн-курс
   Инженерия искусственного интеллекта             | Онлайн-курс
   Как стать DataScientist'ом                  | Вебинар
   Планирование карьеры в DataScience              | Вебинар
   Области применения нейросетей: в какой развивать экспертность | Вебинар
   Программирование глубоких нейронных сетей на Python     | Книга
   Математика для DataScience                  | Книга
   Основы визуализации данных                  | Книга
  (12 rows)
Task:
Внутреннее объединение
# Написание Sql запросов.
Decision:
testbd=> SELECT products.name, product_types.type_name
testbd-> FROM products INNER JOIN product_types
testbd-> ON products.type_id = product_types.id;
                 name               | type_name
  ---------------------------------------------------------------+-------------
   Основы искусственного интеллекта               | Онлайн-курс
   Технологии обработки больших данных             | Онлайн-курс
   Программирование глубоких нейронных сетей           | Онлайн-курс
   Нейронные сети для анализа текстов              | Онлайн-курс
   Нейронные сети для анализа изображений            | Онлайн-курс
   Инженерия искусственного интеллекта             | Онлайн-курс
   Как стать DataScientist'ом                  | Вебинар
   Планирование карьеры в DataScience              | Вебинар
   Области применения нейросетей: в какой развивать экспертность | Вебинар
   Программирование глубоких нейронных сетей на Python     | Книга
   Математика для DataScience                  | Книга
   Основы визуализации данных                  | Книга
  (12 rows)
Task:
Левое внешнее объединение
# Написание Sql запросов.
Decision:
testbd=> SELECT products.name, product_types.type_name
testbd-> FROM products LEFT OUTER JOIN product_types
testbd-> ON products.type_id = product_types.id;
                 name               | type_name
  ---------------------------------------------------------------+-------------
   Основы искусственного интеллекта               | Онлайн-курс
   Технологии обработки больших данных             | Онлайн-курс
   Программирование глубоких нейронных сетей           | Онлайн-курс
   Нейронные сети для анализа текстов              | Онлайн-курс
   Нейронные сети для анализа изображений            | Онлайн-курс
   Инженерия искусственного интеллекта             | Онлайн-курс
   Как стать DataScientist'ом                  | Вебинар
   Планирование карьеры в DataScience              | Вебинар
   Области применения нейросетей: в какой развивать экспертность | Вебинар
   Программирование глубоких нейронных сетей на Python     | Книга
   Математика для DataScience                  | Книга
   Основы визуализации данных                  | Книга
   Анализ временных рядов                    |
  (13 rows)
Task:
Правое внешнее объединение
# Написание Sql запросов.
Decision:
testbd=> SELECT products.name, product_types.type_name
testbd-> FROM products RIGHT OUTER JOIN product_types
testbd-> ON products.type_id = product_types.id;
                 name               | type_name
  ---------------------------------------------------------------+--------------
   Основы искусственного интеллекта               | Онлайн-курс
   Технологии обработки больших данных             | Онлайн-курс
   Программирование глубоких нейронных сетей           | Онлайн-курс
   Нейронные сети для анализа текстов              | Онлайн-курс
   Нейронные сети для анализа изображений            | Онлайн-курс
   Инженерия искусственного интеллекта             | Онлайн-курс
   Как стать DataScientist'ом                  | Вебинар
   Планирование карьеры в DataScience              | Вебинар
   Области применения нейросетей: в какой развивать экспертность | Вебинар
   Программирование глубоких нейронных сетей на Python     | Книга
   Математика для DataScience                  | Книга
   Основы визуализации данных                  | Книга
                                 | Консультация
  (13 rows)
Task:
Полное внешнее объединение
# Написание Sql запросов.
Decision:
testbd=> SELECT products.name, product_types.type_name
testbd-> FROM products FULL OUTER JOIN product_types
testbd-> ON products.type_id = product_types.id;
                 name               | type_name
  ---------------------------------------------------------------+--------------
   Основы искусственного интеллекта               | Онлайн-курс
   Технологии обработки больших данных             | Онлайн-курс
   Программирование глубоких нейронных сетей           | Онлайн-курс
   Нейронные сети для анализа текстов              | Онлайн-курс
   Нейронные сети для анализа изображений            | Онлайн-курс
   Инженерия искусственного интеллекта             | Онлайн-курс
   Как стать DataScientist'ом                  | Вебинар
   Планирование карьеры в DataScience              | Вебинар
   Области применения нейросетей: в какой развивать экспертность | Вебинар
   Программирование глубоких нейронных сетей на Python     | Книга
   Математика для DataScience                  | Книга
   Основы визуализации данных                  | Книга
   Анализ временных рядов                    |
                                 | Консультация
  (14 rows)
Task:
Перекрестное объединение
# Написание Sql запросов.
Decision:
testbd=> SELECT products.name, product_types.type_name
testbd-> FROM products CROSS JOIN product_types;
                 name               | type_name
  ---------------------------------------------------------------+--------------
   Основы искусственного интеллекта               | Онлайн-курс
   Технологии обработки больших данных             | Онлайн-курс
   Программирование глубоких нейронных сетей           | Онлайн-курс
   Нейронные сети для анализа текстов              | Онлайн-курс
   Нейронные сети для анализа изображений            | Онлайн-курс
   Инженерия искусственного интеллекта             | Онлайн-курс
   Как стать DataScientist'ом                  | Онлайн-курс
   Планирование карьеры в DataScience              | Онлайн-курс
   Области применения нейросетей: в какой развивать экспертность | Онлайн-курс
   Программирование глубоких нейронных сетей на Python     | Онлайн-курс
   Математика для DataScience                  | Онлайн-курс
   Основы визуализации данных                  | Онлайн-курс
   Анализ временных рядов                    | Онлайн-курс
   Основы искусственного интеллекта               | Вебинар
   Технологии обработки больших данных             | Вебинар
   Программирование глубоких нейронных сетей           | Вебинар
   Нейронные сети для анализа текстов              | Вебинар
   Нейронные сети для анализа изображений            | Вебинар
   Инженерия искусственного интеллекта             | Вебинар
   Как стать DataScientist'ом                  | Вебинар
   Планирование карьеры в DataScience              | Вебинар
   Области применения нейросетей: в какой развивать экспертность | Вебинар
   Программирование глубоких нейронных сетей на Python     | Вебинар
   Математика для DataScience                  | Вебинар
   Основы визуализации данных                  | Вебинар
   Анализ временных рядов                    | Вебинар
   Основы искусственного интеллекта               | Книга
   Технологии обработки больших данных             | Книга
   Программирование глубоких нейронных сетей           | Книга
   Нейронные сети для анализа текстов              | Книга
   Нейронные сети для анализа изображений            | Книга
   Инженерия искусственного интеллекта             | Книга
Task:
Объединить две таблицы
# Написание Sql запросов.
Decision:
Table: Person
+-------------+---------+
| Column Name | Type  |
+-------------+---------+
| personId  | int   |
| lastName  | varchar |
| firstName | varchar |
+-------------+---------+
Table: Address
+-------------+---------+
| Column Name | Type  |
+-------------+---------+
| addressId | int   |
| personId  | int   |
| city    | varchar |
| state   | varchar |
+-------------+---------+
Напишите SQL-запрос, чтобы сообщить имя, фамилию, город и состояние каждого человека в таблице Person. Если адрес идентификатора человека отсутствует в таблице адресов, вместо этого сообщите null.
Верните таблицу результатов в любом порядке.
Input:
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1    | Wang   | Allen   |
| 2    | Alice  | Bob   |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city     | state   |
+-----------+----------+---------------+------------+
| 1     | 2    | New York City | New York |
| 2     | 3    | Leetcode   | California |
+-----------+----------+---------------+------------+
Output:
+-----------+----------+---------------+----------+
| firstName | lastName | city     | state  |
+-----------+----------+---------------+----------+
| Allen   | Wang   | Null     | Null   |
| Bob   | Alice  | New York City | New York |
+-----------+----------+---------------+----------+
# Написание Sql запросов.
Decision:
SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person AS p LEFT OUTER JOIN Address AS a
ON p.PersonId = a.PersonId;
  personId  lastName  firstName
0 1     Wang    Allen
1 2     Alice   Bob
  addressId personId  city      state
0 1     2     New York City New York
1 2     3     Leetcode    California
Task:
JOIN нескольких таблиц
В какие города летал Bruce Willis
# Написание Sql запросов.
Decision:
SELECT id FROM Passenger WHERE name = 'Bruce Willis';
SELECT trip FROM Pass_in_trip WHERE passenger = 1 OR passenger = 31;
SELECT town_to FROM Trip WHERE id IN (1100, 1123, 1181);
SELECT town_to
FROM Trip JOIN Pass_in_trip
ON Trip.id=Pass_in_trip.trip
JOIN Passenger
ON Pass_in_trip.passenger=Passenger.id
WHERE Passenger.name='Bruce Willis';
SELECT town_to
FROM Trip JOIN Pass_in_trip
ON Trip.id=Pass_in_trip.trip
JOIN Passenger
ON Pass_in_trip.passenger=Passenger.id
JOIN Company
ON Trip.company=Company.id
WHERE Passenger.name='Bruce Willis';
Task:
Схема базы данных
# Написание Sql запросов.
Decision:
testbd=> SELECT * FROM products;
   id |               name               | type_id | price
  ----+---------------------------------------------------------------+---------+-------
   1 | Основы искусственного интеллекта               |   1 | 15000
   2 | Технологии обработки больших данных             |   1 | 50000
   3 | Программирование глубоких нейронных сетей           |   1 | 30000
   4 | Нейронные сети для анализа текстов              |   1 | 50000
   5 | Нейронные сети для анализа изображений            |   1 | 50000
   6 | Инженерия искусственного интеллекта             |   1 | 60000
   7 | Как стать DataScientist'ом                  |   2 |   0
   8 | Планирование карьеры в DataScience              |   2 | 2000
   9 | Области применения нейросетей: в какой развивать экспертность |   2 | 4000
   10 | Программирование глубоких нейронных сетей на Python     |   3 | 1000
   11 | Математика для DataScience                  |   3 | 2000
   12 | Основы визуализации данных                  |   3 | 500
   13 | Анализ временных рядов                    |     | 30000
  (13 rows)
testbd=> SELECT * FROM product_types;
   id | type_name
  ----+--------------
   1 | Онлайн-курс
   2 | Вебинар
   3 | Книга
   4 | Консультация
  (4 rows)
testbd=> SELECT * FROM customers;
   id |   name   |     email    
  ----+-----------------+------------------------
   1 | Иван Петров   | petrov@mail.ru
   2 | Петр Иванов   | ivanov@gmail.com
   3 | Тимофей Сергеев | ts@gmail.com
   4 | Даша Корнеева | dasha.korneeva@mail.ru
   5 | Иван Иван   | petrov@mail.ru
   6 | Сергей Щербаков | user156@yandex.ru
   7 | Катя Самарина | kate@mail.ru
   8 | Андрей Котов  | a.kotoff@yandex.ru
  (8 rows)
testbd=> SELECT * FROM orders;
   id | order_date | customer_id
  ----+------------+-------------
   1 | 2021-01-11 |     1
   2 | 2021-01-15 |     3
   3 | 2021-01-20 |     4
   4 | 2021-01-12 |     2
   5 | 2021-01-25 |     8
   6 | 2021-01-30 |     1
  (6 rows)
testbd=> SELECT * FROM sales;
   product_id | order_id | quantity
  ------------+----------+----------
       3 |    1 |    1
       4 |    6 |    1
       10 |    2 |    2
       11 |    2 |    2
       3 |    3 |    1
       4 |    3 |    1
       5 |    3 |    1
       1 |    4 |    1
       6 |    5 |    1
  (9 rows)
Task:
Продукты в заказе
# Написание Sql запросов.
Decision:
testbd=> SELECT p.id,
testbd-> p.name,
testbd-> p.price,
testbd-> s.quantity,
testbd-> p.price * s.quantity AS total
testbd-> FROM products AS p JOIN sales AS s
testbd-> ON p.id = s.product_id
testbd-> WHERE s.order_id=2;
   id |            name             | price | quantity | total
  ----+-----------------------------------------------------+-------+----------+-------
   10 | Программирование глубоких нейронных сетей на Python | 1000 |    2 | 2000
   11 | Математика для DataScience             | 2000 |    2 | 4000
  (2 rows)
Task:
Все покупки заказчика
# Написание Sql запросов.
Decision:
testbd=> SELECT p.id,
testbd-> p.name,
testbd-> p.price,
testbd-> s.quantity,
testbd-> p.price * s.quantity AS total
testbd-> FROM products AS p JOIN sales AS s
testbd-> ON p.id = s.product_id
testbd-> JOIN orders AS o
testbd-> ON o.id = s.order_id
testbd-> WHERE o.customer_id=1;
   id |         name          | price | quantity | total
  ----+-------------------------------------------+-------+----------+-------
   3 | Программирование глубоких нейронных сетей | 30000 |    1 | 30000
   4 | Нейронные сети для анализа текстов    | 50000 |    1 | 50000
  (2 rows)
Task:
Подзапросы
# Написание Sql запросов.
Decision:
postgres=# SELECT * FROM products;
   id |               name               | type_id | price
  ----+---------------------------------------------------------------+---------+-------
   1 | Основы искусственного интеллекта               |   1 | 15000
   2 | Технологии обработки больших данных             |   1 | 50000
   3 | Программирование глубоких нейронных сетей           |   1 | 30000
   4 | Нейронные сети для анализа текстов              |   1 | 50000
   5 | Нейронные сети для анализа изображений            |   1 | 50000
   6 | Инженерия искусственного интеллекта             |   1 | 60000
   7 | Как стать DataScientist'ом                  |   2 |   0
   8 | Планирование карьеры в DataScience              |   2 | 2000
   9 | Области применения нейросетей: в какой развивать экспертность |   2 | 4000
   10 | Программирование глубоких нейронных сетей на Python     |   3 | 1000
   11 | Математика для DataScience                  |   3 | 2000
   12 | Основы визуализации данных                  |   3 | 500
   13 | Анализ временных рядов                    |     | 30000
  (13 строк)
postgres=# SELECT id, name, price
postgres-# FROM products
postgres-# WHERE price = (SELECT MAX(price)
postgres(# FROM products);
   id |        name         | price
  ----+-------------------------------------+-------
   6 | Инженерия искусственного интеллекта | 60000
  (1 строка)
postgres=# SELECT MAX(price) FROM products;
   max
  -------
   60000
  (1 строка)
postgres=# SELECT id, name, price
postgres-# FROM products
postgres-# WHERE price = 60000;
   id |        name         | price
  ----+-------------------------------------+-------
   6 | Инженерия искусственного интеллекта | 60000
  (1 строка)
Task:
Вывести информацию о самом дорогом продукте
# Написание Sql запросов.
Decision:
postgres=# SELECT id, name, price
postgres-# FROM products
postgres-# WHERE price = (SELECT MAX(price)
postgres(# FROM products);
   id |        name         | price
  ----+-------------------------------------+-------
   6 | Инженерия искусственного интеллекта | 60000
  (1 строка)
Task:
Вывести информацию о продуктах, которые были проданы хотя бы 1 раз
# Написание Sql запросов.
Decision:
postgres=# SELECT id, name, price
postgres-# FROM products
postgres-# WHERE id IN (SELECT product_id
postgres(# FROM sales);
   id |            name             | price
  ----+-----------------------------------------------------+-------
   1 | Основы искусственного интеллекта          | 15000
   3 | Программирование глубоких нейронных сетей     | 30000
   4 | Нейронные сети для анализа текстов         | 50000
   5 | Нейронные сети для анализа изображений       | 50000
   6 | Инженерия искусственного интеллекта         | 60000
   10 | Программирование глубоких нейронных сетей на Python | 1000
   11 | Математика для DataScience             | 2000
  (7 строк)
postgres=# SELECT * FROM sales;
   product_id | order_id | quantity
  ------------+----------+----------
       3 |    1 |    1
       4 |    6 |    1
       10 |    2 |    2
       11 |    2 |    2
       3 |    3 |    1
       4 |    3 |    1
       5 |    3 |    1
       1 |    4 |    1
       6 |    5 |    1
  (9 строк)
postgres=# SELECT product_id FROM sales;
   product_id
  ------------
       3
       4
       10
       11
       3
       4
       5
       1
       6
  (9 строк)
postgres=# SELECT id, name, price
postgres-# FROM products
postgres-# WHERE id IN (3, 4, 10, 11, 3, 4, 5, 1, 6);
   id |            name             | price
  ----+-----------------------------------------------------+-------
   1 | Основы искусственного интеллекта          | 15000
   3 | Программирование глубоких нейронных сетей     | 30000
   4 | Нейронные сети для анализа текстов         | 50000
   5 | Нейронные сети для анализа изображений       | 50000
   6 | Инженерия искусственного интеллекта         | 60000
   10 | Программирование глубоких нейронных сетей на Python | 1000
   11 | Математика для DataScience             | 2000
  (7 строк)
Task:
Индексы
Decision:
postgres=# SELECT * FROM superheroes;
   id |                 name                 |   align    |    eye     |     hair     |     gender     | appearances | year | universe
  ------+-----------------------------------------------------------------------+--------------------+--------------------+-----------------------+------------------------+-------------+------+----------
    1 | Spider-Man (Peter Parker)                       | Good Characters  | Hazel Eyes     | Brown Hair      | Male Characters    |    4043 | 1962 | marvel
    2 | Captain America (Steven Rogers)                   | Good Characters  | Blue Eyes     | White Hair      | Male Characters    |    3360 | 1941 | marvel
    3 | Wolverine (James \"Logan\" Howlett)                 | Neutral Characters | Blue Eyes     | Black Hair      | Male Characters    |    3061 | 1974 | marvel
    4 | Iron Man (Anthony \"Tony\" Stark)                   | Good Characters  | Blue Eyes     | Black Hair      | Male Characters    |    2961 | 1963 | marvel
    5 | Thor (Thor Odinson)                         | Good Characters  | Blue Eyes     | Blond Hair      | Male Characters    |    2258 | 1950 | marvel
    6 | Benjamin Grimm (Earth-616)                      | Good Characters  | Blue Eyes     | No Hair       | Male Characters    |    2255 | 1961 | marvel
    7 | Reed Richards (Earth-616)                       | Good Characters  | Brown Eyes     | Brown Hair      | Male Characters    |    2072 | 1961 | marvel
    8 | Hulk (Robert Bruce Banner)                      | Good Characters  | Brown Eyes     | Brown Hair      | Male Characters    |    2017 | 1962 | marvel
    9 | Scott Summers (Earth-616)                       | Neutral Characters | Brown Eyes     | Brown Hair      | Male Characters    |    1955 | 1963 | marvel
   10 | Jonathan Storm (Earth-616)                      | Good Characters  | Blue Eyes     | Blond Hair      | Male Characters    |    1934 | 1961 | marvel
   11 | Henry McCoy (Earth-616)                       | Good Characters  | Blue Eyes     | Blue Hair       | Male Characters    |    1825 | 1963 | marvel
   12 | Susan Storm (Earth-616)                       | Good Characters  | Blue Eyes     | Blond Hair      | Female Characters   |    1713 | 1961 | marvel
   13 | Ororo Munroe (Earth-616)                       | Good Characters  | Blue Eyes     | White Hair      | Female Characters   |    1512 | 1975 | marvel
   14 | Clinton Barton (Earth-616)                      | Good Characters  | Blue Eyes     | Blond Hair      | Male Characters    |    1394 | 1964 | marvel
   15 | Matthew Murdock (Earth-616)                     | Good Characters  | Blue Eyes     | Red Hair       | Male Characters    |    1338 | 1964 | marvel
   16 | Stephen Strange (Earth-616)                     | Good Characters  | Grey Eyes     | Black Hair      | Male Characters    |    1307 | 1963 | marvel
   17 | Mary Jane Watson (Earth-616)                     | Good Characters  | Green Eyes     | Red Hair       | Female Characters   |    1304 | 1965 | marvel
   18 | John Jonah Jameson (Earth-616)                    | Neutral Characters | Blue Eyes     | Black Hair      | Male Characters    |    1266 | 1963 | marvel
   19 | Robert Drake (Earth-616)                       | Good Characters  | Brown Eyes     | Brown Hair      | Male Characters    |    1265 | 1963 | marvel
   20 | Henry Pym (Earth-616)                         | Good Characters  | Blue Eyes     | Blond Hair      | Male Characters  
Task:
Запрос на поиск данных
# Написание Sql запросов.
Decision:
postgres=# SELECT * FROM superheroes;
postgres=# SELECT name, appearances, eye, hair
postgres-# FROM superheroes
postgres-# WHERE name = 'Iron Man (Anthony \"Tony\" Stark)';
         name        | appearances |  eye  |  hair
  -----------------------------------+-------------+-----------+------------
   Iron Man (Anthony \"Tony\" Stark) |    2961 | Blue Eyes | Black Hair
  (1 строка)
Task:
Создание индекса
# Написание Sql запросов.
Decision:
postgres=# CREATE INDEX superheroes_name_idx
postgres-# ON superheroes(name);
  CREATE INDEX
Task:
Использование индекса при запросе
# Написание Sql запросов.
Decision:
postgres=# SELECT name, appearances, eye, hair
postgres-# FROM superheroes
postgres-# WHERE name = 'Iron Man (Anthony \"Tony\" Stark)';
         name        | appearances |  eye  |  hair
  -----------------------------------+-------------+-----------+------------
   Iron Man (Anthony \"Tony\" Stark) |    2961 | Blue Eyes | Black Hair
  (1 строка)
Task:
Порядок сортировки данных в индексе
# Написание Sql запросов.
Decision:
postgres=# CREATE INDEX superheroes_appearances_idx
postgres-# ON superheroes(appearances DESC);
  CREATE INDEX
Task:
Ограничения
# Написание Sql запросов.
Decision:
postgres=# CREATE TABLE superheroes1(
id INT PRIMARY KEY,
name VARCHAR(100),
align VARCHAR(30),
eye VARCHAR(30),
hair VARCHAR(30),
gender VARCHAR(30),
appearances INT,
year INT,
universe VARCHAR(10)
);
  CREATE TABLE
postgres=# SELECT * FROM superheroes1;
   id | name | align | eye | hair | gender | appearances | year | universe
  ----+------+-------+-----+------+--------+-------------+------+----------
  (0 строк)
Task:
Непустые значения
# Написание Sql запросов.
Decision:
postgres=# CREATE TABLE superheroes2(
id INT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
align VARCHAR(30),
eye VARCHAR(30),
hair VARCHAR(30),
gender VARCHAR(30),
appearances INT,
year INT,
universe VARCHAR(10)
);
  CREATE TABLE  
postgres=# SELECT * FROM superheroes2;
   id | name | align | eye | hair | gender | appearances | year | universe
  ----+------+-------+-----+------+--------+-------------+------+----------
  (0 строк)
Task:
Уникальные значения
# Написание Sql запросов.
Decision:
postgres=# CREATE TABLE superheroes3(
postgres(# id INT PRIMARY KEY,
postgres(# name VARCHAR(100) UNIQUE,
postgres(# align VARCHAR(30),
postgres(# eye VARCHAR(30),
postgres(# hair VARCHAR(30),
postgres(# gender VARCHAR(30),
postgres(# appearances INT,
postgres(# year INT,
postgres(# universe VARCHAR(10)
postgres(# );
CREATE TABLE
postgres=# SELECT * FROM superheroes3;
   id | name | align | eye | hair | gender | appearances | year | universe
  ----+------+-------+-----+------+--------+-------------+------+----------
  (0 строк)
Task:
Уникальные непустые значения
# Написание Sql запросов.
Decision:
postgres=# CREATE TABLE superheroes4(
postgres(# id INT PRIMARY KEY,
postgres(# name VARCHAR(100) UNIQUE NOT NULL,
postgres(# align VARCHAR(30),
postgres(# eye VARCHAR(30),
postgres(# hair VARCHAR(30),
postgres(# gender VARCHAR(30),
postgres(# appearances INT,
postgres(# year INT,
postgres(# universe VARCHAR(10)
postgres(# );
  CREATE TABLE
postgres=# SELECT * FROM superheroes4;
   id | name | align | eye | hair | gender | appearances | year | universe
  ----+------+-------+-----+------+--------+-------------+------+----------
  (0 строк)
Task:
Первичный ключ из нескольких полей
# Написание Sql запросов.
Decision:
postgres=# CREATE TABLE sales1(
postgres(# product_id INT,
postgres(# order_id INT,
postgres(# quantity INT,
postgres(# PRIMARY KEY(product_id, order_id)
postgres(# );
  CREATE TABLE
postgres=# SELECT * FROM sales1;
   product_id | order_id | quantity
  ------------+----------+----------
  (0 строк)
Task:
Первичный и внешний ключи
# Написание Sql запросов.
Decision:
postgres=# CREATE TABLE sales2(
product_id INT REFERENCES products(id),
order_id INT REFERENCES orders(id),
quantity INT,
PRIMARY KEY(product_id, order_id)
);
  CREATE TABLE
postgres=# SELECT * FROM sales2;
   product_id | order_id | quantity
  ------------+----------+----------
  (0 строк)
Task:
Представления с данными из нескольких таблиц
# Написание Sql запросов.
Decision:
postgres=# SELECT * FROM products;
   id |               name               | type_id | price
  ----+---------------------------------------------------------------+---------+-------
   1 | Основы искусственного интеллекта               |   1 | 15000
   2 | Технологии обработки больших данных             |   1 | 50000
   3 | Программирование глубоких нейронных сетей           |   1 | 30000
   4 | Нейронные сети для анализа текстов              |   1 | 50000
   5 | Нейронные сети для анализа изображений            |   1 | 50000
   6 | Инженерия искусственного интеллекта             |   1 | 60000
   7 | Как стать DataScientist'ом                  |   2 |   0
   8 | Планирование карьеры в DataScience              |   2 | 2000
   9 | Области применения нейросетей: в какой развивать экспертность |   2 | 4000
   13 | Анализ временных рядов                    |     | 30000
   10 | Программирование глубоких нейронных сетей на Python     |   3 | 1500
   11 | Математика для DataScience                  |   3 | 2500
   12 | Основы визуализации данных                  |   3 | 1000
  (13 строк)
postgres=# CREATE VIEW products_v
postgres-# AS SELECT p.id AS id,
postgres-# p.name AS product_name,
postgres-# t.type_name AS product_type,
postgres-# p.price AS product_price
postgres-# FROM products AS p JOIN product_types AS t
postgres-# ON p.type_id = t.id;
  CREATE VIEW
postgres=# SELECT * FROM products_v;
   id |             product_name             | product_type | product_price
  ----+---------------------------------------------------------------+--------------+---------------
   1 | Основы искусственного интеллекта               | Онлайн-курс |     15000
   2 | Технологии обработки больших данных             | Онлайн-курс |     50000
   3 | Программирование глубоких нейронных сетей           | Онлайн-курс |     30000
   4 | Нейронные сети для анализа текстов              | Онлайн-курс |     50000
   5 | Нейронные сети для анализа изображений            | Онлайн-курс |     50000
   6 | Инженерия искусственного интеллекта             | Онлайн-курс |     60000
   7 | Как стать DataScientist'ом                  | Вебинар   |       0
   8 | Планирование карьеры в DataScience              | Вебинар   |     2000
   9 | Области применения нейросетей: в какой развивать экспертность | Вебинар   |     4000
   10 | Программирование глубоких нейронных сетей на Python     | Книга    |     1500
   11 | Математика для DataScience                  | Книга    |     2500
   12 | Основы визуализации данных                  | Книга    |     1000
  (12 строк)
Task:
Материализованные представления
# Написание Sql запросов.
Decision:
postgres=# CREATE MATERIALIZED VIEW products_v1
AS SELECT p.id AS id,
p.name AS product_name,
t.type_name AS product_type,
p.price AS product_price
FROM products AS p JOIN product_types AS t
ON p.type_id = t.id;
  SELECT 12
postgres=# SELECT * FROM products_v1;
   id |             product_name             | product_type | product_price
  ----+---------------------------------------------------------------+--------------+---------------
   1 | Основы искусственного интеллекта               | Онлайн-курс |     15000
   2 | Технологии обработки больших данных             | Онлайн-курс |     50000
   3 | Программирование глубоких нейронных сетей           | Онлайн-курс |     30000
   4 | Нейронные сети для анализа текстов              | Онлайн-курс |     50000
   5 | Нейронные сети для анализа изображений            | Онлайн-курс |     50000
   6 | Инженерия искусственного интеллекта             | Онлайн-курс |     60000
   7 | Как стать DataScientist'ом                  | Вебинар   |       0
   8 | Планирование карьеры в DataScience              | Вебинар   |     2000
   9 | Области применения нейросетей: в какой развивать экспертность | Вебинар   |     4000
   10 | Программирование глубоких нейронных сетей на Python     | Книга    |     1500
   11 | Математика для DataScience                  | Книга    |     2500
   12 | Основы визуализации данных                  | Книга    |     1000
  (12 строк)
Task:
Обновление материализованных представлений
# Написание Sql запросов.
Decision:
postgres=# REFRESH MATERIALIZED VIEW products_v1;
  REFRESH MATERIALIZED VIEW
postgres=# SELECT * FROM products_v1;
   id |             product_name             | product_type | product_price
  ----+---------------------------------------------------------------+--------------+---------------
   1 | Основы искусственного интеллекта               | Онлайн-курс |     15000
   2 | Технологии обработки больших данных             | Онлайн-курс |     50000
   3 | Программирование глубоких нейронных сетей           | Онлайн-курс |     30000
   4 | Нейронные сети для анализа текстов              | Онлайн-курс |     50000
   5 | Нейронные сети для анализа изображений            | Онлайн-курс |     50000
   6 | Инженерия искусственного интеллекта             | Онлайн-курс |     60000
   7 | Как стать DataScientist'ом                  | Вебинар   |       0
   8 | Планирование карьеры в DataScience              | Вебинар   |     2000
   9 | Области применения нейросетей: в какой развивать экспертность | Вебинар   |     4000
   10 | Программирование глубоких нейронных сетей на Python     | Книга    |     1500
   11 | Математика для DataScience                  | Книга    |     2500
   12 | Основы визуализации данных                  | Книга    |     1000
  (12 строк)
Task:
Удаление представлений
# Написание Sql запросов.
Decision:
postgres=# DROP VIEW products_v;
  DROP VIEW
postgres=# SELECT * FROM products_v;
  ОШИБКА: отношение "products_v" не существует
  СТРОКА 1: SELECT * FROM products_v;
            ^
Task:
Удаление материализованных представлений
# Написание Sql запросов.
Decision:
postgres=# DROP MATERIALIZED VIEW products_v1;
  DROP MATERIALIZED VIEW
postgres=# SELECT * FROM products_v1;
  ОШИБКА: отношение "products_v1" не существует
  СТРОКА 1: SELECT * FROM products_v1;
Source:
# https://www.asozykin.ru/?ysclid=lk9eaatbqj18673257