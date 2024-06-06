# RandomForestClassifier Training Guide

## Description

This guide outlines the steps to create a `RandomForestClassifier` using `DecisionTreeClassifier` and the `create_bootstrap` function. The focus is on implementing the `.fit` method of the `RandomForestClassifier` class.

## RandomForestClassifier Class

```python
class RandomForestClassifier():
    def __init__(self, n_trees=10, max_depth=np.iinfo(np.int64).max, min_error=1e-6):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_error = min_error
        self.forest = []
        self.is_fit = False

    def fit(self, X_train, y_train):
        # Your code for Stage 3 here
        self.is_fit = True

    def predict(self, X_test):
        if not self.is_fit:
            raise AttributeError('The forest is not fit yet! Consider calling .fit() method.')
        # Your code for Stage 4 here
```

## Objectives

1. **Implement the `.fit` method**:
    - Use bootstrap sampling for each new tree.
    - Set `max_features='sqrt'` for each `DecisionTreeClassifier`.
    - Set `max_depth` and `min_impurity_decrease` parameters.
    - Optionally, use the `tqdm` package to track the fitting process.

2. **Prediction and Accuracy**:
    - Use the first tree of the forest to make predictions on the test set.
    - Calculate and print the accuracy of the test set, rounded to three decimal places.
