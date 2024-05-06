# Combined Income Analysis

## Project Description

In this second stage of our project, we focus on consolidating income data from two accounting companies, Company 1 and Company 2. Building on the foundation set in the initial stage, this segment aims to merge the income transactions from the respective tables of both companies to create a comprehensive overview of the income across all recycling pick-up points.

## Objectives

- **Data Consolidation:** Combine income data from `Income` and `Income_one_day` tables of both companies to form a unified overview of `money_in` transactions.
- **Aggregate Transactions:** Aggregate the `money_in` transactions by `date` and `pick_up_point` ensuring that each entry is unique, akin to the structure found in `Income_one_day`.
- **Handle Transaction Duplication:** Assume transactions with the same `date`, `pick_up_point`, and `money_in` represent the same financial activity. Sum up `money_in` values where `date` and `pick_up_point` match but `money_in` differs.