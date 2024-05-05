WITH Q1_income AS (  -- Calculating Q1 for 'income' table which is needed to calculate IQR
	SELECT
	MAX(money_in) as Q1
	FROM
	(
	SELECT
		money_in,
		NTILE(4) OVER (ORDER BY money_in) as quartile
	FROM 
		Income
	) a
	WHERE quartile = 1
	GROUP BY quartile
), Q3_income AS (  -- Calculating Q3 for 'income' table which is needed to calculate IQR
	SELECT
	MAX(money_in) AS Q3
	FROM
	(
	SELECT
		money_in,
		NTILE(4) OVER (ORDER BY money_in) as quartile
	FROM 
		Income
	) a
	WHERE quartile = 3
	GROUP BY quartile
), Q1_income_one_day AS (  -- Calculating Q1 for 'income_one_day' table which is needed to calculate IQR
	SELECT
	MAX(money_in) as Q1
	FROM
	(
	SELECT
		money_in,
		NTILE(4) OVER (ORDER BY money_in) as quartile
	FROM 
		Income_one_day
	) a
	WHERE quartile = 1
	GROUP BY quartile
), Q3_income_one_day AS (  -- Calculating Q3 for 'income_one_day' table which is needed to calculate IQR
	SELECT
	MAX(money_in) AS Q3
	FROM
	(
	SELECT
		money_in,
		NTILE(4) OVER (ORDER BY money_in) as quartile
	FROM 
		Income_one_day
	) a
	WHERE quartile = 3
	GROUP BY quartile
), median_income AS (  -- Calculating median for 'income' table
	SELECT
	MAX(money_in) AS median
	FROM
	(
	SELECT
		money_in,
		NTILE(2) OVER (ORDER BY money_in) as quartile
	FROM 
		Income
	) a
	WHERE quartile = 1
),  median_income_one_day AS (  -- Calculating median for 'income_one_day' table
	SELECT
	MAX(money_in) AS median
	FROM
	(
	SELECT
		money_in,
		NTILE(2) OVER (ORDER BY money_in) as quartile
	FROM 
		Income_one_day
	) a
	WHERE quartile = 1
)


SELECT
	'Company 1 Income' AS company_name,
    ROUND(AVG(money_in), 2) as mean,
    (SELECT median FROM median_income_one_day) AS median,
    MAX(money_in) - MIN(money_in) as total_range,
	(SELECT Q3 FROM Q3_income_one_day) - (SELECT Q1 FROM Q1_income_one_day) AS interquartile_range,
    ROUND(STDDEV(money_in), 2) as standard_deviation,
    ROUND(VARIANCE(money_in), 2) as variance
FROM 
	Income_one_day
UNION ALL
SELECT
	'Company 2 Income' AS company_name,
    ROUND(AVG(money_in), 2) as mean,
	(SELECT median FROM median_income) AS median,
    MAX(money_in) - MIN(money_in) as total_range,
    (SELECT Q3 FROM Q3_income) - (SELECT Q1 FROM Q1_income) AS interquartile_range,
    ROUND(STDDEV(money_in), 2) as standard_deviation,
    ROUND(VARIANCE(money_in), 2) as variance
FROM 
	Income;