USE FoodCart
DROP PROCEDURE IF EXISTS FindPriceForItem;
DELIMITER //
CREATE PROCEDURE FindPriceForItem (IN searched_product_id integer,OUT searched_price float)
BEGIN
  SELECT price
  INTO searched_price
  FROM products
  WHERE product_id = searched_product_id;
END //
DELIMITER ;


