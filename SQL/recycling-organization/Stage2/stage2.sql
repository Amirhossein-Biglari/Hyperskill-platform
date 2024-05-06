SELECT 
    pick_up_point,
    date, 
    SUM(money_in) as total_money_in
FROM 
    (SELECT
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
        Income_one_day
    WHERE NOT EXISTS (
    	SELECT 1
      	FROM
            Income
      	WHERE
            Income.date = Income_one_day.date 
      	    AND Income.pick_up_point = Income_one_day.pick_up_point
      	    AND Income.money_in = Income_one_day.money_in
        )
    ) as a
GROUP BY pick_up_point, date;
