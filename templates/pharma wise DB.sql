/*
SQLyog Community v13.3.0 (64 bit)
MySQL - 5.6.12-log : Database - epharma
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`epharma` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `epharma`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add billentry',7,'add_billentry'),
(26,'Can change billentry',7,'change_billentry'),
(27,'Can delete billentry',7,'delete_billentry'),
(28,'Can view billentry',7,'view_billentry'),
(29,'Can add customer',8,'add_customer'),
(30,'Can change customer',8,'change_customer'),
(31,'Can delete customer',8,'delete_customer'),
(32,'Can view customer',8,'view_customer'),
(33,'Can add login',9,'add_login'),
(34,'Can change login',9,'change_login'),
(35,'Can delete login',9,'delete_login'),
(36,'Can view login',9,'view_login'),
(37,'Can add medicine',10,'add_medicine'),
(38,'Can change medicine',10,'change_medicine'),
(39,'Can delete medicine',10,'delete_medicine'),
(40,'Can view medicine',10,'view_medicine'),
(41,'Can add order_main',11,'add_order_main'),
(42,'Can change order_main',11,'change_order_main'),
(43,'Can delete order_main',11,'delete_order_main'),
(44,'Can view order_main',11,'view_order_main'),
(45,'Can add pharmacy',12,'add_pharmacy'),
(46,'Can change pharmacy',12,'change_pharmacy'),
(47,'Can delete pharmacy',12,'delete_pharmacy'),
(48,'Can view pharmacy',12,'view_pharmacy'),
(49,'Can add stock',13,'add_stock'),
(50,'Can change stock',13,'change_stock'),
(51,'Can delete stock',13,'delete_stock'),
(52,'Can view stock',13,'view_stock'),
(53,'Can add review',14,'add_review'),
(54,'Can change review',14,'change_review'),
(55,'Can delete review',14,'delete_review'),
(56,'Can view review',14,'view_review'),
(57,'Can add priscription',15,'add_priscription'),
(58,'Can change priscription',15,'change_priscription'),
(59,'Can delete priscription',15,'delete_priscription'),
(60,'Can view priscription',15,'view_priscription'),
(61,'Can add prescriptionpayment',16,'add_prescriptionpayment'),
(62,'Can change prescriptionpayment',16,'change_prescriptionpayment'),
(63,'Can delete prescriptionpayment',16,'delete_prescriptionpayment'),
(64,'Can view prescriptionpayment',16,'view_prescriptionpayment'),
(65,'Can add payment',17,'add_payment'),
(66,'Can change payment',17,'change_payment'),
(67,'Can delete payment',17,'delete_payment'),
(68,'Can view payment',17,'view_payment'),
(69,'Can add order_sub',18,'add_order_sub'),
(70,'Can change order_sub',18,'change_order_sub'),
(71,'Can delete order_sub',18,'delete_order_sub'),
(72,'Can view order_sub',18,'view_order_sub'),
(73,'Can add notification',19,'add_notification'),
(74,'Can change notification',19,'change_notification'),
(75,'Can delete notification',19,'delete_notification'),
(76,'Can view notification',19,'view_notification'),
(77,'Can add complaint',20,'add_complaint'),
(78,'Can change complaint',20,'change_complaint'),
(79,'Can delete complaint',20,'delete_complaint'),
(80,'Can view complaint',20,'view_complaint'),
(81,'Can add cart',21,'add_cart'),
(82,'Can change cart',21,'change_cart'),
(83,'Can delete cart',21,'delete_cart'),
(84,'Can view cart',21,'view_cart');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'myapp','billentry'),
(21,'myapp','cart'),
(20,'myapp','complaint'),
(8,'myapp','customer'),
(9,'myapp','login'),
(10,'myapp','medicine'),
(19,'myapp','notification'),
(11,'myapp','order_main'),
(18,'myapp','order_sub'),
(17,'myapp','payment'),
(12,'myapp','pharmacy'),
(16,'myapp','prescriptionpayment'),
(15,'myapp','priscription'),
(14,'myapp','review'),
(13,'myapp','stock'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-10-29 11:37:16.248645'),
(2,'auth','0001_initial','2024-10-29 11:37:16.443356'),
(3,'admin','0001_initial','2024-10-29 11:37:16.936794'),
(4,'admin','0002_logentry_remove_auto_add','2024-10-29 11:37:17.026788'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-10-29 11:37:17.038805'),
(6,'contenttypes','0002_remove_content_type_name','2024-10-29 11:37:17.181790'),
(7,'auth','0002_alter_permission_name_max_length','2024-10-29 11:37:17.238790'),
(8,'auth','0003_alter_user_email_max_length','2024-10-29 11:37:17.289791'),
(9,'auth','0004_alter_user_username_opts','2024-10-29 11:37:17.300809'),
(10,'auth','0005_alter_user_last_login_null','2024-10-29 11:37:17.346445'),
(11,'auth','0006_require_contenttypes_0002','2024-10-29 11:37:17.352446'),
(12,'auth','0007_alter_validators_add_error_messages','2024-10-29 11:37:17.363462'),
(13,'auth','0008_alter_user_username_max_length','2024-10-29 11:37:17.412091'),
(14,'auth','0009_alter_user_last_name_max_length','2024-10-29 11:37:17.461255'),
(15,'auth','0010_alter_group_name_max_length','2024-10-29 11:37:17.512726'),
(16,'auth','0011_update_proxy_permissions','2024-10-29 11:37:17.526725'),
(17,'myapp','0001_initial','2024-10-29 11:37:18.411257'),
(18,'sessions','0001_initial','2024-10-29 11:37:19.118259');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('a6l1hy3naz097qnl4anfns7omjy0xi6r','OWJhYzQ3NWU5NTIyYjRkMTA0NWU1ZjI4MjE4ZmYwZWFkMWNjYTYwYTp7ImxpZCI6MywibWlkIjoiMSIsIm9pZCI6IjkifQ==','2024-11-23 12:33:40.813484'),
('b5jyl7z0f201x7vva3v8ax3zhnskoajb','ODFiOWNmNmExMzRmYjcyMjZlMWNjZDUwNjlhNThhZGYzNWVhMDE5Njp7ImxpZCI6MywibWlkIjoiMSJ9','2024-11-11 15:40:33.780796'),
('klyb4m0hunn2pfha13n2ia5dlsaua2tw','ODFiOWNmNmExMzRmYjcyMjZlMWNjZDUwNjlhNThhZGYzNWVhMDE5Njp7ImxpZCI6MywibWlkIjoiMSJ9','2024-11-02 11:46:41.400994');

/*Table structure for table `myapp_billentry` */

