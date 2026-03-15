-- burdada ozumuz yaradurug
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
IDENTIFIED BY 'user_0d_1_pwd';
-- her seyede icaze verrik niye cunki ureyimiz ele istiyir
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
