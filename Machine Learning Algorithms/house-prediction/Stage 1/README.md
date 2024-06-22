## Stage 1: Import & Explore

### Description

Before working with your data, you need to explore it first. The dataset contains preprocessed information about houses for sale with the following columns:

- **Price**: The price of the house. Class 0 (affordable, < €700,000) and class 1 (expensive, > €700,000).
- **Area**: The area of the house.
- **Room**: The number of rooms in the house.
- **Lon**: House longitude coordinates.
- **Lat**: House latitude coordinates.
- **Zip_area**: House location in the Netherlands based on the zip code.
- **Zip_loc**: House location in Amsterdam based on the zip code.

Perform Exploratory Data Analysis (EDA) to gain insights into the data and identify potential issues.

### Objectives

To complete this stage:

1. Load the data into a pandas DataFrame.
2. Analyze the data and answer the following questions:
   - How many rows does the DataFrame have?
   - How many columns does the DataFrame have?
   - Are there any missing values in the DataFrame (True or False)?
   - What is the maximum number of rooms across the houses in the dataset?
   - What is the mean area of the houses in the dataset?
   - How many unique values does the column `Zip_loc` contain?

Provide each answer on a new line.

### Example

**Example of DataFrame:**

|    | Price | Area | Room | Lon      | Lat       | Zip_area | Zip_loc |
|----|-------|------|------|----------|-----------|----------|---------|
| 0  | 0     | 64   | 3    | 4.907736 | 52.356157 | 10       | CR      |
| 1  | 0     | 60   | 3    | 4.854476 | 52.348586 | 10       | EL      |
| 2  | 1     | 109  | 4    | 4.944774 | 52.343782 | 10       | SM      |
| 3  | 0     | 128  | 6    | 4.789928 | 52.343712 | 10       | TH      |
| 4  | 1     | 138  | 5    | 4.902503 | 52.410538 | 10       | KN      |

**Output:**

5
7
False
6
99.8
5