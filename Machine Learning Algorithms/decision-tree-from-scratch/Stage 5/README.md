# Prediction Time

## Description

This project involves enhancing a custom model to make predictions on new data samples. The key feature to be added is the `predict()` method, which will utilize an internal recursive method to navigate through the decision tree and make predictions.

### Key Features

1. **predict() Method**:
    - Takes a set of new observations.
    - Returns an array of predicted target variable labels.

2. **Internal Recursive Predicting Method**:
    - Operates on a node and a single sample.
    - Works recursively to traverse the decision tree.
    - If the node is a leaf, returns its label.
    - If not, checks the splitting feature and calls itself on the left or right child node based on the feature value in the sample.

### Objectives

- Implement the `predict()` method to handle a set of new observations.
- Implement the internal recursive predicting method to handle individual samples.
- Ensure the following logging during prediction:
  - If a node is not a leaf, log the splitting feature and its value.
  - If a node is a leaf, log the predicted label.