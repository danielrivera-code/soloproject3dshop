-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema solo_project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema solo_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `solo_project` DEFAULT CHARACTER SET utf8 ;
USE `solo_project` ;

-- -----------------------------------------------------
-- Table `solo_project`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `solo_project`.`users` ;

CREATE TABLE IF NOT EXISTS `solo_project`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `solo_project`.`products`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `solo_project`.`products` ;

CREATE TABLE IF NOT EXISTS `solo_project`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `product_name` TEXT NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `link_to_image` VARCHAR(255) NOT NULL,
  `product_price` VARCHAR(50) NOT NULL,
  `product_available` VARCHAR(50) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `posted_id` INT NOT NULL,
  `product_creator_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_rides_users_idx` (`posted_id` ASC) VISIBLE,
  INDEX `fk_rides_users1_idx` (`product_creator_id` ASC) VISIBLE,
  CONSTRAINT `fk_rides_users`
    FOREIGN KEY (`posted_id`)
    REFERENCES `solo_project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_rides_users1`
    FOREIGN KEY (`product_creator_id`)
    REFERENCES `solo_project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `solo_project`.`listings`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `solo_project`.`listings` ;

CREATE TABLE IF NOT EXISTS `solo_project`.`listings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `product_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_rides1_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_rides1`
    FOREIGN KEY (`product_id`)
    REFERENCES `solo_project`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
