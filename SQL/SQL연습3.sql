-- Find all employees ordred by salary
SELECT *
FROM employee
ORDER BY salary DESC;

-- Find all employees ordered by sex then name
SELECT *
FROM employee
ORDER BY sex, first_name, last_name;

--Find the first 5 employees in the table
SELECT *
FROM employee
LIMIT 5;

--Find the first and last names of all employees
SELECT first_name, last_name
FROM employee;

--Find the forename and surnames names of all employees
SELECT first_name AS forenames, last_name AS surname
FROM employee;

--Find out all the different genders
SELECT DISTINCT sex
FROM employee;
--Find out all the diff branch_id
SELECT DISTINCT branch_id
FROM employee;

--
--
--

--Find the number of employees
SELECT COUNT(emp_id)
FROM employee;
--Find the number of supervisor
SELECT COUNT(super_id)
FROM employee;

--Find the number of female employees born after 1970
SELECT COUNT(emp_id)
FROM employee
WHERE sex = 'F' AND birth_day >= '1971-01-01';

SELECT * FROM employee;

--Find the average of all employee's salaries
SELECT AVG(salary)
FROM employee;
--Find the average of all employee's salaries who are male
SELECT AVG(salary)
FROM employee
WHERE sex = 'M';
--Find the sum of all employee's salaries
SELECT SUM(salary)
FROM employee;

--AGGREGATION
--Find out how many males and females there are
SELECT COUNT(sex), sex
FROM employee
GROUP BY sex;
--Find the total sales of each salesman
SELECT SUM(total_sales), emp_id
FROM works_with
GROUP BY emp_id;

SELECT SUM(total_sales), client_id
FROM works_with
GROUP BY client_id;