DROP TABLE IF EXISTS `myapp_billentry`;

CREATE TABLE `myapp_billentry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `total_amount` bigint(20) NOT NULL,
  `status` varchar(100) NOT NULL,
  `quantity` varchar(100) NOT NULL,
  `paystatus` varchar(100) NOT NULL,
  `PRESCRIPTION_id` int(11) NOT NULL,
  `Stock_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_billentry_PRESCRIPTION_id_d54052f2_fk_myapp_pri` (`PRESCRIPTION_id`),
  KEY `myapp_billentry_Stock_id_3c389b18_fk_myapp_stock_id` (`Stock_id`),
  CONSTRAINT `myapp_billentry_PRESCRIPTION_id_d54052f2_fk_myapp_pri` FOREIGN KEY (`PRESCRIPTION_id`) REFERENCES `myapp_priscription` (`id`),
  CONSTRAINT `myapp_billentry_Stock_id_3c389b18_fk_myapp_stock_id` FOREIGN KEY (`Stock_id`) REFERENCES `myapp_stock` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_billentry` */

insert  into `myapp_billentry`(`id`,`date`,`total_amount`,`status`,`quantity`,`paystatus`,`PRESCRIPTION_id`,`Stock_id`) values 
(15,'2024-10-31',50,'pending','1','paid',1,8),
(16,'2024-10-31',20,'pending','1','pending',2,7),
(17,'2024-11-01',50,'pending','1','pending',1,8);

/*Table structure for table `myapp_cart` */

