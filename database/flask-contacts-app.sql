CREATE DATABASE flask_contacts_app;
USE flask_contacts_app;

CREATE TABLE contacts(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(150),
    phone VARCHAR(20),
    email VARCHAR(100) NOT NULL UNIQUE
);


dile que con lo que has pasado, haga el archivo directamente