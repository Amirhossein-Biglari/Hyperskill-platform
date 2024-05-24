import pandas as pd


class Node:
    def __init__(self):
        # class initialization
        self.left = None
        self.right = None
        self.term = False
        self.label = None
        self.feature = None
        self.value = None

    def set_split(self, feature, value):
        # this function saves the node splitting feature and its value
        self.feature = feature
        self.value = value

    def set_term(self, label):
        # if the node is a leaf, this function saves its label
        self.term = True
        self.label = label


def gini_impurity(labels: list):
    probabilities = [labels.count(label)/len(labels) for label in set(labels)]
    return 1 - sum([prob ** 2 for prob in probabilities])


def weighted_gini_impurity(node1_labels: list, node2_labels: list):
    n = len(node1_labels) + len(node2_labels)
    return len(node1_labels) / n * gini_impurity(node1_labels) + len(node2_labels) / n * gini_impurity(node2_labels)


def split_function(dataset: pd.DataFrame, labels: pd.Series):
    minimum_weighted_gini = 0.51
    best_feature = None
    best_feature_value = None
    best_left_node_index = None
    best_right_node_index = None

    for feature in dataset.columns:
        for value in dataset[feature].unique():
            left_node_index = dataset[dataset[feature] == value].index
            right_node_index = dataset[dataset[feature] != value].index

            weighted_gini = weighted_gini_impurity(labels[left_node_index].values.tolist(),
                                                   labels[right_node_index].values.tolist())

            if weighted_gini < minimum_weighted_gini:
                minimum_weighted_gini = weighted_gini
                best_feature = feature
                best_feature_value = value
                best_left_node_index = left_node_index.tolist()
                best_right_node_index = right_node_index.tolist()

    return minimum_weighted_gini, best_feature, best_feature_value, best_left_node_index, best_right_node_index


def recursive_split_function(dataset: pd.DataFrame, labels: pd.Series, node):
    gini = gini_impurity(labels.values.tolist())
    minimum = 1

    d = dataset.drop_duplicates()
    l = len(d)
    if gini == 0 or len(dataset) <= minimum or l == 1:
        label = labels.mode()[0]
        node.set_term(label)
        return

    minimum_wg, feature, value, left_node_index, right_node_index = split_function(dataset, labels)

    node.set_split(feature, value)
    print(f'Made split {feature} with value {value}')
    left = Node()
    node.left = left

    recursive_split_function(dataset.loc[left_node_index], labels.loc[left_node_index], left)

    right = Node()
    node.right = right
    recursive_split_function(dataset.loc[right_node_index], labels.loc[right_node_index], right)


# df = pd.read_csv(input(), index_col=0)
# root = Node()
# recursive_split_function(dataset, labels, root)
# labels = df.iloc[:, -1]
# dataset = df.iloc[:, :-1]
print(round(gini_impurity(input().split()), 2),
      round(weighted_gini_impurity(input().split(), input().split()), 2))