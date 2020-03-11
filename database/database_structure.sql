CREATE DATABASE  IF NOT EXISTS `stock` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `stock`;
-- MySQL dump 10.13  Distrib 5.7.18, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: stock
-- ------------------------------------------------------
-- Server version	5.7.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `KOSDAQ`
--

DROP TABLE IF EXISTS `KOSDAQ`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `KOSDAQ` (
  `saved_date` datetime NOT NULL,
  `price` varchar(25) NOT NULL,
  `fluc_rate` float NOT NULL,
  `fluc_price` float NOT NULL,
  PRIMARY KEY (`saved_date`),
  UNIQUE KEY `KOSDAQ_saved_date_uindex` (`saved_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `KOSPI`
--

DROP TABLE IF EXISTS `KOSPI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `KOSPI` (
  `saved_date` datetime NOT NULL,
  `price` varchar(25) NOT NULL,
  `fluc_rate` float NOT NULL,
  `fluc_price` float NOT NULL,
  PRIMARY KEY (`saved_date`),
  UNIQUE KEY `KOSPI_saved_date_uindex` (`saved_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `KOSPI200`
--

DROP TABLE IF EXISTS `KOSPI200`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `KOSPI200` (
  `saved_date` datetime NOT NULL,
  `price` varchar(25) NOT NULL,
  `fluc_rate` float NOT NULL,
  `fluc_price` float NOT NULL,
  PRIMARY KEY (`saved_date`),
  UNIQUE KEY `KOSPI200_saved_date_uindex` (`saved_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-11 14:46:48
