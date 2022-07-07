-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               10.4.24-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.0.0.6468
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table mini_project_db.flyway_schema_history
CREATE TABLE IF NOT EXISTS `flyway_schema_history` (
  `installed_rank` int(11) NOT NULL AUTO_INCREMENT,
  `version` varchar(50) DEFAULT '',
  `description` varchar(200) NOT NULL DEFAULT '',
  `type` varchar(20) NOT NULL DEFAULT '',
  `script` varchar(1000) NOT NULL DEFAULT '',
  `checksum` int(11) DEFAULT 0,
  `installed_by` varchar(100) NOT NULL DEFAULT '',
  `installed_on` timestamp NOT NULL DEFAULT current_timestamp(),
  `execution_time` int(11) NOT NULL DEFAULT 0,
  `success` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`installed_rank`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table mini_project_db.materi
CREATE TABLE IF NOT EXISTS `materi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` bigint(11) NOT NULL DEFAULT 0,
  `description` mediumtext DEFAULT '',
  `question_total` int(11) DEFAULT 0,
  `materi` varchar(255) NOT NULL DEFAULT '',
  `teacher` varchar(255) DEFAULT '',
  `question` mediumtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT '[]',
  `create_date` timestamp NULL DEFAULT current_timestamp(),
  `update_date` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table mini_project_db.question
CREATE TABLE IF NOT EXISTS `question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` text NOT NULL DEFAULT '',
  `question` varchar(255) NOT NULL DEFAULT '',
  `answer_true` varchar(255) NOT NULL DEFAULT '',
  `answer_list` varchar(255) NOT NULL DEFAULT '[]',
  `count_used` int(11) NOT NULL DEFAULT 0,
  `publish` tinyint(1) NOT NULL DEFAULT 0,
  `materi_id` bigint(25) NOT NULL DEFAULT 0,
  `school_id` bigint(25) NOT NULL DEFAULT 0,
  `create_date` timestamp NULL DEFAULT current_timestamp(),
  `update_date` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table mini_project_db.school
CREATE TABLE IF NOT EXISTS `school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `head_master` varchar(255) NOT NULL DEFAULT '',
  `phone_number` varchar(255) NOT NULL DEFAULT '',
  `name` varchar(255) NOT NULL DEFAULT '',
  `address` varchar(255) NOT NULL DEFAULT '',
  `create_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_date` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `update_by` varchar(255) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table mini_project_db.traffic_recap
CREATE TABLE IF NOT EXISTS `traffic_recap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `visitors` int(11) NOT NULL DEFAULT 0,
  `this_date` date DEFAULT NULL,
  `school_id` bigint(25) DEFAULT 0,
  `create_date` timestamp NULL DEFAULT current_timestamp(),
  `update_date` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table mini_project_db.user
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `avatar` text DEFAULT '',
  `username` varchar(255) DEFAULT '',
  `password` varchar(255) NOT NULL DEFAULT '',
  `email` varchar(255) DEFAULT '',
  `school_id` bigint(25) DEFAULT 0,
  `roles` mediumtext NOT NULL DEFAULT '[]',
  `device` varchar(255) NOT NULL DEFAULT '',
  `blocked` tinyint(1) NOT NULL DEFAULT 0,
  `guest` tinyint(1) NOT NULL DEFAULT 0,
  `token` varchar(225) NOT NULL DEFAULT '',
  `create_date` timestamp NULL DEFAULT current_timestamp(),
  `update_date` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table mini_project_db.user_answer
CREATE TABLE IF NOT EXISTS `user_answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_correct` tinyint(1) NOT NULL DEFAULT 0,
  `answer` varchar(255) NOT NULL DEFAULT '',
  `user_id` bigint(25) NOT NULL DEFAULT 0,
  `materi_id` bigint(25) NOT NULL DEFAULT 0,
  `school_id` bigint(25) NOT NULL DEFAULT 0,
  `question_id` bigint(25) NOT NULL DEFAULT 0,
  `questions` mediumtext DEFAULT NULL,
  `create_date` timestamp NULL DEFAULT current_timestamp(),
  `update_date` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table mini_project_db.user_score
CREATE TABLE IF NOT EXISTS `user_score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score` int(11) NOT NULL DEFAULT 0,
  `point` int(11) NOT NULL DEFAULT 0,
  `school_id` bigint(25) NOT NULL DEFAULT 0,
  `user_id` bigint(25) NOT NULL DEFAULT 0,
  `materi_id` bigint(25) NOT NULL DEFAULT 0,
  `total_question_answer` int(11) NOT NULL DEFAULT 0,
  `count_question` int(11) NOT NULL DEFAULT 0,
  `create_date` timestamp NULL DEFAULT current_timestamp(),
  `update_date` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table mini_project_db.user_traffic
CREATE TABLE IF NOT EXISTS `user_traffic` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `visitors` int(11) NOT NULL DEFAULT 0,
  `user_id` bigint(25) NOT NULL DEFAULT 0,
  `school_id` bigint(25) DEFAULT 0,
  `users` mediumtext DEFAULT '[]',
  `create_date` timestamp NULL DEFAULT current_timestamp(),
  `update_date` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
