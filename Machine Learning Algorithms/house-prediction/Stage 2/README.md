# Split the Data

## Description
In this stage, we will create a training and test split to proceed with the ML pipeline. It is essential to ensure that the categorical column with many unique values (Zip_loc) includes all unique values in the training dataset. This can be achieved using the `stratify` option in the `train_test_split` function from the scikit-learn library.

## Objectives
To complete this stage:

1. **Import** `train_test_split` from scikit-learn.
2. **Create** two separate datasets:
   - `X` dataset with the columns: `Area`, `Room`, `Lon`, `Lat`, `Zip_area`, and `Zip_loc`.
   - `y` dataset for the target column: `Price`.
3. **Split** the datasets using `train_test_split`:
   - Set the test data proportion to 30%.
   - Set the `stratify` parameter to `X['Zip_loc'].values`.
   - Set `random_state` to 1.
   - This will create four separate datasets.
4. **Print** the value count dictionary of the `Zip_loc` column in the final training dataset.
