-- 코드를 입력하세요
SELECT FLAVOR
FROM (SELECT FIRST_HALF.FLAVOR, SUM(FIRST_HALF.TOTAL_ORDER) + SUM(JULY.TOTAL_ORDER) TOTAL_ORDER
        FROM FIRST_HALF
            JOIN JULY ON FIRST_HALF.FLAVOR = JULY.FLAVOR
        GROUP BY FLAVOR
        ORDER BY TOTAL_ORDER DESC) T
LIMIT 3