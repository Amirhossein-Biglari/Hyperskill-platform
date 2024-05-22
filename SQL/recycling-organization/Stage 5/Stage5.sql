WITH CombinedIncome AS  (
	SELECT 
		pick_up_point,
		date,
		SUM(money_in) AS total_money_in
	FROM
	(
		SELECT 
			pick_up_point,
            date,
            money_in
		FROM
			Income 
		UNION ALL
		SELECT
			pick_up_point,
            date,
            money_in
		FROM
			Income_one_day iod
		WHERE NOT EXISTS (
			SELECT 1
			FROM Income i
			WHERE
				i.pick_up_point = iod.pick_up_point
				AND i.date = iod.date
				AND i.money_in = iod.money_in
		)
	) a
	GROUP BY pick_up_point, date
), CombinedOutcome AS (
	SELECT
		pick_up_point,
        date,
        SUM(money_out) AS total_money_out
	FROM
		(
		SELECT
			pick_up_point,
            date,
            money_out
		FROM
			Outcome
		UNION ALL
		SELECT
			pick_up_point,
            date,
            money_out
		FROM
			Outcome_one_day ood
		WHERE NOT EXISTS (
			SELECT 1
			FROM Outcome o
			WHERE ood.pick_up_point = o.pick_up_point
			AND ood.date = o.date
			AND ood.money_out = o.money_out
		)
	) a
	GROUP BY pick_up_point, date
), Income_Outcome_Left_Join AS (
	SELECT
		ci.pick_up_point,
		ci.date,
		ci.total_money_in,
		coalesce(co.total_money_out, 0) 
	FROM CombinedIncome ci
	LEFT JOIN (
	SELECT *
	FROM CombinedOutcome
	) co ON ci.pick_up_point = co.pick_up_point AND ci.date = co.date
), Income_Outcome_Right_Join AS (
	SELECT
		co.pick_up_point,
		co.date,
		coalesce(ci.total_money_in, 0),
		coalesce(co.total_money_out, 0) 
	FROM CombinedIncome ci
	RIGHT JOIN (
	SELECT *
	FROM CombinedOutcome
	) co ON ci.pick_up_point = co.pick_up_point AND ci.date = co.date
    WHERE ci.pick_up_point IS NULL OR ci.date IS NULL
)

SELECT *
FROM Income_Outcome_Left_Join
UNION
SELECT *
FROM Income_Outcome_Right_Join
ORDER BY pick_up_point, date