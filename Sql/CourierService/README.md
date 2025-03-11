Services:
# Разработка баз данных.
# Написание Sql запросов.
Task:
База данных "Курьерская служба".
There is a company delivering orders - a Courier Service.
The order table contains information about the order that the courier will deliver.
FIO –recipient's full name;
address – delivery address;
courier – code of the employee who delivered the shipment, null by default;
price –delivery cost;
The order tracking trace table contains the history of various order statuses.
state – order status code: 1 – new; 2– accepted at the warehouse; 3– delivered; 4–not delivered
datetime– date and time of the status;
The courier table contains information about employees (couriers and managers).
FIO – Full name of the courier
manager – the courier contains the manager code, null by default
Выведите все доставленные заказы, которые не были приняты на склад.
# Разработка Баз данных.
Decision:
# sudo -i -u postgres
[postgres@i6 ~]$ psql
postgres=# CREATE DATABASE CourierService;
CREATE DATABASE
postgres=# \c courierservice
Вы подключены к базе данных "courierservice" как пользователь "postgres".
courierservice=# CREATE TABLE employees (
id SERIAL PRIMARY KEY,
manager_id INT REFERENCES employees(id),
full_name VARCHAR,
address VARCHAR,
phone VARCHAR,
hired_at TIMESTAMP,
fired_at TIMESTAMP
);
CREATE TABLE
courierservice=# CREATE TABLE order_states (
id SERIAL PRIMARY KEY,
state VARCHAR
);
CREATE TABLE
courierservice=# CREATE TABLE orders (
id SERIAL PRIMARY KEY,
customer VARCHAR,
address VARCHAR,
courier_id INT REFERENCES employees(id),
price NUMERIC
);
CREATE TABLE
courierservice=# CREATE TABLE trace (
id BIGSERIAL PRIMARY KEY,
state_id INT REFERENCES order_states(id),
order_id INT REFERENCES orders(id),
updated_at TIMESTAMP
);
CREATE TABLE
courierservice=# INSERT INTO employees (manager_id, full_name, address, phone, hired_at, fired_at)
VALUES ('1', 'Иванов Иван Иванович', 'Невский проспект, 11', '+790865454', '2022-05-04 12:10:57', '2022-05-006 13:10:57'),
('2', 'Иванова Анна Ивановна', 'Набережная реки Мойки, 48', '+790865454', '2022-05-04 12:10:57', '2022-05-006 13:10:57');
INSERT 0 2
courierservice=# SELECT * FROM employees;
id | manager_id |   full_name   |     address     | phone  |   hired_at   |   fired_at  
----+------------+-----------------------+---------------------------+------------+---------------------+---------------------
1 |     1 | Иванов Иван Иванович | Невский проспект, 11   | +790865454 | 2022-05-04 12:10:57 | 2022-05-06 13:10:57
2 |     2 | Иванова Анна Ивановна | Набережная реки Мойки, 48 | +790865454 | 2022-05-04 12:10:57 | 2022-05-06 13:10:57
(2 строки)
courierservice=# INSERT INTO order_states (state)
VALUES ('новый'),
('в доставке'),
('доставлен'),
('отменен');
INSERT 0 4
courierservice=# SELECT * FROM order_states;
id | state  
----+------------
1 | новый
2 | в доставке
3 | доставлен
4 | отменен
(4 строки)
courierservice=# INSERT INTO orders (customer, address, courier_id, price)
VALUES ('Иванов Алесандр Иванович', 'Баумана, 121', '2', '150'),
('Иванов Андрей Иванович', 'Ленина, 122', '2', '200'),
('Иванов Михаил Иванович', 'Ленина, 122', '1', '150');
INSERT 0 3
courierservice=# SELECT * FROM orders;
id |     customer     | address  | courier_id | price
----+--------------------------+--------------+------------+-------
1 | Иванов Алесандр Иванович | Баумана, 121 |     2 | 150
2 | Иванов Андрей Иванович | Ленина, 122 |     2 | 200
3 | Иванов Михаил Иванович | Ленина, 122 |     1 | 150
(3 строки)
courierservice=# INSERT INTO trace (state_id, order_id, updated_at)
VALUES ('4', '3', '2022-06-06 13:20:57'),
('2', '2', '2022-07-07 13:20:58'),
('3', '1', '2022-05-05 14:02:07');
INSERT 0 3
courierservice=# INSERT INTO trace (state_id, order_id, updated_at)
VALUES ('4', '3', '2022-06-06 13:20:57'),
('4', '3', '2022-07-05 13:25:28'),
('1', '3', '2022-06-05 14:01:07');
INSERT 0 3
courierservice=# SELECT * FROM trace;
id | state_id | order_id |   updated_at  
----+----------+----------+---------------------
1 |    4 |    3 | 2022-06-06 13:20:57
2 |    2 |    2 | 2022-07-07 13:20:58
3 |    3 |    1 | 2022-05-05 14:02:07
4 |    4 |    3 | 2022-06-06 13:20:57
5 |    4 |    3 | 2022-07-05 13:25:28
6 |    1 |    3 | 2022-06-05 14:01:07
(6 строк)
courierservice=# SELECT * FROM order_states;
id | state  
----+------------
1 | новый
2 | в доставке
3 | доставлен
4 | отменен
(4 строки)
courierservice=# SELECT * FROM orders;
id |     customer     | address  | courier_id | price
----+--------------------------+--------------+------------+-------
1 | Иванов Алесандр Иванович | Баумана, 121 |     2 | 150
2 | Иванов Андрей Иванович | Ленина, 122 |     2 | 200
3 | Иванов Михаил Иванович | Ленина, 122 |     1 | 150
(3 строки)
courierservice=# SELECT * FROM trace;
id | state_id | order_id |   updated_at  
----+----------+----------+---------------------
1 |    4 |    3 | 2022-06-06 13:20:57
2 |    2 |    2 | 2022-07-07 13:20:58
3 |    3 |    1 | 2022-05-05 14:02:07
(3 строки)
courierservice=# SELECT orders.*
FROM orders
JOIN trace t ON t.order_id=orders.id AND t.state_id=3
LEFT JOIN trace t2 ON t2.order_id=orders.id AND t2.state_id=2
WHERE t2.id IS NULL;
id |     customer     | address  | courier_id | price
----+--------------------------+--------------+------------+-------
1 | Иванов Алесандр Иванович | Баумана, 121 |     2 | 150
(1 строка)
Task:
Выведите курьеров доставивших больше заказов, чем их менеджеры.
# Написание Sql запросов.
Decision:
courierservice=# SELECT * FROM employees;
id | manager_id |   full_name   |     address     | phone  |   hired_at   |   fired_at  
----+------------+-----------------------+---------------------------+------------+---------------------+---------------------
1 |     1 | Иванов Иван Иванович | Невский проспект, 11   | +790865454 | 2022-05-04 12:10:57 | 2022-05-06 13:10:57
2 |     2 | Иванова Анна Ивановна | Набережная реки Мойки, 48 | +790865454 | 2022-05-04 12:10:57 | 2022-05-06 13:10:57
(2 строки)
courierservice=# SELECT * FROM orders;
id |     customer     | address  | courier_id | price
----+--------------------------+--------------+------------+-------
1 | Иванов Алесандр Иванович | Баумана, 121 |     2 | 150
2 | Иванов Андрей Иванович | Ленина, 122 |     2 | 200
3 | Иванов Михаил Иванович | Ленина, 122 |     1 | 150
(3 строки)
courierservice=# SELECT * FROM trace;
id | state_id | order_id |   updated_at  
----+----------+----------+---------------------
1 |    4 |    3 | 2022-06-06 13:20:57
2 |    2 |    2 | 2022-07-07 13:20:58
3 |    3 |    1 | 2022-05-05 14:02:07
(3 строки)
courierservice=# SELECT k.*
FROM employees k
WHERE k.manager_id
IS NOT NULL AND
(SELECT COUNT(*)
  FROM orders
  WHERE courier_id=k.id) >
