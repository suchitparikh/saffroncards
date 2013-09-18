-- category table
DROP TABLE IF EXISTS `card_category`;

CREATE TABLE `card_category` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `category` varchar(50) DEFAULT NULL,
  `code` varchar(2) DEFAULT NULL,
  PRIMARY KEY(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `inventory`;

CREATE TABLE `inventory` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `category_id` int(3) NOT NULL DEFAULT 0,
  `other_categories_id` varchar(25) NOT NULL DEFAULT '[0]',
  `cost` decimal(5,2) NOT NULL DEFAULT 0.0,
  `suggested_selling_price` decimal(5,2) NOT NULL DEFAULT 4.25,
  `minimum_selling_price` decimal(5,2) NOT NULL DEFAULT 3.0,
  `available` int(3) NOT NULL DEFAULT 1,
  `sold` int(3) NOT NULL DEFAULT 0,
  KEY `card_category_id` (`category_id`),
  CONSTRAINT `card_category_id` FOREIGN KEY(`category_id`) REFERENCES `card_category` (`id`),
  PRIMARY KEY(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
