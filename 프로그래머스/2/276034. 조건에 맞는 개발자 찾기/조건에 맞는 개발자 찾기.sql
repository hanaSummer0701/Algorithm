-- MYSQL
SELECT DISTINCT DE.ID, DE.EMAIL, DE.FIRST_NAME, DE.LAST_NAME
FROM DEVELOPERS DE
JOIN SKILLCODES S
ON (DE.SKILL_CODE & S.CODE) = S.CODE AND  S.NAME IN ('Python', 'C#')
ORDER BY DE.ID;