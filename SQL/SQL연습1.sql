-------------------------------------------------------------------------
-- CREATING TABLES
-------------------------------------------------------------------------
-- creating table
CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20)
);
-- describing the table
DESCRIBE student;
-- deleting table
DROP TABLE student;
-- modifying table
ALTER TABLE student ADD gpa DECIMAL(3,2);
-- removing column of table
ALTER TABLE student DROP COLUMN gpa;


-------------------------------------------------------------------------
-- INSERTING DATA
-------------------------------------------------------------------------
-- getting all(*) the information from the student table
SELECT * FROM student;
-- inserting data into table
INSERT INTO student VALUES(1, 'Jack', 'Biology');
INSERT INTO student VALUES(2, 'Kate', 'Sociology');
INSERT INTO student VALUES(4, 'Jack', 'Biology');
INSERT INTO student VALUES(5, 'Mike', 'Computer Science');
-- inserting data with not including major
INSERT INTO student(student_id, name) VALUES(3, 'Claire');
-- INSERT INTO student VALUES(3, 'Claire', 'Chemistry');

-------------------------------------------------------------------------
-- CONSTRAINTS(제약)
-------------------------------------------------------------------------
--cannot be null
--should be unique(if someone else has the same major, it will be rejected)
CREATE TABLE student (
    student_id INT,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) UNIQUE,
    PRIMARY KEY(student_id)
);

SELECT * FROM student;

INSERT INTO student VALUES(1, 'Jack', 'Biology');
INSERT INTO student VALUES(2, 'Kate', 'Sociology');
-- we cannot insert NULL value into name cuz we specified name not to be NULL
INSERT INTO student VALUES(3, NULL, 'Chemistry');
-- we cannot insert the same major cuz we specified major to be unique
INSERT INTO student VALUES(4, 'Jack', 'Biology');
INSERT INTO student VALUES(5, 'Mike', 'Computer Science');

-- if someone didn't give the major, by default it will be filled with undecided
-- automatically increamenting primary key values
CREATE TABLE student (
    student_id INT AUTO_INCREMENT,
    name VARCHAR(20),
    major VARCHAR(20) DEFAULT 'undecided',
    PRIMARY KEY(student_id)
);
INSERT INTO student(name) VALUES('Jack');
INSERT INTO student(name, major) VALUES('Kate', 'Sociology');
INSERT INTO student(name, major) VALUES(NULL, 'Chemistry');
INSERT INTO student(name, major) VALUES('Jack', 'Biology');
INSERT INTO student(name, major) VALUES('Mike', 'Computer Science');


-------------------------------------------------------------------------
-- UPDATE & DELETE
-------------------------------------------------------------------------
SELECT * FROM student;

--updating data (changing major name into 'Bio' whose name is 'Biology')
UPDATE student
SET major = 'Bio'
WHERE major = 'Biology';

--(chaning major name into 'CS' whose student_id is 4)
UPDATE student
SET major = 'CS'
WHERE student_id = 4;

--using OR logic
UPDATE student
SET major = 'Biochemistry'
WHERE major = 'Bio' OR major = 'Chemistry';

--setting multiple things
UPDATE student
SET name = 'Tom', major = 'undecided'
WHERE student_id = 1;

--applying to every single row in the table
UPDATE student
SET major = 'undecided';

SELECT * FROM student;
-- deleting all rows
DELETE FROM student;
-- deleting row that has student_id of 5
DELETE FROM student
WHERE student_id = 5;
-- deleting row that has name Tom and major
DELETE FROM student
WHERE name = 'Tom' AND major = 'undecided';


-------------------------------------------------------------------------
-- BASIC QUERIES
-------------------------------------------------------------------------
SELECT * FROM student;

INSERT INTO student VALUES(1, 'Jack', 'Biology');
INSERT INTO student VALUES(2, 'Kate', 'Sociology');
INSERT INTO student VALUES(3, 'Claire', 'Chemistry');
INSERT INTO student VALUES(4, 'Jack', 'Biology');
INSERT INTO student VALUES(5, 'Mike', 'Computer Science');

-- getting only names and majors from the table named student
SELECT name, major
FROM student;
-- same thing like above queire but it is clear which table the name and major are coming from
SELECT student.name, student.major
FROM student;
-- ordering by the name in alphabetical order based off the name
-- by default(ascending order), but if u want it in descending order, put it as
-- ORDER BY name DESC;
SELECT name, major
FROM student
ORDER BY name;
-- order by DESC order of std_id even if I'm not getting(returning) std_id
SELECT name, major
FROM student
ORDER BY student_id DESC;
-- to visualize the example above
SELECT *
FROM student
ORDER BY student_id DESC;
-- ascending order
SELECT *
FROM student
ORDER BY student_id ASC;
-- order by major first then std_id (in DESC order)
SELECT *
FROM student
ORDER BY major DESC, student_id DESC;
--limiting the amount of result
SELECT *
FROM student
ORDER BY student_id DESC
LIMIT 2;
--filtering
SELECT *
FROM student
WHERE name = 'Kate' OR major = 'Chemistry';
--comparison
-- <, >, <=, >=, =, <>, AND, OR
SELECT *
FROM student
WHERE major <> 'Chemistry';
-- more example
SELECT *
FROM student
WHERE student_id <= 3 and name <> 'Jack';
-- getting names from student table where the name is in group of values -> ('Jack', 'Mike')
SELECT *
FROM student
WHERE name IN ('Jack', 'Mike')