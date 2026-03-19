--  CREATE DATABASE
CREATE DATABASE userdb;

--  USE DATABASE
USE userdb;

--  CREATE TABLE
CREATE TABLE userlogin (
    userid INT PRIMARY KEY,
    username VARCHAR(30),
    userpassword VARCHAR(30)
);

-- INSERT DATA
INSERT INTO userlogin (userid, username, userpassword)
VALUES 
(1, 'santhosh', 'pass777'),
(2, 'kumar', 'kumar1707'),
(3, 'ajith kumar', 'ajith0075');

--  SELECT ALL DATA
SELECT * FROM userlogin;

-- UPDATE DATA
UPDATE userlogin
SET userpassword = 'newpass123'
WHERE userid = 1;

--  SELECT WITH WHERE 
SELECT * FROM userlogin
WHERE username = 'santhosh';

--  DELETE DATA
DELETE FROM userlogin
WHERE userid = 2;

--  FINAL SELECT 
SELECT * FROM userlogin;