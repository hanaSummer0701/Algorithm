-- MYSQL
# 2022 평가 점수(상,하반기 점수합), 사번, 성명, 직책, 이메일
# HR_GRADE(1,2), EMP_NO, NAME, POSITION, EMAIL
SELECT SUM(GRA.SCORE) AS SCORE, 
       EMP.EMP_NO, 
       EMP.EMP_NAME, 
       EMP.POSITION, 
       EMP.EMAIL
FROM HR_EMPLOYEES EMP
JOIN HR_GRADE GRA ON EMP.EMP_NO = GRA.EMP_NO
WHERE GRA.YEAR = 2022
GROUP BY EMP.EMP_NO
ORDER BY SCORE DESC
LIMIT 1;
