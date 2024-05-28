## Numerical Features

### Description
In this stage, we'll modify the algorithm to consider numerical features in addition to categorical ones. The splitting function from Stage 2 needs to be updated accordingly.

**Data Splitting Concept:**
- **Categorical Features:** Objects with the same value of the selected feature go to the left child node; others go to the right child node.
- **Numerical Features:** Objects with a feature value less than or equal to the threshold go to the left child node; others go to the right child node.

### Objectives
1. **Improve the Splitting Function:**
   - **Input:** Dataset and target variable.
   - **Output:** Minimum weighted Gini impurity, chosen feature, threshold, list of left node indexes, list of right node indexes.
   
2. **Process Steps:**
   - Take the input path to the file with data.
   - Read the data from a `.csv` file.
   - Identify two numerical features: `Age` and `Fare`.
   - Separate the `Survived` column (target variable) from the dataset.
   - Apply the splitting function to the given data.
   - Print the function's return values, rounding float values to three decimal places (only for the answer, not within the functions).
