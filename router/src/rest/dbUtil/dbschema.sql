-- MySQL Script generated by MySQL Workbench -- 09/28/16 01:26:13 -- Model: New Model Version: 1.0 -- MySQL Workbench Forward Engineering
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';
-- Schema router
DROP SCHEMA IF EXISTS router ;
-- Schema router
CREATE SCHEMA IF NOT EXISTS router DEFAULT CHARACTER SET utf8 ;
USE router ;
-- Table router.users
DROP TABLE IF EXISTS router.users ;
CREATE TABLE IF NOT EXISTS router.users(
	idusers INT NOT NULL AUTO_INCREMENT,
	username VARCHAR(45) NOT NULL,
	bio VARCHAR(400) NULL,
	pass VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL,
    privacy VARCHAR(40) NOT NULL,
	PRIMARY KEY (idusers),
	UNIQUE INDEX idusers_UNIQUE (idusers ASC),
	UNIQUE INDEX username_UNIQUE (username ASC)) ENGINE = InnoDB;
-- Table router.routes
DROP TABLE IF EXISTS router.routes ;
CREATE TABLE IF NOT EXISTS router.routes (
	idroutes INT NOT NULL AUTO_INCREMENT,
	route MEDIUMTEXT NOT NULL,
	startPointLat VARCHAR(10) NOT NULL,
	startPointLon VARCHAR(10) NOT NULL,
	userid VARCHAR(45) NOT NULL,
	routeName VARCHAR(64) NOT NULL,
	PRIMARY KEY (idroutes),
	UNIQUE INDEX idroutes_UNIQUE (idroutes ASC)) ENGINE = InnoDB;
-- Table router.comments
DROP TABLE IF EXISTS router.comments ;
CREATE TABLE IF NOT EXISTS router.comments (
	idcomments INT NOT NULL AUTO_INCREMENT,
	text VARCHAR(400) NOT NULL,
	userid VARCHAR(45) NOT NULL,
	timestamp TIMESTAMP,
	parent VARCHAR(45) NOT NULL,
	PRIMARY KEY (idcomments)) ENGINE = InnoDB;
-- Table router.friend
DROP TABLE IF EXISTS router.friend ;
CREATE TABLE IF NOT EXISTS router.friend(
	user_id INT NOT NULL,
	friend_id INT NOT NULL,
	PRIMARY KEY (user_id, friend_id)) ENGINE = InnoDB;
-- Table router.request
DROP TABLE IF EXISTS router.request ;
CREATE TABLE IF NOT EXISTS router.request(
	receiver_id INT NOT NULL,
	sender_id INT NOT NULL,
	PRIMARY KEY (receiver_id,sender_id)) ENGINE = InnoDB;
-- Table router.shared
DROP TABLE IF EXISTS router.shared;
CREATE TABLE IF NOT EXISTS router.shared(
	shared_id INT NOT NULL AUTO_INCREMENT,
	receiver_id INT NOT NULL,
	sender_id INT NOT NULL,
	route_name VARCHAR(64) NOT NULL,
	route MEDIUMTEXT NOT NULL,
	start_point_lat VARCHAR(10) NOT NULL,
	start_point_lon VARCHAR(10) NOT NULL,
	PRIMARY KEY (shared_id)) ENGINE = InnoDB;
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
