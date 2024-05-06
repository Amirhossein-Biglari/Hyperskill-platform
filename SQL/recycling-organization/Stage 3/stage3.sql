SELECT
	'Company 1' AS company_name,
    iod.pick_up_point,
    iod.total_income,
    ood.total_outcome,
    iod.total_income - ood.total_outcome AS net_income
FROM
    (SELECT
    	pick_up_point,
     	SUM(money_in) AS total_income
    FROM
     	Income_one_day
    GROUP BY pick_up_point) iod
    INNER JOIN
    (SELECT
     	pick_up_point,
     	SUM(money_out) AS total_outcome
    FROM 
        Outcome_one_day
    GROUP BY pick_up_point) ood
    ON iod.pick_up_point = ood.pick_up_point
UNION ALL
SELECT
	'Company 2' AS company_name,
    i.pick_up_point,
    i.total_income, 
    o.total_outcome, 
    i.total_income - o.total_outcome AS net_income
FROM
    (SELECT 
    	pick_up_point,
     	SUM(money_in) AS total_income
    FROM
     	Income
    GROUP BY pick_up_point) i
    INNER JOIN
    (SELECT
     	pick_up_point,
     	SUM(money_out) AS total_outcome
    FROM
     	Outcome
    GROUP BY pick_up_point) o
    ON i.pick_up_point = o.pick_up_point
ORDER BY company_name ASC, net_income DESC