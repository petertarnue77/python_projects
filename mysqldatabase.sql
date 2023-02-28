-- How to craete Functional Databases in mysql
-- Making use of the Data Definition Language (DDL)
   -- command (CREATE, ALTER, DROP)

-- Kelvin device Database
--CRUD Operation in databases
CREATE DATABASE mc_devices;

--Select database for usage
USE mc_devices;

-- Crate stock table
CREATE TABLE stock (
    deviceID int NotNull,
    deviceQuanty int NotNull,
    totoal_price decimal NotNull
);

--Create Customers table
CREATE TABLE customers (
    --column name, data type, contraints
    CustomerID char(9) NotNull, 
    FirstName varchar(100) NotNull,
    LastName varchar(100) NotNull,
    Company varchar(100) NotNull,
    CustomerAddress text(500) NotNull,
    City varchar(100), NotNull,
    CustomerState varchar(100), NotNull,
    Country varchar(100), NotNull,
    PostalCode varchar(40) NotNull,
    Phone varchar(20) NotNull,
    Fax varchar(23) NotNull,
    EmailAddress varchar(255) NotNull,
    SuppoertRapid int NotNull
);
-- Create feedback table
CREATE TABLE feedbacks (
    feedbackID varchar(8),
    feedbackType varchar(10),
    feedbackComment text(500)
);

-- show table created
SHOW tables; 

-- Show columns from table created
SHOW columns FROM Customers;

--Droping Database 
DROP DATABASE cm_devices; 

-- Altering a Database
ALTER TABLE customers ADD (
    ContactNumber varchar(20),
    age int, NotNull,
    Nationality varchar(20)
)

--Alter table to remove "nationality"
ALTER TABLE customers DROP COLUMN nationality 

--Alter the data type of a column
ALTER TABLE customers MODIFY Country varchar(25);

-- Populating data in a Database 
INSERT INTO customers (
    CustomerID, FirstName, LastName, Company, CustomerAddress,
    City, CustomerState, Country, PostalCode, Phone, Fax, EmailAddress, SuppoertRapid
)
VALUES (001,"peter","tarnue","Ycwl", ...),
    (002, "kollie" , "tarnue", "mono", ..),
    (003, "esther", "wolobah", "ycwl", ..) 

--Using the INSERT INTO select statement 
-- this command is used to qury data from one table and put into another
-- table
INSERT INTO target_table (colun_name) 
select (column_name)
from source_table

--How to update record in a database table
UPDATE customers 
SET FirstName="Wolobah", LastName="Tarnuewu"
WHERE CustomerID = 002

-- Update all engineering college student
UPDATE customers 
SET Country = "Liberia"
Where LastName = "Tarnue"

--- Updating multiple columns
UPDATE customers 
SET Country = "Liberia", age= 30,
Where LastName = "Tarnue" 


--Deleting rocord from a database table
DELETE FROM Customers 
WHERE LastName == "Tarnue"

--Deleting multiple records from a table
DELETE FROM Customers 
WHERE College == "engineering" 


--Deleting all records from a talbe
DELETE FROM customers  


-- ARITHEMATIC OPERATION IN SQL
SELECT 5 + 5 -- addition operation
SELECT 5 - 5 -- subtration operation
SELECT 5 * 5 -- multiplication operation
SELECT 5 / 5 -- division opertion
SELECT 5 % 5 -- modulus operation. it return the remainder

-- YCWL database
CREATE DATABASE ycwl_db;
USE ycwl; 

CREATE TABLE employee (
    employeeID char(5),
    employeeName varchar(20),
    birthDate date, 
    homeAdress varchar(50),
    assignedLocation  varchar(20),
    salary decimal,
    allowance decimal,
    tax decimal
) 

--Insert data into employee table
INSERT INTO employee (
    employeeID,employeeName,birthDate,
    homeAdress,assignedLocation,salary,allowance
)
VALUES (023, "Peter K Tarnue", 04/23/1992, "Harbel", "Charlesville", 500, 20) 
    (020, "Sizi W. Ford", 01/04/1991, "Harbel", "Charlesville", 500, 20)
    (025, "Weegie Melvin Taylor", 04/2/1985, "Monrovia", "Charlesville", 500, 20)

-- ARITHMETIC OPERATIONS 

-- ADDITION OPERATOR
--  EX.1
SELECT (salary + allowance) as fullSallary 
FROM employee ;

-- EX.2
SELECT * 
FROM employee
WHERE   (salary + allowance) =  2500 ;


-- SUBTRACTION OPERATOR
--EX.1
SELECT (salary - allowance) AS salaryAllowance
FROM employee ;

