CREATE DATABASE IF NOT EXISTS taskdb;

USE taskdb;

CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL
);

INSERT INTO tasks (title, status) VALUES
('Learn Docker', 'Pending'),
('Learn Docker Compose', 'Pending'),
('Learn Jenkins', 'Completed');
