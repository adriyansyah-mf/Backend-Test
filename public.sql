/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : PostgreSQL
 Source Server Version : 160001 (160001)
 Source Host           : localhost:5432
 Source Catalog        : test
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 160001 (160001)
 File Encoding         : 65001

 Date: 29/05/2024 21:56:57
*/


-- ----------------------------
-- Sequence structure for admin_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."admin_id_seq";
CREATE SEQUENCE "public"."admin_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for user_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."user_id_seq";
CREATE SEQUENCE "public"."user_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS "public"."admin";
CREATE TABLE "public"."admin" (
  "id" int8 NOT NULL DEFAULT nextval('admin_id_seq'::regclass),
  "name" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "hashed_password" varchar(250) COLLATE "pg_catalog"."default" NOT NULL,
  "is_login" bool
)
;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO "public"."admin" VALUES (1, 'admin', '$2b$12$kPZCtTUXrT1hSnJTeqcGMuAkMFdJOGOSisenAxfnvS1HHeSsWO21C', 't');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "public"."user";
CREATE TABLE "public"."user" (
  "id" int8 NOT NULL DEFAULT nextval('user_id_seq'::regclass),
  "name" varchar(100) COLLATE "pg_catalog"."default" NOT NULL,
  "hashed_password" varchar(250) COLLATE "pg_catalog"."default" NOT NULL
)
;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO "public"."user" VALUES (2, 'string', '$2b$12$qHDT0rKFUr9PLl9IRao/Ue0iE2eVlW0ldZUJvDBRGiXekWS05.VpG');
INSERT INTO "public"."user" VALUES (1, 'string', '$2b$12$9StE9z7Hdl8sCBoEuQNLFOXl5dpx3KEa1f8qY.lA3X66OfzXB0XyS');

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."admin_id_seq"
OWNED BY "public"."admin"."id";
SELECT setval('"public"."admin_id_seq"', 1, true);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."user_id_seq"
OWNED BY "public"."user"."id";
SELECT setval('"public"."user_id_seq"', 2, true);

-- ----------------------------
-- Uniques structure for table admin
-- ----------------------------
ALTER TABLE "public"."admin" ADD CONSTRAINT "admin_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table admin
-- ----------------------------
ALTER TABLE "public"."admin" ADD CONSTRAINT "admin_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table user
-- ----------------------------
ALTER TABLE "public"."user" ADD CONSTRAINT "user_pkey" PRIMARY KEY ("id");
