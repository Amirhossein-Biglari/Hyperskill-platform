# First Evaluation

## Description

Our model is now complete: it can learn from known data and make predictions on new samples. The next step is to measure its performance quality. For the evaluation, we will use the confusion matrix from `sklearn`.

### Key Points

- Use the Titanic dataset, excluding the Age and Fare features since they are numerical.
- The dataset is already split into training and test sets.
- To avoid overfitting, set the minimum number of samples for a node to be considered a leaf to 74. This value has been tested to produce the best result on the given test set.

### Objectives

1. **Input Handling**:
    - Accept paths to two .csv files: training dataset and test dataset.

2. **Data Processing**:
    - Read data from the .csv files.
    - Train a decision tree on the training set with a minimum of 74 samples per leaf.
    - The target variable is the 'Survived' column, which should be separated from the feature set.

3. **Prediction and Evaluation**:
    - Make predictions on the test set.
    - Separate the 'Survived' feature in the test set.
    - Compute a confusion matrix using the real and predicted values of the target variable.
    - Print true positives and true negatives normalized over the true rows, rounded to three decimal places.

### Example

Normalization over true rows shows a fraction of the correctly predicted samples of a single label over all the samples with that label. 

For example, if you have a dataset with 20 samples: 10 samples with label 1 (positive) and 10 samples with label 0 (negative). A confusion matrix might look as follows:
- True positives = 0.6
- False positives = 0.4
- False negatives = 0.7
- True negatives = 0.3

This means that the model correctly identified label 1 in 6 out of 10 cases and label 0 in 3 out of 10 cases.
