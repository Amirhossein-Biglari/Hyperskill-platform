# Don't get lost in the trees

## Description
In the final stage of this project, we aim to test whether the Random Forest algorithm overfits as the number of trees increases. This involves experimenting with various values for `n_trees` to verify this behavior.

Except for the number of trees, all parameters remain the same as in the previous stage: we fit the algorithm on the entire training set and calculate the accuracy score using the test set.

## Objectives
1. **Fit the RandomForestClassifier**: Train the classifier on the entire training set using `n_trees` ranging from 1 to 600 with a step of 1. This process might take some time, so please be patient.
2. **Calculate Accuracy**: For each classifier, calculate the resulting accuracy on the test set.
3. **Print Accuracy Values**: Print the first 20 of the resulting accuracy values rounded to three decimal places (e.g., 3.141).
4. **Plot Accuracy Dependence (Optional)**: Plot the resulting dependence of accuracy on the number of trees. This objective is optional and will not be part of the test.
