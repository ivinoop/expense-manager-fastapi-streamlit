-- Expense Manager database schema
-- Usage: mysql -u <user> -p < schema.sql

CREATE DATABASE IF NOT EXISTS expense_manager
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

USE expense_manager;

CREATE TABLE IF NOT EXISTS expenses (
  id           INT          NOT NULL AUTO_INCREMENT,
  expense_date DATE         NOT NULL,
  amount       FLOAT        NOT NULL,
  category     VARCHAR(255) NOT NULL,
  notes        TEXT,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Sample data (required by tests/backend/test_db_helper.py)
INSERT INTO expenses (expense_date, amount, category, notes) VALUES
  ('2024-08-15', 10.0, 'Shopping', 'Bought potatoes');