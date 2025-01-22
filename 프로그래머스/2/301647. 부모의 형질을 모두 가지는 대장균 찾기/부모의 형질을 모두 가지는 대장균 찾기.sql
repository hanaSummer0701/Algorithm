-- MYSQL
SELECT B.ID, B.GENOTYPE, P.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA B
     JOIN ECOLI_DATA P
     ON B.PARENT_ID = P.ID
WHERE (B.GENOTYPE & P.GENOTYPE) = P.GENOTYPE
ORDER BY B.ID;