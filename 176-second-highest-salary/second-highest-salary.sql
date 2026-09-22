# Write your MySQL query statement below
SELECT 
    CASE 
        WHEN COUNT(*) =0 THEN NULL
        ELSE MAX(salary)
    END AS SecondHighestSalary
    FROM (
        SELECT salary,DENSE_RANK() OVER (ORDER BY salary DESC) AS r
        FROM Employee
    ) t
    WHERE r =2;