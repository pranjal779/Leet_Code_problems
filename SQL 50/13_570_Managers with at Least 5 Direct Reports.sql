-- 570. Managers with at Least 5 Direct Reports
-- Table: Employee

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | department  | varchar |
-- | managerId   | int     |
-- +-------------+---------+
-- id is the primary key (column with unique values) for this table.
-- Each row of this table indicates the name of an employee, their department, and the id of their manager.
-- If managerId is null, then the employee does not have a manager.
-- No employee will be the manager of themself.
 

-- Write a solution to find managers with at least five direct reports.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Employee table:
-- +-----+-------+------------+-----------+
-- | id  | name  | department | managerId |
-- +-----+-------+------------+-----------+
-- | 101 | John  | A          | null      |
-- | 102 | Dan   | A          | 101       |
-- | 103 | James | A          | 101       |
-- | 104 | Amy   | A          | 101       |
-- | 105 | Anne  | A          | 101       |
-- | 106 | Ron   | B          | 101       |
-- +-----+-------+------------+-----------+
-- Output: 
-- +------+
-- | name |
-- +------+
-- | John |
-- +------+

-- # Write your MySQL query statement below
SELECT e.name
FROM Employee e
JOIN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    Having COUNT(*) >= 5
) m ON e.id = m.managerId;

-- Accepted
-- Runtime: 115 ms
-- Case 1
-- Input
-- Employee =
-- | id  | name  | department | managerId |
-- | --- | ----- | ---------- | --------- |
-- | 101 | John  | A          | null      |
-- | 102 | Dan   | A          | 101       |
-- | 103 | James | A          | 101       |
-- | 104 | Amy   | A          | 101       |
-- | 105 | Anne  | A          | 101       |
-- | 106 | Ron   | B          | 101       |
-- Output
-- | name |
-- | ---- |
-- | John |
-- Expected
-- | name |
-- | ---- |
-- | John |

-- Runtime
-- 762
-- ms
-- Beats
-- 9.56%

-- Hint 1
-- Try to get all the mangerIDs that have count bigger than 5
-- Hint 2
-- Use the last hint's result as a table and do join with origin table at id equals to managerId
-- Hint 3
-- This is a very good example to show the performance of SQL code. Try to work out other solutions and you may be surprised by running time difference.
-- Hint 4
-- If your solution uses 'IN' function and runs more than 5 seconds, try to optimize it by using 'JOIN' instead.
