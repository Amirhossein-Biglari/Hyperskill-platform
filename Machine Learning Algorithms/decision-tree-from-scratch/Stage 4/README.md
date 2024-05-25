# Prediction Time

## Description
The objective of this project is to enhance our custom model by adding the `predict()` method. This method is crucial as it enables the model to make predictions on new data samples. The `predict()` method will return an array of predictions for the target variable based on new observations.

## Implementation Details

### Predict Method
The `predict()` method will:
- Accept a set of new observations.
- Return an array of predicted labels for the target variable.

### Internal Recursive Predicting Method
An internal method will be implemented to be called by `predict()` for each sample. This recursive method will:
- Check if the current node is a leaf node.
  - If it is a leaf, it returns its label as the prediction for the given sample.
  - If it is not a leaf, it checks the splitting feature of this node and, based on its value in the sample, recursively calls itself for the left or right child of the current node.

### Objectives
- Implement the `predict()` method to handle new observations and return predictions.
- Implement the internal recursive method to handle individual samples and nodes, making recursive predictions as necessary.
- During prediction, log messages should be printed to indicate the process:
  - If the node is not a leaf, print the splitting feature and its value.
  - If the node is a leaf, print the predicted label.

### Steps
1. Take the input paths to two files split by a space: the training dataset and the test dataset.
2. Read the data from the .csv files.
3. Train the decision tree on the training set. The target variable is the "Survived" column, which should be separated from the features.
4. Make predictions on the test set using the `predict()` method.
