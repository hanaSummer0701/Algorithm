-- MYSQL
SELECT HISTORY_ID,
       CAR_ID,
       DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
       DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
       CASE WHEN DATEDIFF(END_DATE,START_DATE) >= 29 THEN '장기 대여'
       ELSE '단기 대여' 
       END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(START_DATE, '%Y-%m-%d') BETWEEN '2022-09-01' AND '2022-09-31'
ORDER BY HISTORY_ID DESC;

-- ORACLE
SELECT HISTORY_ID,
       CAR_ID,
       TO_CHAR(START_DATE, 'YYYY-MM-DD') AS START_DATE,
       TO_CHAR(END_DATE, 'YYYY-MM-DD') AS END_DATE,
       CASE WHEN END_DATE - START_DATE >= 29 THEN '장기 대여'
       ELSE '단기 대여' 
       END AS RENT_TYPE
       -- 대여일 계산이므로 첫날 포함하여 +1을 해야 하기 때문에 30이 아닌 29.
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE TO_CHAR(START_DATE, 'YYYY-MM-DD') LIKE '2022-09-%'
ORDER BY HISTORY_ID DESC;
