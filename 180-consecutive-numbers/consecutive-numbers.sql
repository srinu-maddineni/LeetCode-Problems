# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums 
FROM (
    SELECT num,LAG(num) OVER (ORDER BY id) AS la,LEAD(num) OVER (ORDER BY id) AS le
    FROM Logs
)t
WHERE num =la AND le = num