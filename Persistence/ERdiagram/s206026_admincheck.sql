-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: mysql-db.caprover.diplomportal.dk    Database: s206026
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admincheck`
--

DROP TABLE IF EXISTS `admincheck`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admincheck` (
  `courseID` mediumint DEFAULT NULL,
  `course` varchar(40) DEFAULT NULL,
  `room` varchar(40) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `timefrom` varchar(5) DEFAULT NULL,
  `timeuntil` varchar(5) DEFAULT NULL,
  `zoom` tinyint(1) DEFAULT NULL,
  `reqID` mediumint NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`reqID`)
) ENGINE=InnoDB AUTO_INCREMENT=174 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admincheck`
--

LOCK TABLES `admincheck` WRITE;
/*!40000 ALTER TABLE `admincheck` DISABLE KEYS */;
INSERT INTO `admincheck` VALUES (100,'Pathology.SAU','Jerne Aud.','2022-05-02','10:00','14:00',NULL,168),(100,'Pathology.SAU','Ejner Aud.','2022-05-02','12:00','16:00',NULL,169),(101,'System dev.ex','HCO-A111','2022-05-02','12:00','16:00',NULL,170),(102,'System dev.cl','Lille UP','2022-05-02','15:00','17:00',NULL,171),(103,'SSKS','DTUB-X2.70','2022-05-21','15:00','17:00',NULL,172),(104,'Pathology.caf','Panum 21.2.26','2022-05-21','09:00','13:00',NULL,173);
/*!40000 ALTER TABLE `admincheck` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-26  8:35:47
