import pandas as pd
import numpy as np


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


class DecisionTree:
    def __init__(self, _root, minimum=1):
        self.root = _root
        self.minimum = minimum

    def _calculate_gini_impurity(self, node: pd.Series):
        labels_proportion = {}
        for label in node.unique():
            labels_proportion[label] = list(node.values).count(label) / len(node)

        gini_score = 1
        for proportion in labels_proportion.values():
            gini_score -= (proportion ** 2)
        return gini_score

    def _calculate_weighted_gini_impurity(self, left_child: pd.Series, right_child: pd.Series):
        size = len(left_child) + len(right_child)
        return len(left_child) / size * self._calculate_gini_impurity(left_child) + len(
            right_child) / size * self._calculate_gini_impurity(right_child)

    def _split_function(self, features: pd.DataFrame, targets: pd.Series):
        least_gini_index = 1
        feature_name = None
        left_indices = None
        right_indices = None
        split_value = None

        for column in features.columns:
            for column_value in features[column].unique():
                left_node_indices = list(features.loc[features[column] == column_value].index)
                right_node_indices = list(features.loc[features[column] != column_value].index)

                left_node_targets = targets[left_node_indices]
                right_node_targets = targets[right_node_indices]

                gini_index = self._calculate_weighted_gini_impurity(left_node_targets, right_node_targets)

                if gini_index < least_gini_index:
                    least_gini_index = gini_index
                    feature_name = column
                    split_value = column_value
                    left_indices = left_node_indices
                    right_indices = right_node_indices

        return feature_name, split_value, left_indices, right_indices, least_gini_index

    def _recursive_splitting(self, node, features: pd.DataFrame, targets: pd.Series):
        gini_impurity = self._calculate_gini_impurity(targets)

        different_rows = features.drop_duplicates()

        if len(targets) <= self.minimum or gini_impurity == 0 or len(different_rows) == 1:
            index = np.argmax(np.unique(targets, return_counts=True)[1])
            node.set_term(np.unique(targets)[index])
            return

        feature_name, split_value, left_indices, right_indices, least_gini_index = \
            self._split_function(features, targets)

        node.set_split(feature_name, split_value)

        # print(f'Made split: {feature_name} is {split_value}')

        left_child = Node()
        node.left = left_child

        left_features = features.loc[left_indices]
        left_features.index = range(len(features.loc[left_indices]))

        left_targets = targets.loc[left_indices]
        left_targets.index = range(len(targets.loc[left_indices]))

        self._recursive_splitting(left_child, left_features, left_targets)

        right_child = Node()
        node.right = right_child

        right_features = features.loc[right_indices]
        right_features.index = range(len(features.loc[right_indices]))

        right_targets = targets.loc[right_indices]
        right_targets.index = range(len(targets.loc[right_indices]))

        self._recursive_splitting(right_child, right_features, right_targets)

    def fit(self, train_set):
        features = train_set.iloc[:, :-1]
        targets = train_set.iloc[:, -1]

        self._recursive_splitting(self.root, features, targets)

    def _internal_recursive_predicting(self, node, record):
        if node.term:
            print(f'Predicted label: {node.label}')
            return

        if record[node.feature] == node.value:
            print(f'Considering decision rule on feature {node.feature} with value {node.value}')
            self._internal_recursive_predicting(node.left, record)
        else:
            print(f'Considering decision rule on feature {node.feature} with value {node.value}')
            self._internal_recursive_predicting(node.right, record)

    def predict(self, test_set: pd.DataFrame):
        for i in range(len(test_set)):
            feature = test_set.iloc[i]
            print(f'Prediction for sample # {i}')
            self._internal_recursive_predicting(self.root, feature)


# file_name = r'C:\Users\Pars Rayan\Desktop\Decision Tree from Scratch\Decision Tree from Scratch' \
#             r'\task\test\data_stage5_train.csv'

train_address, test_address = input().split()
df_train = pd.read_csv(train_address, index_col=0)
root = Node()
decision_tree = DecisionTree(root)
decision_tree.fit(df_train)

# file_name = r'C:\Users\Pars Rayan\Desktop\Decision Tree from Scratch\Decision Tree from Scratch' \
#             r'\task\test\data_stage5_test.csv'
df_test = pd.read_csv(test_address, index_col=0)
decision_tree.predict(df_test)