DROP TABLE IF EXISTS `myapp_cart`;

CREATE TABLE `myapp_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(100) NOT NULL,
  `Medicine_id` int(11) NOT NULL,
  `User_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_cart_Medicine_id_67e61706_fk_myapp_medicine_id` (`Medicine_id`),
  KEY `myapp_cart_User_id_cd69cff1_fk_myapp_customer_id` (`User_id`),
  CONSTRAINT `myapp_cart_Medicine_id_67e61706_fk_myapp_medicine_id` FOREIGN KEY (`Medicine_id`) REFERENCES `myapp_medicine` (`id`),
  CONSTRAINT `myapp_cart_User_id_cd69cff1_fk_myapp_customer_id` FOREIGN KEY (`User_id`) REFERENCES `myapp_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_cart` */

insert  into `myapp_cart`(`id`,`quantity`,`Medicine_id`,`User_id`) values 
(1,'1',3,1);

/*Table structure for table `myapp_complaint` */

DROP TABLE IF EXISTS `myapp_complaint`;

CREATE TABLE `myapp_complaint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `complaint` varchar(200) NOT NULL,
  `replay` varchar(200) NOT NULL,
  `stauts` varchar(100) NOT NULL,
  `User_id` int(11) NOT NULL,
  `pharmacy_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaint_User_id_55eefbab_fk_myapp_customer_id` (`User_id`),
  KEY `myapp_complaint_pharmacy_id_2fdbac91_fk_myapp_pharmacy_id` (`pharmacy_id`),
  CONSTRAINT `myapp_complaint_pharmacy_id_2fdbac91_fk_myapp_pharmacy_id` FOREIGN KEY (`pharmacy_id`) REFERENCES `myapp_pharmacy` (`id`),
  CONSTRAINT `myapp_complaint_User_id_55eefbab_fk_myapp_customer_id` FOREIGN KEY (`User_id`) REFERENCES `myapp_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_complaint` */

insert  into `myapp_complaint`(`id`,`date`,`complaint`,`replay`,`stauts`,`User_id`,`pharmacy_id`) values 
(1,'2024-10-31','nhhhi uhjijhijon ijojoij','vgjbh jnjknkn, milJ','replaied',1,1),
(2,'2024-10-31','dfhnn vhngjm ','pending','pending',1,1);

/*Table structure for table `myapp_customer` */

DROP TABLE IF EXISTS `myapp_customer`;

CREATE TABLE `myapp_customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_customer_LOGIN_id_23d9edf9_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_customer_LOGIN_id_23d9edf9_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_customer` */

insert  into `myapp_customer`(`id`,`name`,`email`,`phone`,`gender`,`LOGIN_id`) values 
(1,'Abhi','abhi@gmail.com','8943027037','Male',3),
(2,'Varun.k','varunvkd@gmail.com','999444661','Male',4),
(3,'ddddd','varunvkd@gmail.com','9994446111','Male',5);

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin123','admin'),
(2,'leodas@gmail.com','Leomed@123','pharma'),
(3,'abhi@gmail.com','Abhi1234','customer'),
(4,'varunvkd@gmail.com','Varun@123','customer'),
(5,'','',''),
(6,'bashjb@gmail.com','Shop1@123','pharma'),
(7,'basghhhjb@gmail.com','Shop2@123','pharma');

/*Table structure for table `myapp_medicine` */

DROP TABLE IF EXISTS `myapp_medicine`;

CREATE TABLE `myapp_medicine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `ingredients` varchar(100) NOT NULL,
  `quantity` varchar(100) NOT NULL,
  `warning` varchar(100) NOT NULL,
  `exp_date` varchar(100) NOT NULL,
  `manuf_date` varchar(100) NOT NULL,
  `image` varchar(300) NOT NULL,
  `price` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `Pharmacy_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_medicine_Pharmacy_id_4bedc71d_fk_myapp_pharmacy_id` (`Pharmacy_id`),
  CONSTRAINT `myapp_medicine_Pharmacy_id_4bedc71d_fk_myapp_pharmacy_id` FOREIGN KEY (`Pharmacy_id`) REFERENCES `myapp_pharmacy` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_medicine` */

