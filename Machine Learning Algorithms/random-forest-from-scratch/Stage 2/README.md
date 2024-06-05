# Sampling the Sets

## Description

This project focuses on implementing bootstrap sampling, an essential component of the Random Forest model. Bootstrap sampling involves randomly sampling a dataset with replacement.

## Objectives

1. **Create the `create_bootstrap` function:**
   - The function should take features and target values as parameters and return a bootstrap sample.
   - Use `np.random.choice` to create a mask of randomly chosen indexes.
   - Ensure the length of the mask matches the length of the dataset.
   - Use a seed of 52 for the `np.random.choice` function for consistency in tests.

2. **Use the `create_bootstrap` function:**
   - Generate a bootstrap sample from the training data.
   - Print the first ten items of the resulting sample `y-s`.
