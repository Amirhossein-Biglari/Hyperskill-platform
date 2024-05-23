# Gini Impurity Calculation

This project provides functions to calculate the Gini Impurity and weighted Gini Impurity for datasets, commonly used in decision tree algorithms for classification tasks.

## Description

Gini Impurity is a measure of the impurity or disorder in a dataset. It is defined for a dataset \( D \) containing samples from \( n \) classes. The probability of samples belonging to a class at a given node is denoted as \( p_i \), calculated as:
\[ p_i = \frac{\text{number of samples that belong to the } i^{th} \text{ class}}{\text{total number of samples in } D} \]

The Gini Impurity of \( D \) is defined as:
\[ \text{Gini}(D) = 1 - \sum_{i=1}^{n} (p_i)^2 \]

The weighted Gini Impurity accounts for the proportion of objects in the vertices after splitting. If \( D \) is split according to feature \( A \) into subsets \( D_1 \) and \( D_2 \) with sizes \( n_1 \) and \( n_2 \), respectively, the weighted Gini Impurity is:
\[ \text{Weighted Gini}_A(D) = \frac{n_1}{n} \text{Gini}(D_1) + \frac{n_2}{n} \text{Gini}(D_2) \]

## Objectives

- **Compute Gini Impurity for a node**: A function that takes an array of class labels for all samples in one node and outputs the Gini score.
- **Compute Weighted Gini Impurity after splitting**: A function that takes two arrays of class labels for two child nodes and returns a weighted Gini score. The score is rounded to the fifth decimal place.

## Example

- **Gini Impurity for the node** `[1,1,1,0,0,0,0,0,1,1]`
- **Weighted Gini Impurity for the split** `[1,1,1,0]` and `[0,0,0,0,1,1]`

Note: All output numbers are rounded to the second decimal place, though internal calculations maintain higher precision.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gini-impurity-calculation.git
   cd gini-impurity-calculation
