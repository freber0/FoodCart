CREATE DATABASE IF NOT EXISTS FoodCart;
use FoodCart
DROP TABLE IF EXISTS products;
CREATE TABLE products(product_id integer, class_name varchar(20), name varchar(25), price float, image varchar(125));
