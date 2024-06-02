import pandas as pd
from sklearn.metrics import confusion_matrix

class Node:
    def __init__(self):
        # Initialize the node with default values
        self.left = None  # Left child node
        self.right = None  # Right child node
        self.term = False  # Terminal node flag
        self.label = None  # Label for terminal node
        self.feature = None  # Feature used for splitting
        self.value = None  # Value of the feature used for splitting

    def set_split(self, feature, value):
        # This function saves the node splitting feature and its value
        self.feature = feature
        self.value = value

    def set_term(self, label):
        # If the node is a leaf, this function saves its label
        self.term = True
        self.label = label

class DecisionTree:
    def __init__(self, node: Node, minimum_num_samples: int = 74) -> None:
        # Initialize the decision tree with a root node
        self.root = node
        self.minimum_num_samples = minimum_num_samples  # Minimum samples to split

    def _gini_impurity(self, labels: list):
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

    def _weighted_gini_impurity(self, node1_labels: list, node2_labels: list):
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
        return (len(node1_labels) / n * self._gini_impurity(node1_labels) +
                len(node2_labels) / n * self._gini_impurity(node2_labels))

    def _split_function(self, dataset: pd.DataFrame, labels: pd.Series):
        """
        Find the best feature and value to split the dataset based on Gini impurity.

        This function iterates over all features and their unique values to find
        the split that results in the lowest weighted Gini impurity.

        Args:
            dataset (pd.DataFrame): DataFrame containing the feature columns.
            labels (pd.Series): Series containing the labels.

        Returns:
            tuple: Minimum weighted Gini impurity, best feature to split on, 
                value of the best feature to split on, indices of left and right nodes.
        """
        minimum_weighted_gini = 1  # Initialize with a value higher than maximum Gini impurity
        best_feature = None  # To store the best feature found
        best_feature_value = None  # To store the best value of the feature found
        best_left_node_index = None  # To store the indices of the left node
        best_right_node_index = None  # To store the indices of the right node

        # Iterate over each feature in the DataFrame
        for feature in dataset.columns:
            # Iterate over each unique value in the feature
            for value in dataset[feature].unique():
                # Handle continuous features by using <= and > for splitting
                if feature in ('Age', 'Fare'):
                    left_node_index = dataset[dataset[feature] <= value].index
                    right_node_index = dataset[dataset[feature] > value].index
                else:
                    left_node_index = dataset[dataset[feature] == value].index
                    right_node_index = dataset[dataset[feature] != value].index

                # Calculate the weighted Gini impurity for the split
                weighted_gini = self._weighted_gini_impurity(labels[left_node_index].values.tolist(),
                                                            labels[right_node_index].values.tolist())

                # Update the best split if a lower weighted Gini impurity is found
                if weighted_gini < minimum_weighted_gini:
                    minimum_weighted_gini = weighted_gini
                    best_feature = feature
                    best_feature_value = value
                    best_left_node_index = left_node_index.tolist()
                    best_right_node_index = right_node_index.tolist()

        # Return the results of the best split found
        return minimum_weighted_gini, best_feature, best_feature_value, best_left_node_index, best_right_node_index

    def _recursive_split_function(self, dataset: pd.DataFrame, labels: pd.Series, node):
        """
        Recursively split the dataset to build a decision tree.

        This function splits the dataset using the best feature and value, and 
        recursively applies the same process to the resulting child nodes.

        Args:
            dataset (pd.DataFrame): DataFrame containing the feature columns.
            labels (pd.Series): Series containing the labels.
            node (Node): Current node in the decision tree.
        """
        # Calculate the Gini impurity for the current set of labels
        gini = self._gini_impurity(labels.values.tolist())

        # Drop duplicates to avoid redundant splits
        d = dataset.drop_duplicates()
        l = len(d)

        # Check for terminal condition: no impurity, minimum samples, or only one unique sample
        if gini == 0 or len(dataset) <= self.minimum_num_samples or l == 1:
            label = labels.mode()[0]  # Assign the most frequent label
            node.set_term(label)  # Mark the node as terminal
            return

        # Find the best split for the current node
        minimum_wg, feature, value, left_node_index, right_node_index = self._split_function(dataset, labels)

        # Set the split feature and value for the current node
        node.set_split(feature, value)
        print(f'Made split {feature} with value {value}')  # Print the split information

        # Recursively split the left node
        left = Node()
        node.left = left
        self._recursive_split_function(dataset.loc[left_node_index], labels.loc[left_node_index], left)

        # Recursively split the right node
        right = Node()
        node.right = right
        self._recursive_split_function(dataset.loc[right_node_index], labels.loc[right_node_index], right)

    def fit(self, dataset: pd.DataFrame):
        """
        Build a decision tree classifier from the training dataset.

        This function initiates the recursive process of splitting the dataset
        to build the decision tree, starting from the root node.

        Args:
            dataset (pd.DataFrame): DataFrame containing the training data with 
                                    features and labels.
        """
        # Separate features (X) and labels (y) from the dataset
        X = dataset.drop(columns='Survived')
        y = dataset['Survived']
        # Start the recursive splitting process from the root node
        self._recursive_split_function(X, y, self.root)

    def _internal_recursive_predicting(self, node, record):
        """
        Recursively traverse the decision tree to make a prediction for a single record.

        This function traverses the tree from the root node to a leaf node by
        evaluating the decision rules at each node, and returns the label of the
        leaf node as the prediction.

        Args:
            node (Node): The current node in the decision tree.
            record (pd.Series): The record for which to make the prediction.
        """
        if node.term:
            # If the node is terminal, return its label as the prediction
            print(f'Predicted label: {node.label}')
            return node.label  # Return the label of the terminal node

        # Traverse to the left or right child based on the feature value
        if record[node.feature] == node.value or (node.feature in ('Age', 'Fare') and record[node.feature] <= node.value):
            print(f'Considering decision rule on feature {node.feature} with value {node.value}')
            return self._internal_recursive_predicting(node.left, record)
        else:
            print(f'Considering decision rule on feature {node.feature} with value {node.value}')
            return self._internal_recursive_predicting(node.right, record)

    def predict(self, test_set: pd.DataFrame):
        """
        Predict labels for a test dataset using the trained decision tree.

        This function iterates over each record in the test dataset and uses the
        trained decision tree to predict its label.

        Args:
            test_set (pd.DataFrame): DataFrame containing the test data.
        """
        predictions = []  # Initialize list to store predictions
        for i in range(len(test_set)):
            # Get the feature values for the current record
            feature = test_set.iloc[i]
            print(f'Prediction for sample # {i}')
            # Recursively predict the label for the current record
            predictions.append(self._internal_recursive_predicting(self.root, feature))
        return predictions  # Return the list of predictions

# Load dataset from CSV file
df_train = pd.read_csv('data_stage8_train.csv', index_col=0)
df_test = pd.read_csv('data_stage8_test.csv', index_col=0)

root = Node()
# Initialize the decision tree with a root node
ds = DecisionTree(root, minimum_num_samples=1)

# Fit the decision tree model on the training data
ds.fit(df_train)

# Predict labels for the test data
predicted_labels = ds.predict(df_test)
