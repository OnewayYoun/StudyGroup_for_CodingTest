-- WHILDCARDS
-- % = any # characters, _ = one character
--
-- Find any client's who are an LLC
SELECT *
FROM client
WHERE client_name LIKE '%LLC';

-- Find any branch suppliers who are in the label business
SELECT *
FROM branch_supplier
WHERE supplier_name LIKE '%Label%';

-- Find any employee born in October
SELECT *
FROM employee
WHERE birth_day LIKE '____-10%';

-- Find any clients who are schools
SELECT *
FROM client
WHERE client_name LIKE '%school%';

--
--UNION
--
--Rules : must have the same number of columns in both statements
--        they have to be like similar datatype
-- Find a list of employee and branch names
SELECT first_name AS Company_Names
FROM employee
UNION
SELECT branch_name
FROM branch;

-- Find a list of all clients & branch supplier's names
-- client. and branch_supplier. are optional(make reader readable where they are coming from)
SELECT client_name, client.branch_id
FROM client
UNION
SELECT supplier_name, branch_supplier.branch_id
FROM branch_supplier;

-- Find a list of all money spent or earned by the company
SELECT salary
FROM employee
UNION
SELECT total_sales
FROM works_with;