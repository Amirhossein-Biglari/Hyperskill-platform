import pandas as pd

def gini_impurity(labels: list):
    probabilities = [labels.count(label)/len(labels) for label in set(labels)]
    return 1 - sum([prob ** 2 for prob in probabilities])


def weighted_gini_impurity(node1_labels: list, node2_labels: list):
    n = len(node1_labels) + len(node2_labels)
    return len(node1_labels) / n * gini_impurity(node1_labels) + len(node2_labels) / n * gini_impurity(node2_labels)


def split_function(features: pd.DataFrame, labels: pd.Series):
    minimum_weighted_gini = 0.51
    best_feature = None
    best_feature_value = None
    best_left_child = None
    best_right_child = None

    for feature in features.columns:
        for value in features[feature].unique():
            left_node = features[features[feature] == value]
            right_node = features[features[feature] != value]
            left_node_index = left_node.index
            right_node_index = right_node.index

            weighted_gini = weighted_gini_impurity(list(labels[left_node_index].values), list(labels[right_node_index].values))

            if weighted_gini < minimum_weighted_gini:
                minimum_weighted_gini = weighted_gini
                best_feature = feature
                best_feature_value = value
                best_left_child = left_node
                best_right_child = right_node

    return minimum_weighted_gini, best_feature, best_feature_value, best_left_child, best_right_child

print(round(gini_impurity(input().split()), 2), round(weighted_gini_impurity(input().split(), input().split()), 2))
