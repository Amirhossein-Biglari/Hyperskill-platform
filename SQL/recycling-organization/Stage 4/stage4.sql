SELECT 
	pick_up_point AS pick_up_point,
    a.date As date,
    CASE
        WHEN total_outcome_od = total_outcome_o THEN 'both'
        WHEN total_outcome_od IS NULL OR total_outcome_o IS NULL THEN 'once a day'
        ELSE 'more than once a day'
    END AS text
FROM
(
SELECT
        ood.pick_up_point as pick_up_point,
        ood.date as date,
        ood.sum_money_out AS total_outcome_od,
        o.sum_money_out AS total_outcome_o
FROM 
	(SELECT 
		pick_up_point,
        date,
        SUM(money_out) AS sum_money_out
	 FROM 
		Outcome_one_day
	 GROUP BY pick_up_point, date) ood
LEFT JOIN 
	(SELECT
		pick_up_point,
        date,
        SUM(money_out) AS sum_money_out
	 FROM 
		Outcome
	 GROUP BY pick_up_point, date) o
ON ood.pick_up_point = o.pick_up_point AND ood.date = o.date
UNION
SELECT
        o.pick_up_point as pick_up_point,
        o.date as date,
        ood.sum_money_out AS total_outcome_od,
        o.sum_money_out AS total_outcome_o
    FROM 
        (SELECT
			pick_up_point,
            date,
            SUM(money_out) AS sum_money_out
         FROM 
			Outcome_one_day
         GROUP BY pick_up_point, date) ood
    RIGHT JOIN 
        (SELECT
			pick_up_point,
            date,
            SUM(money_out) AS sum_money_out
         FROM 
			Outcome
         GROUP BY pick_up_point, date) o
    ON ood.pick_up_point = o.pick_up_point AND ood.date = o.date
    WHERE ood.pick_up_point IS NULL OR ood.date IS NULL
) a