insert  into `myapp_medicine`(`id`,`name`,`ingredients`,`quantity`,`warning`,`exp_date`,`manuf_date`,`image`,`price`,`category`,`Pharmacy_id`) values 
(1,'covaxin','solution ip','10','internal use only','2025-02-19','2024-10-09','/media/20241019-155033.jpg','50','injection',1),
(3,'Dolo 650','paracetamol tablet','10','internal use only','2025-04-28','2024-05-29','/media/20241028-171927.jpg','20','tablet',1),
(4,'Dolo 650','paracetamol tablet','20','internal use only','2024-11-22','2024-10-27','/media/20241101-101034.jpg','20','tablet',1);

/*Table structure for table `myapp_notification` */

DROP TABLE IF EXISTS `myapp_notification`;

CREATE TABLE `myapp_notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `notification` varchar(100) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `pharmacy_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_notification_customer_id_9530f60a_fk_myapp_customer_id` (`customer_id`),
  KEY `myapp_notification_pharmacy_id_f57fe02c_fk_myapp_pharmacy_id` (`pharmacy_id`),
  CONSTRAINT `myapp_notification_customer_id_9530f60a_fk_myapp_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `myapp_customer` (`id`),
  CONSTRAINT `myapp_notification_pharmacy_id_f57fe02c_fk_myapp_pharmacy_id` FOREIGN KEY (`pharmacy_id`) REFERENCES `myapp_pharmacy` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_notification` */

insert  into `myapp_notification`(`id`,`date`,`notification`,`customer_id`,`pharmacy_id`) values 
(1,'2024-10-29','packed',2,1),
(2,'2024-10-29','delivered',1,1),
(3,'2024-10-29','packed',1,1),
(4,'2024-10-31','delivered',1,1),
(5,'2024-10-31','packed',1,1),
(6,'2024-10-31','assigned',1,1);

/*Table structure for table `myapp_order_main` */

DROP TABLE IF EXISTS `myapp_order_main`;

CREATE TABLE `myapp_order_main` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `amount` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `online` varchar(100) NOT NULL,
  `shop_bills` varchar(100) NOT NULL,
  `Shop_id` int(11) NOT NULL,
  `User_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_order_main_Shop_id_8bc187a9_fk_myapp_pharmacy_id` (`Shop_id`),
  KEY `myapp_order_main_User_id_0f321ded_fk_myapp_customer_id` (`User_id`),
  CONSTRAINT `myapp_order_main_Shop_id_8bc187a9_fk_myapp_pharmacy_id` FOREIGN KEY (`Shop_id`) REFERENCES `myapp_pharmacy` (`id`),
  CONSTRAINT `myapp_order_main_User_id_0f321ded_fk_myapp_customer_id` FOREIGN KEY (`User_id`) REFERENCES `myapp_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_order_main` */

insert  into `myapp_order_main`(`id`,`date`,`amount`,`status`,`type`,`online`,`shop_bills`,`Shop_id`,`User_id`) values 
(1,'0000-00-00','','Successfull','self','pending','',1,1),
(2,'0000-00-00','','Successfull','self','pending','',1,1),
(3,'0000-00-00','','Successfull','self','pending','',1,1),
(4,'0000-00-00','','Successfull','self','pending','',1,1),
(5,'0000-00-00','','Successfull','self','pending','',1,1),
(6,'0000-00-00','','Successfull','self','pending','',1,1),
(7,'0000-00-00','','Successfull','self','pending','',1,1),
(8,'0000-00-00','','Successfull','self','pending','',1,1),
(9,'0000-00-00','','assigned','self','pending','',1,1),
(10,'0000-00-00','','Successfull','self','pending','',1,1),
(11,'0000-00-00','','Successfull','self','pending','',1,1),
(12,'0000-00-00','','Successfull','self','pending','',1,1),
(13,'0000-00-00','0','Successfull','self','pending','',1,2),
(14,'0000-00-00','0','Successfull','self','pending','',1,2),
(15,'0000-00-00','0','Successfull','self','pending','',1,2),
(16,'0000-00-00','0','Successfull','self','pending','',1,2),
(17,'0000-00-00','100.0','packed','self','pending','',1,2),
(18,'0000-00-00','120.0','delivered','self','pending','',1,1),
(19,'2024-10-29','320.0','Successfull','self','pending','',1,1),
(20,'2024-10-29','20.0','delivered','self','pending','',1,1),
(21,'2024-10-31','100.0','packed','self','pending','',1,1),
(22,'2024-10-31','100.0','Successfull','self','pending','',1,1),
(23,'2024-10-31','20.0','assigned','self','pending','',1,1),
(24,'2024-10-31','20.0','Successfull','self','pending','',1,1),
(25,'2024-10-31','20.0','Successfull','self','pending','',1,1),
(26,'2024-10-31','50.0','Successfull','self','pending','',1,1);

/*Table structure for table `myapp_order_sub` */

DROP TABLE IF EXISTS `myapp_order_sub`;

CREATE TABLE `myapp_order_sub` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `Order_main_id` int(11) NOT NULL,
  `Stock_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_order_sub_Order_main_id_d6cb6c9c_fk_myapp_order_main_id` (`Order_main_id`),
  KEY `myapp_order_sub_Stock_id_438ee3e5_fk_myapp_stock_id` (`Stock_id`),
  CONSTRAINT `myapp_order_sub_Order_main_id_d6cb6c9c_fk_myapp_order_main_id` FOREIGN KEY (`Order_main_id`) REFERENCES `myapp_order_main` (`id`),
  CONSTRAINT `myapp_order_sub_Stock_id_438ee3e5_fk_myapp_stock_id` FOREIGN KEY (`Stock_id`) REFERENCES `myapp_stock` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_order_sub` */

