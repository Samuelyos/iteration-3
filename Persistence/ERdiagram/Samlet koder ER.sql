-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema s206026
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema s206026
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `s206026` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `s206026` ;

-- -----------------------------------------------------
-- Table `s206026`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `s206026`.`admin` (
  `firstName` VARCHAR(40) NULL DEFAULT NULL,
  `lastName` VARCHAR(40) NULL DEFAULT NULL,
  `employeeID` VARCHAR(40) NULL DEFAULT NULL,
  `adminID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`adminID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `s206026`.`classrooms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `s206026`.`classrooms` (
  `building` VARCHAR(25) NULL DEFAULT NULL,
  `floor` VARCHAR(10) NULL DEFAULT NULL,
  `roomNr` VARCHAR(14) NULL DEFAULT NULL,
  `capacity` INT NULL DEFAULT NULL,
  `address` VARCHAR(50) NULL DEFAULT NULL,
  `classroomsID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`classroomsID`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `s206026`.`lectures`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `s206026`.`lectures` (
  `courseID` MEDIUMINT NOT NULL AUTO_INCREMENT,
  `course` VARCHAR(40) NULL DEFAULT NULL,
  `room` VARCHAR(40) NULL DEFAULT NULL,
  `date` DATE NULL DEFAULT NULL,
  `timefrom` VARCHAR(5) NULL DEFAULT NULL,
  `timeuntil` VARCHAR(5) NULL DEFAULT NULL,
  `zoom` TINYINT(1) NULL DEFAULT NULL,
  `classrooms_classroomsID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`courseID`, `classrooms_classroomsID`),
  INDEX `fk_lectures_classrooms1_idx` (`classrooms_classroomsID` ASC) VISIBLE,
  CONSTRAINT `fk_lectures_classrooms1`
    FOREIGN KEY (`classrooms_classroomsID`)
    REFERENCES `s206026`.`classrooms` (`classroomsID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 105
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `s206026`.`courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `s206026`.`courses` (
  `courseID` MEDIUMINT NOT NULL AUTO_INCREMENT,
  `courseName` VARCHAR(40) NULL DEFAULT NULL,
  `courseLeaderID` VARCHAR(40) NULL DEFAULT NULL,
  `faculty` VARCHAR(40) NULL DEFAULT NULL,
  `lectures_courseID` MEDIUMINT NOT NULL,
  `lectures_classrooms_classroomsID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`courseID`, `lectures_courseID`, `lectures_classrooms_classroomsID`),
  INDEX `fk_courses_lectures1_idx` (`lectures_courseID` ASC, `lectures_classrooms_classroomsID` ASC) VISIBLE,
  CONSTRAINT `fk_courses_lectures1`
    FOREIGN KEY (`lectures_courseID` , `lectures_classrooms_classroomsID`)
    REFERENCES `s206026`.`lectures` (`courseID` , `classrooms_classroomsID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 20000
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `s206026`.`courseLeader`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `s206026`.`courseLeader` (
  `firstName` VARCHAR(40) NULL DEFAULT NULL,
  `lastName` VARCHAR(40) NULL DEFAULT NULL,
  `employeeID` VARCHAR(40) NULL DEFAULT NULL,
  `courseLeaderID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `courses_courseID` MEDIUMINT NOT NULL,
  `courses_lectures_courseID` MEDIUMINT NOT NULL,
  `courses_lectures_classrooms_classroomsID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`courseLeaderID`, `courses_courseID`, `courses_lectures_courseID`, `courses_lectures_classrooms_classroomsID`),
  INDEX `fk_courseLeader_courses1_idx` (`courses_courseID` ASC, `courses_lectures_courseID` ASC, `courses_lectures_classrooms_classroomsID` ASC) VISIBLE,
  CONSTRAINT `fk_courseLeader_courses1`
    FOREIGN KEY (`courses_courseID` , `courses_lectures_courseID` , `courses_lectures_classrooms_classroomsID`)
    REFERENCES `s206026`.`courses` (`courseID` , `lectures_courseID` , `lectures_classrooms_classroomsID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `s206026`.`Persons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `s206026`.`Persons` (
  `firstName` VARCHAR(40) NULL DEFAULT NULL,
  `lastName` VARCHAR(40) NULL DEFAULT NULL,
  `employeeID` VARCHAR(40) NULL DEFAULT NULL,
  `role` VARCHAR(15) NULL DEFAULT NULL,
  `PersonID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `admin_adminID` INT UNSIGNED NOT NULL,
  `courseLeader_courseLeaderID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`PersonID`, `admin_adminID`, `courseLeader_courseLeaderID`),
  INDEX `fk_Persons_admin1_idx` (`admin_adminID` ASC) VISIBLE,
  INDEX `fk_Persons_courseLeader1_idx` (`courseLeader_courseLeaderID` ASC) VISIBLE,
  CONSTRAINT `fk_Persons_admin1`
    FOREIGN KEY (`admin_adminID`)
    REFERENCES `s206026`.`admin` (`adminID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Persons_courseLeader1`
    FOREIGN KEY (`courseLeader_courseLeaderID`)
    REFERENCES `s206026`.`courseLeader` (`courseLeaderID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `s206026`.`Login`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `s206026`.`Login` (
  `ID` VARCHAR(6) NULL DEFAULT NULL,
  `role` VARCHAR(40) NULL DEFAULT NULL,
  `password` VARCHAR(40) NULL DEFAULT NULL,
  `LoginID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Persons_PersonID` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`LoginID`, `Persons_PersonID`),
  INDEX `fk_Login_Persons1_idx` (`Persons_PersonID` ASC) VISIBLE,
  CONSTRAINT `fk_Login_Persons1`
    FOREIGN KEY (`Persons_PersonID`)
    REFERENCES `s206026`.`Persons` (`PersonID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `s206026`.`admincheck`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `s206026`.`admincheck` (
  `courseID` MEDIUMINT NULL DEFAULT NULL,
  `course` VARCHAR(40) NULL DEFAULT NULL,
  `room` VARCHAR(40) NULL DEFAULT NULL,
  `date` DATE NULL DEFAULT NULL,
  `timefrom` VARCHAR(5) NULL DEFAULT NULL,
  `timeuntil` VARCHAR(5) NULL DEFAULT NULL,
  `zoom` TINYINT(1) NULL DEFAULT NULL,
  `reqID` MEDIUMINT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`reqID`))
ENGINE = InnoDB
AUTO_INCREMENT = 166
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `s206026`.`admin_has_admincheck`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `s206026`.`admin_has_admincheck` (
  `admin_adminID` INT UNSIGNED NOT NULL,
  `admincheck_reqID` MEDIUMINT NOT NULL,
  PRIMARY KEY (`admin_adminID`, `admincheck_reqID`),
  INDEX `fk_admin_has_admincheck_admincheck1_idx` (`admincheck_reqID` ASC) VISIBLE,
  INDEX `fk_admin_has_admincheck_admin1_idx` (`admin_adminID` ASC) VISIBLE,
  CONSTRAINT `fk_admin_has_admincheck_admin1`
    FOREIGN KEY (`admin_adminID`)
    REFERENCES `s206026`.`admin` (`adminID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_admin_has_admincheck_admincheck1`
    FOREIGN KEY (`admincheck_reqID`)
    REFERENCES `s206026`.`admincheck` (`reqID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
