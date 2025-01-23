-- MYSQL
-- 2022.10.5 게시물의 ID, ID, 제목, 가격, 거래상태
-- 거래상태 SALE = 판매중, RESE=예약중, DONE=거래완료
SELECT BOARD_ID,
       WRITER_ID,
       TITLE,
       PRICE,
       CASE WHEN STATUS = 'SALE' THEN '판매중'
       WHEN STATUS = 'RESERVED' THEN '예약중'
       ELSE '거래완료'
       END AS STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE = '2022-10-05'
ORDER BY BOARD_ID DESC;