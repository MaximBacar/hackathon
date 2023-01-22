DROP DATABASE IF EXISTS `cob`;
CREATE DATABASE `cob`;
USE `cob`




CREATE TABLE `accounts` (
    `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `email` varchar(255) NOT NULL UNIQUE,
    `firstName` varchar(64) NOT NULL,
    `lastName` varchar(64) NOT NULL,
    `password` varchar(255) NOT NULL
)

CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

CREATE TABLE `transactions`(
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `gross_price` FLOAT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `date_time` DATETIME NOT NULL,
    `location`  VARCHAR(255)
)

CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

CREATE TABLE `subscritptions`(
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `service_name` VARCHAR(255) NOT NULL,
    `gross_price` FLOAT NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE,
    `pay_period` INT NOT NULL
)

CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

CREATE TABLE `income`(
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `net_income` FLOAT NOT NULL,
    `pay_period` INT NOT NULL
)

CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

INSERT INTO `accounts` VALUES (0,"maximbacar@hotmail.ca", "Maxim", "Bacar", "11ba65852271cd24c56c865a9635b90616326949ff2bf6cd07eacaf788bad320");


INSERT INTO `transactions` VALUES (0, 1, 34.32, "DOLLARAMA", "2022-01-04 17:24:19", "Montreal, QC");
INSERT INTO `transactions` VALUES (0, 1, 19.00, "TIM HORTONS", "2023-01-04 17:24:19", "Montreal, QC");
INSERT INTO `transactions` VALUES (0, 1, 4.32, "DEP", "2021-01-04 17:24:19", "Montreal, QC");



SELECT * FROM `accounts`;

SELECT * FROM `transactions`;

