CREATE TABLE IF NOT EXISTS `ngram_1`(
   `ngram1_id` INT UNSIGNED AUTO_INCREMENT,
   `ngram1_word` VARCHAR(100) NOT NULL,
   `ngram1_possibility` DOUBLE NOT NULL,
   `punishment` DOUBLE,
   PRIMARY KEY ( `ngram1_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `ngram_2`(
   `ngram2_id` INT UNSIGNED AUTO_INCREMENT,
   `ngram2_under_word` VARCHAR(100) NOT NULL,
   `ngram2_after_word` VARCHAR(100) NOT NULL,
   `ngram2_possibility` DOUBLE NOT NULL,
   `punishment` DOUBLE,
   PRIMARY KEY ( `ngram2_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `ngram_3`(
   `ngram3_id` INT UNSIGNED AUTO_INCREMENT,
   `ngram3_under_word` VARCHAR(100) NOT NULL,
   `ngram3_after_word` VARCHAR(100) NOT NULL,
   `ngram3_possibility` DOUBLE NOT NULL,
   `punishment` DOUBLE,
   PRIMARY KEY ( `ngram3_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;