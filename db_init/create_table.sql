CREATE DATABASE IF NOT EXISTS FoodCart;
use FoodCart
DROP TABLE IF EXISTS products;
CREATE TABLE products(product_id integer, class_name varchar(20), name varchar(25), price float, image varchar(130));

DROP TABLE IF EXISTS orders;
CREATE TABLE orders(orderId varchar(100), purchasedDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, userId varchar(20));

DROP TABLE IF EXISTS orderItem;
CREATE TABLE orderItem(productId integer, orderId varchar(40), quantity integer);

DROP TABLE IF EXISTS user;
CREATE TABLE user(username VARCHAR(20), password VARCHAR(100), nom VARCHAR(20), prenom VARCHAR(20), email VARCHAR(40), address VARCHAR(40), PRIMARY KEY (username));
