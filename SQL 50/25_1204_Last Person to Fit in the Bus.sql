-- # Write your MySQL query statement below
SELECT person_name FROM Queue q WHERE (SELECT Sum(weight) FROM queue WHERE q.turn >= turn) <= 1000
ORDER BY turn DESC
LIMIT 1;
