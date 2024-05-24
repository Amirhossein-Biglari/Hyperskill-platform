# Recursive Splitting

## Description

This project implements a recursive splitting process for building a decision tree. The process involves a recursive function that calls a splitting function for each node in the tree.

### Recursive Function Workflow

1. **Leaf Check**: The function first checks if the current node is a leaf.
   - A node is a leaf if:
     - The amount of data is less than or equal to the minimum (1 in this case).
     - The Gini Impurity is 0.
     - All objects have the same values for all features.

2. **Leaf Node**: If the node is a leaf:
   - The function stores its label (0 if not survived, otherwise 1).
   - The recursive process ends.

3. **Non-Leaf Node**: If the node is not a leaf:
   - The function calls the splitting function for the current node.
   - It stores the chosen feature and its threshold value.
   - Creates the left child node and stores it in the current node.
     - The dataset for the left child is formed using the array of left node indexes returned by the splitting function.
     - Indexes in the left node are reset using `range(number_of_objects_in_the_left_node)`.
   - The recursive function is called for the left child node.
   - Creates the right child node and stores it in the current node.
     - The dataset for the right child is formed using the array of right node indexes returned by the splitting function.
     - Indexes in the right node are reset using `range(number_of_objects_in_the_right_node)`.
   - The recursive function is called for the right child node.

### Node Class

```python
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.term = False
        self.label = None
        self.feature = None
        self.value = None

    def set_split(self, feature, value):
        self.feature = feature
        self.value = value

    def set_term(self, label):
        self.term = True
        self.label = label
