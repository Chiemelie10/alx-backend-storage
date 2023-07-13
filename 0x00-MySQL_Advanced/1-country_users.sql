-- This script creates a table 'users' that has the following columns:
-- 1) id, integer, never null, auto increment and primary key.
-- 2) email, string (255 characters), never null and unique.
-- 3) name, string (255 characters).
-- 4) country, enumeration of countries: US, CO and TN, never null(default
--    will be the first element of the enumeration, here US)
-- Additional instructions:
-- The script should not fail if the table already exists.
-- The script can be executed from any database.


-- Creates users table with columns id, email, name, country.
CREATE TABLE IF NOT EXISTS `users` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `name` VARCHAR(255),
  `country` ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
