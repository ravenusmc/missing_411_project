CREATE DATABASE missing_411;

use missing_411;

--Table for the users. 
CREATE TABLE users
(
  user_id INT NOT NULL AUTO_INCREMENT,
  firstName VARCHAR(240) NOT NULL,
  lastName VARCHAR(240) NOT NULL,
	username VARCHAR(240) NOT NULL,
  email VARCHAR(240) NOT NULL,
  password VARCHAR(240) NOT NUll,
  PRIMARY KEY(user_id)
);