(SELECT COUNT(*)
  FROM orders
  WHERE courier_id=k.manager_id);
Task:
Выведите менеджеров и стоимость всех доставленных их курьерами заказов, за последний месяц.
# Написание Sql запросов.
Decision:
courierservice=# SELECT * FROM trace;
id | state_id | order_id |   updated_at  
----+----------+----------+---------------------
1 |    4 |    3 | 2022-06-06 13:20:57
2 |    2 |    2 | 2022-07-07 13:20:58
3 |    3 |    1 | 2022-05-05 14:02:07
(3 строки)
courierservice=# SELECT * FROM orders;
id |     customer     | address  | courier_id | price
----+--------------------------+--------------+------------+-------
1 | Иванов Алесандр Иванович | Баумана, 121 |     2 | 150
2 | Иванов Андрей Иванович | Ленина, 122 |     2 | 200
3 | Иванов Михаил Иванович | Ленина, 122 |     1 | 150
(3 строки)
courierservice=# SELECT * FROM employees;
id | manager_id |   full_name   |     address     | phone  |   hired_at   |   fired_at  
----+------------+-----------------------+---------------------------+------------+---------------------+---------------------
1 |     1 | Иванов Иван Иванович | Невский проспект, 11   | +790865454 | 2022-05-04 12:10:57 | 2022-05-06 13:10:57
2 |     2 | Иванова Анна Ивановна | Набережная реки Мойки, 48 | +790865454 | 2022-05-04 12:10:57 | 2022-05-06 13:10:57
(2 строки)
courierservice=# SELECT k2.*, SUM(o.price) AS price
FROM trace t
JOIN orders o ON o.id=t.order_id
JOIN employees k ON k.id=o.courier_id
JOIN employees k2 ON k2.id=k.manager_id
WHERE t.state_id = 3 AND
  t.updated_at>date_sub(current_date(), INTERVAL 1 MONTH)
GROUP BY k2.id;
Task:
Выведите менеджеров, у которых не более трех курьеров.
# Написание Sql запросов.
Decision:
courierservice=# SELECT k.*, COUNT(k2.id)
FROM employees k
LEFT JOIN employees k2 ON k2.manager_id = k.id
WHERE k.manager_id IS NULL
GROUP BY k.id
HAVING COUNT(k2.id) < 4;
Task:
Выведите заказы и последний установленный у него статус. Оставить в отчете только статусы: новый и принят на склад.
# Написание Sql запросов.
Decision:
courierservice=# SELECT * FROM orders;
id |     customer     | address  | courier_id | price
----+--------------------------+--------------+------------+-------
1 | Иванов Алесандр Иванович | Баумана, 121 |     2 | 150
2 | Иванов Андрей Иванович | Ленина, 122 |     2 | 200
3 | Иванов Михаил Иванович | Ленина, 122 |     1 | 150
(3 строки)
courierservice=# SELECT * FROM trace;
id | state_id | order_id |   updated_at  
----+----------+----------+---------------------
1 |    4 |    3 | 2022-06-06 13:20:57
2 |    2 |    2 | 2022-07-07 13:20:58
3 |    3 |    1 | 2022-05-05 14:02:07
(3 строки)
courierservice=# SELECT o.*,
  (SELECT state_id
  FROM trace WHERE order_id=o.id
  ORDER BY updated_at DESC LIMIT 1) AS status
FROM orders o
HAVING status IN (1, 2);
Source:
# https://www.asozykin.ru/?ysclid=lk9eaatbqj18673257