insert  into `myapp_order_sub`(`id`,`quantity`,`amount`,`Order_main_id`,`Stock_id`) values 
(24,'1','20',23,7),
(25,'1','20',24,7),
(26,'1','20',25,7),
(27,'1','50',26,8);

/*Table structure for table `myapp_payment` */

DROP TABLE IF EXISTS `myapp_payment`;

CREATE TABLE `myapp_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `Order_main_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_payment_Order_main_id_ba4bfdec_fk_myapp_order_main_id` (`Order_main_id`),
  CONSTRAINT `myapp_payment_Order_main_id_ba4bfdec_fk_myapp_order_main_id` FOREIGN KEY (`Order_main_id`) REFERENCES `myapp_order_main` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_payment` */

insert  into `myapp_payment`(`id`,`date`,`amount`,`status`,`Order_main_id`) values 
(1,'20241019','100','paid',1),
(2,'20241027','100','paid',10),
(3,'20241027','100','paid',11),
(4,'20241028','50','paid',12),
(5,'20241028','100','paid',14),
(6,'20241028','100','paid',15),
(7,'20241028','100','paid',16),
(8,'20241028','100','paid',17),
(9,'20241028','120','paid',18),
(10,'20241029','320','paid',19),
(11,'20241029','20','paid',20),
(12,'20241031','100','paid',21),
(13,'20241031','100','paid',22),
(14,'20241031','20','paid',23),
(15,'20241031','20','paid',24),
(16,'20241031','20','paid',25),
(17,'20241031','50','paid',26);

/*Table structure for table `myapp_pharmacy` */

DROP TABLE IF EXISTS `myapp_pharmacy`;

CREATE TABLE `myapp_pharmacy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shop_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `owner_name` varchar(100) NOT NULL,
  `owner_phone` varchar(100) NOT NULL,
  `document` varchar(200) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `photo` varchar(200) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_pharmacy_LOGIN_id_fb220615_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_pharmacy_LOGIN_id_fb220615_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_pharmacy` */

