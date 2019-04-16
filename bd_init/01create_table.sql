CREATE DATABASE IF NOT EXISTS FoodCart;
use FoodCart

DROP TABLE IF EXISTS user;
CREATE TABLE user(username VARCHAR(20) NOT NULL UNIQUE, password VARCHAR(100) NOT NULL, lastname VARCHAR(20) NOT NULL, firstname VARCHAR(20) NOT NULL, email VARCHAR(40) NOT NULL, address VARCHAR(80) NOT NULL, PRIMARY KEY (username));

DROP TABLE IF EXISTS products;
CREATE TABLE products(product_id integer NOT NULL UNIQUE , class_name varchar(20) NOT NULL, name varchar(25) NOT NULL, price float NOT NULL, image varchar(130) NOT NULL, PRIMARY KEY (product_id), INDEX USING BTREE (class_name));

DROP TABLE IF EXISTS orders;
CREATE TABLE orders(orderId varchar(100) NOT NULL UNIQUE, purchasedDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, username varchar(20) NOT NULL, PRIMARY KEY (orderId), FOREIGN KEY(username) REFERENCES user(username));

DROP TABLE IF EXISTS orderItem;
CREATE TABLE orderItem(productId integer NOT NULL, orderId varchar(40) NOT NULL, quantity integer NOT NULL, FOREIGN KEY(productId) REFERENCES products(product_id), FOREIGN KEY(orderId) REFERENCES orders(orderId));

CREATE USER 'apptester' IDENTIFIED by '1234';
GRANT SELECT ON FoodCart.* TO'apptester';
GRANT UPDATE,INSERT ON FoodCart.user TO 'apptester';
GRANT INSERT ON FoodCart.orders TO 'apptester';
GRANT INSERT ON FoodCart.orderItem To 'apptester';
