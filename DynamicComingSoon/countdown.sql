CREATE DATABASE coming_soon;

USE coming_soon;

CREATE TABLE countdown (
    id INT AUTO_INCREMENT PRIMARY KEY,
    launch_date DATETIME NOT NULL,
    message VARCHAR(255) NOT NULL
);

INSERT INTO countdown (launch_date, message) VALUES 
('2025-01-30 00:00:00', 'Our website is launching soon!');
