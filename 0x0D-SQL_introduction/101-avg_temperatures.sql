-- display the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG((value * 9/5) + 32) AS avg_temp
FROM temperatures
GROUP BY city, value
ORDER BY avg_temp;