-- EX.2 
SELECT * 
FROM employee 
WHERE (salary - allowance) = 100; 

-- SQL comparision Operators
-- (= equal to),(< less than), (> greater than), (<= less than or equal to)
-- (> greater than or equal to), (<> not equal to)  
-- Examples 
SELECT * 
FROM employee
WHERE salary = 500; 

SELECT * 
FROM employee 
WHERE salary < 500;

SELECT * 
FROM employee 
WHERE salary > 500;

SELECT * 
FROM employee 
WHERE salary <= 500; 

SELECT * 
FROM employee 
WHERE salary >= 500; 

SELECT * 
FROM employee 
WHERE salary <> 500; 


-- The WHERE CLAUSE 
SELECT * 
FROM employee 
WHERE employeeName Like "Sc%" --- search for employee in table whose name starts with "Sc"  

-- The WHERE CLAUSE 
SELECT * 
FROM employee 
WHERE employeeName Like "%ter"; --- search for employee in table whose name ends with "ter"

-- The WHERE CLAUSE 
SELECT * 
FROM employee 
WHERE employeeName IN("USA", "UK"); --- search for employee in table who are from USA and UK" 

--- The DISTINCT CLAUSE 
SELECT DISTINCT employeeName 
FROM employee 
WHERE employeeName;

--- The COUNT & DISTINCT CLAUSE 
SELECT COUNT(DISTINCT employeeName) 
FROM employee; 

SELECT SUM(DISTINCT salary) 
FROM employee;

SELECT  (DISTINCT employeeName) 
FROM employee; 

-- building database 
-- Building a database schema for a restuarent booking scenario
---Few things to consider why buiding the schema of this database
   --- You must counsider that customers make reservations for table and those tables 
    -- have orders associated with with them.
    -- an order will have associated menu items that belong to a menu.
    -- And the orders  are served by a waiter 

-- THE LOGICAL DATABASE SCHEMA 
-- In an example like this, databse engineers usually draw 
-- a diagram known as ER-D (Entity Relationship Diagram) 


--CREATE RESTAURENT DATABASE
CREATE DATABASE restuarent;

-- USE RESTAURENT DATABASE 
USE restuarent;

-- LOCATION TABLE 
CREATE TABLE tbl (
    table_id INT,
    locatioin varchar(255),
    PRIMARY KEY (table_id)
); 

-- WAITER TABLE
CREATE TABLE waiter (
   wiater_id INT, 
   name varchar(150),
   contact_no varchar(10),
   shift VARCHAR(10),
   PRIMARY KEY (waiter_id)
); 

-- ORDER TABLE
CREATE TABLE Table_order (
    order_id INT,
    date_time DATETIME,
    waiter_id INT,
    table_id INT,
    PRIMARY KEY (order_id) 
    FOREIGN KEY (table_id) REFERENCES tbl(table_id),
    FOREIGN KEY (waiter_id) REFERENCES waiter(wiater_id),
); 

-- CUSTOMER TABLE
CREATE TABLE customer (
    customer_id INT,
    name VARCHAR(100),
    NIC_no VARCHAR(12),
    contact_no VARCHAR(10)
    PRIMARY KEY (customer_id)
);
-- RESERVATION TABLE
CREATE TABLE reservation (
    reservation_id INT, 
    date_time DATETIME,
    number_of_pax INT,
    order_id INt,
    table_id INT, 
    customer_id INT 

    PRIMARY KEY (reservation_id) 

    FOREIGN KEY (order_id) REFERENCES Table_order(order_id),
 
    FOREIGN KEY (table_id) REFERENCES tbl(table_id)
  
    FOREIGN key (customer_id) REFERENCES customer(customer_id)
);

-- menu table 
CREATE TABLE menu(
    menu_id INT,
    description VARCHAR(255),
    availability INT, 
    PRIMARY KEY (menu_id)
); 

-- MENU ITEMS TABLE 
CREATE TABLE menu_item(
    menu_item_id INT,
    description VARCHAR(255),
    price FLOAT 
    availability INT, 
    menu_id, INT, 
    PRIMARY KEY (menu_item_id),
    FOREIGN KEY (menu_id) REFERENCES menu(menu_id)
); 

-- ORDER MENU ITEMS 
CREATE TABLE order_menu_item(
    order_id INT, 
    menu_item_id, INT, 
    quantity INT, 

    PRIMARY KEY (order_id, menu_item_id),
    
    FOREIGN KEY (order_id) REFERENCES Table_order(order_id),
    
    FOREIGN key (menu_item_id) REFERENCES menu_item(menu_item_id) 

)