insert  into `myapp_pharmacy`(`id`,`shop_name`,`email`,`owner_name`,`owner_phone`,`document`,`place`,`post`,`pin`,`district`,`status`,`photo`,`LOGIN_id`) values 
(1,'Leo medicals','leomedicals@gmail.com','Vshnu das','8943027041','/media/20241019-154804-1.jpg','kuttikattoor','kuttikattoor','673585','kozhikode','approved','/media/20241019-154804.jpg',2),
(2,'Open medicals','openmed@gmail.com','open group','9667773331','/media/20241030-164520-1.jpg','narikkuni','narikkuni','673585','kozhikode','approved','/media/20241030-164520.jpg',6),
(3,'Shop@2','basghhhjb@gmail.com','ghghbh','6667772231','/media/20241030-164641-1.jpg','dsdshjhj','jomio','673546','gtdf','rejected','/media/20241030-164641.jpg',7);

/*Table structure for table `myapp_prescriptionpayment` */

DROP TABLE IF EXISTS `myapp_prescriptionpayment`;

CREATE TABLE `myapp_prescriptionpayment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `BILLENTRY_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_prescriptionpa_BILLENTRY_id_2e305ecc_fk_myapp_bil` (`BILLENTRY_id`),
  CONSTRAINT `myapp_prescriptionpa_BILLENTRY_id_2e305ecc_fk_myapp_bil` FOREIGN KEY (`BILLENTRY_id`) REFERENCES `myapp_billentry` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_prescriptionpayment` */

insert  into `myapp_prescriptionpayment`(`id`,`date`,`amount`,`status`,`BILLENTRY_id`) values 
(2,'20241031','50.0','paid',15);

/*Table structure for table `myapp_priscription` */

DROP TABLE IF EXISTS `myapp_priscription`;

CREATE TABLE `myapp_priscription` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `Pharmacy_id` int(11) NOT NULL,
  `User_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_priscription_Pharmacy_id_cadd16b6_fk_myapp_pharmacy_id` (`Pharmacy_id`),
  KEY `myapp_priscription_User_id_6903988d_fk_myapp_customer_id` (`User_id`),
  CONSTRAINT `myapp_priscription_Pharmacy_id_cadd16b6_fk_myapp_pharmacy_id` FOREIGN KEY (`Pharmacy_id`) REFERENCES `myapp_pharmacy` (`id`),
  CONSTRAINT `myapp_priscription_User_id_6903988d_fk_myapp_customer_id` FOREIGN KEY (`User_id`) REFERENCES `myapp_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_priscription` */

insert  into `myapp_priscription`(`id`,`file`,`date`,`Pharmacy_id`,`User_id`) values 
(1,'/media/prescription/20241025-102958.jpg','2024-10-25',1,1),
(2,'/media/prescription/20241025-104700.jpg','2024-10-25',1,1),
(3,'/media/prescription/20241028-230440.jpg','2024-10-28',1,1),
(4,'/media/prescription/20241031-170040.jpg','2024-10-31',1,1),
(5,'/media/prescription/20241101-102302.jpg','2024-11-01',1,1);

/*Table structure for table `myapp_review` */

DROP TABLE IF EXISTS `myapp_review`;

CREATE TABLE `myapp_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `review` varchar(100) NOT NULL,
  `User_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_review_User_id_cbfc30f6_fk_myapp_customer_id` (`User_id`),
  CONSTRAINT `myapp_review_User_id_cbfc30f6_fk_myapp_customer_id` FOREIGN KEY (`User_id`) REFERENCES `myapp_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_review` */

insert  into `myapp_review`(`id`,`date`,`review`,`User_id`) values 
(1,'2024-10-27','Avarage shopping experience',2),
(2,'2024-10-31','wonderful paltform medicine shoping',1),
(3,'2024-10-31','really helpful to find pharmacies',1);

/*Table structure for table `myapp_stock` */

DROP TABLE IF EXISTS `myapp_stock`;

CREATE TABLE `myapp_stock` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(100) NOT NULL,
  `Medicine_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_stock_Medicine_id_4031046f_fk_myapp_medicine_id` (`Medicine_id`),
  CONSTRAINT `myapp_stock_Medicine_id_4031046f_fk_myapp_medicine_id` FOREIGN KEY (`Medicine_id`) REFERENCES `myapp_medicine` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `myapp_stock` */

insert  into `myapp_stock`(`id`,`quantity`,`Medicine_id`) values 
(7,'7',3),
(8,'49',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
