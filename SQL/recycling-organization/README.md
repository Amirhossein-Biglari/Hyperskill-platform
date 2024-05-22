# Discover the Recycle Organization Database

## About the Project

Welcome to the "Discover the Recycle Organization Database" project, specifically designed for students who have completed the SQL for Data Analysis track. This project serves as a deep dive into the world of SQL, employing advanced techniques and functions to analyze income and outcome data from two accounting companies hired by a recycling organization.

As a novice data analyst, you will explore the intricacies of financial records to unearth insights that could aid in decision-making and strategic planning. This project aims to enhance the efficiency of financial transactions within the recycling organization by leveraging your SQL skills.

## Project Goals

- **Analyze Financial Data:** Compare and analyze the financial data from two distinct accounting companies to understand how they manage recycling organization funds.
- **Advanced SQL Techniques:** Utilize advanced SQL functions including `percentile_cont`, various types of JOINs, multiple subqueries, and an array of aggregate functions.
- **Deep Dive into SQL:** Explore `GROUP BY`, set operations, and conditional functions to master SQL's full capabilities.

## Learning Outcomes

By participating in this project, you will:
- Gain hands-on experience with complex SQL queries and database management.
- Develop a nuanced understanding of how financial data can inform business strategy and operational efficiency.
- Enhance your analytical skills, preparing you for more advanced roles in data analysis and business intelligence.

### Table Details

#### Income_one_day (Company 1)
- **pick_up_point:** An identifier for each collection point.
- **date:** The date of the transaction without time details.
- **money_in:** The amount of money received at the collection point for the specified date.

#### Outcome_one_day (Company 1)
- **pick_up_point:** Identifies each collection point.
- **date:** Records the date of the transaction without time components.
- **money_out:** Represents the amount of money issued to recyclable material distributors for the given date.

#### Income (Company 2)
- **code:** Primary key that tracks income transactions.
- **pick_up_point:** Identifies each collection point.
- **date:** Records transaction dates without time details.
- **money_in:** Reflects the amount of money received at the collection point for the specified date.

#### Outcome (Company 2)
- **code:** Primary key that tracks outcome transactions.
- **pick_up_point:** Identifies each collection point.
- **date:** Records transaction dates without time details.
- **money_out:** Represents the amount of money issued to recyclable material distributors for the given date.
