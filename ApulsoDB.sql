-- MariaDB dump 10.19  Distrib 10.6.16-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: pressureless_health
-- ------------------------------------------------------
-- Server version	10.6.16-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add auth token',6,'add_authtoken'),(22,'Can change auth token',6,'change_authtoken'),(23,'Can delete auth token',6,'delete_authtoken'),(24,'Can view auth token',6,'view_authtoken'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add reminder',8,'add_reminder'),(30,'Can change reminder',8,'change_reminder'),(31,'Can delete reminder',8,'delete_reminder'),(32,'Can view reminder',8,'view_reminder'),(33,'Can add notification history',9,'add_notificationhistory'),(34,'Can change notification history',9,'change_notificationhistory'),(35,'Can delete notification history',9,'delete_notificationhistory'),(36,'Can view notification history',9,'view_notificationhistory'),(37,'Can add goal history',10,'add_goalhistory'),(38,'Can change goal history',10,'change_goalhistory'),(39,'Can delete goal history',10,'delete_goalhistory'),(40,'Can view goal history',10,'view_goalhistory'),(41,'Can add contact',11,'add_contact'),(42,'Can change contact',11,'change_contact'),(43,'Can delete contact',11,'delete_contact'),(44,'Can view contact',11,'view_contact'),(45,'Can add challenge history',12,'add_challengehistory'),(46,'Can change challenge history',12,'change_challengehistory'),(47,'Can delete challenge history',12,'delete_challengehistory'),(48,'Can view challenge history',12,'view_challengehistory'),(49,'Can add debug log',13,'add_debuglog'),(50,'Can change debug log',13,'change_debuglog'),(51,'Can delete debug log',13,'delete_debuglog'),(52,'Can view debug log',13,'view_debuglog'),(53,'Can add measurement',14,'add_measurement'),(54,'Can change measurement',14,'change_measurement'),(55,'Can delete measurement',14,'delete_measurement'),(56,'Can view measurement',14,'view_measurement'),(57,'Can add medication',15,'add_medication'),(58,'Can change medication',15,'change_medication'),(59,'Can delete medication',15,'delete_medication'),(60,'Can view medication',15,'view_medication'),(61,'Can add medication frequency',16,'add_medicationfrequency'),(62,'Can change medication frequency',16,'change_medicationfrequency'),(63,'Can delete medication frequency',16,'delete_medicationfrequency'),(64,'Can view medication frequency',16,'view_medicationfrequency'),(65,'Can add article',17,'add_article'),(66,'Can change article',17,'change_article'),(67,'Can delete article',17,'delete_article'),(68,'Can view article',17,'view_article'),(69,'Can add challenge',18,'add_challenge'),(70,'Can change challenge',18,'change_challenge'),(71,'Can delete challenge',18,'delete_challenge'),(72,'Can view challenge',18,'view_challenge'),(73,'Can add goal',19,'add_goal'),(74,'Can change goal',19,'change_goal'),(75,'Can delete goal',19,'delete_goal'),(76,'Can view goal',19,'view_goal'),(77,'Can add requirement',20,'add_requirement'),(78,'Can change requirement',20,'change_requirement'),(79,'Can delete requirement',20,'delete_requirement'),(80,'Can view requirement',20,'view_requirement');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_challengehistory`
--

DROP TABLE IF EXISTS `core_challengehistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_challengehistory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `succeeded` tinyint(1) NOT NULL,
  `challenge_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `end_date` datetime(6) DEFAULT NULL,
  `start_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_challengehistor_challenge_id_1b6ddc77_fk_gamificat` (`challenge_id`),
  KEY `core_challengehistory_user_id_213f2cc3_fk_core_user_id` (`user_id`),
  CONSTRAINT `core_challengehistor_challenge_id_1b6ddc77_fk_gamificat` FOREIGN KEY (`challenge_id`) REFERENCES `gamification_challenge` (`id`),
  CONSTRAINT `core_challengehistory_user_id_213f2cc3_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_challengehistory`
--

LOCK TABLES `core_challengehistory` WRITE;
/*!40000 ALTER TABLE `core_challengehistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_challengehistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_contact`
--

DROP TABLE IF EXISTS `core_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_contact` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) NOT NULL,
  `address` varchar(50) DEFAULT NULL,
  `relationship` varchar(50) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_contact_user_id_2570c512_fk_core_user_id` (`user_id`),
  CONSTRAINT `core_contact_user_id_2570c512_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_contact`
