# Combined Data Compilation

## Description
In this final stage, the goal is to merge income and outcome data from both accounting companies into a single dataset. The aim is to create a comprehensive compilation of financial transactions, ensuring each pick-up point and date combination is accurately represented. This consolidated dataset provides insights into the organization's financial activities, facilitating further analysis and decision-making.

## Objectives
- Combine income (`Income` and `Income_one_day`) and outcome (`Outcome` and `Outcome_one_day`) data for both accounting companies as in Stage 2.
- Create the final combined data compilation from both combinations of income and outcome. The final query should include:
  - `pick_up_point`
  - `date`
  - `total_money_in`
  - `total_money_out`
- If a `total_money_in` transaction exists for a specific date and pick-up point but a corresponding `total_money_out` transaction does not exist, assign the `total_money_out` value as 0, and vice versa.
- As in Stage 2, rows for tables `Income` and `Income_one_day` or `Outcome` and `Outcome_one_day` with the same date, pick_up_point, and money_in/money_out represent the same transactions. If the date and pick_up_point are the same but money_in/money_out are different, sum the values from both tables or within the `Income`/`Outcome` table if multiple transactions for one date and pick_up_point exist.
- Utilize the `JOIN` function effectively to combine multiple tables accurately, and consider using the `COALESCE` function to handle instances where a value may be 0. Additionally, it is recommended to use the `WITH (CTE)` function to efficiently reuse the same subqueries multiple times throughout the query.
- Employ the `GROUP BY` function to effectively group the query results by pick_up_point and date.
- Ensure the final results are `ORDER BY` first by pick_up_point and then by date for clear organization and readability.
- The column order is essential.
