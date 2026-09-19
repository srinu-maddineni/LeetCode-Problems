-- Write your PostgreSQL query statement below
SELECT d.name AS Department,e.name AS Employee,e.salary AS Salary
FROM Employee AS e
JOIN Department AS d
ON e.departmentId = d.id
where e.salary = (
    SELECT max(e1.salary)
    FROM Employee AS e1
    where e.departmentId = e1.departmentId
)