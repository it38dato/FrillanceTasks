Task:
База данных "Staff".
Сотрудники зарабатывают больше, чем их менеджеры
Table: Employee
+-------------+---------+
| Column Name | Type  |
+-------------+---------+
| id     | int   |
| name    | varchar |
| salary   | int   |
| managerId | int   |
+-------------+---------+
Напишите SQL-запрос, чтобы найти сотрудников, которые зарабатывают больше, чем их менеджеры. Верните таблицу результатов в любом порядке.
# Написание Sql запросов.
Decision:
postgres=# DROP TABLE IF EXISTS Employee;
  ЗАМЕЧАНИЕ: таблица "employee" не существует, пропускается
  DROP TABLE
postgres=# CREATE TABLE Employee(
postgres(# id INT,
postgres(# name VARCHAR,
postgres(# salary INT,
postgres(# managerid INT
postgres(# );
  CREATE TABLE
postgres=# SELECT * FROM Employee;
   id | name | salary | managerid
  ----+------+--------+-----------
  (0 строк)
postgres=# INSERT INTO Employee(id, name, salary, managerid) VALUES (1, 'Joe', 70000, 3);
  INSERT 0 1
postgres=# INSERT INTO Employee(id, name, salary, managerid) VALUES (2, 'Henry', 80000, 4);
  INSERT 0 1
postgres=# INSERT INTO Employee(id, name, salary) VALUES (3, 'Sam', 60000);
  INSERT 0 1
postgres=# INSERT INTO Employee(id, name, salary) VALUES (4, 'Max', 90000);
  INSERT 0 1
postgres=# SELECT * FROM Employee;
   id | name | salary | managerid
  ----+-------+--------+-----------
   1 | Joe | 70000 |     3
   2 | Henry | 80000 |     4
   3 | Sam | 60000 |
   4 | Max | 90000 |
  (4 строки)
postgres=# SELECT * FROM Employee AS e JOIN Employee AS m
postgres-# ON e.managerid = m.id;
   id | name | salary | managerid | id | name | salary | managerid
  ----+-------+--------+-----------+----+------+--------+-----------
   1 | Joe | 70000 |     3 | 3 | Sam | 60000 |
   2 | Henry | 80000 |     4 | 4 | Max | 90000 |
  (2 строки)
postgres=# SELECT * FROM Employee AS e JOIN Employee AS m
ON e.managerid = m.id
postgres-# WHERE e.salary > m.salary;
   id | name | salary | managerid | id | name | salary | managerid
  ----+------+--------+-----------+----+------+--------+-----------
   1 | Joe | 70000 |     3 | 3 | Sam | 60000 |
  (1 строка)
postgres=# SELECT e.name FROM Employee AS e JOIN Employee AS m
ON e.managerid = m.id
WHERE e.salary > m.salary;
   name
  ------
   Joe
  (1 строка)
postgres=# SELECT e.name AS Employee FROM Employee AS e JOIN Employee AS m
ON e.managerid = m.id
WHERE e.salary > m.salary;
   employee
  ----------
   Joe
  (1 строка)
Task:
Самая высокая зарплата в отделе
Table: Employee
+--------------+---------+
| Column Name | Type  |
+--------------+---------+
| id     | int   |
| name     | varchar |
| salary   | int   |
| departmentId | int   |
+--------------+---------+
Table: Department
+-------------+---------+
| Column Name | Type  |
+-------------+---------+
| id     | int   |
| name    | varchar |
+-------------+---------+
Напишите SQL-запрос, чтобы найти сотрудников с самой высокой зарплатой в каждом из отделов.
Верните таблицу результатов в любом порядке.
# Написание Sql запросов.
Decision:
postgres=# DROP TABLE IF EXISTS Employee;
TE TABLE Employee(
  Id INT,
  Name VARCHAR,
  Salary INT,
  DepartmentId INT
);
  DROP TABLE IF EXISTS DROP TABLE
postgres=# CREATE TABLE Employee(
postgres(#   Id INT,
postgres(#   Name VARCHAR,
postgres(#   Salary INT,
postgres(#   DepartmentId INT
postgres(# );
CREATE TABLE Department(
  Id Int,
  Name VARCHAR
);
  INSERT INCREATE TABLE
postgres=# DROP TABLE IF EXISTS Department;
  DROP TABLE
postgres=# CREATE TABLE Department(
postgres(#   Id Int,
postgres(#   Name VARCHAR
postgres(# );
  CREATE TABLE
postgres=# INSERT INTO Employee(Id, Name, Salary, DepartmentId) VALUES(1, 'Joe', 70000, 1);
  ERT INSERT 0 1
postgres=# INSERT INTO Employee(Id, Name, Salary, DepartmentId) VALUES(2, 'Jim', 90000, 1);
  NSERINSERT 0 1
postgres=# INSERT INTO Employee(Id, Name, Salary, DepartmentId) VALUES(3, 'Henry', 80000, 2);
  O EmplINSERT 0 1
postgres=# INSERT INTO Employee(Id, Name, Salary, DepartmentId) VALUES(4, 'Sam', 60000, 2);
  INSERT 0 1
postgres=# INSERT INTO Employee(Id, Name, Salary, DepartmentId) VALUES(5, 'Max', 90000, 1);
  NSERINSERT 0 1
postgres=# INSERT INTO Department(Id, Name) VALUES (1, 'IT');
  INSERT INTO DepartmINSERT 0 1
postgres=# INSERT INTO Department(Id, Name) VALUES (2, 'Sales');
  INSERT 0 1
postgres=# SELECT * FROM Employee;
   id | name | salary | departmentid
  ----+-------+--------+--------------
   1 | Joe | 70000 |      1
   2 | Jim | 90000 |      1
   3 | Henry | 80000 |      2
   4 | Sam | 60000 |      2
   5 | Max | 90000 |      1
  (5 строк)
postgres=# SELECT * FROM Department;
   id | name
  ----+-------
   1 | IT
   2 | Sales
  (2 строки)
postgres=# SELECT MAX(salary), departmentid FROM Employee GROUP BY departmentid;
   max | departmentid
  -------+--------------
   80000 |      2
   90000 |      1
  (2 строки)
postgres=# SELECT d.name, m.max_salary
FROM Department AS d
JOIN (SELECT MAX(salary) AS max_salary, departmentid FROM Employee GROUP BY departmentid) AS m
ON d.id=m.departmentid;
   name | max_salary
  -------+------------
   IT  |   90000
   Sales |   80000
  (2 строки)
postgres=# SELECT d.name, e.name, m.max_salary
postgres-# FROM Department AS d
postgres-# JOIN (SELECT MAX(salary) AS max_salary, departmentid FROM Employee GROUP BY departmentid) AS m
postgres-# ON d.id=m.departmentid
postgres-# JOIN Employee AS e
postgres-# ON e.salary=m.max_salary;
   name | name | max_salary
  -------+-------+------------
   Sales | Henry |   80000
   IT  | Jim |   90000
   IT  | Max |   90000
  (3 строки)
postgres=# SELECT d.name AS Department, e.name AS Employee, m.max_salary AS Salary
postgres-# FROM Department AS d
IN (Spostgres-# JOIN (SELECT MAX(salary) AS max_salary, departmentid FROM EmploROUP BY departmentid) AS m
postgres-# ON d.id=m.departmentid
postgres-# JOIN Employee AS e
postgres-# ON e.salary=m.max_salary;
   department | employee | salary
  ------------+----------+--------
   Sales   | Henry  | 80000
   IT     | Jim   | 90000
   IT     | Max   | 90000
  (3 строки)
postgres=# SELECT d.name AS Department, e.name AS Employee, m.max_salary AS Salary
postgres-# FROM Department AS d
postgres-# JOIN (SELECT MAX(salary) AS max_salary, departmentid FROM Employee GROUP BY departmentid) AS m
postgres-# ON d.id=m.departmentid
postgres-# JOIN Employee AS e
postgres-# ON e.salary=m.max_salary AND e.departmentid=m.departmentid;
   department | employee | salary
  ------------+----------+--------
   IT     | Max   | 90000
   IT     | Jim   | 90000
   Sales   | Henry  | 80000
  (3 строки)
Source:
# https://www.asozykin.ru/?ysclid=lk9eaatbqj18673257