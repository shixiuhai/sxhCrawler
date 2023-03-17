/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : localhost:3306
 Source Schema         : 1688goods

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 17/03/2023 22:53:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 1688_kj_commodity
-- ----------------------------
DROP TABLE IF EXISTS `1688_kj_commodity`;
CREATE TABLE `1688_kj_commodity`  (
  `id` bigint(0) NOT NULL AUTO_INCREMENT,
  `cate_level` int(0) NULL DEFAULT NULL COMMENT '1 一级标题，2 二级标题，3 三级标题，4 四级标题，5 五级标题',
  `cate_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '标题名称',
  `gmt_create` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '上架时间',
  `gmt_create_detail` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '上架时间的精确时间',
  `offer_picurl` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '商品图片地址',
  `price` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '商品价格',
  `subject` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '商品描述',
  `offer_id` int(0) NULL DEFAULT NULL COMMENT '商品id',
  `offer_url` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '商品详情页url',
  `created_time` datetime(0) NULL DEFAULT NULL COMMENT '数据创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 1688_kj_commodity
-- ----------------------------

-- ----------------------------
-- Table structure for 1688_kj_commodity_detail
-- ----------------------------
DROP TABLE IF EXISTS `1688_kj_commodity_detail`;
CREATE TABLE `1688_kj_commodity_detail`  (
  `id` bigint(0) NOT NULL,
  `commodity_id` bigint(0) NULL DEFAULT NULL COMMENT '商品表id',
  `user_evaluate` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '买家评价',
  `created_time` datetime(0) NULL DEFAULT NULL COMMENT '数据创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 1688_kj_commodity_detail
-- ----------------------------

-- ----------------------------
-- Table structure for 1688_kj_commodity_trend
-- ----------------------------
DROP TABLE IF EXISTS `1688_kj_commodity_trend`;
CREATE TABLE `1688_kj_commodity_trend`  (
  `id` int(0) NOT NULL,
  `commodity_id` bigint(0) NULL DEFAULT NULL COMMENT '商品表id',
  `xxx1` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `xxx2` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL,
  `created_time` datetime(0) NULL DEFAULT NULL COMMENT '数据创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 1688_kj_commodity_trend
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
