-- Display the top 3 cities' temperature during July and August
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)  -- Filter data for July and August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;  -- Limit the results to top 3 cities
