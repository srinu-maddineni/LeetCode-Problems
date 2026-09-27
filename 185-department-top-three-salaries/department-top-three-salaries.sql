# Write your MySQL query statement below
SELECT  d.name AS Department , e.name AS Employee , e.salary
FROM Employee e
JOIN Department d
ON e.departmentId = d.id
WHERE 3> (
    SELECT count(distinct e1.salary) 
    FROM Employee AS e1
    WHERE e1.salary>e.salary AND e1.departmentId = e.departmentId )
order by 1, 3 desc