SET NAMES utf8mb4

-- convert database to utf8
ALTER DATABASE hbtn_0c_0 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- convert table
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- convert field
ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;