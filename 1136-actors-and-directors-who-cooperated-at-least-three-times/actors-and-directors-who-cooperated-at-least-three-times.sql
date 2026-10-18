# Write your MySQL query statement below
SELECT actor_id , director_id
FROM ActorDirector as a 
GROUP BY actor_id,director_id
HAVING COUNT(*)>=3