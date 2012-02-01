/*
MySQL Data Transfer
Source Host: localhost
Source Database: totome
Target Host: localhost
Target Database: tocome
Date: 2012/01/31 17:40
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for todo
-- ----------------------------
DROP TABLE IF EXISTS `tocome`;
CREATE TABLE `tocome` (
  `id` int(11) NOT NULL auto_increment,
  `title` varchar(300) default NULL,
  `finished` int(11) default '0',
  `moneyed` int(11) default '0',
  `post_date` datetime default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records 
-- ----------------------------
INSERT INTO `tocome` VALUES ('4', '这是一条测试0', '1', '0', '2011-06-04 23:00:47');
INSERT INTO `tocome` VALUES ('5', '这是一条测试1', '1','0', '2011-06-04 23:01:31');
INSERT INTO `tocome` VALUES ('6', '这是一条测试2', '1','1', '2012-01-31 11:01:31');
INSERT INTO `tocome` VALUES ('7', '这是一条测试3', '1','1', '2012-01-31 11:01:35');
