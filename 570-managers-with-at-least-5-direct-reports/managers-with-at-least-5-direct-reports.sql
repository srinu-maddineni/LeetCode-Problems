# Write your MySQL query statement below
SELECT m.name 
FROM Employee e
JOIN Employee m
ON m.id = e.managerId
Group BY m.id
HAVING COUNT(*)>=5