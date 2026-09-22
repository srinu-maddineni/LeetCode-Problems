# Write your MySQL query statement below
-- SELECT c.name  AS Customers
-- FROM Customers AS c
-- WHERE c.id NOT IN (
--     SELECT customerId
--     FROM Orders 
-- )
SELECT C.name AS Customers
FROM Customers AS C
LEFT JOIN Orders AS O
ON c.id = o.customerId
WHERE o.customerId IS  NULL
