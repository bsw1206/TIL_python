SELECT * FROM departments;
SELECT * FROM employees;

SELECT  
    d.name AS department,
    e.name AS oldest_employee,
    AVG(e.age) AS avg_age,
    MAX(e.age) AS max_age   
FROM employees AS e
INNER JOIN departments AS d
ON e.departmentId = d.id
GROUP BY d.name;

SELECT  
    d.name AS department,
    e.name AS highest_paid_employee,
    MAX(e.salary) AS max_salary   
FROM employees AS e
INNER JOIN departments AS d
ON e.departmentId = d.id
GROUP BY d.name;

SELECT 
    d.name AS department,
    CASE 
        WHEN e.age <= 30 THEN 'Under 30'
        WHEN e.age > 30 AND e.age < 40 THEN 'BETWEEN 30-40'
        WHEN e.age >= 40 THEN 'Over 40'
    END AS age_group,
    COUNT(e.id) AS num_employees
FROM employees AS e
INNER JOIN departments AS d
    ON e.departmentId = d.id    
GROUP BY         
    d.name,                              
    age_group                             
ORDER BY 
    d.name, 
    age_group;
SELECT  
    d.name AS department,
    (SUM(e.salary) - max(e.salary)) / (count(e.id)-1)  AS avg_salary_excluding_highest
     
FROM employees AS e
INNER JOIN departments AS d
ON e.departmentId = d.id
GROUP BY d.name;


