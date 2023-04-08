/*
Navicat MySQL Data Transfer

Source Server         : local_mysql
Source Server Version : 80028
Source Host           : localhost:3306
Source Database       : public

Target Server Type    : MYSQL
Target Server Version : 80028
File Encoding         : 65001

Date: 2023-02-23 13:14:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for eyesight_res
-- ----------------------------
DROP TABLE IF EXISTS `eyesight_res`;
CREATE TABLE `eyesight_res` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `depart_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT '' COMMENT '单位id',
  `depart_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT '' COMMENT '单位名称',
  `user_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT '' COMMENT '用户id',
  `user_code` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '序号/学号',
  `user_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT '' COMMENT '用户名',
  `user_sex` int DEFAULT '0' COMMENT '性别：0-男；1-女',
  `left_eyesight` decimal(12,1) DEFAULT '0.0' COMMENT '左眼视力',
  `right_eyesight` decimal(12,1) DEFAULT NULL COMMENT '右眼视力',
  `device_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT '' COMMENT '测试设备名称',
  `device_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT '' COMMENT '测试设备编号',
  `test_time` datetime DEFAULT NULL COMMENT '测试时间',
  `memo` varchar(2000) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT '' COMMENT '其它备注',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `create_user_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT '' COMMENT '创建者用户id',
  `update_user_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT '' COMMENT '更新者用户id',
  `is_deleted` int NOT NULL DEFAULT '0' COMMENT '是否删除：0-否；1-是',
  `enable_mark` int NOT NULL DEFAULT '1' COMMENT '是否允许：0-否；1-是',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci COMMENT='检测结果表';

-- ----------------------------
-- Records of eyesight_res
-- ----------------------------
INSERT INTO `eyesight_res` VALUES ('1', '', '1', '', '1', '1', '0', '5.0', '1.0', '1', '1', '2023-02-23 12:57:03', '', '2023-03-02 12:57:14', '2023-02-23 12:57:29', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('2', '', '', '', '1', '', '0', '5.3', '12.0', '', '', '2023-02-17 12:57:35', '', '2022-05-04 12:57:43', '2023-02-23 12:57:51', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('3', '', '', '', '3', '', '0', '5.0', '3.0', '', '', '2023-02-23 13:01:05', '', '2022-10-01 13:00:57', '2023-02-23 13:01:15', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('4', '', '', '', '4', '', '0', '5.0', null, '', '', null, '', '2022-05-19 13:03:10', '2023-02-23 13:03:32', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('5', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2023-05-23 13:04:55', '2023-02-23 13:06:35', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('6', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2023-05-23 13:06:37', '2023-02-23 13:06:45', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('7', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2023-03-30 13:10:53', '2023-02-23 13:11:04', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('8', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2023-06-22 13:11:05', '2023-02-23 13:11:14', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('9', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-06-23 13:11:31', '2023-02-23 13:11:45', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('10', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-03-23 13:11:55', '2023-02-23 13:12:05', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('11', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-12-23 13:12:10', '2023-02-23 13:12:21', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('12', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-06-23 13:12:26', '2023-02-23 13:12:36', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('13', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-02-23 13:13:08', '2023-02-23 13:13:21', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('14', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-04-23 13:13:23', '2023-02-23 13:13:34', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('15', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-08-23 13:13:39', '2023-02-23 13:13:48', '', '', '0', '1');

INSERT INTO `eyesight_res` VALUES ('1', '', '1', '', '1', '1', '0', '5.0', '1.0', '1', '1', '2023-02-23 12:57:03', '', '2023-03-02 12:57:14', '2023-02-23 12:57:29', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('2', '', '', '', '1', '', '0', '5.3', '12.0', '', '', '2023-02-17 12:57:35', '', '2022-05-04 12:57:43', '2023-02-23 12:57:51', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('3', '', '', '', '3', '', '0', '5.0', '3.0', '', '', '2023-02-23 13:01:05', '', '2022-10-01 13:00:57', '2023-02-23 13:01:15', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('4', '', '', '', '4', '', '0', '5.0', null, '', '', null, '', '2022-05-19 13:03:10', '2023-02-23 13:03:32', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('5', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2023-05-23 13:04:55', '2023-02-23 13:06:35', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('6', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2023-05-23 13:06:37', '2023-02-23 13:06:45', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('7', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2023-03-30 13:10:53', '2023-02-23 13:11:04', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('8', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2023-06-22 13:11:05', '2023-02-23 13:11:14', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('9', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-06-23 13:11:31', '2023-02-23 13:11:45', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('10', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-03-23 13:11:55', '2023-02-23 13:12:05', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('11', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-12-23 13:12:10', '2023-02-23 13:12:21', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('12', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-06-23 13:12:26', '2023-02-23 13:12:36', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('13', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-02-23 13:13:08', '2023-02-23 13:13:21', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('14', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-04-23 13:13:23', '2023-02-23 13:13:34', '', '', '0', '1');
INSERT INTO `eyesight_res` VALUES ('15', '', '', '', '1', '', '0', '5.0', null, '', '', null, '', '2022-08-23 13:13:39', '2023-02-23 13:13:48', '', '', '0', '1');
