-- CREATING A TABLE
DROP TABLE student;

CREATE TABLE student(
    student_id INT PRIMARY KEY, 
    Name VARCHAR(30),
    course VARCHAR(30)
);

-- To see the values in the table
SELECT*FROM student;

-- Describing the table structure
DESCRIBE student; -- to see the structure of the table

-- DROP TABLE student;   
DROP TABLE student;

-- Altering the table to add a new column
ALTER TABLE student ADD age INT;

-- Altering multiple columns to the database
ALTER TABLE student 
    ADD COLUMN enrollment_no VARCHAR(12),
    ADD COLUMN SECTION VARCHAR(15);


-- Inserting values into the table
INSERT INTO student VALUES(1 ,'Anurag', 'CSE', 20);

-- Insering values into the table with specific columns/attributes
INSERT INTO student(student_id, Name, Course) VALUES(2, 'Mohit', 'CSE DS');
INSERT INTO student(student_id, Name, Course) VALUES(3, 'Rohit', 'CSE AI');


-- Renaming a table
ALTER TABLE old_table_name
RENAME TO new_table_name;

----------------------------------------------------------------------------------------------------------------------
-- CREATING A TABLE WITH CONSTRAINTS
DROP TABLE student;

-- Creating a table with constraints
CREATE TABLE student(
    student_id INT,
    name VARCHAR(20) NOT NULL,
    SECTION VARCHAR(15) DEFAULT 'CSE-7',
    enrollment_no VARCHAR(12) UNIQUE,
    PRIMARY KEY(enrollment_no)
);

-- Inserting values into the table
INSERT INTO student(student_id, name, enrollment_no) VALUES(1, 'Anurag', 'A1234567890');
INSERT INTO student VALUES(2, 'HARSHIL', 'CSE-7', 'A2365987410' );

-- Inserting multiple values/rows into the table at once
INSERT INTO student(student_id, name, enrollment_no) VALUES
(3, 'Mohit', 'A3456789120'),
(4, 'Rohit', 'A4567891230'),
(5, 'Soham', 'A5678912340');



-- Creating temporary table
DROP TABLE IF EXISTS temp_student;
CREATE TEMPORARY TABLE temp_student (
  id INT,
  marks INT
);


-- Copy the table structure without data
CREATE TABLE student_template LIKE student;
SELECT * FROM student_template;

-- Copy the table structure with data
CREATE TABLE student_backup AS SELECT * FROM student;
SELECT * FROM student_backup;


----------------------------------------------------------------------------------------------------------------------
-- UPDATE OPERATIONS ON TABLE
DROP TABLE student;

CREATE TABLE student(
    student_id INT AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(50) ,
    enrollment_no VARCHAR(12) UNIQUE,
    PRIMARY KEY(student_id)
);

INSERT INTO student(name, major, enrollment_no) VALUES
('Anurag', 'Computer Science', 'A123654987'),
('Tanmay', 'Automobile', 'A258741369'),
('Naman', 'Electronic & Communication Engineering', 'A123456987'),
('Anu', 'Computer Science', 'A254136987'),
('Raman', 'Biology', 'A523698741'),
('Rohan', 'Chemistry', 'A963258741');

SELECT*FROM student;

-- Updating a record in the table
UPDATE student
SET major = 'CSE'
WHERE major='Computer Science';

UPDATE student
SET major = 'ECE'
Where major = 'Electronic & Communication Engineering';

UPDATE student
SET major = 'CSE'
WHERE name = 'Tanmay';

UPDATE student
SET major = 'Biochemistry'
WHERE major = 'Chemistry' OR major = 'Biology';


-- DELETE OPERATIONS ON TABLE
--Deleting all values/rows from the table
DELETE FROM student;

-- Deleting specific values/rows from the table
DELETE FROM student
WHERE student_id =3;

DELETE FROM student
WHERE major = 'CSE';

-- Deleting multiple values/rows from the table
DELETE FROM student
WHERE major = 'ECE' OR major = 'Biochemistry';
-- OR
DELETE FROM student
WHERE major IN ('ECE', 'Biochemistry');


-----------------------------------------------------------------------------------------------------------------------
-- BASIC QUERIES 
SELECT * FROM student;

-- Selecting specific columns
SELECT name
FROM student;
-- OR
SELECT student.name, student.major, student.student_id
FROM student
ORDER BY name; -- Ascending order by default using name column
-- OR
ORDER BY student_id DESC; -- Descending order using name column

-- Playing with WHERE keyword
SELECT student.name, student.major, student.student_id
FROM student
WHERE major ='Computer Science'; -- Selecting only CSE students
 -- <, >, <=, >=, != (<>), AND, OR, IN
SELECT student.name, student.major, student.student_id
FROM student
WHERE major <> 'Computer Science'; -- Selecting all students except CSE students

SELECT student.name, student.major, student.student_id
FROM student
WHERE name IN ('Anurag', 'Anu', 'Tanmay') AND student_id<=2; -- Selecting specific students   


