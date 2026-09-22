-- Write your PostgreSQL query statement below
SELECT id
FROM (
    SELECT
        id,temperature ,recordDate
        ,LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_temperature 
    FROM Weather
) t
WHERE temperature  > prev_temperature AND recordDate =prev_date+1 ;