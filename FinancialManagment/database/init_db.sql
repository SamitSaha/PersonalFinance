-- Create Database
CREATE DATABASE PersonalFinanceDB;

USE PersonalFinanceDB;

-- Users Table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

-- Income Table
CREATE TABLE income (
    income_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    source VARCHAR(100),
    amount FLOAT,
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Expenses Table
CREATE TABLE expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category VARCHAR(100),
    amount FLOAT,
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Savings Table
CREATE TABLE savings (
    savings_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    goal_amount FLOAT,
    current_savings FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
