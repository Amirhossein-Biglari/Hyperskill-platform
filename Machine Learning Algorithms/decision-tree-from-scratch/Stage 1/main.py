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


"""
Example:
    Inputs:
    input_1 = 1 0 1 1 0 1 0 1 0
    input_2 = 1 0 1 1
    input_3 = 0 1 0 1 0

    Outputs:
    Gini Impurity -> 0.49
    Weighted Gini Impurity -> 0.43
"""

# Read inputs from the user
input_1 = input().split()
input_2 = input().split()
input_3 = input().split()

# Calculate and print Gini impurity and weighted Gini impurity
print(
    round(gini_impurity(input_1), 2),
    round(weighted_gini_impurity(input_2, input_3), 2)
)
