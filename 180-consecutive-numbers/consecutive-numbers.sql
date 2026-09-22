# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums 
FROM (
    SELECT num,LAG(num,1) OVER (ORDER BY id) AS la,LAG(num,2) OVER (ORDER BY id) AS le
    FROM Logs
)t
WHERE num =la AND le = num