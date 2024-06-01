import pandas as pd


def gini_impurity(labels: list):
    """
    Calculate the Gini impurity for a list of labels.

    Gini impurity measures the likelihood of an incorrect classification
    of a new instance of a random variable. It reaches its minimum (zero) 
    when all cases in a node fall into a single target category.

    Args:
        labels (list): A list of labels.

    Returns:
        float: The Gini impurity of the labels.
    """
    # Calculate the probability of each unique label
    probabilities = [labels.count(label) / len(labels) for label in set(labels)]
    # Calculate the Gini impurity
    return 1 - sum([prob ** 2 for prob in probabilities])


def weighted_gini_impurity(node1_labels: list, node2_labels: list):
    """
    Calculate the weighted Gini impurity for two sets of labels.

    The weighted Gini impurity takes into account the size of each node
    and combines their Gini impurities to give an overall measure.

    Args:
        node1_labels (list): A list of labels for the first node.
        node2_labels (list): A list of labels for the second node.

    Returns:
        float: The weighted Gini impurity of the two nodes.
    """
    # Total number of labels
    n = len(node1_labels) + len(node2_labels)
    # Calculate the weighted Gini impurity
    return (len(node1_labels) / n * gini_impurity(node1_labels) +
            len(node2_labels) / n * gini_impurity(node2_labels))

def split_function(features: pd.DataFrame, labels: pd.Series):
    """
    Determine the best feature and value to split the data for decision tree.

    This function iterates over all features and their unique values to find
    the split that results in the lowest weighted Gini impurity.

    Args:
        features (pd.DataFrame): A DataFrame containing the feature columns.
        labels (pd.Series): A Series containing the labels.

    Returns:
        tuple: Minimum weighted Gini impurity, best feature to split on, 
               value of the best feature to split on, left child DataFrame, 
               right child DataFrame.
    """
    # 1 or 0.51?
    minimum_weighted_gini = 1  # Initialize with a value higher than maximum Gini impurity
    best_feature = None  # To store the best feature found
    best_feature_value = None  # To store the best value of the feature found
    best_left_child = None  # To store the left child DataFrame
    best_right_child = None  # To store the right child DataFrame

    # Iterate over each feature in the DataFrame
    for feature in features.columns:
        # Iterate over each unique value in the feature
        for value in features[feature].unique():
            # Split the data into left and right nodes based on the feature value
            left_node = features[features[feature] == value]
            right_node = features[features[feature] != value]
            left_node_index = left_node.index
            right_node_index = right_node.index

            # Calculate the weighted Gini impurity for the split
            weighted_gini = weighted_gini_impurity(list(labels[left_node_index].values), list(labels[right_node_index].values))

            # Update the best split if a lower weighted Gini impurity is found
            if weighted_gini < minimum_weighted_gini:
                minimum_weighted_gini = weighted_gini
                best_feature = feature
                best_feature_value = value
                best_left_child = left_node
                best_right_child = right_node

    # Return the results of the best split found
    return minimum_weighted_gini, best_feature, best_feature_value, best_left_child, best_right_child


# Read the input CSV file into a DataFrame
df = pd.read_csv(input(), index_col=0)

# Perform the split function to find the best split based on Gini impurity
X, y = df.iloc[:, :-1], df.iloc[:, -1]
minimum_weighted_gini, feature, value, left, right = split_function(X, y)

# Print the results: minimum weighted Gini impurity, best feature, best feature value, and indices of the left and right child nodes
print(minimum_weighted_gini, feature, value, list(left.index), list(right.index))
