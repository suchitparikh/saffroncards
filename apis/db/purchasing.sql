DROP TABLE IF EXISTS `purchase`;

CREATE TABLE `purchase` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `purchased_on` datetime DEFAULT NULL,
  `store` varchar(255) DEFAULT NULL,
  `item` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `units` int(3) NOT NULL,
  `pieces_per_unit` int(4) NOT NULL,
  `unit_price` decimal(5,2) NOT NULL,
  `discount` decimal(5,2) NOT NULL DEFAULT 0.0,
  `discount_type` tinyint(1) NOT NULL DEFAULT 0,
  `shipping` decimal(5,2) NOT NULL DEFAULT 0.0,
  `tax` decimal(4,2) NOT NULL DEFAULT 0.0,
  `total_cost` decimal(5,2) DEFAULT NULL,
  `unit_cost` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
