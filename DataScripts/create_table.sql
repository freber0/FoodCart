CREATE DATABASE IF NOT EXISTS FoodCart;
use FoodCart;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS user;
CREATE TABLE products(product_id integer, class_name varchar(20), name varchar(25), price float, image varchar(130));
CREATE TABLE user(username VARCHAR(20), password VARCHAR(100), nom VARCHAR(20), prenom VARCHAR(20), email VARCHAR(40), adresse VARCHAR(40), PRIMARY KEY (username));