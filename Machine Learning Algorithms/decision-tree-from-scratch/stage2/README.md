# Titanic Passenger Survival Prediction

This project aims to create a function to split a dataset recursively based on categorical features, using the weighted Gini Impurity to minimize impurity at each node. The end goal is to build a decision tree model that predicts Titanic passengers' chances of survival.

## Description

The project focuses on the following tasks:
- **Splitting the dataset**: Identify the feature and value that minimize the weighted Gini Impurity when splitting the data.
- **Recursive data splitting**: Use the identified feature and value to divide the dataset into left and right child nodes.
- **Dataset**: The Titanic passenger dataset, which includes various features such as class, gender, age, number of siblings/spouses, number of parents/kids, and fare, with the target variable being survival (0 = No, 1 = Yes).

## Objectives

- **Compose the splitting function**: The function should take the dataset and the target variable as arguments and return the minimum weighted Gini Impurity for the current node, the chosen feature, its value, and lists of left and right node indexes.

## Steps

1. **Input the path to the file with data**.
2. **Read the data from a .csv file**.
3. **Separate the target variable (Survived) from the dataset with features**.
4. **Apply the splitting function to the given data**.
5. **Print the function output**.

## Features in the Dataset

- **Survived**: Whether a person survived or not (0 = No; 1 = Yes) - target variable.
- **Pclass**: Passenger class (1 = 1st; 2 = 2nd; 3 = 3rd).
- **Sex**: Gender (0 = Male, 1 = Female).
- **Age**: Age of the passenger.
- **Sibsp**: Number of siblings/spouses aboard.
- **Parch**: Number of parents/kids aboard.
- **Fare**: Passenger fare.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/titanic-survival-prediction.git
   cd titanic-survival-prediction
