-- Active: 1777349674988@@127.0.0.1@3306
ALTER TABLE
zoo
DROP COLUMN species;
ALTER TABLE
zoo
ADD COLUMN
species TEXT NOT NULL DEFAULT 'default value';

UPDATE zoo SET species = 'Panthera leo' WHERE name = 'Lion';
UPDATE zoo SET species = 'Loxodonta africana' WHERE name = 'Elephant';
UPDATE zoo SET species = 'Giraffa camelopard' WHERE name = 'Giraffe';
UPDATE zoo SET species = 'Cebus capucinus' WHERE name = 'Monkey';

UPDATE zoo
SET height = height * 2.54;