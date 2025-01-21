-- ORACLE
SELECT A.FLAVOR
FROM ICECREAM_INFO A
JOIN FIRST_HALF B ON A.FLAVOR = B.FLAVOR
WHERE TOTAL_ORDER >= 3000 AND INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC;