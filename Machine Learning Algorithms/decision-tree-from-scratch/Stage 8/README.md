# Splitting and Prediction for Numerical Features

## Description
In this step, we update the recursive predicting function to handle numerical features. For numerical features, values are compared for inequality. A sample goes to the left child node if the feature value is less than or equal to the threshold; otherwise, it goes to the right child node. For categorical features, the algorithm remains unchanged.

## Objectives
1. Incorporate the one-node-split function from the previous stage into the `DecisionTree` class. Add a new parameter to the class: a list of numeric feature names. Ensure the recursive splitting function works with the updated one-node-split function.
2. Update the recursive predicting method:
   - Input paths to two files (training and test datasets) split by a space.
   - Read data from the .csv files.
   - There are two numerical features: `Age` and `Fare`.
   - Train a decision tree on the training set, with a minimum of 1 sample per leaf node. The `Survived` column is the target variable and should be separated from the feature dataset.
   - Make predictions on the test set, ensuring the `Survived` feature is also separated in the test set.

