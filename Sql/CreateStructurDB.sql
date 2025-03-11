/*
Создайте структуру базы данных по одной из предложенных тематик.
К базе данных предъявляются следующие требования:
1. должно быть не менее 4 сущностей (включая технические объекты);
2. должна быть хотя бы одна связь один-ко-многим
3. должна быть хотя бы одна связь многие-ко-многим;
4. все отношения приведены к 3НФ.
Предметная область:
1. Продажа автомобилей.
2. Приют для животных.
3. Железнодорожные перевозки.
4. Служба доставки.
5. Организация марафона.
Требования к оформлению:
ER-диаграмму необходимо составлять на app.dbdesigner.net, на проверку нужно присылать ссылку на диаграмму. Также необходимо сделать таблицу в Google Sheets с примерами данных в таблицах.
Возьмите в работу ER-диаграмму, разработанную вами. Разработайте DDL для нее. Создайте файл Sql-Ddl2.sql, в котором должно быть:
1. DDL создания всех таблиц, с правильным указанием имен, типов и ограничений целостности.
2. Для каждой таблицы приведите 2-3 команды INSERT для наполнения данных. Обращайте внимание на типизацию вставляемых данны
*/
/*CREATE TABLE de13ma.gabn_dz2_brands (
id_brand SERIAL PRIMARY KEY,
title VARCHAR (255)
);*/
/*INSERT INTO de13ma.gabn_dz2_brands (title) VALUES 
('Nissan'),
('Chevrolet'),
('Datsun'),
('Hyundai'),
('Lada');*/
/*CREATE TABLE de13ma.gabn_dz2_transmittion_box (
id_box SERIAL PRIMARY KEY,
title VARCHAR (255)
);
INSERT INTO de13ma.gabn_dz2_transmittion_box (title) VALUES 
('Автомат'),
('Механика'),
('Вариатор');*/
/*CREATE TABLE de13ma.gabn_dz2_country_partner (
id_country SERIAL PRIMARY KEY,
title VARCHAR (255)
);
INSERT INTO de13ma.gabn_dz2_country_partner (title) VALUES 
('Russia'),
('Japane'),
('USA'),
('South Korea');*/
/*CREATE TABLE de13ma.gabn_dz2_clients (
id_client SERIAL PRIMARY KEY,
fio VARCHAR (255),
phone VARCHAR (255),
city VARCHAR (255)
);
INSERT INTO de13ma.gabn_dz2_clients 
(fio, phone, city) 
VALUES 
('David', '88886666000', 'Kutaisi'),
('Angelina', '88880000665', 'Irkutsk'),
('Leonid', '88886666111', 'Irkutsk');*/
/*CREATE TABLE de13ma.gabn_dz2_cars (
id_car SERIAL PRIMARY KEY,
id_brand INT REFERENCES de13ma.gabn_dz2_brands(id_brand),
model VARCHAR (255),
price NUMERIC,
releases TIMESTAMP,
id_box INT REFERENCES de13ma.gabn_dz2_transmittion_box(id_box),
id_country INT REFERENCES de13ma.gabn_dz2_country_partner(id_country)
);
INSERT INTO de13ma.gabn_dz2_cars (id_brand, model, price, releases, id_box, id_country) VALUES 
(1, 'Windgroad', 250000, '2006-09-12 12:12:12', 1, 2),
(2, 'Aveo', 450000, '2013-09-12 12:12:12', 3, 3),
(3, 'On-do', 300000, '2015-09-12 12:12:12', 2, 2),
(4, 'Solaris1', 750000, '2017-09-12 12:12:12', 1, 4),
(4, 'Solaris2', 900000, '2020-09-12 12:12:12', 1, 4),
(5, 'Vesta', 850000, '2021-09-12 12:12:12', 3, 1);*/
/*CREATE TABLE de13ma.gabn_dz2_sale (
id_sale SERIAL PRIMARY KEY,
id_car INT REFERENCES de13ma.gabn_dz2_cars(id_car),
id_client INT REFERENCES de13ma.gabn_dz2_clients(id_client),
dates TIMESTAMP
);
INSERT INTO de13ma.gabn_dz2_sale (id_car, id_client, dates) VALUES 
(1, 1, '2006-09-12 12:12:12'),
(2, 2, '2014-09-12 12:12:12'),
(3, 1, '2015-09-12 12:12:12'),
(4, 2, '2017-09-12 12:12:12'),
(5, 3, '2020-09-12 12:12:12'),
(6, 1, '2021-09-12 12:12:12');*/
SELECT * from de13ma.gabn_dz2_sale;