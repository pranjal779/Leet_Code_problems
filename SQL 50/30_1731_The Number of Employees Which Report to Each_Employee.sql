-- # Write your MySQL query statement below
SELECT m.employee_id, m.name, COUNT(e.reports_to) as reports_count, ROUND(AVG(e.age * 1.0), 0) as average_age
FROM Employees e JOIN Employees m ON e.reports_to = m.employee_id
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id;
