CREATE DATABASE persons;
use persons;

CREATE TABLE persons (
  firstname VARCHAR(255),
  lastname VARCHAR(255)
);

INSERT INTO persons
  (firstname, lastname)
VALUES
  ('Mike', 'Blueberry'),
  ('Bob', 'Banana');