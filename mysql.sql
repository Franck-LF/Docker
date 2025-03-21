DROP DATABASE IF EXISTS persons;
CREATE DATABASE IF NOT EXISTS persons;
USE persons;

SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';

DROP TABLE IF EXISTS persons;

CREATE TABLE persons (
  firstname VARCHAR(255),
  lastname VARCHAR(255)
);

INSERT INTO persons
  (firstname, lastname)
VALUES
  ('Mike', 'Blueberry'),
  ('Bob', 'Banana');