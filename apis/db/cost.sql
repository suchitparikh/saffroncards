DROP TABLE IF EXISTS `cost`;

CREATE TABLE `cost` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `card_part` varchar(255) DEFAULT NULL,
  `cost` decimal(5,2) NOT NULL DEFAULT 0.0,
  PRIMARY KEY(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
