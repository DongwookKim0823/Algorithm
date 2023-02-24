-- 코드를 입력하세요
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') REVIEW_DATE
FROM MEMBER_PROFILE MP
    JOIN REST_REVIEW RR ON MP.MEMBER_ID = RR.MEMBER_ID
WHERE MP.MEMBER_ID IN (SELECT MEMBER_ID
                        FROM (SELECT MEMBER_ID, COUNT(*) CNT
                                FROM REST_REVIEW
                                GROUP BY MEMBER_ID
                                ORDER BY COUNT(*)) T2
                        WHERE CNT IN (SELECT MAX(CNT) CNT
                                    FROM (SELECT MEMBER_ID, COUNT(*) CNT
                                        FROM REST_REVIEW
                                        GROUP BY MEMBER_ID
                                        ORDER BY COUNT(*)) T1))
ORDER BY REVIEW_DATE, REVIEW_TEXT