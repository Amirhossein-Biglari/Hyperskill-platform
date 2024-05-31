# Final Evaluation

## Description
The algorithm is now complete! In the final stage, let's measure the quality of the model once again and see whether the new features improved its performance.

## Objectives
1. Take the input paths to two files split by a space: the first one is the training dataset, and the second one is the test dataset.
2. Read the data from the .csv files.
3. There are two numerical features: Age and Fare.
4. Train a decision tree on the training set. The minimum number of samples for a node to be considered a leaf should be 74. This value is a parameter of the DecisionTree class. As in the previous stages, the Survived column is the target variable. Separate it from the dataset with features.
5. Make predictions on the test set. Don't forget to separate the Survived feature in the test set as well.
6. Given the real and predicted values of the target variable, compute a confusion matrix.
7. As an answer, print true positives and true negatives normalized over the true rows. Round the float values to three decimal places.
