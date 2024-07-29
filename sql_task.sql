-- Выберите уникальные регионы сбора грибов.
SELECT DISTINCT name FROM regions

-- Выведите название, сезон сбора и съедобность грибов, которые относятся к категории «Трубчатые».
SELECT (M.name, M.seson, M.edible) FROM  Mushrooms 
JOIN categories ON M.category_id = C.category_id WHERE C.name (трубчатые)

-- Посчитайте количество грибов для каждой категории. Выведите название категории и количество в порядке убывания.
SELECT C.name, COUNT(M.mushroom_id ) AS mus_co
FROM categories JOIN Mushrooms ON C.category_id = M.category_id
GROUP BY C.name ORDER BY mus_co DESC

-- Выведите названия всех грибов, которые растут весной, относятся к категории «Пластинчатые» и которые лучше всего собирать в местах размером до 6000 условных единиц (size).
SELECT M.name FROM Mushrooms
JOIN categories ON C.category_id = M.category_id
JOIN regions ON M.primary_region_id = R.region_id
WHERE M.seson = "весна" AND C.name = "пластичные"
AND R.size < 6000