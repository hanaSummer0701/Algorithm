-- ORACLE
-- SELECT BOOK_ID, TO_CHAR(PUBLISHED_DATE, 'YYYY-MM-DD') AS PUBLISHED_DATE
-- FROM BOOK
-- WHERE TO_CHAR(PUBLISHED_DATE, 'YYYY') = '2021' AND CATEGORY = '인문'
-- ORDER BY BOOK_ID ASC;

SELECT
    BOOK_ID,
    TO_CHAR(PUBLISHED_DATE, 'YYYY-MM-DD')
FROM BOOK
WHERE CATEGORY = '인문' AND TO_CHAR(PUBLISHED_DATE, 'YYYY') = '2021'
ORDER BY PUBLISHED_DATE ASC