-- 코드를 작성해주세요
SELECT
    SCORE,
    HE.EMP_NO,
    EMP_NAME,
    POSITION,
    EMAIL
FROM (
    SELECT
        EMP_NO,
        SUM(SCORE) AS SCORE
    FROM
        HR_GRADE
    WHERE
        YEAR = 2022
    GROUP BY
        EMP_NO
    ORDER BY
        SCORE DESC
    LIMIT 1
) AS HG
JOIN
    HR_EMPLOYEES AS HE
ON HG.EMP_NO = HE.EMP_NO
