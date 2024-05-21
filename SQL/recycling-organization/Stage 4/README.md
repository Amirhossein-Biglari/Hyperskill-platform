# Comparison of Outcome Money Between Companies

## Description
This project aims to compare the outcome money between two accounting companies of a recycling organization to identify discrepancies in financial reporting practices. By analyzing outcome records, we will pinpoint instances where one company's reported outcome money differs from the other.

## Objectives
- Identify the leader in accounting between Company 1 and Company 2 by comparing the total money_out transactions between each pair of pick_up_points with matching values from the tables Outcome_one_day and Outcome.
- Determine the format of reporting:
  - "once a day" if payments are higher for Company 1.
  - "more than once a day" if payments are higher for Company 2.
  - "both" if payments are the same for both companies.
- Use SQL JOIN, COALESCE, CASE, and GROUP BY functions to achieve the comparison and produce results ordered by pick_up_point and date.