--

LOCK TABLES `core_contact` WRITE;
/*!40000 ALTER TABLE `core_contact` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_debuglog`
--

DROP TABLE IF EXISTS `core_debuglog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_debuglog` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_debuglog_user_id_8cfcd531_fk_core_user_id` (`user_id`),
  CONSTRAINT `core_debuglog_user_id_8cfcd531_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_debuglog`
--

LOCK TABLES `core_debuglog` WRITE;
/*!40000 ALTER TABLE `core_debuglog` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_debuglog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_goalhistory`
--

DROP TABLE IF EXISTS `core_goalhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_goalhistory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `reached_on` datetime(6) NOT NULL,
  `goal_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_goalhistory_goal_id_e314f992_fk_gamification_goal_id` (`goal_id`),
  KEY `core_goalhistory_user_id_3d1a87ac_fk_core_user_id` (`user_id`),
  CONSTRAINT `core_goalhistory_goal_id_e314f992_fk_gamification_goal_id` FOREIGN KEY (`goal_id`) REFERENCES `gamification_goal` (`id`),
  CONSTRAINT `core_goalhistory_user_id_3d1a87ac_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_goalhistory`
--

LOCK TABLES `core_goalhistory` WRITE;
/*!40000 ALTER TABLE `core_goalhistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_goalhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_notificationhistory`
--

DROP TABLE IF EXISTS `core_notificationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_notificationhistory` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `body` varchar(50) DEFAULT NULL,
  `send_date` datetime(6) NOT NULL,
  `reminder_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_notificationhis_reminder_id_6fb6148a_fk_core_remi` (`reminder_id`),
  KEY `core_notificationhistory_user_id_923fcece_fk_core_user_id` (`user_id`),
  CONSTRAINT `core_notificationhis_reminder_id_6fb6148a_fk_core_remi` FOREIGN KEY (`reminder_id`) REFERENCES `core_reminder` (`id`),
  CONSTRAINT `core_notificationhistory_user_id_923fcece_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_notificationhistory`
--

LOCK TABLES `core_notificationhistory` WRITE;
/*!40000 ALTER TABLE `core_notificationhistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_notificationhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_reminder`
--

DROP TABLE IF EXISTS `core_reminder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_reminder` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `active` tinyint(1) NOT NULL,
  `triggered_times` int(10) unsigned NOT NULL CHECK (`triggered_times` >= 0),
  `medication_frequency_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_reminder_medication_frequency_id_437f6dbc_uniq` (`medication_frequency_id`),
  CONSTRAINT `core_reminder_medication_frequency_437f6dbc_fk_health_me` FOREIGN KEY (`medication_frequency_id`) REFERENCES `health_medicationfrequency` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_reminder`
--

LOCK TABLES `core_reminder` WRITE;
/*!40000 ALTER TABLE `core_reminder` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_reminder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user`
--

DROP TABLE IF EXISTS `core_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `age` int(10) unsigned DEFAULT NULL CHECK (`age` >= 0),
  `weight` int(10) unsigned DEFAULT NULL CHECK (`weight` >= 0),
  `country` varchar(50) DEFAULT NULL,
  `gender` varchar(50) NOT NULL,
  `points` int(10) unsigned NOT NULL CHECK (`points` >= 0),
  `avatar_url` varchar(255) NOT NULL,
  `password_reset_code` varchar(7) DEFAULT NULL,
  `password_reset_code_last_request` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `core_user_email_92a71487_uniq` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user`
--

LOCK TABLES `core_user` WRITE;
/*!40000 ALTER TABLE `core_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user_groups`
--

DROP TABLE IF EXISTS `core_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_user_groups_user_id_group_id_c82fcad1_uniq` (`user_id`,`group_id`),
  KEY `core_user_groups_group_id_fe8c697f_fk_auth_group_id` (`group_id`),
  CONSTRAINT `core_user_groups_group_id_fe8c697f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `core_user_groups_user_id_70b4d9b8_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_groups`
--

LOCK TABLES `core_user_groups` WRITE;
/*!40000 ALTER TABLE `core_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user_user_permissions`
--

DROP TABLE IF EXISTS `core_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_user_user_permissions_user_id_permission_id_73ea0daa_uniq` (`user_id`,`permission_id`),
  KEY `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` (`permission_id`),
  CONSTRAINT `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `core_user_user_permissions_user_id_085123d3_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_user_permissions`
--

LOCK TABLES `core_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `core_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_core_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(12,'core','challengehistory'),(11,'core','contact'),(13,'core','debuglog'),(10,'core','goalhistory'),(9,'core','notificationhistory'),(8,'core','reminder'),(7,'core','user'),(18,'gamification','challenge'),(19,'gamification','goal'),(20,'gamification','requirement'),(17,'health','article'),(14,'health','measurement'),(15,'health','medication'),(16,'health','medicationfrequency'),(6,'knox','authtoken'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'gamification','0001_initial','2024-06-15 01:43:42.878582'),(2,'contenttypes','0001_initial','2024-06-15 01:43:42.903974'),(3,'contenttypes','0002_remove_content_type_name','2024-06-15 01:43:42.939998'),(4,'auth','0001_initial','2024-06-15 01:43:43.054428'),(5,'auth','0002_alter_permission_name_max_length','2024-06-15 01:43:43.081719'),(6,'auth','0003_alter_user_email_max_length','2024-06-15 01:43:43.087950'),(7,'auth','0004_alter_user_username_opts','2024-06-15 01:43:43.093801'),(8,'auth','0005_alter_user_last_login_null','2024-06-15 01:43:43.099811'),(9,'auth','0006_require_contenttypes_0002','2024-06-15 01:43:43.101671'),(10,'auth','0007_alter_validators_add_error_messages','2024-06-15 01:43:43.107645'),(11,'auth','0008_alter_user_username_max_length','2024-06-15 01:43:43.113998'),(12,'auth','0009_alter_user_last_name_max_length','2024-06-15 01:43:43.120503'),(13,'auth','0010_alter_group_name_max_length','2024-06-15 01:43:43.136861'),(14,'auth','0011_update_proxy_permissions','2024-06-15 01:43:43.146639'),(15,'auth','0012_alter_user_first_name_max_length','2024-06-15 01:43:43.152812'),(16,'core','0001_initial','2024-06-15 01:43:43.583176'),(17,'admin','0001_initial','2024-06-15 01:43:43.645245'),(18,'admin','0002_logentry_remove_auto_add','2024-06-15 01:43:43.659280'),(19,'admin','0003_logentry_add_action_flag_choices','2024-06-15 01:43:43.672777'),(20,'health','0001_initial','2024-06-15 01:43:43.714600'),(21,'health','0002_measurement_used_recommended_method','2024-06-15 01:43:43.747696'),(22,'health','0003_medication_medicationfrequency','2024-06-15 01:43:43.833938'),(23,'health','0004_alter_medication_deleted','2024-06-15 01:43:43.850139'),(24,'health','0005_alter_medication_description_alter_medication_name_and_more','2024-06-15 01:43:43.938947'),(25,'health','0006_measurement_comments','2024-06-15 01:43:43.974713'),(26,'health','0007_articles','2024-06-15 01:43:43.986342'),(27,'health','0008_rename_articles_article','2024-06-15 01:43:44.014847'),(28,'health','0009_alter_measurement_measurement_date','2024-06-15 01:43:44.029554'),(29,'core','0002_alter_challengehistory_event_date','2024-06-15 01:43:44.046507'),(30,'core','0003_alter_challengehistory_event_date','2024-06-15 01:43:44.061776'),(31,'core','0004_alter_challengehistory_event_date','2024-06-15 01:43:44.077432'),(32,'core','0005_alter_challengehistory_event_date','2024-06-15 01:43:44.092126'),(33,'core','0006_alter_challengehistory_event_date','2024-06-15 01:43:44.108443'),(34,'core','0007_remove_challengehistory_event_date_and_more','2024-06-15 01:43:44.279110'),(35,'core','0008_alter_challengehistory_end_date_and_more','2024-06-15 01:43:44.329849'),(36,'core','0009_alter_challengehistory_start_date','2024-06-15 01:43:44.345088'),(37,'core','0010_alter_challengehistory_start_date','2024-06-15 01:43:44.361957'),(38,'core','0011_alter_challengehistory_start_date','2024-06-15 01:43:44.376668'),(39,'core','0012_alter_challengehistory_start_date','2024-06-15 01:43:44.391822'),(40,'core','0013_remove_medicationfrequency_medication_and_more','2024-06-15 01:43:44.532539'),(41,'core','0014_user_points','2024-06-15 01:43:44.564353'),(42,'core','0015_user_avatar_url','2024-06-15 01:43:44.596229'),(43,'core','0016_alter_user_email','2024-06-15 01:43:44.622807'),(44,'core','0017_user_password_reset_code','2024-06-15 01:43:44.649545'),(45,'core','0018_user_password_reset_code_last_request','2024-06-15 01:43:44.673982'),(46,'core','0019_alter_contact_email_alter_contact_last_name','2024-06-15 01:43:44.732708'),(47,'core','0020_alter_reminder_medication_frequency','2024-06-15 01:43:44.818489'),(48,'core','0021_contact_deleted','2024-06-15 01:43:44.848583'),(49,'core','0022_debuglog','2024-06-15 01:43:44.890280'),(50,'gamification','0002_alter_challenge_time_limit_challengerequirement','2024-06-15 01:43:44.969214'),(51,'gamification','0003_goal_requirements','2024-06-15 01:43:45.048822'),(52,'gamification','0004_delete_goalrequirement','2024-06-15 01:43:45.057887'),(53,'gamification','0005_challenge_requirements_delete_challengerequirement','2024-06-15 01:43:45.142579'),(54,'gamification','0006_challenge_reward','2024-06-15 01:43:45.170090'),(55,'gamification','0007_challenge_repeatable_challenge_repetition_interval','2024-06-15 01:43:45.208493'),(56,'gamification','0008_requirement_distinct_days','2024-06-15 01:43:45.233760'),(57,'gamification','0009_challenge_order','2024-06-15 01:43:45.258017'),(58,'health','0010_alter_medicationfrequency_deleted','2024-06-15 01:43:45.265970'),(59,'health','0011_medicationfrequency_friday_and_more','2024-06-15 01:43:45.434429'),(60,'health','0012_remove_medicationfrequency_weekday','2024-06-15 01:43:45.455185'),(61,'health','0013_measurement_deleted','2024-06-15 01:43:45.486142'),(62,'knox','0001_initial','2024-06-15 01:43:45.529186'),(63,'knox','0002_auto_20150916_1425','2024-06-15 01:43:45.586736'),(64,'knox','0003_auto_20150916_1526','2024-06-15 01:43:45.627308'),(65,'knox','0004_authtoken_expires','2024-06-15 01:43:45.651812'),(66,'knox','0005_authtoken_token_key','2024-06-15 01:43:45.691903'),(67,'knox','0006_auto_20160818_0932','2024-06-15 01:43:45.764786'),(68,'knox','0007_auto_20190111_0542','2024-06-15 01:43:45.787953'),(69,'knox','0008_remove_authtoken_salt','2024-06-15 01:43:45.815259'),(70,'sessions','0001_initial','2024-06-15 01:43:45.841143');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gamification_challenge`
--

DROP TABLE IF EXISTS `gamification_challenge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gamification_challenge` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `time_limit` bigint(20) DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `reward` int(10) unsigned NOT NULL CHECK (`reward` >= 0),
  `repeatable` tinyint(1) NOT NULL,
  `repetition_interval` int(10) unsigned DEFAULT NULL CHECK (`repetition_interval` >= 0),
  `order` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gamification_challenge`
--

LOCK TABLES `gamification_challenge` WRITE;
/*!40000 ALTER TABLE `gamification_challenge` DISABLE KEYS */;
/*!40000 ALTER TABLE `gamification_challenge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gamification_challenge_requirements`
--

DROP TABLE IF EXISTS `gamification_challenge_requirements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gamification_challenge_requirements` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `challenge_id` bigint(20) NOT NULL,
  `requirement_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `gamification_challenge_r_challenge_id_requirement_c60c6e1a_uniq` (`challenge_id`,`requirement_id`),
  KEY `gamification_challen_requirement_id_5a0c79eb_fk_gamificat` (`requirement_id`),
  CONSTRAINT `gamification_challen_challenge_id_5ffd0516_fk_gamificat` FOREIGN KEY (`challenge_id`) REFERENCES `gamification_challenge` (`id`),
  CONSTRAINT `gamification_challen_requirement_id_5a0c79eb_fk_gamificat` FOREIGN KEY (`requirement_id`) REFERENCES `gamification_requirement` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gamification_challenge_requirements`
--

LOCK TABLES `gamification_challenge_requirements` WRITE;
/*!40000 ALTER TABLE `gamification_challenge_requirements` DISABLE KEYS */;
/*!40000 ALTER TABLE `gamification_challenge_requirements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gamification_goal`
--

DROP TABLE IF EXISTS `gamification_goal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gamification_goal` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `reward` int(10) unsigned NOT NULL CHECK (`reward` >= 0),
  `enabled` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gamification_goal`
--

LOCK TABLES `gamification_goal` WRITE;
/*!40000 ALTER TABLE `gamification_goal` DISABLE KEYS */;
/*!40000 ALTER TABLE `gamification_goal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gamification_goal_requirements`
--

DROP TABLE IF EXISTS `gamification_goal_requirements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gamification_goal_requirements` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `goal_id` bigint(20) NOT NULL,
  `requirement_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `gamification_goal_requir_goal_id_requirement_id_887fc4f7_uniq` (`goal_id`,`requirement_id`),
  KEY `gamification_goal_re_requirement_id_86b8a934_fk_gamificat` (`requirement_id`),
  CONSTRAINT `gamification_goal_re_goal_id_392e0583_fk_gamificat` FOREIGN KEY (`goal_id`) REFERENCES `gamification_goal` (`id`),
  CONSTRAINT `gamification_goal_re_requirement_id_86b8a934_fk_gamificat` FOREIGN KEY (`requirement_id`) REFERENCES `gamification_requirement` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gamification_goal_requirements`
--

LOCK TABLES `gamification_goal_requirements` WRITE;
/*!40000 ALTER TABLE `gamification_goal_requirements` DISABLE KEYS */;
/*!40000 ALTER TABLE `gamification_goal_requirements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gamification_requirement`
--

DROP TABLE IF EXISTS `gamification_requirement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gamification_requirement` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `code` varchar(50) NOT NULL,
  `value` varchar(50) NOT NULL,
  `required` tinyint(1) NOT NULL,
  `time_limit` varchar(50) DEFAULT NULL,
  `distinct_days` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gamification_requirement`
--

LOCK TABLES `gamification_requirement` WRITE;
/*!40000 ALTER TABLE `gamification_requirement` DISABLE KEYS */;
/*!40000 ALTER TABLE `gamification_requirement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `health_article`
--

DROP TABLE IF EXISTS `health_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `health_article` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(250) NOT NULL,
  `content` varchar(1024) DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health_article`
--

LOCK TABLES `health_article` WRITE;
/*!40000 ALTER TABLE `health_article` DISABLE KEYS */;
/*!40000 ALTER TABLE `health_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `health_measurement`
--

DROP TABLE IF EXISTS `health_measurement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `health_measurement` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `measurement_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `systolic_pressure` decimal(5,2) NOT NULL,
  `diastolic_pressure` decimal(5,2) NOT NULL,
  `heart_rate` int(11) DEFAULT NULL,
  `temperature` int(11) DEFAULT NULL,
  `blood_oxygen` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `used_recommended_method` tinyint(1) NOT NULL,
  `comments` varchar(1024) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_measurement_user_id_b7631ab8_fk_core_user_id` (`user_id`),
  CONSTRAINT `health_measurement_user_id_b7631ab8_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health_measurement`
--

LOCK TABLES `health_measurement` WRITE;
/*!40000 ALTER TABLE `health_measurement` DISABLE KEYS */;
/*!40000 ALTER TABLE `health_measurement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `health_medication`
--

DROP TABLE IF EXISTS `health_medication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `health_medication` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `description` varchar(1024) DEFAULT NULL,
  `deleted` tinyint(1) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_medication_user_id_d71bb9e0_fk_core_user_id` (`user_id`),
  CONSTRAINT `health_medication_user_id_d71bb9e0_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health_medication`
--

LOCK TABLES `health_medication` WRITE;
/*!40000 ALTER TABLE `health_medication` DISABLE KEYS */;
/*!40000 ALTER TABLE `health_medication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `health_medicationfrequency`
--

DROP TABLE IF EXISTS `health_medicationfrequency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `health_medicationfrequency` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `hour` varchar(50) NOT NULL,
  `dose` varchar(250) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  `medication_id` bigint(20) NOT NULL,
  `friday` tinyint(1) NOT NULL,
  `monday` tinyint(1) NOT NULL,
  `saturday` tinyint(1) NOT NULL,
  `sunday` tinyint(1) NOT NULL,
  `thursday` tinyint(1) NOT NULL,
  `tuesday` tinyint(1) NOT NULL,
  `wednesday` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_medicationfre_medication_id_b719cf91_fk_health_me` (`medication_id`),
  CONSTRAINT `health_medicationfre_medication_id_b719cf91_fk_health_me` FOREIGN KEY (`medication_id`) REFERENCES `health_medication` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health_medicationfrequency`
--

LOCK TABLES `health_medicationfrequency` WRITE;
/*!40000 ALTER TABLE `health_medicationfrequency` DISABLE KEYS */;
/*!40000 ALTER TABLE `health_medicationfrequency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `knox_authtoken`
--

DROP TABLE IF EXISTS `knox_authtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `knox_authtoken` (
  `digest` varchar(128) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `expiry` datetime(6) DEFAULT NULL,
  `token_key` varchar(8) NOT NULL,
  PRIMARY KEY (`digest`),
  KEY `knox_authtoken_user_id_e5a5d899_fk_core_user_id` (`user_id`),
  KEY `knox_authtoken_token_key_8f4f7d47` (`token_key`),
  CONSTRAINT `knox_authtoken_user_id_e5a5d899_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `knox_authtoken`
--

LOCK TABLES `knox_authtoken` WRITE;
/*!40000 ALTER TABLE `knox_authtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `knox_authtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'pressureless_health'
--

--
-- Dumping routines for database 'pressureless_health'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-16  3:01:49
