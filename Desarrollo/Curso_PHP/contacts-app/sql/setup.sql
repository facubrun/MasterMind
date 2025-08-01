-- contacts-app database setup script
DROP DATABASE IF EXISTS contacts_app;

CREATE DATABASE contacts_app;

USE contacts_app;


-- user & contacts tables
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    user_id INT NOT NULL,
    phone_number VARCHAR(255),

    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- address table

CREATE TABLE address (
    id INT AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(255),
    user_id INT NOT NULL,

    FOREIGN KEY (user_id) REFERENCES users(id)
);